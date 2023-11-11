import socket

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9999)
    
    try:
        server.bind(server_address)
        server.listen()
        
        print(f"Server listening on {server_address}")

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
        client.close()
        server.close()

if __name__ == "__main__":
    run_server()
