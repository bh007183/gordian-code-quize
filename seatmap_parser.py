import xml.etree.ElementTree as ET

import json
tree1 = ET.parse('seatmap1.xml')
root1 = tree1.getroot()
tree2 = ET.parse('seatmap2.xml')
root2 = tree2.getroot()



dictionary = {
"seatmap1" : {

},
"seatmap2" : {

}
}
# lastChar = [-20:]
def parseToJSON(root, map):
    for level1 in range(len(root)):
        firsltelm = list(root[level1])
        Atributes = root[level1].attrib
        text = root[level1].text
        item = str(root[level1]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
        dictionary[map][item] = {"Atributes" : Atributes, "text": text}
        for level2 in range(len(firsltelm)):
            # lastChar = str(firsltelm[level2])[-20:]
            secelm = list(firsltelm[level2])
            Atributes = firsltelm[level2].attrib
            text = firsltelm[level2].text
            two = str(firsltelm[level2]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
            dictionary[map][item][two] = {"Atributes" : Atributes, "text": text}
            for level3 in range(len(secelm)):
                # lastChar = str(secelm[level3])[-20:]
                thirdelm = list(secelm[level3])
                three = str(secelm[level3]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                Atributes = secelm[level3].attrib
                text = secelm[level3].text
                dictionary[map][item][two][three] = {"Atributes" : Atributes, "text": text}
                for level4 in range(len(thirdelm)):
                    # lastChar = str(thirdelm[level4])[-20:]
                    fourthelm = list(thirdelm[level4])
                    four = str(thirdelm[level4]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                    Atributes = thirdelm[level4].attrib
                    text = thirdelm[level4].text
                    dictionary[map][item][two][three][four] = {"Atributes" : Atributes, "text": text }
                    for level5 in range(len(fourthelm)):
                        # lastChar = str(fourthelm[level5])[-20:]
                        fifthelm = list(fourthelm[level5])
                        five = str(fourthelm[level5]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                        Atributes = fourthelm[level5].attrib
                        text = fourthelm[level5].text
                        dictionary[map][item][two][three][four][five] = {"Atributes" : Atributes, "text": text }
                        for level6 in range(len(fifthelm)):
                            # lastChar = str(fifthelm[level6])[-20:]
                            sixthelm = list(fifthelm[level6])
                            six = str(fifthelm[level6]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                            Atributes = fifthelm[level6].attrib
                            text = fifthelm[level6].text
                            dictionary[map][item][two][three][four][five][six] = {"Atributes" : Atributes, "text": text }
                            for level7 in range(len(sixthelm)):
                                seventhelm = list(sixthelm[level7])
                                seven = str(sixthelm[level7]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                                Atributes = sixthelm[level7].attrib
                                text = sixthelm[level7].text
                                dictionary[map][item][two][three][four][five][six][seven] = {"Atributes" : Atributes, "text": text }
                                for level8 in range(len(seventhelm)):
                                    eighthelm = list(seventhelm[level8])
                                    eight = str(seventhelm[level8]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                                    Atributes = seventhelm[level8].attrib
                                    text = seventhelm[level8].text
                                    dictionary[map][item][two][three][four][five][six][seven][eight] = {"Atributes" : Atributes, "text": text }
                                    for level9 in range(len(eighthelm)):
                                        ninthelm = list(eighthelm[level9])
                                        nine = str(eighthelm[level9]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                                        Atributes = eighthelm[level9].attrib
                                        text = eighthelm[level9].text
                                        dictionary[map][item][two][three][four][five][six][seven][eight][nine] = {"Atributes" : Atributes, "text": text }
                                        for level10 in range(len(ninthelm)):
                                            tenthelm = list(ninthelm[level10])
                                            ten = str(ninthelm[level10]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                                            Atributes = ninthelm[level10].attrib
                                            text = ninthelm[level10].text
                                            dictionary[map][item][two][three][four][five][six][seven][eight][nine][ten] = {"Atributes" : Atributes, "text": text }
                                            for level11 in range(len(tenthelm)):
                                                eleventhelm = list(tenthelm[level11])
                                                eleven = str(tenthelm[level11]).replace("<Element '{http://www.iata.org/IATA/EDIST/2017.2}","").replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
                                                Atributes = tenthelm[level11].attrib
                                                text = tenthelm[level11].text
                                                dictionary[map][item][two][three][four][five][six][seven][eight][nine][ten][eleven] = {"Atributes" : Atributes, "text": text }
parseToJSON(root2, "seatmap2")


parseToJSON(root1, "seatmap1")



# def parse(elementArray):
#     for index in range(len(elementArray)):
#         embededElements = list(elementArray[index])
#         attributes = list(elementArray[index].attrib)
#         depth = str(elementArray[index]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
#         stringedAttributes = [str(i) for i in attributes]
        # dict[item][depth] = {"Atributes" : stringedAttributes}

    # else:
    #     lastChar = str(level1)[-20:]
    #     item = str(level1).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
    #     dict[item] = {"text": level1.text, "attributes": level1.attrib}

j_data = json.dump(dictionary, open("FILENAME_parsed.json", 'w'))
