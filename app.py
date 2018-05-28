import os

from flask import Flask, jsonify
from proveedor import GoogleLogin



os.environ["GOOGLE_LOGIN_CLIENT_ID"] = "364672633912-hbhtatjd9kbkbeaocn0902pivum4t0cd.apps.googleusercontent.com"
os.environ["GOOGLE_LOGIN_CLIENT_SECRET"] = "b_HGPbqiY-gBHSCBuS38fVau"


app = Flask(__name__)
app.config.update(
  SECRET_KEY="x34sdfm34",
)



for config in (
  "GOOGLE_LOGIN_CLIENT_ID",
  "GOOGLE_LOGIN_CLIENT_SECRET"

):app.config[config] = os.environ[config]



google_login = GoogleLogin(app)




@app.route("/")
def index():
  return """
<html>
<a href="{}">Python Login con con cuenta de Google </a>
""".format(google_login.authorization_url())


@google_login.login_success
def login_success(token, profile):
  return jsonify(token=token, profile=profile)

@google_login.login_failure
def login_failure(e):
  return jsonify(error=str(e))



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)