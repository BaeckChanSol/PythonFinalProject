from tkinter import *
from tkinter import font
from DataBase import  *
from GraphData import *
from Gmap import *
from tkinter import messagebox
import webbrowser
from urllib import parse
import base64
from PIL import Image,ImageTk
from io import BytesIO
from Gmail import *
import spam
class FrameWork:
    def __init__(self):
        # 데이터 베이스 생성
        self.param = "&rowSize=8"
        self.index = 1
        #window 생성
        self.window = Tk()
        self.window.title("Find for")
        self.window.geometry("800x600")
        self.window.configure(bg="silver")
        self.fontstyle = font.Font(self.window, size = 12, weight='bold', family = 'Consolas')
        self.fontstyle2 = font.Font(self.window, size=10, weight='bold', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=8, weight='bold', family='Consolas')
        self.ectType = {'010': "정상", '020': "가출인", '040': "시설보호무연고자", '060': '지적장애인', '061': '지적장애인(18세미만)', \
                        '062': '지적장애인(18세이상)', '070': '치매질환자', '080': '불상(기타)'}
        #전체 버튼 생성 함수
        self.setupButton()
        #전체 글자 출력 함수
        self.setupLabel()
        #전체 입력 부분 생성 함수
        self.setupEntry()
        #라디오 버튼 생성 함수
        self.setupRadio()
        #리스트 생성 함수
        self.setupListBox(self.index)

        #실종아동 이미지용 라벨
        self.photo = Canvas(self.window, width=200,height=200, bg='white')
        self.photo.place(x=10,y=10)

        #그래프 캠버스
        self.GraphCanvas = Canvas(self.window,width=340,height=370,bg="white")
        self.GraphCanvas.place(x=440,y=10)
        self.DownloadGraphData()
        self.DrawGraphCanvas()
        self.window.mainloop()

    def DownloadGraphData(self):
        self.GraphData = {};
        self.GraphData["010"] = (GraphData(1, "&rowSize=1&writngTrgetDscds=" + "010").getPage())
        self.GraphData["020"] =( GraphData(1, "&rowSize=1&writngTrgetDscds=" + "020").getPage())
        self.GraphData["040"] = (GraphData(1, "&rowSize=1&writngTrgetDscds=" + "040").getPage())
        self.GraphData["060"] = (GraphData(1, "&rowSize=1&writngTrgetDscds=" + "060").getPage())
        self.GraphData["061"] = (GraphData(1, "&rowSize=1&writngTrgetDscds=" + "061").getPage())
        self.GraphData["062"] = (GraphData(1, "&rowSize=1&writngTrgetDscds=" + "062").getPage())
        self.GraphData["070"] = (GraphData(1, "&rowSize=1&writngTrgetDscds=" + "070").getPage())
        self.GraphData["080"] = (GraphData(1, "&rowSize=1&writngTrgetDscds=" + "080").getPage())

    def DrawGraphCanvas(self):
        maxCount = max(self.GraphData.values())
        dataCode = ["010", "020", "040", "060", "061", "062", "070", "080"]
        for i in range(8):
            self.GraphCanvas.create_rectangle(40 * i + 20, 340, 40 * i + 45, 370 - (30+300 * self.GraphData[dataCode[i]] / maxCount),fill='black')
            self.GraphCanvas.create_text(40 * i + 32 ,  370 - (40+300 * self.GraphData[dataCode[i]] / maxCount)\
                                         , text = str(self.GraphData[dataCode[i]]), font=self.fontstyle3)
            self.GraphCanvas.create_text(40 * i + 32, 350, text=dataCode[i],font=self.fontstyle)
    def setupListBox(self, num):
        #리스트 생성시 정보 불러오기
        self.listBox = Listbox(self.window, width=58, height=8, font=self.fontstyle2)
        self.listBox.place(x=10, y=250)
        self.listBoxCount = 8
        try:
            self.data = DataBase(num, self.param)
            for i in range(8):
                self.listBox.insert(i, self.data.toStringData(i))
        except:
            messagebox.showinfo(title="XML 관련 안내",message="XML 데이터 로드에 실패하였습니다.")


    def setupButton(self):
        self.gMapImage = PhotoImage(file = "구글지도.png")
        self.telegramImage = PhotoImage(file="텔레그램.png")
        self.gMailImage = PhotoImage(file="G메일.png")

        #구글맵 버튼
        self.GMapButton = Button(self.window, image = self.gMapImage, command=self.pressedGMap)
        self.GMapButton.config(image=self.gMapImage)
        self.GMapButton.place(x=440, y=450)

        #텔레그램 버튼
        self.TelegramButton = Button(self.window,image = self.telegramImage, command=self.pressedTelegram)
        self.TelegramButton.place(x=560, y=450)

        #GMail 버튼
        self.GMailButton = Button(self.window,image = self.gMailImage, command=self.pressedGMail)
        self.GMailButton.place(x=680, y=455)

        #검색 버튼
        self.SearchButton = Button(self.window,text = "검색", width = 8, height = 1,font = self.fontstyle, command = self.pressedSearch)
        self.SearchButton.place(x=340,y=555)

        #실종 아동 리스트 페이지 넘기기용
        self.PageUpButton = Button(self.window,text = "<", width = 8, height = 1,font = self.fontstyle, command = self.pressedPrew)
        self.PageUpButton.place(x=10, y=400)


        self.PageDownButton = Button(self.window, text=">", width=8, height=1, font=self.fontstyle, command=self.pressedNext)
        self.PageDownButton.place(x=340, y=400)

        # 정보 갱신 버튼
        self.PageUpButton = Button(self.window, text="정보 갱신", width=12, height=1, font=self.fontstyle,
                                   command=self.pressedRenewal)
        self.PageUpButton.place(x=160, y=400)

        self.DetailInfo = Button(self.window, text="상세", width=8, height=1, font=self.fontstyle2, command=self.pressedInfo)
        self.DetailInfo.place(x=580, y=410)

    def pressedInfo(self):
        self.miniWindow2 = Tk()
        fontstyle = font.Font(self.miniWindow2, size=10, weight='bold', family='Consolas')
        dataCode = ["010", "020", "040", "060", "061", "062", "070", "080"]
        for i in range(8):
            Label(self.miniWindow2,width = 20,  text=dataCode[i] + " : " + self.ectType[dataCode[i]], font = fontstyle, anchor=W).pack()
        Button(self.miniWindow2, text="닫기", width=8, height=1, font=fontstyle, command=self.DestroyMini).pack()
        self.miniWindow2.mainloop()
    def DestroyMini(self):
        self.miniWindow2.destroy()

    def setupLabel(self):
        #검색한 결과 라벨
        self.LResultName = Label(text="이름: ", font = self.fontstyle, bg='silver')
        self.LResultName.place(x=220,y=10)


        self.LResultGender = Label(text="성별: ", font=self.fontstyle, bg='silver')
        self.LResultGender.place(x=220, y=55)

        self.LResultTime = Label(text="발생 일시: ",  font=self.fontstyle, bg='silver')
        self.LResultTime.place(x=220, y=100)

        self.LResultAge = Label(text="당시 나이: ", font=self.fontstyle, bg='silver')
        self.LResultAge.place(x=220, y=145)

        self.LResultCurrentAge = Label(text="현재 나이: ", font=self.fontstyle, bg='silver')
        self.LResultCurrentAge.place(x=220, y=185)

        self.LResultRemarks = Label(text="비고: ",font=self.fontstyle3,bg='silver')
        self.LResultRemarks.place(x=10,y=220)

        self.LResultPoint = Label(text="각 실종자 분류 별 그래프", font=self.fontstyle, bg='silver', anchor="center")
        self.LResultPoint.place(x=525, y=390)

        #검색하는 곳 라벨
        self.LSearchName = Label(text = "이름:", width = 8, height = 1, font = self.fontstyle, bg='silver')
        self.LSearchName.place(x=-10,y=450)

        self.LSearchAge = Label(text="당시 나이:", width=8, height=1, font=self.fontstyle, bg='silver')
        self.LSearchAge.place(x=240, y=450)

        self.LSearchGender = Label(text="성별:", width=8, height=1, font=self.fontstyle, bg='silver')
        self.LSearchGender.place(x=-10, y=485)

        self.LSearchPoint = Label(text="발생 장소:", width=8, height=1, font=self.fontstyle, bg='silver')
        self.LSearchPoint.place(x=10, y=520)

        self.LSearchTime = Label(text="발생 날짜:", width=8, height=1, font=self.fontstyle, bg='silver')
        self.LSearchTime.place(x=10, y=555)

        #우측 아래 버튼의 라벨
        self.LGmailText = Label(text="지도 열기", font = self.fontstyle ,bg = 'silver')
        self.LGmailText.place(x = 460, y=560)

        self.LTelegramText = Label(text="Telegram 전송", font=self.fontstyle, bg='silver')
        self.LTelegramText.place(x=555, y=560)

        self.LTelegramText = Label(text="GMail 전송", font=self.fontstyle, bg='silver')
        self.LTelegramText.place(x=690, y=560)

    def setupEntry(self):
        #이름 입력받는 Entry
        self.name_var = StringVar()
        self.ESearchName = Entry(self.window,font = self.fontstyle, width = 19, textvariable=self.name_var)
        self.ESearchName.place(x=50,y=450)

        #나이 입력받는 Entry
        self.age_var = StringVar()
        self.ESearchAge = Entry(self.window,font = self.fontstyle, width=11, textvariable=self.age_var)
        self.ESearchAge.place(x = 320,y=450)

        #실종사건 발생장소 입력받는 Entry
        self.point_var = StringVar()
        self.ESearchPoint = Entry(self.window, font=self.fontstyle, width=36, textvariable=self.point_var)
        self.ESearchPoint.place(x=90, y=520)

        #실종사건 발생날짜 입력받는 Entry
        self.date_var = StringVar()
        self.ESearchTime = Entry(self.window, font=self.fontstyle, width=25, textvariable=self.date_var)
        self.ESearchTime.place(x=90, y=555)

    def setupRadio(self):
        #성별 받는 라디오 버튼
        self.gender_var = IntVar()
        self.RSearchMale = Radiobutton(self.window,text = '남자',value = 1, variable = self.gender_var, font=self.fontstyle,bg = 'silver')
        self.RSearchMale.place(x=50,y=485)

        self.RSearchFemale = Radiobutton(self.window, text='여자', value=2, variable=self.gender_var, font=self.fontstyle, bg='silver')
        self.RSearchFemale.place(x=200, y=485)

        self.RSearchFemale = Radiobutton(self.window, text='모두', value=3, variable=self.gender_var, font=self.fontstyle, bg='silver')
        self.RSearchFemale.place(x=350, y=485)

    def pressedGMail(self):
        try:
            person = self.data.getData(self.listBox.curselection()[0])
            self.message = ["이름 : " + str(person["name"]), "성 : " + str(person["gender"]),
                      "나이 : " + str(person["age"]) + "->" + str(person["ageNow"])
                      ,"지역: "+ str(person["occrAdres"]), "발생 일시 : " + person["occrde"] ,
                            "기타 사항 : "+ self.ectType[person["etc"]]]
            with open("picture.gif","wb") as f:
                f.write(base64.b64decode(person["photo"]))
            print(self.message)
        except:
            messagebox.showinfo(title="메일 이용 안내", message="메일 전송 전에 데이터를 선택해주세요.")
            return

        self.miniWindow = Tk()
        fontstyle = font.Font(self.miniWindow, size=10, weight='bold', family='Consolas')
        Label(self.miniWindow,text="이메일").grid(row=0,column=0)
        self.emailstr = StringVar()
        self.miniEntry = Entry(self.miniWindow,textvariable=self.emailstr)
        self.miniEntry.grid(row=0,column=1)
        Button(self.miniWindow, text="데이터 전송", font=fontstyle, command=self.PressedsendMail).grid(row=0,column=2)
        self.miniWindow.mainloop()

    def PressedsendMail(self):
        to = self.miniEntry.get()
        Gmail.sendMessage(to, "실종 아동 데이터", self.message)
        self.miniWindow.destroy()
    def pressedGMap(self):
        try:
            person = self.data.getData(self.listBox.curselection()[0])
        except:
            messagebox.showinfo(title="지도 이용 안내",message="지도를 열고 싶은 데이터를 선택해주세요.")
            return
        Gmap.updateLocation(person["occrAdres"])
        webbrowser.open_new('osm.html')

    def pressedTelegram(self):
        import socket
        data = ""
        try:
            person = self.data.getData(self.listBox.curselection()[0])
            with open("picture.gif","wb") as f:
                f.write(base64.b64decode(person["photo"]))
            data += "이름 : " +person["name"] + "\t"
            data += "성별 : " +person["gender"] + "\t"
            data += "주소 : " +person["occrAdres"]  + "\t"
            data += "분류 : " +self.ectType[person["etc"]] + "\t"
            data += "발생일시 : " +person["occrde"] + "\t"
            data += "현재나이 ; " +person["ageNow"] + "\t"
            data += "당시나이 : " +person["age"] + "\t"
            data += "발생장소 : " +person["occrAdres"]
        except:
            messagebox.showinfo(title="텔레그램 이용 안내",message="정보 갱신을 통해 보내고자하는 데이터를 선택해주세요.")
            return
        HOST = '127.0.0.1'  # localhost
        PORT = 50007  # 서버와 같은 포트를 사용함
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 소켓 생성
            s.connect((HOST, PORT))
            s.send(data.encode())  # 문자를 보냄
            code = s.recv(1024)  # 서버로 부터 정보를 받음
            s.close()
            print(code.decode())
            messagebox.showinfo(title="텔레그램 이용 안내",message="텔레그램 데이터 전송 완료.\n텔레그렘 봇에 " + code.decode() + "를 입력해주세요.")
        except:
            messagebox.showinfo(title="텔레그램 이용 안내",message="텔레그램 서버가 닫혀있습니다.")
            return

    def pressedSearch(self):
        self.param = "&rowSize=8"
        name = self.name_var.get()
        if name != "":
            self.param += "&nm="+parse.quote(name)
        age = self.age_var.get()
        if age != "":
            self.param += "&age1="+age
            self.param += "&age2=" + age
        area = self.point_var.get()
        if area != "":
            self.param += "&occrAdres="+parse.quote(area)
        time = self.date_var.get()
        if time != "":
            self.param += "&detailDate1="+time
            self.param += "&detailDate2=" + time
        gender = self.gender_var.get()
        if gender == 1:
            self.param += "&sexdstnDscd=" + str(gender)
        elif gender == 2:
            self.param += "&sexdstnDscd=" + str(gender)
        self.index = 1
        self.setupListBox(self.index)

    def pressedPrew(self):
        #실종아동 리스트에서 < 버튼 눌렀을시
        if self.index <= 1:
            self.index = 1
        else:
            self.index  -= 1
        self.setupListBox(self.index)

    def pressedNext(self):
        #실종아동 리스트에서 > 버튼 눌렀을시
        self.index += 1
        self.setupListBox(self.index)








    def pressedRenewal(self):
        #리스트 눌러졌을 때의 처리
        try:
            person = self.data.getData(self.listBox.curselection()[0])
            self.LResultName.configure(text= "이름: " + person["name"])
            self.LResultGender.configure(text="성별: " + person["gender"])
            self.LResultRemarks.configure(text= "비고: " + person["occrAdres"] + "/ " + self.ectType[person["etc"]]\
                                          + " / " + spam.calc(person["occrde"]) + " 째 실종")
            self.LResultTime.configure(text= "발생 일시: " + person["occrde"])
            self.LResultCurrentAge.configure(text="현재 나이: " + person["ageNow"])
            self.LResultAge.configure(text="당시 나이: " + person["age"])
        except:
            messagebox.showinfo(title="갱신 안내", message="갱신하고자 하는 데이터를 선택해주세요.")
        try:
            img = ImageTk.PhotoImage(Image.open(BytesIO(base64.b64decode(person['photo']))))
            self.photo.delete("all")
            self.photo.create_image(100, 100, image=img)
            self.photo.image = img
        except:
            self.photo.delete("all")
            messagebox.showinfo(title="사진 미출력", message="본 데이터에는 사진 데이터가 없습니다.")

FrameWork()