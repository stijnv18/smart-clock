from signal import alarm
from flask import Flask, render_template,request,url_for
from numpy import asscalar
from ApiCanvas import *
import time
import datetime
import os
from canvasapi import Canvas
app = Flask(__name__,static_url_path='', static_folder='clean',template_folder='clean')

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
 


@app.route('/')
def index():
	return render_template('clean.html')

@app.route('/ajax')
def ajax():
	lessen=Api.getcourse()
	print(lessen[0][0].due_at)
	current_time=datetime.datetime.now()
	listassdue=[]
	for vak in lessen:
		for ass in vak:
			try:
				if current_time < datetime.datetime.strptime(ass.due_at, r'%Y-%m-%dT%H:%M:%SZ'):
					listassdue.append(ass)
					print(ass)
			except:
				pass
	print(listassdue[0])
	return "return"


@app.route('/setoffset',methods=["POST"])
def setoffset():
	roosterlist=roost.dataisvanmij()
	offset = str(request.form["settingup"])
	arryoffset=[]
	temarry=[]
	for vak in roosterlist:
		a=datetime.timedelta(hours=int(vak[2].split(':')[0]), minutes=int(vak[2].split(':')[1]))
		a+=datetime.timedelta(hours=int(offset.split(':')[0]), minutes=int(offset.split(':')[1]))
		temarry.append(str(a).split(':')[0])
		temarry.append(str(a).split(':')[1])
		temarry.append(vak[1].split('-')[2])
		temarry.append(vak[1].split('-')[1])
		temarry.append(vak[1].split('-')[0])
		arryoffset.append(temarry)
		temarry=[] 
	unday=[]
	truearryoffset=[]
	for day in arryoffset:
		if [day[2],day[3],day[4]] not in unday:
			unday.append([day[2],day[3],day[4]])
			truearryoffset.append(day)
		#18:00 3 5 2022 
	alarmen=[]
	for day in truearryoffset:
		
		string = day[0]+":"+day[1]
		currdate= string+" "+day[2]+" "+day[3]+" "+day[4]
		alarmen.append(currdate)

	try:
		with open("alarm.txt", "r") as f:
			for line in f:
				line = line.split("\n")[0]
				alarmen.append(line)

	except:
		alarmen=[]
	with open("alarm.txt","w") as f:
		for alarm in alarmen:
			f.write(alarm+"\n")    

	return "aaa"



@app.route('/alarmsetup',methods=["POST"])
def alarmsetup():
	string = str(request.form["settingup"])
	currdate= datetime.datetime.now()
	#(string)
	alarmen=[]
	try:
		with open("alarm.txt", "r") as f:
			for line in f:
				line = line.split("\n")[0]
				alarmen.append(line)
				#print(alarmen)
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
		#print("file not empty")
		afgaan = datetime.datetime(int(alarmen[0].split(" ")[3]), int(alarmen[0].split(" ")[2]), int(alarmen[0].split(" ")[1]), int(alarmen[0].split(" ")[0].split(":")[0]), int(alarmen[0].split(" ")[0].split(":")[1]))
	else:
		#print("file empty")
		afgaan = datetime.datetime(int(2010), int(1), int(1), int(1), int(1))
	now = datetime.datetime.now()
	keep=[]

	#print(alarmen)

	for a in alarmen:
		afgaan = datetime.datetime(int(a.split(" ")[3]), int(a.split(" ")[2]), int(a.split(" ")[1]), int(a.split(" ")[0].split(":")[0]), int(a.split(" ")[0].split(":")[1]))
		
		if afgaan.day == now.day and afgaan.hour==now.hour and afgaan.year == now.year and afgaan.second== now.second:
			return "Wekker werkt"
		elif int((afgaan-now).days)>=0:
			keep.append(a)
		else: 
			pass
			#print(afgaan)
			#print(a)
			#print(afgaan.day) 
				
	#print(keep)
	with open("alarm.txt","w") as f:
		for k in keep:
			f.write(k+"\n")
	return "geen alarm"
@app.route('/tijd')
def tijd():
	tijd=time.strftime('%H:%M:%S',time.localtime())
	return tijd
if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0', port=5050)