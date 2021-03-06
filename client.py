import http.client
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import pickle
import json
import time
import textwrap

wrapper = textwrap.TextWrapper(width=50)

doc_as_file = open("docaskey.txt","r")
doc_as_key = doc_as_file.read().encode()
doc_as_file.close()
fernet_as = Fernet(doc_as_key)

doc_rs_file = open("docrskey.txt","r")
doc_rs_key = doc_rs_file.read().encode()
doc_rs_file.close()
fernet_rs = Fernet(doc_rs_key)

with open("docprivatekey.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

def create_auth_as():
    """create the authentication package to send to as as a encrypted serialized json"""
    doctor_id = input('Enter Doctor ID\n>')
    password = input('Enter Doctor PW\n>')
    patient_id = input('Enter Patient ID\n>')
    timestamp = time.time()
    auth_json = {
        "doctorID": doctor_id,
        "doctorPW": password,
        "patientID": patient_id,
        "timestamp": timestamp
    }
    serialized_json = json.dumps(auth_json)
    byte_serialized_json = serialized_json.encode()
    encrypted_json = fernet_as.encrypt(byte_serialized_json)
    return encrypted_json

def create_auth_rs(ticket):
    doctor_id = input('Enter Doctor ID\n>')
    patient_id = input('Enter Patient ID\n>')
    timestamp = time.time()
    auth_json = {
        "doctorID": doctor_id,
        "patientID": patient_id,
        "timestamp": timestamp,
        "ticket": ticket
    }
    serialized_json = json.dumps(auth_json)
    byte_serialized_json = serialized_json.encode()
    signature = create_signature(byte_serialized_json)
    byte_message = merge_signature(auth_json, signature)
    encrypted_message = fernet_rs.encrypt(byte_message)
    return encrypted_message

def receive_ticket(message):
    """receive the response from as and decrypt and extract the ticket as a string"""
    plaintext_bytes = fernet_as.decrypt(message)
    plaintext = plaintext_bytes.decode()
    return plaintext

def receive_records(message):
    plaintext = fernet_rs.decrypt(message)
    json_message = json.loads(plaintext)
    return json_message

def create_signature(message):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def merge_signature(byte_serialized_json, signature):
    message_sig_json = {
        "content": byte_serialized_json,
        "signature": signature
    }
    serialized_message_sig = pickle.dumps(message_sig_json)
    return serialized_message_sig

while True:
    print("-------------------------------------------------")
    print("Client Start")
    print("-------------------------------------------------")
    # get server ip and port
    while True:
        cmd = input('Enter \'server:port\'\n>')
        try:
            server = cmd.split(':')[0]
            port = int(cmd.split(':')[1])
            # localhost
            # 8080(AS) or 8081(RS)
            break;
        except:
            print("Invalid input")

    conn = http.client.HTTPConnection(server, port)

    headers = {'Content-type': 'text/plain'}

    if port == 8080:
        print("\n\n-------------------------------------------------")
        print("Authentication")
        print("-------------------------------------------------")
        body = create_auth_as()
        conn.request('POST', '/post', body, headers)
        http_response = conn.getresponse()
        message = http_response.read()
        print("\n\n-------------------------------------------------")
        print("Received from port", port, ":")
        print("-------------------------------------------------")
        if message.decode() != "failed":
            ticket = receive_ticket(message)
            print(wrapper.fill(text=ticket))
        else:
            print("\nBad credentials . . . Authentication failed")

    if port == 8081 or port == 8082:
        body = create_auth_rs(ticket)
        conn.request('POST', '/post', body, headers)
        http_response = conn.getresponse()
        message = http_response.read()
        print("\n\n-------------------------------------------------")
        print("Received from port", port, ":")
        print("-------------------------------------------------")
        if message.decode() == "failed":
            print("\nAuthentication failed")
        elif message.decode() == "auth":
            print("\nTicket mismatch . . . Authentication failed")
        elif message.decode() == "timeout":
            print("\nTicket expired . . . Authentication failed")
        elif message.decode() == "signature":
            print("\nSignature validation error . . . Authentication failed")
        else:
            records = receive_records(message)
            print(json.dumps(records, indent=4))

    print("\n\n\nSession completed . . . Closing connection\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    conn.close()
