from flask import Flask,render_template,request,jsonify
from calculation import LoanEMICalculator

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    try:
        principal = float(data["principal"])
        annual_rate = float(data["annual_rate"])
        months = int(data["months"])
    except ValueError:
        return jsonify({"error": "Please enter numbers only"})
    calculation = LoanEMICalculator(principal, annual_rate, months)

    result=calculation.validate()
    if result is not True:
        return jsonify({"error":result})
    return jsonify({"emi": round(calculation.calculate_EMI(), 2)})


if __name__ == "__main__":
    app.run(debug=True)