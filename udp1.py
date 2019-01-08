from socket import *
def server():
    HOST=''
    PORT=12580
    BUFSIZ=1024
    ADDR=(HOST,PORT)

    udpsersock=socket(AF_INET,SOCK_DGRAM)
    udpsersock.bind(ADDR)

    while True:
        print('等待连接：')
        data,addr=udpsersock.recvfrom(BUFSIZ)
        print(data)
        udpsersock.sendto(bytes('收到',encoding='utf8'),addr)
    udpsersock.close()

if __name__=='__main__':
    server()