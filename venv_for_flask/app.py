import json
from pathlib import Path
from flask import Flask, request, render_template
from jinja2 import Template
import os
template_dir = os.path.abspath('templates')
app = Flask(__name__)

@app.route('/', methods=['GET'])
def request_donate():
    return render_template('donate.html')

@app.route('/request/donate', methods=['POST'])
def make_donate():
    return render_template('make_donate.html')

@app.route('/thank/donate', methods=['POST'])
def thank_for_donate():
    with open('data.json', 'r') as f:
        cont = json.load(f)
    row_dict = {'name': request.form['donation_item'], 'amount': request.form['donation_amount']}
    cont.append(row_dict)
    with open('data.json', 'w') as f:
        json.dump(cont, f)
    return render_template('thank_for_donate.html')

@app.route('/ask/donate', methods=['POST'])
def ask_donate():
    with open('data.json', 'r') as f:
        cont = json.load(f)

    if not cont:
        return render_template('empty_cont.html')

    item = cont.pop()
    with open('data.json', 'w') as f:
        json.dump(cont, f)

    return render_template('full_cont.html', item=item)
    # return f'{item["name"], item["amount"]}' """
    #     <html>
    #       <body>
    #         <form action='/' method='post'>
    #           <a href='/'> Вернуться на главную страницу </a>
    #         </form>
    #       </body>
    #     </html>
    #     """

if __name__ == '__main__':
    app.run(debug=True)