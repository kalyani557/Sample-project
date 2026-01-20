from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"  # Required for login session

# Dummy credentials (for now)
USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/")
def home():
    return render_template("index.html")

# Login Page
@app.route("/login")
def login():
    return render_template("login.html")

# Handle Login
@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        session["user"] = username
        return redirect(url_for("dashboard"))
    else:
        return "Invalid username or password", 401

# Dashboard (Protected)
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect(url_for("login"))

# Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# Contact Form
@app.route("/contact", methods=["POST"])
def contact():
    return redirect(url_for("success"))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # temporary check
        if username == "admin" and password == "admin":
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
