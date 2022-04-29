from flask import Flask, render_template,request,url_for
from ApiCanvas import *
import time
import datetime
import os
app = Flask(__name__,static_url_path='', static_folder='clean',template_folder='clean')


 


@app.route('/')
def index():
    return render_template('clean.html')

@app.route('/ajax')
def ajax():
    roosterlist=roost.dataisvanmij()
    print(roosterlist)
    return "return"

@app.route('/alarmsetup',methods=["POST"])
def alarmsetup():
    string = str(request.form["settingup"])
    currdate= datetime.datetime.now()
    print(string)
    alarmen=[]
    try:
        with open("alarm.txt", "r") as f:
            for line in f:
                line = line.split("\n")[0]
                alarmen.append(line)
                print(alarmen)
    except:
        alarmen=[]
    alarmen.append(string+" "+str(currdate.day)+" "+str(currdate.month)+" "+str(currdate.year))
    with open("alarm.txt","w") as f:
        for alarm in alarmen:
            f.write(alarm+"\n")

    return "return"

@app.route('/alarmcheck')
def alamrchek():
    alarmen=[]
    try:
        with open("alarm.txt", "r") as f:
            for line in f:
                line = line.split("\n")[0]
                alarmen.append(line)
    except:
        return("No alarms set")
    
    if os.stat('alarm.txt').st_size != 0:
        print("filen not empty")
        afgaan = datetime.datetime(int(alarmen[0].split(" ")[3]), int(alarmen[0].split(" ")[2]), int(alarmen[0].split(" ")[1]), int(alarmen[0].split(" ")[0].split(":")[0]), int(alarmen[0].split(" ")[0].split(":")[1]))
    else:
        print("fille empty")
        afgaan = datetime.datetime(int(2010), int(1), int(1), int(1), int(1))
    now = datetime.datetime.now()

    if afgaan.day == now.day and afgaan.hour==now.hour and afgaan.year == now.year and afgaan.second== now.second:
        return "Wekker werkt"
    elif int((afgaan-now).days)<0:
        with open("alarm.txt","w") as f:
            for alarm in alarmen:
                if int((afgaan-now).days)<0:
                    pass
                else:   
                    f.write(alarm+"\n")
    return "geen alarm"
@app.route('/tijd')
def tijd():
    tijd=time.strftime('%H:%M:%S',time.localtime())
    return tijd
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)