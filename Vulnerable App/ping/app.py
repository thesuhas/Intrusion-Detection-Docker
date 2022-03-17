from flask import Flask, render_template,jsonify,request,abort
import os
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/",methods=["GET"])
def test():
    return "Hello World",200

@app.route("/api/ping",methods=["POST"])
def list_add_user():
    if request.method == 'POST':
        IP = request.get_json()["IP"]
        cmd = "ping -c 4 "+ IP
        stream = os.popen(cmd)
        output = stream.read()
        return output,200
    else:
        return 405

if __name__ == '__main__':
    # app.debug = True
    app.run(port=8081,host='0.0.0.0')
