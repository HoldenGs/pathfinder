#!/usr/bin/python3

"""
Application for finding quickest path between two Wikipedia pages.

"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/', methods = ['POST'])
def pathfinder():
    """Handle form data from client."""
    search_items = request.form['search'].split(",")
    start_item = search_items[0]
    end_item = search_items[1]
    return (start_item, end_item)

@app.route('/')
def index():
    """Render webpage."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
