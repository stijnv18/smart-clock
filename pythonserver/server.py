from flask import Flask, render_template
import time
app = Flask(__name__,static_url_path='', static_folder='../www',template_folder='../www')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)