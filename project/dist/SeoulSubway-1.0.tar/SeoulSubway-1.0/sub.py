# Import Module -----------------------------

from tkinter import *
import xml.etree.ElementTree as etree
import urllib.request
import urllib
import spam
from tkinter import font

# -------------------------------------------

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"
htmlFileName = "data.txt"

# TK Inter -----------------------------------

import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("1280x720+125+40")
DataList = []

photo = PhotoImage(file="./image/back.png")
imageLabel = Label(g_Tk, image=photo)
imageLabel.pack()

search = PhotoImage(file="./image/search.png")
searchLock = PhotoImage(file="./image/searchLock.png")
save = PhotoImage(file='./image/save.png')
mail = PhotoImage(file='./image/mail.png')
map = PhotoImage(file='./image/map.png')
big = PhotoImage(file='./image/subway.png')

MapCount = 0
StartButtonCount = 0
EndButtonCount = 0
StationButtonCount = 0
TrainButtonCount = 0
DayButtonCount = 0

class Data:
    right = None
    arrived_0 = None
    left = None
    arrived_1 = None
    startLock = False
    endLock = False
    stationLock = False
    trainLock = False
    dayLock = False
    station = 0
    money = 0
    endToNum = 0
    y = 10

# Subway Map ------------------------------------------------------------------

def back():
    SearchButton = Button(g_Tk, image = photo, borderwidth = 0)
    SearchButton.pack()
    SearchButton.place(x=0, y=0)

def Map():
    SearchButton = Button(g_Tk, image = map, command=MapAction, borderwidth = 0, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=23, y=119)

def MapOk():
    SearchButton = Button(g_Tk, image = big, command=MapAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=-10, y=-Data.y)

def MapAction():
    global MapCount
    global MapCount
    global StartButtonCount
    global EndButtonCount
    global StationButtonCount
    global TrainButtonCount
    global DayButtonCount

    if MapCount % 2 is 0:
        MapOk()

    else:
        Data.startLock = False
        Data.endLock = False
        Data.stationLock = False
        Data.trainLock = False
        Data.dayLock = False

        StartButtonCount = 0
        EndButtonCount = 0
        StationButtonCount = 0
        TrainButtonCount = 0
        DayButtonCount = 0
        back()
        StationSelect()
        TrainSelect()
        DaySelect()
        FirstLastStation()
        FirstLastTrain()
        FirstLastDay()
        InputStartStation()
        InputEndStation()
        InputEmailAddress()
        SearchStartStation()
        SearchEndStation()
        sendEmail()
        ShortestRenderText()
        ArrivalRenderText()
        PositionRenderText()
        ScheduleRenderText()
        MoneyRenderText()
        TimeRenderText()
        Map()

    MapCount += 1

# First Last Train  -----------------------------------------------------------

def StationSelect():
    global InputStation
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    InputStation = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 10, relief = 'ridge')
    InputStation.pack()
    InputStation.place(x=1030, y=170)

def TrainSelect():
    global InputTrain
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    InputTrain = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 10, relief = 'ridge')
    InputTrain.pack()
    InputTrain.place(x=1030, y=220)

def DaySelect():
    global InputDay
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    InputDay = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 10, relief = 'ridge')
    InputDay.pack()
    InputDay.place(x=1030, y=270)


def FirstLastStation():
    SearchButton = Button(g_Tk, image = search, command=FirstLastStationAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1200, y=170)

def FirstLastTrain():
    SearchButton = Button(g_Tk, image = search, command=FirstLastTrainAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1200, y=220)

def FirstLastDay():
    SearchButton = Button(g_Tk, image = search, command=FirstLastDayAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1200, y=270)


def FirstLastStationOK():
    SearchButton = Button(g_Tk, image = searchLock, command=FirstLastStationAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1200, y=170)

def FirstLastTrainOK():
    SearchButton = Button(g_Tk, image = searchLock, command=FirstLastTrainAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1200, y=220)

def FirstLastDayOK():
    SearchButton = Button(g_Tk, image = searchLock, command=FirstLastDayAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1200, y=270)


def FirstLastStationAction():
    global StationButtonCount

    if StationButtonCount % 2 is 0:
        FirstLastStationOK()
        print("Locked")
        Data.stationLock = True

    else:
        FirstLastStation()
        print("UnLocked")
        Data.stationLock = False

    StationButtonCount += 1

    if Data.dayLock is True and Data.trainLock is True and Data.stationLock is True:
        schedule()

