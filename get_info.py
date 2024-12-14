import requests
import xml.etree.ElementTree as ET

url = "http://192.168.1.100/xml/zone/getChanges.xml?visuid=90&now"

response = requests.get(url)

interesting_tags = ["uptimeInSeconds", "zoneDescription", "volume", "artist", "album", "track"]

if response.status_code == 200:
    root = ET.fromstring(response.content)
    for elem in root.iter():
        tag = elem.tag
        if tag in interesting_tags:
            print(f"{elem.tag}: {elem.text}")
else:
    print(f"FAile to retrieve data from {url}. Status code {response.status_code}")





