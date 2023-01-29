import threading
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


def client_receive():
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if len(data) > 0:
                print(data)

        except:
            print('Err!')
            client.close()
            break


def client_send():
    while True:
        command = input()
        client.send(command.encode('utf-8'))


receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
