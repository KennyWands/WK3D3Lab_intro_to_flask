from webbrowser import get
from flask import render_template  # associates the html pages with the flask app

from app import app  # our instance of flask
from models.order_list import *


@app.route("/orders")  # routes implement different urls. this known as a decorator,
# adds extra functionality to function
# this decorator associates url with the function below
def index():  # view function
    return render_template("index.html", title="home", orders=orders)
    # index template, title,
    # render-temp part of jinja2 template engine gives the {{ }} functionality
    # arguments passed here will go to the html in the {{ }}sections


# @app.route("/orders/0")
# def order():
#     return render_template("order.html", title="home", order_list=orders[0])


@app.route("/order/<index>")
def order(index):
    chosen_order= orders[int(index)]
    return render_template("order.html", order= chosen_order)
