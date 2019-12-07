import http.client
from cryptography.fernet import Fernet
import json
import time

doc_as_file = open("docaskey.txt","r")
doc_as_key = doc_as_file.read().encode()
doc_as_file.close()

fernet_as = Fernet(doc_as_key)

def create_auth_as():
    """create the authentication package to send to as as a encrypted serialized json"""
    doctor_id = input('enter Doctor ID\n>')
    password = input('enter Doctor PW\n>')
    patient_id = input('enter Patient ID\n>')
    timestamp = time.time()
    auth_json = {
        "doctorID": doctor_id,
        "password": password,
        "patientID": patient_id,
        "timestamp": timestamp
    }
    serialized_json = json.dumps(auth_json)
    byte_serialized_json = serialized_json.encode()
    encrypted_json = fernet_as.encrypt(byte_serialized_json)
    return encrypted_json

def receive_ticket(raw_response):
    """receive the response from as and decrypt and extract the ticket as a string"""
    plaintext_bytes = fernet_as.decrypt(raw_response)
    plaintext = plaintext_bytes.decode()
    return plaintext


while True:
    print("\n-------------")
    # get server ip and port
    # while True:
    #     cmd = input('enter \'server port\'\n>')
    #     try:
    #         server, port = cmd.split()
    #         # localhost
    #         # 8080(AS) or 8081(RS)
    #         break;
    #     except:
    #         print("invalid input")
    server = 'localhost'
    port = 8080
    conn = http.client.HTTPConnection(server, port)

    headers = {'Content-type': 'text/plain'}

    if port == 8080:
        body = create_auth_as()
        conn.request('POST', '/post', body, headers)
        http_response = conn.getresponse()
        message = http_response.read()
        # print(message.decode())
        ticket = receive_ticket(message)
        # print(ticket)

    if port == 8081:
        body = create_auth_as()
        conn.request("POST", "", body)
        raw_response = conn.getresponse()
        ticket = receive_ticket(raw_response)

    print("Session completed\nClosing connection")
    conn.close()
