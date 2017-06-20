from flask import Flask
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            </style>
        </head>
    <body>
    <form action="#" method='post' id="usrform">
        <label for="usrform">rotate by:
            <input name="rot" type="text" value=0>
            </label>

        <textarea name="text" form="usrform">
        </textarea>
        <input type="submit"/>

    </form>
    </body>

</html>"""



@app.route('/')
def index():
    return form

app.run()