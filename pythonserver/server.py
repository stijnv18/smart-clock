from flask import Flask, render_template,request,url_for
import time
app = Flask(__name__,static_url_path='', static_folder='../www',template_folder='../www')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax',methods=["POST"])
def ajax():
    string = str(request.form["getal"])
    print(string)
    return "aaaaaaaaaaaaa"

@app.route('/tijd')
def tijd():
    tijd=time.strftime('%H:%M:%S',time.localtime())
    return tijd

@app.route('/timer')
def timer():
    timertime =time.strftime('%H:%M:%S',request.form["settingup"])
    with open("timers.txt", "wb") as f:
        f.write()
    print(timertime)
    return timertime

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)