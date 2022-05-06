from canvasapi import Canvas
from canvasapi.course import Course

API_URL =  "https://thomasmore.instructure.com"
API_KEY="13183~xbeZJanB9HgJVqg0kfsX1IndBAJdlWIg2jVpSNwmtIZtyGM1RwkE3wMMiYJhrtyU"
canvas=Canvas(API_URL,API_KEY)
def getcourse():
	les=canvas.get_courses(enrollment_status='active')
	#print(les[0])
	lessen=[]
	canvaslessen=[]
	tedoen=[]
	for vak in les:
		lessen.append(int(str(vak).split('(')[(len(str(vak).split('(')))-1].replace(')','')))
	#print(les[0].get_assignment())
	for vak in lessen:
		canvaslessen.append(canvas.get_course(vak))
	for les in canvaslessen:
		tedoen.append(les.get_assignments())
	return tedoen
	#print(le.get_assignment())
	#for l in les:
		#le=canvas.get_course(l)
		#print(l.start_at_date)

	#listassi=le.get_assignments()
	#ass=le.get_assignment(168073)
	#print(ass.due_at)
	#for assi in listassi:
		#print(assi)    

