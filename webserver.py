from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Webserver is online and connected to the monitor."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()