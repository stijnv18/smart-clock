import requests
import datetime

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"}
cookies = {"zoneview": "false", "JSESSIONID": "826432FF7374D64C1EF6677800F4098B"}

y = int(input("jaar: "))
m = int(input("maand: "))
d = int(input("dag: "))
b_ts = int(datetime.datetime(y, m, d).timestamp() * 1000)
e_ts = int(datetime.datetime(y, m, d+6, 23, 59, 59, 999999).timestamp() * 1000)


r = requests.get(f"https://rooster.thomasmore.be/export?format=CSV&locale=en_GB&group=false&groupByWeek=false&addSubscriptions=false&startDate={b_ts}&endDate={e_ts}", headers=headers, cookies=cookies)


with open("rooster.CSV", "wb") as f:
    f.write(r.content)








