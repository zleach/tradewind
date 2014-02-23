import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    """Render main page."""
    return render_template('base.html')