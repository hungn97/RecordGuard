import http.server
from cryptography.fernet import Fernet
import json
import time

doc_as_file = open("docaskey.txt","r")
doc_as_key = doc_as_file.read().encode()
doc_as_file.close()
fernet_doc = Fernet(doc_as_key)

as_rs_file = open("asrskey.txt","r")
as_rs_key = as_rs_file.read().encode()
as_rs_file.close()
fernet_rs = Fernet(as_rs_key)

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
    "Encrypts ticket as authentication for client to send to record server"
    encrypted_ticket = fernet_rs.encrypt(ticket)
    return encrypted_ticket


class S(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        message = self.rfile.read(length)
        decrypted_message = decrypt_message(message)

        if message is not None: #verify_credentials(decrypted_message):
            ticket = create_ticket(decrypted_message)
            serialized_ticket = json.dumps(ticket).encode()
            encrypted_ticket = encrypt_ticket(serialized_ticket)
            outbound_message = fernet_doc.encrypt(encrypted_ticket)
            print(outbound_message)
        else:
            outbound_message = "failed".encode()

        self._set_headers()
        self.wfile.write(outbound_message)



# def verify_ds(ds):
#     "Check that digital signature affirms identity"
#
#     return

# def verify_credentials(message):
#     "Access database and fetch user credetials for verification"
#     #could use actual sql database or just a csv file to mock it
#     #need a function to seach through sql database and return true if found
#     #found = verify_database(message["doctorID"], message["doctorPW"], message["patientID"])
#     if found and verify_ds(message.ds):
#         return True
#     else:
#         return False



(server, port) = ('', 8080)

httpd = http.server.HTTPServer((server, port), S)
print("serving at port", port)
httpd.serve_forever()
