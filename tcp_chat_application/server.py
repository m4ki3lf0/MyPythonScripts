import logging
import queue
import socket
import threading

HEADER = 64
PORT = 55555  # YOUR PORT HERE
HOST = "0.0.0.0"
ADDR = (HOST, PORT)

clientsObj = []
usernames = []
msgQueue = queue.Queue()


def recv(conn):
    while True:
        try:
            msgLength = conn.recv(HEADER).decode()
            if msgLength:
                msg = conn.recv(int(msgLength)).decode()
            return msg
        except Exception as e:
            return "WinError"


def remove(sockObject, user):
    clientsObj.remove(sockObject)
    usernames.remove(user)
    msgToQueue = f"Server> {user} has disconnected."
    msgQueue.put(msgToQueue)
    logging.info(f"Client {user} has disconnected.")
    return


def send(clientObject, msgToSend):
    msgLength = len(msgToSend) + 1
    msgToSend = msgToSend.encode()
    headerMsg = str(msgLength).encode()
    headerMsg += b" " * (HEADER - int(msgLength))
    clientObject.send(headerMsg)
    clientObject.send(msgToSend)
    return


def threadClient(sockObject, user):
    while True:
        try:
            msg = recv(sockObject)
            if msg != "exit":
                msgToQueue = f"{user}> " + msg
                msgQueue.put(msgToQueue)
            elif msg == "WinError":
                remove(sockObject, user)
                break
            else:
                msgToUser = f"Server> Bye bye !"
                send(sockObject, msgToUser)
                remove(sockObject, user)
                break
        except TimeoutError:
            break
    sockObject.close()
    return


def threadServer():
    logging.debug("Serveur is starting.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen()
    logging.debug("Server is listening.")
    while True:
        socketObject, ip = sock.accept()
        clientsObj.append(socketObject)

        user = recv(socketObject)
        print(f"Nouveau client : {user}, {ip}")
        if user != "SocketCloseBeforeResponse":
            usernames.append(user)
            logging.info(f"New client {user}: {ip}")
            threading.Thread(target=threadClient, args=(socketObject, user)).start()
        else:
            clientsObj.remove(socketObject)
            socketObject.close()


def threadBroadcast():
    while True:
        msgToBroadcast = msgQueue.get()
        print(msgToBroadcast)
        logging.info(msgToBroadcast)
        for client in clientsObj:
            send(client, msgToBroadcast)


def main():
    logging.basicConfig(
        filename="./log.txt",
        level=logging.DEBUG,
        format="%(asctime)s: %(message)s",
        filemode="a",
    )
    threading.Thread(target=threadServer).start()
    threading.Thread(target=threadBroadcast).start()


main()
