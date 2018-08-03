from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "29610CFB83FA70C360C77B07AAB215E240BBF836E34214E208E742AEB2DB681C"
# askjba;skjfb
    
@app.route('/')
def index():    
    print(session)
    if 'count' not in session:
        session['count'] = 1
    return render_template("index.html",  count=session['count'])
@app.route('/increment', methods=['POST'])
def addtwo():
    session['count']+=2
    return redirect('/')

@app.route('/destroy_session', methods = ['POST'])
def goodbyegemaia():
    print(request.form)
    session.pop('count')
    return redirect('/')
app.run(debug=True)
