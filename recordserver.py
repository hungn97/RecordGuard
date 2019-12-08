import http.server
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import json
import pickle
import sqlite3

doc_rs_file = open("docrskey.txt","r")
doc_rs_key = doc_rs_file.read().encode()
doc_rs_file.close()
fernet_doc = Fernet(doc_rs_key)

as_rs_file = open("asrskey.txt","r")
as_rs_key = as_rs_file.read().encode()
as_rs_file.close()
fernet_as = Fernet(as_rs_key)

with open("docpublickey.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

with sqlite3.connect("patient_database.db") as db:
    cursor = db.cursor()

def decrypt_message(message):
    plaintext = fernet_doc.decrypt(message)
    return plaintext

def split_signature(message):
    messsage_sig_json = pickle.loads(message)
    auth_json = messsage_sig_json["content"]
    signature = messsage_sig_json["signature"]
    return auth_json, signature

def decrypt_ticket(ticket):
    """Encrypts ticket as authentication for client to send to record server"""
    decrypted_ticket = fernet_as.decrypt(ticket)
    return decrypted_ticket

def verify_signature(message, signature):
    """Check that digital signature affirms identity"""
    serialized_message = json.dumps(message)
    byte_message = serialized_message.encode()
    match = True
    try:
        public_key.verify(
            signature,
            byte_message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
            )
    except:
        match = False
    return match


def verify_credentials(auth_json, records):
    """Access database and fetch user credetials for verification"""
    if records and verify_ticket(auth_json):
        return True
    else:
        return False

def fetch_records(patientID):
    find_patients = ("SELECT * FROM patients WHERE patientid = ?")
    cursor.execute(find_patients, patientID)
    results = cursor.fetchall()
    results = results[0]
    print(results)
    if results:
        json_records = {
            "patientID": results[0],
            "name": results[1] + " " + results[2]
        }
        return json_records
    else:
        return False


def verify_ticket(auth_json):
    ticket = fernet_as.decrypt(auth_json["ticket"].encode())
    str_ticket = ticket.decode()
    json_ticket = json.loads(str_ticket)
    if ((auth_json["doctorID"] == json_ticket["doctorID"]) and
        (auth_json["patientID"] == json_ticket["patientID"]) and
        ((json_ticket["timestamp"] - auth_json["timestamp"]) < 60)):
        return True
    else:
        return False


class S(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        message = self.rfile.read(length)
        decrypted_message = decrypt_message(message)
        print(decrypted_message)
        auth_json, signature = split_signature(decrypted_message)
        print(auth_json, "\n", signature)
        if verify_signature(auth_json, signature) is False:
            outbound_message = b"Request Denied"
        else:
            records = fetch_records(auth_json["patientID"])
            if verify_credentials(auth_json, records):
                serialized_records = json.dumps(records)
                byte_records = serialized_records.encode()
                outbound_message = fernet_doc.encrypt(byte_records)
                print(outbound_message)
            else:
                outbound_message = b"failed"

        self._set_headers()
        self.wfile.write(outbound_message)


(server, port) = ('', 8081)

httpd = http.server.HTTPServer((server, port), S)
print("serving at port", port)
httpd.serve_forever()
