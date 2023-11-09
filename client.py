import socket

def run_client():
    # Connect to the already existing server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(("localhost", 9999))

        done = False

        while not done:
            message = input("Client: ")
            client.send(message.encode('utf-8'))

            response = client.recv(1024).decode('utf-8')
            if response == 'exit':
                done = True
            else:
                print(response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    run_client()
