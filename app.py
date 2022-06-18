from crypt import methods
from logging import debug
import os
import pytz
from datetime import datetime
from secrets import token_urlsafe
from flask import Flask, render_template, request, redirect, abort, jsonify
from dotenv import load_dotenv
from flaskext.markdown import Markdown

from flask_wtf import Form
from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField
from flask_pagedown import PageDown

from datetime import datetime
from flask_mongoengine import MongoEngine
import uuid

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
Markdown(app)
load_dotenv()
pagedown = PageDown(app)

# Switching to MongoDB
app.config["MONGODB_HOST"] = os.environ.get("MONGO_URI")
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'txtCollection',
#     'host': 'localhost',
#     'port': 27017
# }

db = MongoEngine()
db.init_app(app)

class Txt(db.Document):
    identifier = db.StringField() #gen
    txt_data = db.StringField() #gen
    date = db.DateTimeField()
    edit_key = db.StringField() #gen

    def to_json(self):
        return{
            "identifier": self.identifier,
            "txt_data": self.txt_data,
            "date": self.date,
            "edit_key": self.edit_key,
        }

class Log(db.Document):
    timestamp = db.StringField()
    success = db.StringField()
    failed = db.StringField()

    def to_json(self):
        return{
            "timestamp": self.timestamp,
            "success": self.success,
            "failed": self.failed,
        }

#TODO: Implement Live md editing
class LiveMDEditing(Form):
    pagedown = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')

@app.route('/live/', methods = ["GET", "POST"])
def lmao():
    form = LiveMDEditing()
    if request.method == "POST":
        print("Post requested... peep")
        if form.validate_on_submit():
            print("form validated...poooop")
            txt_data = form.pagedown.data
            identifier = token_urlsafe(5)
            edit_key = str(uuid.uuid4())
            txt = Txt(txt_data=txt_data,
            identifier=identifier,
            date=datetime.now(pytz.timezone('Asia/Dhaka')),
            edit_key=edit_key)
            txt.save()
            return redirect(request.host_url + identifier + "/page/")
    return render_template('live.html', form = form)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        txt_data = request.form.get("txt-data").strip()
        identifier = token_urlsafe(5)
        edit_key = str(uuid.uuid4())
        txt = Txt(txt_data=txt_data,
        identifier=identifier,
        date=datetime.now(pytz.timezone('Asia/Dhaka')),
        edit_key=edit_key)
        txt.save()

        return redirect(request.host_url + identifier)
    return render_template("index.html")

@app.route("/<string:identifier>/")
def render_txt(identifier):
    try:
        txt = Txt.objects(identifier=identifier).as_pymongo()
    except:
        abort(404)

    return render_template("showtxt.html", txt=txt)

@app.route("/<string:identifier>/raw/")
def render_txt_raw(identifier):
    try:
        txt = Txt.objects(identifier=identifier).as_pymongo()
    except:
        abort(404)

    return render_template("raw.html", txt=txt)

@app.route("/<string:identifier>/page/")
def render_markdown(identifier):
    try:
        txt = Txt.objects(identifier=identifier).as_pymongo()
    except:
        abort(404)

    return render_template("page.html", txt=txt)

@app.route("/howto/", methods=['GET'])
def render_howto():

    return render_template("howto.html")

@app.route("/api/v1/logData", methods=["POST"])
def render_api_log():
    date=datetime.now(pytz.timezone('Asia/Dhaka'))
    success = "10"
    failed = "20"
    log = Log(timestamp = date,
    success=success,
    failed=failed
    )
    log.save()
    return log.to_json()



if __name__ == "__main__":
    app.run(debug=False)
