from canvasapi import Canvas
from canvasapi.course import Course

API_URL =  "https://thomasmore.instructure.com"
API_KEY="13183~xbeZJanB9HgJVqg0kfsX1IndBAJdlWIg2jVpSNwmtIZtyGM1RwkE3wMMiYJhrtyU"
canvas=Canvas(API_URL,API_KEY)
def getcourse():
    les=canvas.get_courses(enrollment_status='active')
    le = canvas.get_course(20220)
    for l in les:
        #le=canvas.get_course(l)
        print(l.start_at_date)

    listassi=le.get_assignments()
    for assi in listassi:
        print(assi)    
