import socket
import json

__public_key = 12345
__private_key = 54321
__shared_key = 11111

conn = sqlite3.connect('doctor_data.db')

def server_hello():
    "Creates JSON containing server's public key"
    hello = {
        "publicKey": __public_key
    }
    serialized_hello = json.dumps(hello)
    return serialized_hello

def decrypt_message(ciphertext):
    "Decrypt ciphertext into plaintext using private key"
    plaintext = ciphertext
    return plaintext

def verify_ds(ds):
    "Check that digital signature affirms identity"

    return

def verify_credentials(message):
    "Access database and fetch user credetials for verification"
    #could use actual sql database or just a csv file to mock it
    #need a function to seach through sql database and return true if found
    #found = verify_database(message.doctorID, message.doctorPW, message.securityAns, message.patientID)
    if found and verify_ds(message.ds):
        return True
    else:
        return False

def create_ticket(message):
    ticket = {
        "doctorID": message.doctorID,
        "patientID": message.patientID,
        "timestamp": message.timestamp
    }
    return ticket

def encrypt_ticket(ticket):
    "Encrypts ticket as authentication for client"
    #use encryption from package
    return encrypted_ticket

soc = socket.socket()
print("Socket created")

port = 10000

soc.bind(('', port))
print("Socket binded to %s" %port)

soc.listen(1)
print("Socket is listening")

while True:
    client, addr = soc.accept()
    print("Connection from", addr)
    client.send(server_hello())
    message = client.recv(1024)
    if message is not None:
        decrypted_message = decrypt_message(message)
        json_message = json.loads(decrypted_message)
        if verify_creditials(json_message):
                ticket = create_ticket(json_message)
                serialized_ticket = json.dumps(ticket)
                encrypted_ticket = encrypt_ticket(serialized_ticket)
                client.send(encrypted_ticket)
