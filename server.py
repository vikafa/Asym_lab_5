import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8081

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

msg = pickle.loads(conn.recv(1024))
p, g, A = msg

b = random.randint(2, 10)
B = (g ** b) % p
conn.send(pickle.dumps(B))

K = (A ** b) % p
print("Server's calculated key:", K)

encrypted_message = conn.recv(1024).decode()
decrypted_message = ''.join([chr(ord(char) - K) for char in encrypted_message])
print("Client's message:", decrypted_message)

response = "Hi, client!"
encrypted_response = ''.join([chr(ord(char) + K) for char in response])
conn.send(encrypted_response.encode())

conn.close()
