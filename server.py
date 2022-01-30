from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'keep it secret, keep it safe'



@app.route('/')
def index():
    if 'num' not in session:
        session['num']=random.randint(1,100)
        session['color']=  'coral'
    if 'guess' not in session:
        session['guess']='Time to guess!'
    if 'guesscnt' not in session:
        session['guesscnt']= 0

    return render_template("index.html")

@app.route('/reset',methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/guess',methods=['POST','GET'])
def userinput():
    userguess=int(request.form.get("userguess"))
    session['guess']=userguess
    if session['guesscnt'] < 5:
        if userguess>session['num']:
            session['guesscnt']+=1
            session['guess']="Too High!"
            session['color']=  'red'
        elif userguess<session['num']:
            session['guesscnt']+=1
            session['guess']="Too Low!"
            session['color']=  'red'
        else:
            session['guess']=("You got it!")
            session['color']=  'green'
            session['winner']=True
    else:
        session['guess'] = 'You Lose! Better luck next time!'
        session['color'] = 'yellow'
    return redirect('/')

@app.route('/HOF', methods=['POST','GET'])
def halloffameinduction():
    newHOFName=request.form.get("winname")
    session['winner']=newHOFName
    return render_template("index2.html")



if __name__ == "__main__":
    app.run(debug=True)