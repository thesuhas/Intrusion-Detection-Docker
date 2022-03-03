from flask import Flask, request, url_for, render_template, redirect


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/api/xss_r", methods=['POST'])
def index():
    xss = request.form['string']
    return "good", 200
    # TODO
    # Need to setup a page so that xss can work on that page
    # return render_template("index.html",xss = xss)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8084)