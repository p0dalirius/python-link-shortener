#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : app.py
# Author             : Podalirius (@podalirius_)
# Date created       : 3 Jun 2023


import random
from flask import Flask, render_template, request, redirect


saved_links = {}


def generate_link_id(length=8):
    """
    Generates a random link ID of specified length.

    :param length: The length of the generated link ID (default is 10).
    :return: A randomly generated link ID string.
    """

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    link_id = "".join([random.choice(alphabet) for k in range(length)])
    while link_id not in saved_links.keys():
        link_id = "".join([random.choice(alphabet) for k in range(length)])

    return link_id


app = Flask(
    __name__,
    static_url_path="/static/",
    static_folder="./static/",
    template_folder="./templates/"
)


@app.route('/<string:link_id>')
def dereference_link(link_id):
    if link_id in saved_links.keys():
        return redirect(saved_links[link_id], code=302)
    else:
        return redirect("/")


@app.route('/', methods=["GET", "POST"])
def generate_link():
    if "url" in request.args.keys():
        link_id = generate_link_id()
        shorten_link = request.url_root + link_id

        saved_links[link_id] = request.args.get("url")

        return render_template("index.html", shorten_link=shorten_link)
    else:
        return render_template("index.html", shorten_link=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

