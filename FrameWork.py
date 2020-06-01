from tkinter import *
from tkinter import font
from DataBase import  *
class FrameWork:
    def __init__(self):
        # 데이터 베이스 생성
        self.data = DataBase()
        if self.data == None:
            print("XML 데이터 읽기를 실패하였습니다.")
            return None

        self.index = 1

        #window 생성
        self.window = Tk()
        self.window.title("Find for")
        self.window.geometry("800x600")
        self.window.configure(bg="silver")
        self.fontstyle = font.Font(self.window, size = 12, weight='bold', family = 'Consolas')
        self.fontstyle2 = font.Font(self.window, size=10, weight='bold', family='Consolas')
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

        #실종아동 이미지용 캔버스
        self.PhothCanvas = Canvas(self.window, width=200,height=200,bg="white")
        self.PhothCanvas.place(x=10,y=10)

        #지도용 캠버스
        self.MapCanvas = Canvas(self.window,width=340,height=370,bg="white")
        self.MapCanvas.place(x=440,y=10)

        self.window.mainloop()

    def setupListBox(self, num):
        #리스트 생성시 정보 불러오기
        self.listBox = Listbox(self.window, width=58, height=8, font=self.fontstyle2)
        self.listBox.place(x=10, y=250)
        self.listBoxCount = 8
        for i in range(8*(num-1), 8*num):
            self.listBox.insert(i, self.data.toStringData(i))


    def setupButton(self):
        #구글맵 버튼
        self.GMapButton = Button(self.window, width=14, height=6, command=self.pressedTelegram)
        self.GMapButton.place(x=440, y=450)

        #텔레그램 버튼
        self.TelegramButton = Button(self.window, width=14, height=6, command=self.pressedGMap)
        self.TelegramButton.place(x=560, y=450)

        #GMail 버튼
        self.GMailButton = Button(self.window, width=14, height=6, command=self.pressedGMail)
        self.GMailButton.place(x=680, y=450)

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

        self.LResultRemarks = Label(text="비고 사항: ",font=self.fontstyle2,bg='silver')
        self.LResultRemarks.place(x=10,y=220)

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

        self.LResultPoint = Label(text="발생 장소:", width=8, height=1, font=self.fontstyle, bg='silver')
        self.LResultPoint.place(x=460, y=400)

        #우측 아래 버튼의 라벨
        self.LGmailText = Label(text="구글 지도 열기", font = self.fontstyle ,bg = 'silver')
        self.LGmailText.place(x = 435, y=560)

        self.LTelegramText = Label(text="Telegram 전송", font=self.fontstyle, bg='silver')
        self.LTelegramText.place(x=555, y=560)

        self.LTelegramText = Label(text="GMail 전송", font=self.fontstyle, bg='silver')
        self.LTelegramText.place(x=690, y=560)

    def setupEntry(self):
        #이름 입력받는 Entry
        self.ESearchName = Entry(self.window,font = self.fontstyle, width = 19)
        self.ESearchName.place(x=50,y=450)

        #나이 입력받는 Entry
        self.ESearchAge = Entry(self.window,font = self.fontstyle, width=11)
        self.ESearchAge.place(x = 320,y=450)

        #실종사건 발생장소 입력받는 Entry
        self.ESearchPoint = Entry(self.window, font=self.fontstyle, width=36)
        self.ESearchPoint.place(x=90, y=520)

        #실종사건 발생날짜 입력받는 Entry
        self.ESearchTime = Entry(self.window, font=self.fontstyle, width=25)
        self.ESearchTime.place(x=90, y=555)

    def setupRadio(self):
        #성별 받는 라디오 버튼
        gender = IntVar()
        self.RSearchMale = Radiobutton(self.window,text = '남자',value = 1, variable = gender, font=self.fontstyle,bg = 'silver')
        self.RSearchMale.place(x=50,y=485)

        self.RSearchFemale = Radiobutton(self.window, text='여자', value=2, variable=gender, font=self.fontstyle, bg='silver')
        self.RSearchFemale.place(x=200, y=485)

        self.RSearchFemale = Radiobutton(self.window, text='모두', value=3, variable=gender, font=self.fontstyle, bg='silver')
        self.RSearchFemale.place(x=350, y=485)

    def pressedGMail(self):
        #GMail버튼 누를시
        pass

    def pressedGMap(self):
        #구글지도 버튼 누를시
        pass

    def pressedTelegram(self):
        #텔레그램 버튼 누를시
        pass

    def pressedSearch(self):
        #검색 버튼 누를시
        pass
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

    def ectType(self, person):
        #비고사항 구분
        if person == '010':
            return "정상"
        if person == '020':
            return "가출인"
        if person == '040':
            return "시설보호무연고자"
        if person == '060':
            return "지적장애인"
        if person == '061':
            return "지적장애인(18세미만)"
        if person == '062':
            return "지적장애인(18세이상)"
        if person == '070':
            return "치매질환자"
        if person == '080':
            return "불상(기타)"
        return ""


    def pressedRenewal(self):
        #리스트 눌러졌을 때의 처리
        person = self.data.getData(self.listBox.curselection()[0])
        self.LResultName.configure(text= "이름: " + person["name"])
        self.LResultGender.configure(text="성별: " + person["gender"])
        self.LResultRemarks.configure(text= "비고 사항: " + person["occrAdres"] + "/" + self.ectType(person["etc"]))
        self.LResultTime.configure(text= "발생 일시: " + person["occrde"])
        self.LResultCurrentAge.configure(text="현재 나이: " + person["ageNow"])
        self.LResultAge.configure(text="당시 나이: " + person["age"])



FrameWork()