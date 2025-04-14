from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        option = int(request.form["option"])
        if option == 1:
            temp = float(request.form["temperature"])
            result = (temp * 9/5) + 32
            unit = "°F"
        elif option == 2:
            temp = float(request.form["temperature"])
            result = temp + 273.15
            unit = "°K"
        elif option == 3:
            temp = float(request.form["temperature"])
            result = (temp - 32) * 5/9
            unit = "°C"
        elif option == 4:
            temp = float(request.form["temperature"])
            result = (temp + 459.67) * 5/9
            unit = "°K"
        elif option == 5:
            temp = float(request.form["temperature"])
            result = temp - 273.15
            unit = "°C"
        elif option == 6:
            temp = float(request.form["temperature"])
            result = (temp * 9/5) - 459.67
            unit = "°F"
        elif option == 7:
            return render_template("index.html", result=None, error="Exiting...")
        else:
            result = None
            error = "Invalid option! Please select a valid option."
            return render_template("index.html", result=result, error=error)
        
        return render_template("index.html", result=f"{result} {unit}", error=None)
    
    return render_template("index.html", result=None, error=None)

if __name__ == "__main__":
    app.run(debug=True)
