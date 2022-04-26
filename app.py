from flask import Flask, request, render_template,flash

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["APPLICATION_ROOT"] = "/"


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        print(request.form.get('lat'))
        print(request.form.get('long'))
        lat = request.form.get('lat')
        long = request.form.get('long')
        error = None
        if error is not None:
            flash(error)
        return render_template('base.html', lat=lat, long=long)
    else:
        return render_template('base.html')
