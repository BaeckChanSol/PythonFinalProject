import telepot
import threading
import time
import socket
HOST = ''
PORT = 50007

class Telegram:
    def process(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
            return
        text = msg['text']
        args = text.split(' ')
        print(chat_id)
        print(args)
        if args[0] in self.data.keys() and len(args) == 1:
            if type(self.data[args[0]]) == type(""):
                self.sendMessage(chat_id, self.data[args[0]])
            if type(self.data[args[0]]) == type([]):
                for str in args[0]:
                    self.sendMessage(chat_id, str)
            self.DelDataInList(args[0])
        else:
            self.sendMessage(chat_id, "요청되지 않은 실종 아동 정보 데이터 요청코드입니다.")

    def __init__(self):
        ID = ''
        PASS = ''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))


        self.bot = telepot.Bot(ID+':'+PASS)
        self.bot.message_loop(lambda msg : Telegram.process(self, msg))
        self.data = {}
        print("텔레그렘 봇 작동을 개시합니다.")
        while 1:
            self.socket.listen(1)
            conn, addr = self.socket.accept()
            print('Connected by', addr)

            data = conn.recv(1024).decode().split()
            print(data)
            tmp = []
            if len(data) >= 2:
                for i in range(1, len(data)):
                    tmp.append(data[i])
                self.addDatatoList(data[0], tmp)
            conn.close()


    def checkTelegramBot(self):
        return self.bot.getMe()
    def sendMessage(self, ID, Message):
        self.bot.sendMessage(ID, Message)

    def addDatatoList(self, code, str):
        self.data[code] = str
        threading.Timer(600, lambda code : self.DelDataInList(code)).start()
    def DelDataInList(self, code):
        if code in self.data.keys():
            del self.data[code]


Telegram()