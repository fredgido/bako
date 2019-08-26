import requests
import json
headers = {"Referer": 'https://www.pixiv.net/'}

with open("getlist.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n\r")
        r = requests.get("https://www.pixiv.net/ajax/illust/"+line, headers=headers)
        open(line+".json", 'wb').write(r.content)
        print(json.loads(r.text)["body"]["urls"])
        url = json.loads(r.text)["body"]["urls"]["original"]
        with open(url.split('/')[-1], 'wb') as f:
            r = requests.get(url, headers=headers)
            f.write(r.content)
