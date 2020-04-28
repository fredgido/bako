import requests
import json
headers = {"Referer": 'https://www.pixiv.net/'}


def download(id):
    if not isinstance(id, str):
        id = id.__str__();
    r = requests.get("https://www.pixiv.net/ajax/illust/" + id, headers=headers)
    open('static/pixiv/'+id + ".json", 'wb').write(r.content)
    print(json.loads(r.text)["body"]["urls"])
    url = json.loads(r.text)["body"]["urls"]["original"]
    with open('static/pixiv/'+url.split('/')[-1], 'wb') as f:
        r = requests.get(url, headers=headers)
        f.write(r.content)
def main():
    with open("shortgetlist.txt", "r") as f:
        for line in f:
           line = line.rstrip("\n\r")
           try:
               ftest= open('static/pixiv/' + line + ".json")
           except FileNotFoundError:
               download(line)
           finally:
               ftest.close()

if __name__ == "__main__":
    main()
