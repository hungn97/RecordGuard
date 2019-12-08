import http.server
from cryptography.fernet import Fernet
import json
import sqlite3
import textwrap

wrapper = textwrap.TextWrapper(width=50)

doc_as_file = open("docaskey.txt","r")
doc_as_key = doc_as_file.read().encode()
doc_as_file.close()
fernet_doc = Fernet(doc_as_key)

as_rs_file = open("asrskey.txt","r")
as_rs_key = as_rs_file.read().encode()
as_rs_file.close()
fernet_rs = Fernet(as_rs_key)

with sqlite3.connect("doctor_database.db") as db:
    cursor = db.cursor()

def decrypt_message(message):
    plaintext = fernet_doc.decrypt(message)
    json_message = json.loads(plaintext)
    return json_message

def create_ticket(message):
    ticket = {
        "doctorID": message["doctorID"],
        "patientID": message["patientID"],
        "timestamp": message["timestamp"]
    }
    return ticket

def encrypt_ticket(ticket):
    """Encrypts ticket as authentication for client to send to record server"""
    encrypted_ticket = fernet_rs.encrypt(ticket)
    return encrypted_ticket

def verify_credentials(message):
    find_user = "SELECT * FROM user WHERE userid = ? AND userpw = ? AND patientid = ?"
    cursor.execute(find_user, [message["doctorID"], message["doctorPW"], message["patientID"]])
    results = cursor.fetchall()

    if results:
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
        print("\n\n-------------------------------------------------")
        print("Received from port", port, ":")
        print("-------------------------------------------------")
        print("Ciphertext:\n", wrapper.fill(text=message.decode()))
        print("\nPlaintext:\n", json.dumps(decrypted_message, indent=4))
        if verify_credentials(decrypted_message):
            ticket = create_ticket(decrypted_message)
            serialized_ticket = json.dumps(ticket).encode()
            encrypted_ticket = encrypt_ticket(serialized_ticket)
            outbound_message = fernet_doc.encrypt(encrypted_ticket)
        else:
            print("\nBad Auth")
            outbound_message = "failed".encode()

        self._set_headers()
        self.wfile.write(outbound_message)


(server, port) = ('', 8080)

httpd = http.server.HTTPServer((server, port), S)
print("Serving at port", port)
httpd.serve_forever()
