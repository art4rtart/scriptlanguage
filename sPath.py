import urllib.request
import urllib

class GetShortesData:
    key = '676a78647663686c3937454f514c57'
    hangul_utf8 = urllib.parse.quote("정왕/강남구청")
    url = ("http://swopenapi.seoul.go.kr/api/subway/%s/xml/shortestRoute/0/5/" % key + hangul_utf8)

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        f = open("shortest.xml", "wb")
        f.write(data)
        f.close()

getData = GetShortesData()
getData.main()