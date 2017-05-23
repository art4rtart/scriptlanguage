import urllib.request
import urllib

class GetShortesData:
    key = '7174657a6a63686c313232516c424667'
    hangul_utf8 = urllib.parse.quote("정왕")
    url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimeStationArrival/0/5/" % key + hangul_utf8)

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        f = open("arrival.xml", "wb")
        f.write(data)
        f.close()

getData = GetShortesData()
getData.main()