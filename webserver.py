from flask import Flask, render_template,request,url_for
from ApiCanvas import *
import time
app = Flask(__name__,static_url_path='', static_folder='www',template_folder='www')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajax',methods=["POST"])
def ajax():
    string = str(request.form["getal"])
    print(string)
    aaaa=roost.dataisvanmij()
    print(aaaa)
    return "return"
@app.route('/tijd')
def tijd():
    tijd=time.strftime('%H:%M:%S',time.localtime())
    return tijd
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)