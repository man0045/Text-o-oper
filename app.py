from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/')

def index():
 return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login/log.html')

@app.route('/signup')
def signup():
    return render_template('Signup/signup.html')


if __name__ =="__main__":
 app.run(host="0.0.0.0")