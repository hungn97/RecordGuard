import http.client
import http.server
from cryptography.fernet import Fernet
import json
import pickle
import textwrap

wrapper = textwrap.TextWrapper(width=50)

doc_rs_file = open("docrskey.txt","r")
doc_rs_key = doc_rs_file.read().encode()
doc_rs_file.close()
fernet_doc = Fernet(doc_rs_key)



def decrypt_message(message):
    """Decrypts message received from client with shared key"""
    plaintext = fernet_doc.decrypt(message)
    return plaintext

def split_signature(message):
    messsage_sig_json = pickle.loads(message)
    auth_json = messsage_sig_json["content"]
    signature = messsage_sig_json["signature"]
    return auth_json, signature

def modify_message(auth_json):
    modified_json = auth_json
    modified_json["doctorID"] = "30426205"
    modified_json["patientID"] = "2"
    modified_json["timestamp"] = auth_json["timestamp"] - 500
    return modified_json

def merge_signature(byte_serialized_json, signature):
    message_sig_json = {
        "content": byte_serialized_json,
        "signature": signature
    }
    serialized_message_sig = pickle.dumps(message_sig_json)
    return serialized_message_sig

def create_auth_rs(auth_json, signature):
    byte_message = merge_signature(auth_json, signature)
    encrypted_message = fernet_doc.encrypt(byte_message)
    return encrypted_message


class S(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        message = self.rfile.read(length)
        decrypted_message = decrypt_message(message)
        auth_json, signature = split_signature(decrypted_message)
        print("\n\n-------------------------------------------------")
        print("Received from port", port, ":")
        print("-------------------------------------------------")
        print("Ciphertext:\n", wrapper.fill(text=message.decode()))
        print("\nPlaintext:\n", json.dumps(auth_json, indent=4))
        print(signature)

        modified_json = modify_message(auth_json)

        outbound_message = create_auth_rs(modified_json, signature)

        conn = http.client.HTTPConnection("localhost", 8081)
        headers = {'Content-type': 'text/plain'}
        conn.request('POST', '/post', outbound_message, headers)
        http_response = conn.getresponse()
        relay_message = http_response.read()
        conn.close()

        self._set_headers()
        self.wfile.write(relay_message)



(server, port) = ('', 8082)

httpd = http.server.HTTPServer((server, port), S)
print("serving at port", port)
httpd.serve_forever()

