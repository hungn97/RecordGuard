import http.client
from cryptography.fernet import Fernet
import sys
import json
import time

doc_as_key = open("docaskey.txt","r")
fernet_as = Fernet(doc_as_key)

def create_auth_as():
    doctor_id = input('Doctor ID')
    password = input('Doctor PW')
    patient_id = input('Patient ID')
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
    plaintext_bytes = fernet_as.decrypt(raw_response)
    plaintext = plaintext_bytes.decode()
    return plaintext


#get server ip and port
server = sys.argv[1] #should be localhost 127.0.0.1
port = sys.argv[2]  #8080(AS) or 8081(RS)

conn = http.client.HTTPConnection(server, port)

while True:
    if port == 8080:
        body = create_auth_as()
        conn.request("POST", "", body)
        raw_response = conn.getresponse()
        ticket = receive_ticket(raw_response)


