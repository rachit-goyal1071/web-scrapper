import requests


def fetchAndSave(url, path):
    r=requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url ="https://aktu.ac.in/"

# r= requests.get(url)

fetchAndSave(url, "aktu.html")

