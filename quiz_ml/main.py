# flask
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static',
)