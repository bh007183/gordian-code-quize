import xml.etree.ElementTree as ET
import json
tree = ET.parse('seatmap1.xml')
root = tree.getroot()

dict = {}


for elem in tree.iter():
    if len(elem) > 0:
        lastChar = str(elem)[-20:]
        print(lastChar)
        item = str(elem).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
        dict[item] = {"element": list(str(elem.iter()).join(" ")), "attributes": elem.attrib}
    if len(elem) == 0:
        item = str(elem).replace("<Element '{http://www.opentravel.org/OTA/2003/05/common/}", "")
        dict[item] = {"attributes": elem.attrib}


# print(ET.tostring(root, encoding='utf8').decode('utf8'))
#  element.attrib
#
j_data = json.dump(dict, open("FILENAME_parsed.json", 'w'))

# print(dict)
