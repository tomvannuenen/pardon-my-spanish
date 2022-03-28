from flask import Flask, render_template, request
from spanishdict import answers
from random import choice

app = Flask(__name__)

spanish_list = []
with open('spanishdict.txt', 'r') as f:
    for line in f:
        try:
            line = line.strip('\n')
            spa,eng = line.split('-')
            # remove spaces at beginning/ending of word
            ####
            if '/' in spa:
                spa1,spa2 = spa.split('/')
                l = [eng,spa1,spa2] 
            else:
                spa1, spa2 = spa, "NA"
                l = [eng,spa1,spa2] 
            spanish_list.append(l)       
        except:
            continue

@app.route('/')
def index():    
    load_q = choice(spanish_list)
    eng = load_q[0]
    spa_a = [s.lower() for s in load_q[1:]]
    q = f"Translate: {eng}".lower()
    return render_template('index.html', q=q)

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    user_a = request.form['text'].upper()        
    if request.method == "POST":
        if user_a in spa_a:
            return text
        else:
            return f"WRONG, right answer is {spa_a}"



if __name__ == "__main__":
    app.debug = True
    app.run()