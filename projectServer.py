from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'softwareapplicationssecret'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/')
def game():
    return render_template('game.html')

# @app.route('/slides')
# def slides():
#     user = session['user']
#     topics = ["Introduction", "What is Software?"]
#     return render_template('slides2.html', user=user, slides=topics)

@app.route('/login', methods=['POST'])
def login():
    user1 = request.form['user1']
    user2 = request.form['user2']
    session['user1'] = user1.title()
    session['user2'] = user2.title()
    session['currentPlayer']= session['user1']
    session['score1'] = 0
    session['score2'] = 0
    session['color']= 'red'
    
    # session['winner'] = 'NO winner'
    return render_template('game.html', player1=session['user1'], player2=session['user2'], player=session['currentPlayer'], score1=  session['score1'], score2= session['score2'])

@app.route('/roll', methods=['POST'])
def roll():
    # user1 = request.form['user1']
    # user2 = request.form['user2']
    
    value= random.randrange(1,7)
    session['value'] = value

    if (value!=1 and (session['currentPlayer'] == session['user1'])):
        if(session['score1']>0):
            total = session['score1']
        else:
            total = 0    
        session['score1'] =  total+value
    elif(value==1 and (session['currentPlayer'] == session['user1'])):
        session['score1'] =0
        session['currentPlayer'] = session['user2']
        session['color']= 'blue'
        # session['value']=0
    elif (value!=1 and (session['currentPlayer'] == session['user2'])):
        if(session['score2']>0):
             total = session['score2']
        else:
             total = 0    
        session['score2'] =  total+value
    elif(value==1 and (session['currentPlayer'] == session['user2'])):
         session['score2'] =0
         session['currentPlayer'] = session['user1']  
         session['color']= 'red' 
        #  session['value']=0 

    if (session['score1'] >= 20):
        session['winner']= session['user1']
        return render_template('game.html',color= session['color'],winner=session['winner'], value= session['value'] , player=session['currentPlayer'] ,player1=session['user1'], player2=session['user2'], score1=  session['score1'], score2= session['score2'])
    elif (session['score2'] >= 20):
        session['winner']= session['user2']
        return render_template('game.html',color= session['color'],winner=session['winner'], value= session['value'] , player=session['currentPlayer'] ,player1=session['user1'], player2=session['user2'], score1=  session['score1'], score2= session['score2'])

    return render_template('game.html',color= session['color'], value= session['value'] , player=session['currentPlayer'] ,player1=session['user1'], player2=session['user2'], score1=  session['score1'], score2= session['score2'])

@app.route('/hold',methods=['POST'])
def hold():
    if((session['currentPlayer'] == session['user1'])):
        session['currentPlayer'] = session['user2']
        session['color']= 'blue'
    elif((session['currentPlayer'] == session['user2'])):
        session['currentPlayer'] = session['user1']  
        session['color']= 'red' 
    return render_template('game.html',color= session['color'], value= session['value'] , player=session['currentPlayer'] ,player1=session['user1'], player2=session['user2'], score1=  session['score1'], score2= session['score2'])


@app.route('/logout')
def logout():
    del session['user1']
    del session['user2']
    # if(session['value']):
    #    del session['value']
    session.pop('value', None)  

    del session['score1']
    
    del session['score2']
   
    del session['currentPlayer']
    # if(session['winner']):
    #  del session['winner']
    session.pop('winner', None)

    del session['color']
    # session.pop('user1', None)
    # session.pop('user2', None)
    # session.pop('value', None)
    # session.pop('score1', None)
    # session.pop('score2', None)
    # session.pop('currentPlayer', None)
    # session.pop('winner', None)
    # session.pop('color', None)
    return redirect('/')

if __name__ == '__main__':
   app.run(debug=True)