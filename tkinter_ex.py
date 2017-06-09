from tkinter import *
from tkinter import font
import tkinter.messagebox
g_Tk = Tk()
g_Tk.geometry("1280x720+125+40")
DataList = []

photo = PhotoImage(file="back.gif")
imageLabel = Label(g_Tk, image=photo)
imageLabel.pack()

search = PhotoImage(file="search.png")
searchLock = PhotoImage(file="searchLock.png")
save = PhotoImage(file='save.png')
mail = PhotoImage(file='mail.png')

StartButtonCount = 0
EndButtonCount = 0

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[서울시 근린시설 검색 App]")
    MainText.pack()
    MainText.place(x=20)
# InitTopText()


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

# -----------------------------------------------------------------------------

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

    else:
        SearchStartStation()
        print("UnLocked")

    StartButtonCount += 1

def EndStationAction():
    global EndButtonCount
    global end

    if EndButtonCount % 2 is 0:
        end = InputEnd.get() # 입력한 값 저장
        SearchEndStationOK()
        print("Locked")

    else:
        SearchEndStation()
        print("UnLocked")

    EndButtonCount += 1

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

def ShortestPathRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=440, y=450)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=38, height=6, borderwidth=5, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=350, y=560)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

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

def ArrivalRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=440, y=450)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=38, height=8, borderwidth=5, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=693, y=160)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

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

# ------------------------------

InputStartStation()
InputEndStation()
InputEmailAddress()

# saveData()
sendEmail()

SearchStartStation()
SearchEndStation()

#------------------------------

ShortestPathRenderText()
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


#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()