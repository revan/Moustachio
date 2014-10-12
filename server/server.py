#!/bin/python2
import os
import subprocess
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def root():
    return "Moustachio server is running! Request /[url] for some sweet staches."

@app.route("/<path:url>")
def stache(url):
    print url
    subprocess.call(['rm', 'out.png'])
    subprocess.call(['python2', 'transforms/moustachio.py', url])
    return send_file('out.png')

if __name__ == '__main__':
    app.run()
