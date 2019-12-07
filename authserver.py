import http.server
import socketserver
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
fernet_rs = Fernet(doc_as_key)

# dbconn = sqlite3.connect('doctor_data.db')

def decrypt_message(message):
    cipher_txt = fernet_doc.decrypt(message)
    json_message = json.loads(cipher_txt)
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

    def do_GET(self):
        self._set_headers()
        print("getting")
        self.wfile.write("get".encode())

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        message = self.rfile.read(length)
        decrypted_message = decrypt_message(message)
        # if verify_credentials(decrypted_message):
        #     create_ticket(decrypted_message)
        ticket = create_ticket(decrypted_message)
        print(ticket)
        self._set_headers()
        self.wfile.write(message)



# def verify_ds(ds):
#     "Check that digital signature affirms identity"
#
#     return

# def verify_credentials(message):
#     "Access database and fetch user credetials for verification"
#     #could use actual sql database or just a csv file to mock it
#     #need a function to seach through sql database and return true if found
#     #found = verify_database(message.doctorID, message.doctorPW, message.securityAns, message.patientID)
#     if found and verify_ds(message.ds):
#         return True
#     else:
#         return False



(server, port) = ('', 8080)

httpd = http.server.HTTPServer((server, port), S)
print("serving at port", port)
httpd.serve_forever()

# while True:
#     client, addr = soc.accept()
#     print("Connection from", addr)
#     message = client.recv(1024)
#     if message is not None:
#         decrypted_message = decrypt_message(message)
#         json_message = json.loads(decrypted_message)
#         if verify_creditials(json_message):
#                 ticket = create_ticket(json_message)
#                 serialized_ticket = json.dumps(ticket)
#                 encrypted_ticket = encrypt_ticket(serialized_ticket)
#                 client.send(encrypted_ticket)
