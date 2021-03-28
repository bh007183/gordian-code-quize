import xml.etree.ElementTree as ET

import json
tree = ET.parse('seatmap1.xml')
root = tree.getroot()

dict = {}


# for level1 in tree.iter():
print(value(root))
    # if len(level1) > 0:
    #     # lastChar = str(level1)[-20:]
    #     item = str(level1).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
    #
    #     elmarray = list(level1)
    #     # basearr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "") for i in elmarray]
    #     dict[item] = {"Elements": elmarray, "attributes": level1.attrib}

#
# for i in range(len(test_list)):
#     print (i, end = " ")
#     print (test_list[i])
#
#         #
        # for level2 in elmarray:
        #     if len(level2) > 0:
            #     lastChar = str(level2)[-20:]
            #     item = str(level2).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
            #     elmarray = list(level2)
            #     fixedarr = [str(i).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "") for i in elmarray]
            #     dict[item] = {"Elements": fixedarr, "attributes": level2.attrib}
        #         for level3 in level2:
        #             if len(level3) > 0:
        #                 for level4 in level3:
        #                     if len(level4) > 0:
        #                         for level5 in level4:
        #                             if len(level5) > 0:
        #                                 for level6 in level5:
        #                                     print(level6)
        #
        #                             else:
        #                                 lastChar = str(level5)[-20:]
        #                                 item = str(level5).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
        #                                 dict[item] = {"text": level5.text, "attributes": level5.attrib}
        #                     else:
        #                         lastChar = str(level4)[-20:]
        #                         item = str(level4).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
        #                         dict[item] = {"text": level4.text, "attributes": level4.attrib}
        #             else:
        #                 lastChar = str(level3)[-20:]
        #                 item = str(level3).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
        #                 dict[item] = {"text": level3.text, "attributes": level3.attrib}
            # else:
            #     lastChar = str(level2)[-20:]
            #     item = str(level2).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
            #     dict[item] = {"text": level2.text, "attributes": level2.attrib}


    # else:
    #     lastChar = str(level1)[-20:]
    #     item = str(level1).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
    #     dict[item] = {"text": level1.text, "attributes": level1.attrib}

# j_data = json.dump(dict, open("FILENAME_parsed.json", 'w'))
