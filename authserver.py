import socket

__private_key = 54321
__shared_key = 11111

def decrypt_message(ciphertext):
    "Decrypt ciphertext into plaintext using private key"
    plaintext = ciphertext
    return plaintext

def verify_ds(ds):
    "Check that digital signature affirms identity"
    return

def fetch_credentials(self, username, password, security_ans, patient):
    "Access database and fetch user credetials for verification"
    #could use actual sql database or just a csv file to mock it
    #if timestamp = verify_database(username, password, security_ans, patient):
    #else:
    #  timestamp = None
    return timestamp

def user_validation(self, message):
    "Verify received ticket has proper clearance to access records"
    valid = False
    timestamp = fetch_credentials(message.username, message.password, message.security_ans)
    if (message.timestamp - timestamp) < 10: #within acceptable range
        valid = True
    return valid

def create_ticket(username, password, timestamp):
    "Encapsulate and encode information using key shared only between AS and Record Server"
    #serialize and encrypt the ticket object
    return ticket

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
    client.send("Established contact with authentication server")
    client.send("authentication server public key: 12345")
    message = None
    message = client.recv(1024)
    if message:
        plaintext = decrypt_message(message)
        if user_validation(plaintext):
            ticket = create_ticket(plaintext.username, plaintext.password, plaintext.timestamp)
            client.send(ticket)