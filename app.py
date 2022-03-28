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
                spa1, spa2 = spa, 'n/a'
                l = [eng,spa1,spa2] 
            spanish_list.append(l)       
        except:
            continue

loaded_q = []
answers = []
with open('user_score.txt', 'w') as f:
    f.write(str(0))

@app.route('/', methods=['GET', 'POST'])
def basic():
    with open('user_score.txt', 'r') as f:
        score = int(f.read())
    response = ""
    loaded_q.append(choice(spanish_list))
    eng = loaded_q[len(loaded_q)-1][0]
    spa_a = [a.lower().strip(" ") for a in loaded_q[len(loaded_q)-2][1:]]
    if "n/a" in spa_a:
        spa_a = loaded_q[len(loaded_q)-2][1].lower()
    q = f"Translate: {eng}"    
    if request.method == 'POST':
        if request.form['text']:
            answers.append(request.form['text'])
            if request.form['text'].lower() in spa_a:
                response = "Good!"
                with open('user_score.txt', 'r') as f:
                    score = int(f.read())
                score += 1
                with open('user_score.txt', 'w') as f:
                    f.write(str(score))
            else:
                response = f"Sorry, right answer was: {spa_a}"
    return render_template('index.html', q=q, response=response,loaded_q=loaded_q, spa_a=spa_a,score=score)

app.run(debug=True)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')