from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Signup')
def Signup():
    return render_template('signup.html')

@app.route('/Signin')
def Signin():
    return render_template('signin.html')

@app.route('/Dasborad')
def Dasborad():
    return render_template('dasborad.html')

@app.route('/Dashboards')
def Dashboards():
    return render_template('dashboards.html')

@app.route('/Work')
def Work():
    return render_template('work.html')

@app.route('/Create_job')
def Create_job():
    return render_template('create_job.html')

if __name__ == '__main__':
    app.run(debug=True)