from flask import Flask, render_template

# website object instance
app = Flask("Website")


# flask is configured to look for "templates" folder in root path

# when user visits the /home url the home() function is called
# to view tutorial.html with this code you have to add /home to the url path, this creates an error
# alternatively could delete the param in @app.route to show the tutorial.html file
# the @ symbol on app is a decorator, connecting decorator (url path) to the function
@app.route("/home")
def home():
    return render_template("tutorial.html")


@app.route("/about/")
def about():
    return render_template("about.html")


app.run(debug=True)
