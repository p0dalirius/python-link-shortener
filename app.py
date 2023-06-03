#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : app.py
# Author             : Podalirius (@podalirius_)
# Date created       : 3 Jun 2023


import random
from flask import Flask, render_template, request, redirect


saved_links = {}


def generate_link_id():
    max_len = 10
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    link_id = ""
    for k in range(max_len):
        link_id += random.choice(alphabet)
    return link_id


app = Flask(
    __name__,
    static_url_path="/static/",
    static_folder="./static/",
    template_folder="./templates/"
)


@app.route('/<string:link_id>')
def dereference_link(link_id):
    return redirect(saved_links[link_id], code=302)


@app.route('/', methods=["GET", "POST"])
def generate_link():
    print(request.args.keys())
    if "url" in request.args.keys():
        linkid = generate_link_id()
        saved_links[linkid] = request.args.get("url")
        return render_template("index.html", linkid=linkid)
    else:
        return render_template("index.html", linkid=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

