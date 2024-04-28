import requests
import time
def fetchAndSave(url, path):
    time.sleep(15)  # Wait for 5 seconds
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)


url = "https://srip.iitgn.ac.in/portal/projects/"

fetchAndSave(url, "iitg.html")

