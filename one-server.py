import socket
class Node:
    def __init__(self,data):
        self.CharAlphbet=data
        self.c_right=None
        self.c_left=None


def dataInsertion():
    root = Node('p')

    root.c_left = Node('h')
    root.c_left.c_left = Node('d')
    root.c_left.c_right = Node('l')
    root.c_left.c_left.c_left = Node('b')
    root.c_left.c_left.c_right = Node('f')
    root.c_left.c_right.c_left = Node('j')
    root.c_left.c_right.c_right = Node('n')
    root.c_left.c_left.c_left.c_left = Node('a')
    root.c_left.c_left.c_left.c_right = Node('c')
    root.c_left.c_left.c_right.c_left = Node('e')
    root.c_left.c_left.c_right.c_right = Node('g')

    root.c_left.c_right.c_left.c_left = Node('i')
    root.c_left.c_right.c_left.c_right = Node('k')
    root.c_left.c_right.c_right.c_left = Node('m')
    root.c_left.c_right.c_right.c_right = Node('o')

    root.c_right = Node('t')
    root.c_right.c_left = Node('r')

    root.c_right.c_right = Node('x')

    root.c_right.c_left.c_left = Node('q')
    root.c_right.c_left.c_right = Node('s')

    root.c_right.c_right.c_left = Node('v')
    root.c_right.c_right.c_right = Node('y')

    root.c_right.c_right.c_left.c_left = Node('u')
    root.c_right.c_right.c_left.c_right = Node('w')

    root.c_right.c_right.c_right.c_right = Node('z')
    return root

class LenghtBST:
    def __init__(self,data):
        self.data=data
        self.info=[]
        self.infoPw=[]
        self.left=None
        self.right=None

def RootLengthTree():
    root=None
    list_length=[16,8,24,4,12,20,28,2,6,10,14,18,22,26,29,1,3,5,7,9,11,13,15,17,19,21,23,25,27,30]
    length=len(list_length)
    print(length)

    for i in range(0,length):
        print("data",list_length[i])
        root = insert(root,list_length[i])
    return root

def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return LenghtBST(key)
    # Traverse to the right place and insert the node
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