def FirstLastTrainAction():
    global TrainButtonCount

    if TrainButtonCount % 2 is 0:
        FirstLastTrainOK()
        print("Locked")
        Data.trainLock = True

    else:
        FirstLastTrain()
        print("UnLocked")
        Data.trainLock = False

    TrainButtonCount += 1

    if Data.dayLock is True and Data.trainLock is True and Data.stationLock is True:
        schedule()

def FirstLastDayAction():
    global DayButtonCount

    if DayButtonCount % 2 is 0:
        FirstLastDayOK()
        print("Locked")
        Data.dayLock = True

    else:
        FirstLastDay()
        print("UnLocked")
        Data.dayLock = False

    DayButtonCount += 1

    if Data.dayLock is True and Data.trainLock is True and Data.stationLock is True:
        schedule()

# -----------------------------------------------------------------------------

def InputStartStation():
    global InputStart
    TempFont = font.Font(g_Tk, size=16, weight='bold', family = 'Consolas')
    InputStart = Entry(g_Tk, font = TempFont, width = 10, borderwidth = 5, relief = 'ridge')
    InputStart.pack()
    InputStart.place(x=105, y=525)

def InputEndStation():
    global InputEnd
    TempFont = font.Font(g_Tk, size=16, weight='bold', family = 'Consolas')
    InputEnd = Entry(g_Tk, font = TempFont, width = 10, borderwidth = 5, relief = 'ridge')
    InputEnd.pack()
    InputEnd.place(x=105, y=616)

def InputEmailAddress():
    global InputEmail
    TempFont = font.Font(g_Tk, size=16, weight='bold', family = 'Consolas')
    InputEmail = Entry(g_Tk, font = TempFont, width = 17, borderwidth = 5, relief = 'ridge')
    InputEmail.pack()
    InputEmail.place(x=1030, y=560)

# Draw ------------------------------------------------------------------------

def SearchStartStation():
    SearchButton = Button(g_Tk, image = search, command=StartStationAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=250, y=525)

def SearchStartStationOK():
    SearchButton = Button(g_Tk, image = searchLock, command=StartStationAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=250, y=525)

def SearchEndStation():
    SearchButton = Button(g_Tk, image = search, command=EndStationAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=250, y=615)

def SearchEndStationOK():
    SearchButton = Button(g_Tk, image = searchLock, command=EndStationAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=250, y=615)

# Button Action ---------------------------------------------------------------

def StartStationAction():
    global StartButtonCount
    global start

    if StartButtonCount % 2 is 0:
        start = InputStart.get() # 입력한 값 저장
        SearchStartStationOK()
        print("Locked")
        Data.startLock = True

    else:
        SearchStartStation()
        print("UnLocked")
        Data.startLock = False

    StartButtonCount += 1
    if Data.startLock is True:
        if Data.endLock is True:
            getReceiveTime()
            shortest()
            money()
            arrival()
            subPos()

def EndStationAction():
    global EndButtonCount
    global end

    if EndButtonCount % 2 is 0:
        end = InputEnd.get() # 입력한 값 저장
        SearchEndStationOK()
        print("Locked")
        Data.endLock = True

    else:
        SearchEndStation()
        print("UnLocked")
        Data.endLock = False

    EndButtonCount += 1

    if Data.startLock is True:
        if Data.endLock is True:
            getReceiveTime()
            shortest()
            arrival()
            subPos()
            money()

# -----------------------------------------------------------------------------

def sendEmail():
    SearchButton = Button(g_Tk, image = mail, command=sendEmailAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1080, y=605)

def sendEmailAction():
    sendToUser = InputEmail.get()

    global host, port
    html = ""
    senderAddr = "sq7r9760@gmail.com"
    pwd = "chldnwls3665"
    recipientAddr = sendToUser
    title = "서울 지하철 알리미"

    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    htmlFD = open(htmlFileName, 'rb')
    HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
    htmlFD.close()

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(HtmlPart)

    print("connect smtp server ... ")
    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, pwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")

# -----------------------------------------------------------------------------

def ArrivalRenderText(): # 수정 해야함
    TempFont = font.Font(g_Tk, size=14, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=26, height=5, borderwidth=5, relief='ridge')
    RenderText.pack()
    RenderText.place(x=695, y=158)

def ShortestRenderText():
    TempFont = font.Font(g_Tk, size=17, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=21, height=3, borderwidth=5, relief='ridge')
    RenderText.pack()
    RenderText.place(x=345, y=560)

def PositionRenderText():
    TempFont = font.Font(g_Tk, size=14, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=26, height=5, borderwidth=5, relief='ridge')
    RenderText.pack()
    RenderText.place(x=693, y=350)

