# linux/mac
# buat venv di vscode bash "python3 -m venv env"
# aktifkan venv "source flask_env/bin/activate"

# pip3 install flask

# windows
# python -m venv env

# aktifkan venv
# env bypass "Set-ExecutionPolicy -Scope CurrentUser Unrestricted"
# menjalankan (powershell) "env flask_env\Scripts\activate.ps1"

# pip install flask

# untuk manual
# set for windows, export for mac, linux
# to "set FLASK_APP=flaskblog.py"
# live view (debugger) "set FLASK_DEBUG=1"
# run "flask run"

# import os
# print(os.getcwd())


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '< h1 > Hello, World!< /h1 > nahlo err'


# jalan secara automatic run di terminal "python flaskblog.py"
if __name__ == '__main__':
    app.run(debug=True)