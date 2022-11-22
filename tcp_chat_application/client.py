import socket
import sys
import threading

HEADER = 64
PORT = 55555
HOST = "192.168.133.68"
ADDR = (HOST, PORT)


def send(clientObject, msgToSend):
    msgLength = len(msgToSend) + 1
    msgToSend = msgToSend.encode()
    headerMsg = str(msgLength).encode()
    headerMsg += b" " * (HEADER - int(msgLength))
    clientObject.send(headerMsg)
    clientObject.send(msgToSend)
    return


def recv(conn):
    msgLength = conn.recv(HEADER).decode()
    if msgLength:
        msg = conn.recv(int(msgLength)).decode()
    return msg


def threadInput(clientObject, username):
    while True:
        try:
            msgToSend = input(f"{username}> ")
            if msgToSend and msgToSend.strip():
                if msgToSend == "exit":
                    send(clientObject, msgToSend)
                    break
                else:
                    send(clientObject, msgToSend)
            else:
                continue
        except (KeyboardInterrupt, EOFError):
            send(clientObject, "exit")
            break
    sys.exit(0)


def threadOutput(clientObject, user):
    while True:
        try:
            msgToPrint = recv(clientObject)
            if msgToPrint.split(">")[0] == user:
                continue
            elif msgToPrint != "Server> Bye bye !":
                print()
                print(msgToPrint)

            else:
                print()
                print(msgToPrint)
                break
        except:
            continue
    clientObject.close()
    sys.exit(0)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(ADDR)
    user = input("Server> Choose your nickname : ")
    send(sock, user)
    tO = threading.Thread(target=threadOutput, args=(sock, user))
    tI = threading.Thread(target=threadInput, args=(sock, user))
    try:
        tO.start()
        tI.start()
    except (KeyboardInterrupt, SystemExit):
        print()


main()
