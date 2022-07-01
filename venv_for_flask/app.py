import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/request/donate', methods=['POST'])
def make_donate():
    with open('data.json', 'r') as f:
        cont = json.load(f)
    row_dict = {'name': request.form['donation_item'], 'amount': request.form['donation_amount']}
    cont.append(row_dict)
    with open('data.json', 'w') as f:
        json.dump(cont, f)
    return """
    <html>
       <body>
         <form action='/request/donate' method='post'>            
           <input id='donation_item' placeholder='Пожертвование'> 
           </br>           
           <input id='donation_amount' placeholder='Количество'>
           </br>
           <button type='submit'> Пожертововать </button> 
           </br>
           <a href='/'> Вернуться на главную страницу </a>
         </form>
       </body>
    </html
    """

@app.route('/', methods=['GET'])
def request_donate():
    return """
    <html>
       <body>
         <form action='/ask/donate' method='post'>           
           <label> Регистрация Прошения </label>            
           </br>
           <button type='submit'>            
           Просить
           </button>
         </form>
         <form action='/request/donate' method='post'>           
           <label> Регистрация Пожертвования </label>            
           </br>
           <button type='submit'>            
           Пожертвовать
           </button>
         </form>
       </body>
    </html
    """
@app.route('/ask/donate', methods=['POST'])
def give_donate():
    with open('data.json', 'r') as f:
        cont = json.load(f)

    if not cont:
        return """
        <html>
          <body>
            <form action='/' method='post'>
              <p> У нас ничего нет для вас, заходите позже </p>
              <a href='/'> Вернуться на главную страницу </a>
            </form>
          </body>
        </html>
        """
    item = cont.pop()
    with open('data.json', 'w') as f:
        json.dump(cont, f)
    return f'{item["name"]}' """
        <html>
          <body>
            <form action='/' method='post'>
              <a href='/'> Вернуться на главную страницу </a>
            </form>
          </body>
        </html>
        """



if __name__ == '__main__':
    app.run(debug=True)