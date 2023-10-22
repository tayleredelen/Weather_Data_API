from flask import Flask, render_template

# website object instance
app = Flask(__name__)


# flask is configured to look for "templates" folder in root path

# when user visits the /home url the home() function is called
# to view tutorial.html with this code you have to add /home to the url path, this creates an error
# alternatively could delete the param in @app.route to show the tutorial.html file
# the @ symbol on app is a decorator, connecting decorator (url path) to the function
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    # df = pandas.read.csv("")
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)
