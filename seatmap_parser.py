import xml.etree.ElementTree as ET
import json
tree = ET.parse('seatmap1.xml')
root = tree.getroot()

dict = {}

for elem in tree.iter():
    if len(elem) > 0:
        item = str(elem)
        dict[item] = str(list(elem.iter()))


# print(ET.tostring(root, encoding='utf8').decode('utf8'))print()
 # element.attrib
# print(dict)
j_data = json.dumps(dict)
print(j_data)

with open("FILENAME_parsed.json", "w") as outfile:
    json.dump(j_data, outfile)
