"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq8502qv2dcb93qa3g-a.oregon-postgres.render.com",
        database="todo_1m3g",
        user="root",
        password="PSN5vsV9oHdnFc1vMC0ESVX1LCL0WTmc")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
