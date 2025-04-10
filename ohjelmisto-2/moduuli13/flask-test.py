from flask import Flask, request

app = Flask(__name__)
@app.route("/sum")
def summa():
    args = request.args
    num1 = float(args.get("num1"))
    num2 = float(args.get("num2"))
    summa = num1 + num2
    response = {
        "number 1": num1,
        "number 2": num2,
        "sum": summa
    }
    return response

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
