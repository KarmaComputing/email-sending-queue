from flask import Flask, request
from time import time

"""
Receive email from POST request and save to folder
where incron will notice and try and send it.
"""

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    email = request.form.get("email")
    with open(f"./queue/{time()}", "w") as fp:
        print("Email written to file")
        fp.write(email)
    return "Thanks!"
