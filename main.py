from flask import Flask, request
from caesar import rotate_string

app = Flask (__name__)
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
        <form action="/" method="post">
            <label for="rot">Rotate By:</label>
            <input id="rot" type="text" name="rot" value="{1}"/>
            <textarea name="text_box">{0}</textarea>
            <p><input type="submit"/></p>

    </body>
</html>
"""


@app.route("/", methods=['GET'])
def index():
    return form.format('',0)

@app.route("/", methods=['POST'])
def encrypt():
    get_text = request.form['text_box']
    rotate_by = int(request.form['rot'])
    return form.format(rotate_string(get_text, rotate_by),rotate_by)

app.run()