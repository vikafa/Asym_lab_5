import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g = random.randint(2, 73), random.randint(2, 73)
a = random.randint(2, 10)
A = (g ** a) % p
sock.send(pickle.dumps((p, g, A)))

msg = pickle.loads(sock.recv(1024))
B = msg

K = (B ** a) % p
print("Client's calculated key:", K)

message = "Hello, server!"
encrypted_message = ''.join([chr(ord(char) + K) for char in message])
sock.send(encrypted_message.encode())

encrypted_response = sock.recv(1024).decode()
decrypted_response = ''.join([chr(ord(char) - K) for char in encrypted_response])
print("Server's response:", decrypted_response)

sock.close()
