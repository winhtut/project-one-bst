import socket

class Client:
    def __init__(self):
        self.target_host = 'localhost'
        self.target_port = 9998

    def runClient(self,data:'register or lgoin'):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_host, self.target_port))

        client.send(data)

        recvFromServer = client.recv(4096)

        recvFromServer= recvFromServer.decode('utf-8')
        print(type(recvFromServer))
        status , message = recvFromServer.split(' ')

        if status == '201':
            print( status , message)
        elif status == '200':
            print(status , message)
            print("you can do transtion now ")
            data = '3'+' '+'uname'+' '+'acceptName'
            data=bytes(data,'utf-8')
            try:
                self.runClient(data)
                print('success')
            except Exception as err:
                print(err)

        client.close()

    def option(self):
        option = input("[+]Press-1 to Register\n[+]Press-2 to Login!")
        if option=='1':
            r_name = input("Enter username to Register=>:")
            r_pw = input("Enter password to Register=>:")
            r_pw2 = input("Enter password again to confirm=>:")
            if r_pw == r_pw2:
                r_allData=option+' '+r_name+' '+r_pw
                r_allData:bytes = bytes(r_allData,'utf-8')
                self.runClient(r_allData)
        elif option=='2':
            l_name = input("Enter username to Login=>:")
            l_pw = input("Enter password to Login=>:")
            l_allData = option+' '+l_name+' '+l_pw
            l_allData:bytes = bytes(l_allData,'utf-8')
            self.runClient(l_allData)

if __name__ == "__main__":
    tcpClient:Client=Client()
    while True:
        tcpClient.option()





