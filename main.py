from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True
form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            </style>
        </head>
    <body>
    <form action="#" method='post' id="usrform">
        <label for="usrform">rotate by:
            <input name="rot" type="text" value=0>
            </label>

        <textarea name="text" form="usrform">{message}
        </textarea>
        <input type="submit"/>

    </form>
    </body>

</html>"""



@app.route('/')
def index():
    return form.format(message='')

@app.route('/', methods=['POST'])
def encrypt1():
    rot = request.form["rot"]
    text = request.form["text"]
    rot = int(rot)
    text = str(text)

    context = encrypt(text,rot)
    context = str(context)

    return form.format(message=context)



app.run()
