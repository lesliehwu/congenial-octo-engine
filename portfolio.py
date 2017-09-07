from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def port_index():
    return render_template("index.html")

@app.route("/projects")
def port_proj():
    return render_template("projects.html")

@app.route("/about")
def port_about():
    return render_template("about.html")

app.run(debug=True)
