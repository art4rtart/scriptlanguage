import xml.etree.ElementTree as etree
import urllib.request
import urllib
import os
# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

class GetArrivalData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '7174657a6a63686c313232516c424667'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimeStationArrival/0/5/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()

        f = open("arrival.xml", "wb")
        f.write(data)
        f.close()

class GetSubPosData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '6c4e636b7263686c3131326b4e4c5456'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimePosition/0/5/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()
        f = open("position.xml", "wb")
        f.write(data)
        f.close()

class GetShortestData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '676a78647663686c3937454f514c57'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://swopenapi.seoul.go.kr/api/subway/%s/xml/shortestRoute/0/5/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()

        f = open("shortest.xml", "wb")
        f.write(data)
        f.close()

class GetScheduleData:
    key = '655a454a4563686c34325379714367 '
    hangul_utf8 = urllib.parse.quote("정왕")
    url = ("http://swopenapi.seoul.go.kr/api/subway/%s/xml/firstLastTimetable/0/5/정왕" % key + hangul_utf8)

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        f = open("schedule.xml", "wb")
        f.write(data)
        f.close()

def arrival():
    name = str(input("역 입력 : "))

    getData = GetArrivalData(name)
    getData.main()

    arrival = etree.parse('arrival.xml')
    rootArrival = arrival.getroot()


    for a in rootArrival.findall('row'):
        print(a.findtext('trainLineNm'))
        print(a.findtext('recptnDt'))
        print("====================")

        if a.findtext("rowNum") == "2":
            break

def subPos():
    name = str(input("호선 입력 : "))

    getData = GetSubPosData(name)
    getData.main()

    pos = etree.parse('position.xml')
    rootPos = pos.getroot()

    for a in rootPos.findall('row'):
        print("====================")
        print(a.findtext('subwayNm'))
        print(a.findtext('statnNm'))
        print(a.findtext('recptnDt'))

        if a.findtext("rowNum") == "2":
            break

def schedule():
    getData = GetScheduleData()
    getData.main()

    sc = etree.parse('schedule.xml')
    rootSc = sc.getroot()

    for a in rootSc.findall('row'):
        print(a.findtext('weekendTranHour'))
        print(a.findtext('saturdayTranHour'))
        print(a.findtext('holidayTranHour'))

        if a.findtext("rowNum") == "2":
            break

def shortest():
    begin = input("출발역 : ")
    end = input("도착역 : ")
    name = begin + "/" + end

    getData = GetShortestData(name)
    getData.main()

    short = etree.parse('shortest.xml')
    rootShort = short.getroot()

    for a in rootShort.findall('row'):
        print("====================")
        print(a.findtext('statnFnm'), "->", a.findtext('statnTnm'))
        print(a.findtext('minTransferMsg'))
        # print(a.findtext('shtStatnNm'))
        break

def showMenu():
    print("====================")
    print("서울시 지하철 서비스 ")
    print("====================")
    print("1. 실사간 도착 시간")
    print("2. 실시간 열차 위치")
    print("3. 최단  경로  검색 ")
    print("4. 첫차  막차  검색 ")
    print("5. 주변  버스  검색 ")
    print("6. 인터넷 메일 전송 ")
    print("====================")

def sendMail():
    global host, port
    html = ""
    title = str(input('Title :'))
    senderAddr = str(input('sender email address :'))
    recipientAddr = str(input('recipient email address :'))
    messageText = str(input('write message :'))
    pwd = str(input(' input your password of gmail account :'))

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

    msgPart = MIMEText(messageText, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

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

def main():
    global key

    while 1:
        showMenu()
        key = eval(input("메뉴를 선택하세요 : "))
        if key is 1:
            arrival()

        elif key is 2:
            subPos()

        elif key is 3:
            shortest()

        elif key is 4:
            schedule()

        elif key is 5:
            sendMail()

        elif key is 0:
            break

     # ************************************************************************

if __name__ == "__main__":
    main()


