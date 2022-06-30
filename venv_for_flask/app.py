from flask import Flask
app = Flask(__name__)

@app.route('/request/donate', methods=['POST'])
def make_donate():
    return """
    <html>
       <body>
         <form action='/' method='post'>
           <label> Пожертвование </label> 
           <input> 
           </br>
           <label> Количество </label> 
           <input>
           </br>
           <button type='submit'> Пожертововать </button>
         </form>
       </body>
    </html
    """

@app.route('/', methods=['GET'])
def request_donate():
    return """
    <html>
       <body>
         <form action='/' method='post'>           
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
if __name__ == '__main__':
    app.run(debug=True)