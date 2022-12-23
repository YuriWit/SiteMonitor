import requests, re, os
from datetime import datetime

sites = [
    "https://www.lipocorpus.com.br/",
    "https://www.revitabeauty.com.br/",
    "https://www.clearbeauty.com.br/"
    ]

def logInfo(message): 
    print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} info: {message}')

def logError(message): 
    print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} error: {message}')

def toPath(url):
    return "last_status/" + re.sub(r'[^\w_. -]', '_', url) + ".status"

def getLastStatus(url):
    with open(toPath(url), "r") as f:
        return str(f.read())

def saveLastStatus(url, status):
    with open(toPath(url), "w") as f:
        f.write(status)

for site in sites:
    if not os.path.isfile(toPath(site)):
        with open(toPath(site), "w") as f:
            pass

for site in sites:
    try:
        resp = requests.get(site, timeout=10)
        resp.raise_for_status()
        if resp.ok:
            status = "Up"
    except:
        status = "Down"

    if status == getLastStatus(site):
        continue

    logInfo(f'site={site} changed to status={status}')
    saveLastStatus(site, status)