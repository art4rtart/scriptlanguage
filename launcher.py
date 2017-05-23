import xml.etree.ElementTree as etree

def main():
    short = etree.parse('shortest.xml')
    rootShort = short.getroot()

    # ************************************************************************

    for a in rootShort.findall('RESULT'):
        print(a.findtext('message'))
        print("---------------------")

    for a in rootShort.findall('row'):
        print(a.findtext('statnFnm'), "->", a.findtext('statnTnm'))
        print(a.findtext('minTransferMsg'))
        # print(a.findtext('shtStatnNm'))
        print("---------------------")
        break
    # ************************************************************************
    arrival = etree.parse('arrival.xml')
    rootArrival = arrival.getroot()


    for a in rootArrival.findall('row'):
        print(a.findtext('trainLineNm'))
        print(a.findtext('recptnDt'))
        print("-----------")

        if a.findtext("rowNum") == "2":
            break

        # ************************************************************************

    pos = etree.parse('position.xml')
    rootPos = pos.getroot()

    for a in rootPos.findall('row'):
        print(a.findtext('subwayNm'))
        print(a.findtext('statnNm'))
        print(a.findtext('recptnDt'))
        print("-----------")

        if a.findtext("rowNum") == "2":
            break

        # ************************************************************************
if __name__ == "__main__":
    main()
