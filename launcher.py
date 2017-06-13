import xml.etree.ElementTree as etree
import urllib.request
import urllib
import os

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"
htmlFileName = "data.html"

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
        self.url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimePosition/1/50/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()
        f = open("./xml/position.xml", "wb")
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

        f = open("./xml/shortest.xml", "wb")
        f.write(data)
        f.close()

class GetScheduleData:
    def __init__(self, n):
        self.name = n

    def main(self):
        key = '676a78647663686c3937454f514c57'
        hangul_utf8 = urllib.parse.quote(self.name)
        self.url = ("http://openAPI.seoul.go.kr:8088/%s/xml/SearchFirstAndLastTrainInfobyLineService/1/25/" % key + hangul_utf8)

        data = urllib.request.urlopen(self.url).read()
        f = open("schedule.xml", "wb")
        f.write(data)
        f.close()

def arrival():
    name = str(input("역 입력 : "))

    getData = GetArrivalData(name)
    getData.main()

    arrival = etree.parse('./xml/arrival.xml')
    rootArrival = arrival.getroot()


    if(rootArrival.findtext('code') == 'INFO-200'):
        print("====================")
        print(rootArrival.findtext('message'))

    else:
        for a in rootArrival.findall('row'):
            print("====================")
            print(a.findtext('trainLineNm'))
            print(a.findtext('arvlMsg2'))

            if a.findtext("rowNum") == "2":
                break

    key = input()
    if(key == 'b'):
        os.system('cls')

def subPos():
    name = str(input("호선 입력 : "))

    getData = GetSubPosData(name)
    getData.main()

    pos = etree.parse('./xml/position.xml')
    rootPos = pos.getroot()

    sub = str(input("역 입력 : "))

    if(rootPos.findtext('code') == 'INFO-200'):
        print("====================")
        print(rootPos.findtext('message'))

    else:
        for a in rootPos.findall('row'):
            if(sub == a.findtext('statnNm')):
                print("====================")
                print("지하철역:", a.findtext('statnNm'))

                if(a.findtext('trainSttus') == '0'):
                    print('열차 상태 : 진입')

                elif(a.findtext('trainSttus') == '1'):
                    print('열차 상태 : 도착')

                else:
                    print('열차 상태 : 출발')

                print("종착역:", a.findtext('statnTnm'))

                if(a.findtext('directAt') == '0'):
                    print('급행 : X')

                else:
                    print('급행 : O')

                if(a.findtext('lstcarAt') == '0'):
                    print('막차 : X')

                else:
                    print('막차 : O')

        print("====================")

    key = input()
    if(key == 'b'):
        os.system('cls')

def shortest():
    begin = input("출발역 : ")
    end = input("도착역 : ")
    name = begin + "/" + end

    getData = GetShortestData(name)
    getData.main()

    short = etree.parse('./xml/shortest.xml')
    rootShort = short.getroot()

    for a in rootShort.findall('row'):
        print("====================")
        print(a.findtext('statnFnm'), "->", a.findtext('statnTnm'))
        print(a.findtext('minTransferMsg'))
        # print(a.findtext('shtStatnNm'))
        break

    b = input("자주 지나는 경로로 추가 하시겠습니까? (Y/N) : ")

    if b is 'y':
        a = rootShort.findtext('row/minTransferMsg')
        a.split()

        f = open('logo.html', 'w')
        f.write(rootShort.findtext('row/statnFnm'))
        f.write(" 에서 ")
        f.write(rootShort.findtext('row/statnTnm'))
        f.write(" 까지 ")
        f.write(a)
        f.close()
        os.system('cls')

    else:
        os.system('cls')

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

def showMenu():
    print("====================")
    print("서울시 지하철 서비스 ")
    print("====================")
    print("1. 실사간 도착 시간")
    print("2. 실시간 열차 위치")
    print("3. 최단  경로  검색 ")
    print("4. 첫차  막차  검색 ")
    print("5. 인터넷 메일 전송 ")
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
