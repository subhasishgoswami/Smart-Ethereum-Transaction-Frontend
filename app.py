
import numpy as np
# Flask utils
from flask import Flask, redirect, url_for, request, render_template,g
from werkzeug.utils import secure_filename

#For Heroku Server Web App
from gevent.pywsgi import WSGIServer
import joblib
# Define a flask app
app = Flask(__name__)


#Load your trained model

model= joblib.load(open('model.sav', 'rb'))



def transaction(t):
    print(t)
    s= np.reshape(t, (1,-1))
    i= model.predict(s)
    return int(i[0])
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')
@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
            
            
            temp= [request.form['value(Eth)'],request.form['gas_price'],request.form['gas_limit'],request.form['previousBlockDifficulty'],(0 if request.form['CA(0)/EA(1)']== 'on' else 1),request.form['previousBlockDifficulty'],request.form['appearHour'],request.form['appearHour'],request.form['time2mine'],request.form['last20'],request.form['last120'],request.form['last360'],request.form['last420'],request.form['last600'],6*request.form['last600'],float(request.form['gas_price'])*float(request.form['gas_limit'])]
            s = transaction(temp)
            if s==0:
                t= "In Less Than 30 Seconds"
            elif s== 1:
                t= "Between 30 Seconds And 1 Minute"
            elif s ==2:
                t= "Between 1 Minute And 2 Minutes"
            elif s== 3:
                t= "Between 2 Minutes And 6 Minutes"
            elif s== 4:
                t= "In More Than 6 Minutes"
            e= "ethereum"+ str(s)+ ".png"
            return render_template('ethereum.html', transaction= t, e= e)
            


if __name__ == '__main__':
        app.run(threaded = False)
