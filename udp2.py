from socket import *
def client():
    HOST='0.0.0.0'
    PORT=12580
    ADDR=(HOST,PORT)
    BUFSIZ=1024
    udpclient=socket(AF_INET,SOCK_DGRAM)
    while True:
        data=input(">")
        data=bytes(data,encoding='utf8')
        udpclient.sendto(data,ADDR)
        data,ADDR=udpclient.recvfrom(BUFSIZ)
        if not data:
            break
        print(data)
    udpclient.close()

if __name__=='__main__':
    client()