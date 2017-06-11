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

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=280, y=490)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화공간")
    SearchListBox.pack()
    SearchListBox.place(x=140, y=490)
    # 140
    ListBoxScrollbar.config(command=SearchListBox.yview)
# InitSearchListBox()

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
class Check:
    startLock = False
    endLock = False

check = Check()

def StartStationAction():
    global StartButtonCount
    global start

    if StartButtonCount % 2 is 0:
        start = InputStart.get() # 입력한 값 저장
        SearchStartStationOK()
        print("Locked")
        check.startLock = True

    else:
        SearchStartStation()
        print("UnLocked")
        check.startLock = False

    StartButtonCount += 1

    if check.startLock is True:
        if check.endLock is True:
            shortest()
            arrival()

def EndStationAction():
    global EndButtonCount
    global end

    if EndButtonCount % 2 is 0:
        end = InputEnd.get() # 입력한 값 저장
        SearchEndStationOK()
        print("Locked")
        check.endLock = True

    else:
        SearchEndStation()
        print("UnLocked")
        check.endLock = False

    EndButtonCount += 1

    if check.startLock is True:
        if check.endLock is True:
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

def ArrivalRenderText():
    TempFont = font.Font(g_Tk, size=14, family='Consolas')
    RenderText = Text(g_Tk, font=TempFont, width=26, height=5, borderwidth=5, relief='ridge')
    RenderText.pack()
    RenderText.place(x=695, y=160)

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
    RenderText = Text(g_Tk, width=28, height=23, borderwidth=5, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=1032, y=159)
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


    for a in rootArrival.findall('row'):
        TempFont = font.Font(g_Tk, size=14, family='Consolas')
        RenderText = Text(g_Tk, font=TempFont, width=26, height=5, borderwidth=5, relief='ridge')

        print(a.findtext('trainLineNm'))
        s = a.findtext('trainLineNm')
        print(s.split())

        RenderText.insert(INSERT, a.findtext('trainLineNm'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, a.findtext('arvlMsg2'))
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, a.findtext('trainLineNm'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, a.findtext('arvlMsg2'))
        RenderText.insert(INSERT, "\n")

        RenderText.pack()
        RenderText.place(x=695, y=160)


# ------------------------------

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

def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes

            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes

                    if subitems[3].firstChild.nodeValue == InputLabel.get():  # 援??대쫫??媛숈쓣 寃쎌슦
                        pass
                    elif subitems[5].firstChild.nodeValue == InputLabel.get():  # ???대쫫??媛숈쓣 寃쎌슦
                        pass
                    else:
                        continue

                    # ?곗씠???쎌엯 援ш컙. ?곕씫泥섍? ?놁쓣 ?뚯뿉??"-"???ｋ뒗??
                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass  # ?꾩떆
                        if tel[0] is not '0':
                            tel = "02-" + tel
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))

            for i in range(len(DataList)):
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "] ")
                RenderText.insert(INSERT, "시설명: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "주소: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "전화번호: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")

g_Tk.mainloop()

#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()
