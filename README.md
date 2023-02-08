# Distributed-System

This is a system that supports a TCP server that accepts and holds a maximum of N clients (where N is configurable).

The clients send commands to the server which distributes them among the clients.

## Techologies and Tools

- Python
- Sockets

## Features

- The clients are assigned ranks on first-come-first-serve basis.The ranks are from 0–N, 0 being the highest rank.
- Only a client with a lower rank can execute a command of a higher rank client. 
- Higher rank clients cannot execute commands by lower rank clients, so these commands are rejected. 
- Logs of different events for system monitoring

The demo below shows a distributed system where commands send by one client are sent to another client.

![dist](https://user-images.githubusercontent.com/74382189/217649876-848d5711-2939-4511-b2da-44707f742eda.jpg)

## Getting started

Clone the repository

cd into that directory 

> Ensure you have Python installed. To check if you have Python you can run `python -V` or `python3 -V` if you are on a mac.

Run the server file using `python server.py`

Enter the number of clients expected when prompted.

Connect the clients to the server by running `python client.py`

Send a message to the server and the command will be distributed to other clients based on their ranks.

### References
- [Sockets](https://docs.python.org/3/howto/sockets.html#socket-howto)

### To-do
- Improve system to become a load balancer.
