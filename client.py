import socket

# Connect to the already existing server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

done = False

while not done:
    client.send(input("Server: ").encode('utf-8'))
    message = client.recv(1024).decode('utf-8')
    if message == 'exit':
        done = True
    else:
        print(message)
    
client.close()