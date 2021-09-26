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

load_dotenv()

client = FaunaClient(
    secret=os.environ.get("FAUNA_SECRET"),
    domain="db.us.fauna.com",
    port=443,
    scheme="https",
)
txt_id = "CJkVBHw"
txt = client.query(q.get(q.match(q.index("get_txt"), txt_id)))
print(txt)
