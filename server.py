import socket

# Create a socket that communicates over IPv4 network using the TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assign an IP address and a port number to this socket instance
server_address = ('localhost', 9999)
server.bind(server_address)

# Prepare for incoming connections
server.listen()

# Accept the incoming connections
client, addr = server.accept()

done = False

while not done:
    message = client.recv(1024).decode('utf-8')
    if message == 'exit':
        done = True
    else:
        print(message)
    client.send(input("Client: ").encode('utf-8'))

client.close()
server.close()