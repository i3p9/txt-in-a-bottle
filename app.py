from logging import debug
import os
import pytz
from datetime import datetime
from secrets import token_urlsafe
from flask import Flask, render_template, request, redirect, abort
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from dotenv import load_dotenv
from flaskext.markdown import Markdown
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


app = Flask(__name__)
Markdown(app)
#Bootstrap(app)
load_dotenv()

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


client = FaunaClient(
    secret=os.environ.get("FAUNA_SECRET"),
    domain="db.us.fauna.com",
    port=443,
    scheme="https",
)

class TxtForm(FlaskForm):
    data = StringField('data', validators=[DataRequired()])


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #txt_title = request.form.get("txt-title").strip()
        txt_data = request.form.get("txt-data").strip()

        identifier = token_urlsafe(5)
        txt = client.query(q.create(q.collection("txtbottle"), {
            "data": {
                "identifier": identifier,
                "txt_data": txt_data,
                # "txt_title": txt_title,
                "date": datetime.now(pytz.UTC)
            }
        }))

        return redirect(request.host_url + identifier)
    return render_template("index.html")

# @app.route("/page/", methods=["GET", "POST"])
# def new_form():
#     form = TxtForm()

#     return render_template("page.html", form=form)

@app.route("/<string:txt_id>/")
def render_txt(txt_id):
    try:
        txt = client.query(q.get(q.match(q.index("get_txt"), txt_id)))
    except:
        abort(404)

    return render_template("showtxt.html", txt=txt["data"])

@app.route("/<string:txt_id>/raw/")
def render_txt_raw(txt_id):
    try:
        txt = client.query(q.get(q.match(q.index("get_txt"), txt_id)))
    except:
        abort(404)

    return render_template("raw.html", txt=txt["data"])

@app.route("/<string:txt_id>/page/")
def render_markdown(txt_id):
    try:
        txt = client.query(q.get(q.match(q.index("get_txt"), txt_id)))
    except:
        abort(404)

    return render_template("page.html", txt=txt["data"])


if __name__ == "__main__":
    app.run(debug=True)
