
import requests
import datetime
from calendar import monthrange

def dataisvanmij():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
    cookies = {"zoneview": "false", "JSESSIONID": "540E3FE7ED8D8874DB6C5297D106A013"}

    currdate= datetime.datetime.now()


    y = currdate.year #int(input("jaar: "))
    m = currdate.month#int(input("maand: "))
    d = currdate.day#int(input("dag: "))

    ar=[]
    rooster=[]
    nonintb_ts=datetime.datetime(y, m, d)
    dayofweek = nonintb_ts.today().weekday()


    if dayofweek !=6:
        nonintb_ts=nonintb_ts-datetime.timedelta(days=dayofweek)
    else:
        nonintb_ts=nonintb_ts-datetime.timedelta(days=5-dayofweek)
    datem=datetime.datetime.strptime(str(nonintb_ts), "%Y-%m-%d %H:%M:%S")
    b_ts = int(nonintb_ts.timestamp() * 1000)
    
    num_days = monthrange(y, m)[1]
    datem = datem-datetime.timedelta(days=-6)
    e_ts = int(datetime.datetime(datem.year, datem.month, datem.day, 23, 59, 59, 999999).timestamp() * 1000)


    r = requests.get(f"https://rooster.thomasmore.be/export?format=CSV&locale=en_GB&group=false&groupByWeek=false&addSubscriptions=false&startDate={b_ts}&endDate={e_ts}", headers=headers, cookies=cookies)


    with open("rooster.CSV", "wb") as f:
        f.write(r.content)

    with open("rooster.CSV" ,"r") as r:
        for line in r:
            ar.append(line.split(";"))

    for i in range(2,len(ar)):
        temparr=[]
        temparr.append(ar[i][0])
        temparr.append(ar[i][4]) 
        temparr.append(ar[i][5])  
        rooster.append(temparr) 
    return rooster

