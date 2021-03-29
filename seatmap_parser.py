import xml.etree.ElementTree as ET

import json
tree = ET.parse('seatmap1.xml')
root = tree.getroot()
dict = {}



# for level1 in tree.iter():
if len(root[0]) > 0:
    lastChar = str(root[0])[-20:]
    # item = str(root[0]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
    item = str(root[0]).replace("<Element '{http://schemas.xmlsoap.org/soap/envelope/}", "").replace(lastChar,'')
    elmarray = list(root[0])
    basearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in elmarray]
    dict[item] = {}
    for level2 in range(len(elmarray)):
        secelm = list(elmarray[level2])
        attributArr = list(elmarray[level2].attrib)
        test = str(elmarray[level2]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
        secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in secelm]
        stringedAttributArr = [str(i) for i in attributArr]
        dict[item][test] = {"Atributes" : stringedAttributArr}
        for level3 in range(len(secelm)):
            thirdelm = list(secelm[level3])
            three = str(secelm[level3]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
            thirdattributArr = list(secelm[level3].attrib)
            secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in thirdelm]
            thirdAttributArr = [str(index) for index in thirdattributArr]
            dict[item][test][three] = {"Atributes" : thirdAttributArr}
            for level4 in range(len(thirdelm)):
                fourthelm = list(thirdelm[level4])
                four = str(thirdelm[level4]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
                fourthattributArr = list(thirdelm[level4].attrib)
                secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in fourthelm]
                fourthAttributArr = [str(index) for index in fourthattributArr]
                dict[item][test][three][four] = {"Atributes" : fourthAttributArr}
                for level5 in range(len(fourthelm)):
                    fifthelm = list(fourthelm[level5])
                    five = str(fourthelm[level5]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
                    fifthattributArr = list(fourthelm[level5].attrib)
                    secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in fifthelm]
                    fifthAttributArr = [str(index) for index in fifthattributArr]
                    dict[item][test][three][four][five] = {"Atributes" : fifthAttributArr}
                    for level6 in range(len(fifthelm)):
                        sixthelm = list(fifthelm[level6])
                        six = str(fifthelm[level6]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
                        sixthattributArr = list(fifthelm[level5].attrib)
                        secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in sixthelm]
                        sixthAttributArr = [str(index) for index in sixthattributArr]
                        dict[item][test][three][four][five][six] = {"Atributes" : sixthAttributArr}
                        for level7 in range(len(sixthelm)):
                            seventhelm = list(sixthelm[level7])
                            seven = str(sixthelm[level7]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
                            seventhattributArr = list(sixthelm[level7].attrib)
                            secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in seventhelm]
                            seventhAttributArr = [str(index) for index in seventhattributArr]
                            dict[item][test][three][four][five][six] = {"Atributes" : seventhAttributArr}
                            for level7 in range(len(sixthelm)):
                                seventhelm = list(sixthelm[level7])
                                seven = str(sixthelm[level7]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
                                seventhattributArr = list(sixthelm[level7].attrib)
                                secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in seventhelm]
                                seventhAttributArr = [str(index) for index in seventhattributArr]
                                dict[item][test][three][four][five][six][seven] = {"Atributes" : seventhAttributArr}
                                for level8 in range(len(seventhelm)):
                                    eighthelm = list(seventhelm[level8])
                                    eight = str(seventhelm[level8]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
                                    eighthattributArr = list(seventhelm[level8].attrib)
                                    secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in eighthelm]
                                    eighthAttributArr = [str(index) for index in eighthattributArr]
                                    dict[item][test][three][four][five][six][seven][eight] = {"Atributes" : eighthAttributArr}
                                    for level9 in range(len(eighthelm)):
                                        ninthelm = list(eighthelm[level9])
                                        nine = str(eighthelm[level9]).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'')
                                        ninthattributArr = list(eighthelm[level9].attrib)
                                        secbasearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "").replace(lastChar,'') for i in ninthelm]
                                        ninthAttributArr = [str(index) for index in ninthattributArr]
                                        dict[item][test][three][four][five][six][seven][eight][nine] = {"Atributes" : ninthAttributArr}
















# print(secelm)
# print(thirdelm)



# for i in range(len(test_list)):
#     print (i, end = " ")
#     print (test_list[i])
#
#

    # else:
    #     lastChar = str(level1)[-20:]
    #     item = str(level1).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
    #     dict[item] = {"text": level1.text, "attributes": level1.attrib}

j_data = json.dump(dict, open("FILENAME_parsed.json", 'w'))
