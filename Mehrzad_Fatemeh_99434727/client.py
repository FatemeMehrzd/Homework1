import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    print("ارتباط با سرور برقرار شد.")

    while True:
        message = input("شما: ")
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break
        response = client_socket.recv(1024).decode()
        if response.lower() == 'exit':
            print("ارتباط قطع شد.")
            break
        print(f"سرور: {response}")

    client_socket.close()

if name == "__main__":
    start_client()