def ScheduleRenderText():
    global RenderText

    TempFont = font.Font(g_Tk, size=11, family='Consolas')
    RenderText = Text(g_Tk, font = TempFont, width=25, height=8, borderwidth=5, relief='ridge')
    RenderText.insert(INSERT, "1. 지하철역 입력")
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, "- STATION NAME")
    RenderText.insert(INSERT, "\n\n")
    RenderText.insert(INSERT, "2. 호선 입력")
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, "- LINE NUMBER")
    RenderText.insert(INSERT, "\n\n")
    RenderText.insert(INSERT, "3. 요일 입력")
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, "- (평일 / 토요일 / 일요일)")
    RenderText.insert(INSERT, "\n")
    RenderText.pack()
    RenderText.place(x=1029, y=315)

    RenderText.configure(state='disabled')

def MoneyRenderText():
    TempFont = font.Font(g_Tk, size=17, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=20, height=3, borderwidth=5, relief='ridge')
    RenderText.pack()
    RenderText.place(x=695, y=558)

def TimeRenderText():
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=20, height=0, borderwidth=5, relief='ridge')
    RenderText.pack()
    RenderText.place(x=20, y=70)


# ------------------------------

class GetShortestData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '676a78647663686c3937454f514c57'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://swopenapi.seoul.go.kr/api/subway/%s/xml/shortestRoute/0/5/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()

        f = open("./xml/shortest.xml", "wb")
        f.write(data)
        f.close()

def shortest():
    first = InputStart.get()
    last = InputEnd.get()
    name = first + "/" + last

    getData = GetShortestData(name)
    getData.main()

    short = etree.parse('./xml/shortest.xml')
    rootShort = short.getroot()

    for a in rootShort.findall('row'):
        TempFont = font.Font(g_Tk, size=17, family='Consolas')
        RenderText = Text(g_Tk, font=TempFont, width=21, height=3, borderwidth=5, relief='ridge')
        x = a.findtext('minTravelTm')
        y = a.findtext("minStatnCnt")
        z = a.findtext("minTransferCnt")
        hour = int(int(x) / 60)
        minute = int(x) % 60

        time = str(hour) + "시간 " + str(minute) + "분"
        transition = str(y) + "개 정거장"
        sPass = str(z) + "회  환승"

        Data.station = int(y)

        RenderText.insert(INSERT, "      " + time)
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "      " + sPass)
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "      " + transition)

        RenderText.pack()
        RenderText.place(x=345, y=560)

        RenderText.configure(state='disabled')

        l = rootShort.findtext('row/minTransferMsg')

        f = open('data.txt', 'w')
        f.write("안녕하세요. 서울 지하철 알리미 입니다.\n\n")
        f.write("* 소요 시간 *\n")
        f.write(rootShort.findtext('row/statnFnm'))
        f.write(" 에서 ")
        f.write(rootShort.findtext('row/statnTnm'))
        f.write(" 까지 ")
        f.write(l)
        f.write(" \n")
        f.close()

        break

class GetArrivalData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '7174657a6a63686c313232516c424667'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimeStationArrival/0/5/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()

        f = open("./xml/arrival.xml", "wb")
        f.write(data)
        f.close()

def arrival():
    name = InputStart.get()

    getData = GetArrivalData(name)
    getData.main()

    arrival = etree.parse('./xml/arrival.xml')
    rootArrival = arrival.getroot()

    count = 0

    for a in rootArrival.findall('row'):
        if count is 0:
            Data.right = a.findtext('trainLineNm')
            Data.arrived_0 = a.findtext('arvlMsg2')
            b = open('data.txt', 'a')
            b.write("\n* 도착 정보 *")
            b.write("\n" + str(a.findtext('trainLineNm')) + "은 " + str(a.findtext('arvlMsg2')) + " (도착) 입니다.")
            b.close()

        if count is 1:
            Data.left = a.findtext('trainLineNm')
            Data.arrived_1 = a.findtext('arvlMsg2')
            b = open('data.txt', 'a')
            b.write("\n" + str(a.findtext('trainLineNm')) + "은 " + str(a.findtext('arvlMsg2')) + " (도착) 입니다.\n")
            b.close()

        count += 1

    TempFont = font.Font(g_Tk, size=14, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=26, height=5, borderwidth=5, relief='ridge')
    RenderText.insert(INSERT, Data.right)
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, Data.arrived_0)
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, Data.left)
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, Data.arrived_1)
    RenderText.insert(INSERT, "\n")

    RenderText.pack()
    RenderText.place(x=695, y=158)

class GetSubPosData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '6c4e636b7263686c3131326b4e4c5456'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimePosition/1/1000/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()
        f = open("./xml/position.xml", "wb")
        f.write(data)
        f.close()

