# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:36:20 2022

@author: DELL
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run()