# Import Module -----------------------------

from tkinter import *
import xml.etree.ElementTree as etree
import urllib.request
import urllib
from tkinter import font

# -------------------------------------------

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"
htmlFileName = "data.html"

# TK Inter -----------------------------------

import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("1280x720+125+40")
DataList = []

photo = PhotoImage(file="back.png")
imageLabel = Label(g_Tk, image=photo)
imageLabel.pack()

search = PhotoImage(file="search.png")
searchLock = PhotoImage(file="searchLock.png")
save = PhotoImage(file='save.png')
mail = PhotoImage(file='mail.png')

StartButtonCount = 0
EndButtonCount = 0

class Data:
    right = None
    arrived_0 = None
    left = None
    arrived_1 = None
    startLock = False
    endLock = False

# First Last Train  -----------------------------------------------------------

def StationSelect():
    global InputStart
    TempFont = font.Font(g_Tk, size=10, weight='bold', family = 'Consolas')
    InputStart = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 10, relief = 'ridge')
    InputStart.pack()
    InputStart.place(x=1030, y=170)

def TrainSelect():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=1215, y=215)

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=20, height=1, borderwidth=10, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "1호선")
    SearchListBox.insert(2, "2호선")
    SearchListBox.insert(3, "3호선")
    SearchListBox.insert(4, "4호선")
    SearchListBox.insert(5, "5호선")
    SearchListBox.insert(6, "6호선")
    SearchListBox.insert(7, "7호선")
    SearchListBox.insert(8, "8호선")
    SearchListBox.insert(9, "9호선")
    SearchListBox.pack()
    SearchListBox.place(x=1030, y=225)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def DaySelect():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=1215, y=270)

    TempFont = font.Font(g_Tk, size=10, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=20, height=1, borderwidth=10, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "평일")
    SearchListBox.insert(2, "토요일")
    SearchListBox.insert(3, "일요일 / 공휴일")

    SearchListBox.pack()
    SearchListBox.place(x=1030, y=280)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def SearchFirstLast():
    SearchButton = Button(g_Tk, image = search, command=StartFirstLastAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1200, y=170)

def StartFirstLastAction():
    print("ok")

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
            shortest()
            arrival()

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
            shortest()
            arrival()

# -----------------------------------------------------------------------------

def saveData():
    SearchButton = Button(g_Tk, image = save, command=saveDataAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1080, y=535)

def sendEmail():
    SearchButton = Button(g_Tk, image = mail, command=sendEmailAction, borderwidth = 5, relief = 'ridge')
    SearchButton.pack()
    SearchButton.place(x=1080, y=605)

def saveDataAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchLibrary()
    elif iSearchIndex == 1:
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:  # 留덉폆
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()

    RenderText.configure(state='disabled')

def sendEmailAction():
    sendToHim = InputEmail.get()
    print(sendToHim)

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
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=440, y=450)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=38, height=8, borderwidth=5, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=693, y=355)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

def ScheduleRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=440, y=450)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=28, height=10, borderwidth=5, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=1032, y=330)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

def ReceiveTimeRenderText():
    global RenderText

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=30, height=1, borderwidth=5, relief='ridge')
    RenderText.pack()
    RenderText.place(x=20, y=70)

    RenderText.configure(state='disabled')

def MoneyRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=440, y=450)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=38, height=6, borderwidth=5, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=693, y=560)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

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

        RenderText.insert(INSERT, "      " + time)
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "      " + sPass)
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "     " + transition)

        RenderText.pack()
        RenderText.place(x=345, y=560)

        RenderText.configure(state='disabled')
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

        if count is 1:
            Data.left = a.findtext('trainLineNm')
            Data.arrived_1 = a.findtext('arvlMsg2')

        count += 1

    TempFont = font.Font(g_Tk, size=14, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=26, height=5, borderwidth=5, relief='ridge')
    RenderText.insert(INSERT, Data.right)
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, Data.arrived_0)
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, "=========================\n")
    RenderText.insert(INSERT, Data.left)
    RenderText.insert(INSERT, "\n")
    RenderText.insert(INSERT, Data.arrived_1)
    RenderText.insert(INSERT, "\n")

    RenderText.pack()
    RenderText.place(x=695, y=158)

class GetScheduleData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '676a78647663686c3937454f514c57'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://openAPI.seoul.go.kr:8088/%s/xml/SearchFirstAndLastTrainInfobyLineService/1/50/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()
        f = open("schedule.xml", "wb")
        f.write(data)
        f.close()

def schedule():
    begin = input("호선 입력(숫자) : ")
    station = input("역명 입력(한글) : ")
    print("====================")
    print("      요일 선택     ")
    print("====================")
    print("1. 평일")
    print("2. 토요일")
    print("3. 일요일 / 공휴일")
    end = input("요일 입력 : ")
    print("====================")
    name = begin + "/" + end + "/1"

    getData = GetScheduleData(name)
    getData.main()

    sc = etree.parse('./xml/schedule.xml')
    rootSc = sc.getroot()

    for a in rootSc.findall('row'):
        if(station == a.findtext('STATION_NM')):
            print(a.findtext('STATION_NM'))
            print("첫차:", a.findtext('FIRST_TIME'))
            print("막차:", a.findtext('LAST_TIME'))
            print("====================")

    key = input()
    if(key == 'b'):
        os.system('cls')

# ------------------------------
StationSelect()
TrainSelect()
DaySelect()
SearchFirstLast()

InputStartStation()
InputEndStation()
InputEmailAddress()

# saveData()
sendEmail()

SearchStartStation()
SearchEndStation()

#------------------------------

ShortestRenderText()
ArrivalRenderText()
PositionRenderText()
ScheduleRenderText()
MoneyRenderText()
ReceiveTimeRenderText()

# ------------------------------

g_Tk.mainloop()

#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
