import socket
import json

__public_key = 56789
__private_key = 98765
__shared_key = 11111

def server_hello():
    "Creates JSON containing server's public key"
    hello = {
        "key": __public_key
    }
    serialized_hello = json.dumps(hello)
    return serialized_hello

def decrypt_message(self, ciphertext):
    "Decrypt ciphertext into plaintext using private key"
    plaintext = ciphertext
    return plaintext

def decrypt_ticket(self, ticket):
    "Decrypt ticket using shared key"
    return self.ticket

def verify_ds(ds):
    "Check that digital signature affirms identity"

    return

def fetch_record(self, patient):
    "Fetch patients records"
    #Search and return records from database
    return record

def encrypt_record(self, record, key):
    "Encrypt records to send"
    self.record = record
    return self.record

def ticket_validation(self, message):
    "Verify received ticket has proper clearance to access records"
    serialized_ticket = decrypt_ticket(message.ticket)
    ticket = json.loads(serialized_ticket)
    #use arbitrary value for timestamp tolerances
    if (message.doctorID == ticket.doctorID) \
            and (message.doctorPW == ticket.doctorPW) \
            and ((message.timestamp - ticket.timestamp) < 10)\
            and verify_ds(message.ds):
        valid = True
    else:
        valid = False
    return valid

soc = socket.socket()
print("Socket created")

port = 10001

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
        if ticket_validation(json_message):
            record = fetch_record(json_message.patient)
            serialized_record = json.dumps(record)
            encrypted_record = encrypt_record(serialized_record, message.publicKey)
            client.send(encrypted_record)