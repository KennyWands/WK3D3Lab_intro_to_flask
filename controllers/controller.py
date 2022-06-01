from webbrowser import get
from flask import render_template

from app import app
from models.order_list import *


@app.route("/orders")
def index():
    return render_template("index.html", title="home", order_list=orders)


# @app.route("/orders/0")
# def order():
#     return render_template("order.html", title="home", order_list=orders[0])


@app.route("/orders/index", methods=["get"])
def order():
    return render_template("order.html", title="home", print=orders)
