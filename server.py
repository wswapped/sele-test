from flask import Flask
import selenc as S
from flask import request
import sys
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "https://uplus.rw/scripts/browser_automation/imbwa.html"
    url = str(request.args.get('url'))
    #print(request.args, file=sys.stderr)
    resp = S.getContent(url)
    return resp


app.run()

