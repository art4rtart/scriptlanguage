import xml.etree.ElementTree as etree
import urllib.request
import urllib

def showMenu():
    print("Load XML : L")
    print("실사간 도착 시간 : A")
    print("실시간 열차 위치 : P")
    print("최단 경로 : S")
    print("첫차 막차 정보 : ")


class GetShortestData:
    key = '676a78647663686c3937454f514c57'
    hangul_utf8 = urllib.parse.quote("정왕/금정")
    url = ("http://swopenapi.seoul.go.kr/api/subway/%s/xml/shortestRoute/0/5/" % key + hangul_utf8)

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        f = open("shortest.xml", "wb")
        f.write(data)
        f.close()

class GetStationPosData:
    key = '6c4e636b7263686c3131326b4e4c5456'
    hangul_utf8 = urllib.parse.quote("1호선")
    url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimePosition/0/5/" % key + hangul_utf8)

    def main(self):
        data = urllib.request.urlopen(self.url).read()
        f = open("position.xml", "wb")
        f.write(data)
        f.close()

class GetArrivalData:
    key = '7174657a6a63686c313232516c424667'
    hangul_utf8 = urllib.parse.quote("정왕")
    url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimeStationArrival/0/5/" % key + hangul_utf8)

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        f = open("arrival.xml", "wb")
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

def shortest():
    getData = GetShortestData()
    getData.main()

    short = etree.parse('shortest.xml')
    rootShort = short.getroot()

    for a in rootShort.findall('RESULT'):
        print("====================")
        print(a.findtext('message'))
        print("====================")

    for a in rootShort.findall('row'):
        print(a.findtext('statnFnm'), "->", a.findtext('statnTnm'))
        print(a.findtext('minTransferMsg'))
        # print(a.findtext('shtStatnNm'))
        print("====================")
        break

def arrival():
    getData = GetArrivalData()
    getData.main()

    arrival = etree.parse('arrival.xml')
    rootArrival = arrival.getroot()


    for a in rootArrival.findall('row'):
        print(a.findtext('trainLineNm'))
        print(a.findtext('recptnDt'))
        print("====================")

        if a.findtext("rowNum") == "2":
            break

def station():
    getData = GetStationPosData()
    getData.main()

    pos = etree.parse('position.xml')
    rootPos = pos.getroot()

    for a in rootPos.findall('row'):
        print(a.findtext('subwayNm'))
        print(a.findtext('statnNm'))
        print(a.findtext('recptnDt'))
        print("====================")

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
        print("====================")

        if a.findtext("rowNum") == "2":
            break

def main():
    global key
    # ************************************************************************

    showMenu()
    key = input(("메뉴를 선택하세요 : "))
    # schedule()

    # ************************************************************************

    if key is 's':
        shortest()

    # ************************************************************************
    elif key is 'a':
        arrival()

    # ************************************************************************
    elif key is 'p':
        station()

     # ************************************************************************

if __name__ == "__main__":
    main()

