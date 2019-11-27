import socket

__private_key = 54321
__shared_key = 11111

def decrypt_message(self, ciphertext):
    "Decrypt ciphertext into plaintext using private key"
    plaintext = ciphertext
    return plaintext

def decrypt_ticket(self, ticket):
    "Decrypt ticket using shared key"
    return self.ticket

def parse_plaintext(self, plaintext):
    "Separate ticket from the rest of the plaintext"
    return message, ticket

def create_record(self, patient):
    "Fetch patients records"

def encrypt_record(self, record, key):
    "Encrypt records to send"
    self.record = record
    return self.record

def ticket_validation(self, message, ticket):
    "Verify received ticket has proper clearance to access records"

    if (message.username == ticket.username) \
            and (message.password == ticket.password) \
            and ((message.timestamp - ticket.timestamp) < 10): #arbitrary value for timeframe of messages
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
    client.send("Established contact with record server")
    client.send("Record server public key: 12345")
    message = None
    message = client.recv(1024)
    if message:
        plaintext = decrypt_message(message)
        message, encrypted_ticket = parse_plaintext(plaintext)
        ticket = decrypt_ticket(encrypted_ticket)
        if ticket_validation(message, ticket):
            record = create_record(message.patient)
            encrypted_record = encrypt_record(record, message.key)
            client.send(encrypted_record)