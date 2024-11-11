import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)

    print("سرور آماده‌ی پذیرش ارتباط است...")
    client_socket, client_address = server_socket.accept()
    print(f"ارتباط برقرار شد با: {client_address}")

    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            print("ارتباط قطع شد.")
            break
        print(f"کلاینت: {message}")
        response = input("شما: ")
        client_socket.send(response.encode())
        if response.lower() == 'exit':
            break

    client_socket.close()
    server_socket.close()

if name == "__main__":
    start_server()