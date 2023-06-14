from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models import cookie_model

@app.route('/')
def index():
    #display all the cookie orders here
    orders  = cookie_model.Cookie_order.show_orders()
    return render_template("cookies.html", cookie_orders=orders)

@app.route("/cookies/new")
def new_order():
    return render_template("new_order.html")

@app.route("/cookies/", methods = ['post'])
def add_cookies():
    cookie_order = request.form
    if not cookie_model.Cookie_order.validate_order(cookie_order):
        return redirect('/cookies/new')
    cookie_model.Cookie_order.create_cookie_order(cookie_order)
    return redirect('/')