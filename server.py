import threading
import socket
import logging
logging.basicConfig(level=logging.INFO,
                    filename="server_log.log", filemode="a")


host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
N = int(input('Please configure the maximum connections needed ?'))
server.listen(N)
clients = []
commands = []


# Main function to receive the clients connection

def receive():
    while True:
        print('Server is listening..')
        client, address = server.accept()

        logging.info(f'connection is established with {str(address)}')

        clients.append(client)
        rank = clients.index(client)
        client_details = [rank, client]

        client_details[1].send(
            f'{client_details[0]} you are now connected!'.encode('utf-8'))

        thread = threading.Thread(
            target=handle_client, args=(client_details, clients))
        thread.start()


def handle_client(client_details, clients):
    while True:
        try:
            message = client_details[1].recv(1024).decode('utf-8')
            commands.append([client_details[0], message])

            if len(clients) > 1:
                if len(commands) > 1:
                    for i in range(1, len(commands)):
                        if commands[i][0] > commands[i-1][0] or commands[i-1][0] < commands[i][0]:

                            client_to = clients[commands[i][0]]
                            client_to.send(
                                f'command from client rank {commands[i-1][0]}: {commands[i-1][1]}!'.encode('utf-8'))
                            commands.pop(i-1)

                        elif commands[i-1][0] > commands[i][0]:

                            client_to = clients[commands[i-1][0]]

                            logging.info(
                                f'executing on client rank {commands[i-1][0]} total clients are {len(clients)}')
                            client_to.send(
                                f'command from client rank {commands[i][0]}: {commands[i][1]}!'.encode('utf-8'))
                            commands.pop(i)

                        else:
                            logging.info('command rejected')
                            continue
            else:
                continue
        except:
            client_details[1].close()

            # pop client from client list and all commands associated with client
            clients.pop(client_details[0])
            for i in range(len(commands)):
                if commands[i][0] == client_details[0]:
                    commands.pop(i)

            logging.exception('error')
            break


if __name__ == "__main__":
    receive()
