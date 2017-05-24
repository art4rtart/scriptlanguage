import urllib.request
import urllib

class GetStationData:
    key = '6c4e636b7263686c3131326b4e4c5456'
    hangul_utf8 = urllib.parse.quote("4호선")
    url = ("http://swopenAPI.seoul.go.kr/api/subway/%s/xml/realtimePosition/0/5/" % key + hangul_utf8)

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        f = open("position.xml", "wb")
        f.write(data)
        f.close()

getData = GetStationData()
getData.main()