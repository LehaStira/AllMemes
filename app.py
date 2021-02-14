from flask import Flask
from conf import Configuration


app = Flask(__name__)
app.config.from_object(Configuration())