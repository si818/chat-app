import socket

def run_server():
    # Create a socket that communicates over IPv4 network using the TCP protocol
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Assign an IP address and a port number to this socket instance
    server_address = ('localhost', 9999)
    
    try:
        server.bind(server_address)
        server.listen()
        
        print(f"Server listening on {server_address}")

        # Accept the incoming connections
        client, addr = server.accept()

        done = False

        while not done:
            message = client.recv(1024).decode('utf-8')
            if message == 'exit':
                done = True
            else:
                print(message)
            
            response = input("Server: ")
            client.send(response.encode('utf-8'))
            
    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the client socket and the server socket
        client.close()
        server.close()

if __name__ == "__main__":
    run_server()