def subPos():
    name = "4호선"
    sub = InputStart.get()

    getData = GetSubPosData(name)
    getData.main()

    pos = etree.parse('./xml/position.xml')
    rootPos = pos.getroot()

    TempFont = font.Font(g_Tk, size=14, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=26, height=5, borderwidth=5, relief='ridge')
    countMe = 0
    for a in rootPos.findall('row'):
        if(sub == a.findtext('statnNm')):
            RenderText.insert(INSERT, a.findtext('statnNm') + "역")

            if(a.findtext('trainSttus') == '0'):
                RenderText.insert(INSERT, " : 진입")
                RenderText.insert(INSERT, "\n")

            elif(a.findtext('trainSttus') == '1'):
                RenderText.insert(INSERT, " : 도착")
                RenderText.insert(INSERT, "\n")

            elif (a.findtext('trainSttus') == '2'):
                RenderText.insert(INSERT, " : 출발")
                RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "종착역 : " + a.findtext('statnTnm'))
            RenderText.insert(INSERT, "\n")

            if(a.findtext('directAt') == '0'):
                RenderText.insert(INSERT, "급행이 아닙니다")
                RenderText.insert(INSERT, "\n")

            else:
                RenderText.insert(INSERT, "급행입니다")
                RenderText.insert(INSERT, "\n")

            if(a.findtext('lstcarAt') == '0'):
                RenderText.insert(INSERT, "막차가 아닙니다")
                RenderText.insert(INSERT, "\n")

            else:
                RenderText.insert(INSERT, "막차입니다")
                RenderText.insert(INSERT, "\n")

            RenderText.insert(INSERT, "\n")


    RenderText.pack()
    RenderText.place(x=693, y=350)

class GetScheduleData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '676a78647663686c3937454f514c57'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://openAPI.seoul.go.kr:8088/%s/xml/SearchFirstAndLastTrainInfobyLineService/1/100/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()
        f = open("./xml/schedule.xml", "wb")
        f.write(data)
        f.close()

def schedule():
    station = InputStation.get()
    train = InputTrain.get()
    day = InputDay.get()

    name = train[0:1] + "/" + str(Data.endToNum) + "/1"

    getData = GetScheduleData(name)
    getData.main()

    sc = etree.parse('./xml/schedule.xml')
    rootSc = sc.getroot()

    if(day == "평일"):
        Data.endToNum = 1

    if(day == "토요일"):
        Data.endToNum = 2

    if(day == "일요일" or day == "공휴일"):
        Data.endToNum = 3

    TempFont = font.Font(g_Tk, size=11, family='Consolas')
    RenderText = Text(g_Tk, font = TempFont, width=25, height=8, borderwidth=5, relief='ridge')

    for a in rootSc.findall('row'):
        if(station == a.findtext('STATION_NM')):
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "       " + a.findtext('STATION_NM') + " [" + day + "]")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "  첫차 시간 : " + a.findtext('FIRST_TIME'))
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "  막차 시간 : " + a.findtext('LAST_TIME'))

    RenderText.pack()
    RenderText.place(x=1029, y=315)

def money():
    TempFont = font.Font(g_Tk, size=17, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=20, height=3, borderwidth=5, relief='ridge')
    RenderText.pack()

    if Data.station > 0:
        Data.money = 1250

    if Data.station > 5:
        Data.money = 1350

    if Data.station > 8:
        Data.money = 1450

    if Data.station > 10:
        Data.money = 1550

    if Data.station > 12:
        Data.money = 1650

    if Data.station > 14:
        Data.money = 1750

    if Data.station > 20:
        Data.money = 2050

    if Data.station > 30:
        Data.money = 2150

    if Data.station > 40:
        Data.money = 2350

    RenderText.insert(INSERT, "\n       " + str(Data.money) + "원")
    RenderText.place(x=695, y=558)

    b = open('data.txt', 'a')
    b.write("\n* 요금 정보 *")
    b.write("\n요금은 " + str(Data.money) + " 원 입니다.")
    b.close()

def getReceiveTime():
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=20, height=0, borderwidth=5, relief='ridge')
    RenderText.insert(INSERT, spam.time("get receive time"))
    RenderText.pack()
    RenderText.place(x=20, y=70)


# ------------------------------
StationSelect()
TrainSelect()
DaySelect()
FirstLastStation()
FirstLastTrain()
FirstLastDay()
InputStartStation()
InputEndStation()
InputEmailAddress()
SearchStartStation()
SearchEndStation()
sendEmail()
ShortestRenderText()
ArrivalRenderText()
PositionRenderText()
ScheduleRenderText()
MoneyRenderText()
TimeRenderText()
Map()
# ------------------------------

g_Tk.mainloop()

#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