class TCPserver:
    def __init__(self):
        self.server_ip='localhost'
        self.server_port = 9998
        self.sock = None
        self.AlphaRoot = dataInsertion()
        self.RLTroot = RootLengthTree()
        if self.AlphaRoot:
            print('AlphaDatabase created!')
            self.inorderForAlpha(self.AlphaRoot)
            print('\n')
        if self.RLTroot:
            print('[+][+] Root lenght tree created')
            self.inorderForRLT(self.RLTroot)
            print('\n')

    def inorderForRLT(self,RLTroot):
        if RLTroot is not None:
            self.inorderForRLT(RLTroot.left)
            print(RLTroot.data,' >',end=' ')
            self.inorderForRLT(RLTroot.right)

    def inorderForAlpha(self,AlphaRoot):
        if AlphaRoot is not None:
            self.inorderForAlpha(AlphaRoot.c_left)
            print(AlphaRoot.CharAlphbet,' >',end=' ')
            self.inorderForAlpha(AlphaRoot.c_right)


    def main(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen(1)
        print(f'[*] Listening on {self.server_ip}:{self.server_port} >:')
        while True:
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            self.handle_client(client)

    def handle_client(self,client):

        with client as self.sock:
            request = self.sock.recv(4096)
            client_sms=request.decode("utf-8")
            print(f'[*] Received:',client_sms)
            option , c_uname , c_pw=client_sms.split(' ')
            if option=='1':
                print("This is for registration")
                success =self.forRegistration(c_uname,c_pw)
                print('Testing for ',success)
                if success == 'success':
                    data = '201'+' '+'SuccessRegistration'
                    data = bytes(data,'utf-8')
                    self.sock.send(data)

            elif option=='2':
                self.loginAlpha(c_uname,c_pw)

            elif option=='3':
                print('Transtion proceed!')
                data = '301' + ' ' + 'fromOption3'
                data = bytes(data , "utf-8")
                self.sock.send(data)


    def forRegistration(self,uname , pw ):

        uname  = uname.lower()
        firstData =uname[0]

        Length =len(uname)
        success =self.searchInAlpha(self.AlphaRoot, uname, firstData,Length,pw)
        print('for registartion function',success)
        return success
    def searchInAlpha(self,AlphaRoot, uname , firstData , Lenght , pw ):
        success = None
        alphaNo =ord(AlphaRoot.CharAlphbet)
        firstNo = ord(firstData)
        if AlphaRoot is None:
            print('Alpha root is empty cannot be proceed!')
        if AlphaRoot.CharAlphbet == firstData:
            print("Alpha was found : ",AlphaRoot.CharAlphbet)
            success =self.insertInRLT(self.RLTroot,Lenght,uname,pw)
            print('Return from insertInRLT:',success)
            success = success
            return success
        elif alphaNo < firstNo :
            return self.searchInAlpha(AlphaRoot.c_right , uname , firstData , Lenght ,pw )
        elif alphaNo > firstNo:
            return self.searchInAlpha(AlphaRoot.c_left, uname, firstData, Lenght, pw)

    def insertInRLT(self,RLTroot , Lenght , uname , pw ):
        flag = None
        if RLTroot is None:
            print('RLT root is empty cannot be proceed!')
        if RLTroot.data == Lenght:
            print('for insertInRLT ',RLTroot.data )
            RLTroot.info.append(uname)
            RLTroot.infoPw.append(pw)
            flag = 'success'
            print(flag)
            return flag

        elif RLTroot.data < Lenght :
            return self.insertInRLT(RLTroot.right, Lenght , uname ,pw )
        elif RLTroot.data > Lenght:
            return self.insertInRLT(RLTroot.left, Lenght , uname ,pw )

    def loginAlpha(self,uname , pw ):
        uname  = uname.lower()
        firstData =uname[0]
        Length = len(uname)
        self.login_SearchInAlpha(self.AlphaRoot , uname , firstData , Length ,pw )

    def login_SearchInAlpha(self,AlphaRoot , uname , firstData , Lenght , pw):
        alphaNo = ord(AlphaRoot.CharAlphbet)
        firstNo = ord(firstData)
        if AlphaRoot is None:
            print('Alpha root is empty cannot be proceed!in Login!')
        if AlphaRoot.CharAlphbet == firstData:
            print("Alpha was found : ", AlphaRoot.CharAlphbet)
            self.login_serachinRLT(self.RLTroot, Lenght, uname, pw)

        elif alphaNo < firstNo:
            return self.login_SearchInAlpha(AlphaRoot.c_right, uname, firstData, Lenght, pw)
        elif alphaNo > firstNo:
            return self.login_SearchInAlpha(AlphaRoot.c_left, uname, firstData, Lenght, pw)

    def login_serachinRLT(self,RLTroot , Length , uname , pw ):
        if RLTroot is None:
            print('RLT root is empty cannot be proceed! in Login!')
        if RLTroot.data == Length:
            print('from Login_searchinRLT:',RLTroot.data )
            InfoNameLength = len(RLTroot.info)
            for i in range(0,InfoNameLength):
                if RLTroot.info[i] == uname and RLTroot.infoPw[i]==pw :
                    print("Login Success for User:",RLTroot.info[i])
                    data ='200'+' '+RLTroot.info[i]
                    data = bytes(data,'utf-8')

                    self.sock.send(data)
            data = '400' + '' +uname
            data = bytes(data,'utf-8')
            self.sock.send(data)


        elif RLTroot.data < Length :
            return self.login_serachinRLT(RLTroot.right, Length , uname ,pw )
        elif RLTroot.data > Length:
            return self.login_serachinRLT(RLTroot.left, Length , uname ,pw )

if __name__ == "__main__":
    tcpServer :TCPserver =TCPserver()
    tcpServer.main()