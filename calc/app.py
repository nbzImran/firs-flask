# Put your app in here
from flask import Flask, request

app = Flask(__name__)


# @app.route('/add')
# def add():
#     a = request.args.get("a", type=int)
#     b = request.args.get("a", type=int)

#     result = a + b

#     return str(result)

# @app.route('/sub')
# def sub():
#     a = request.args.get("a", type=int)
#     b = request.args.get("b", type=int)

#     res = a - b

#     return str(res)


# @app.route('/mult')
# def mult():
#     a = request.args.get("a", type=int)
#     b = request.args.get("b", type=int)

#     rest = a * b

#     return str(rest)


# @app.route('/div')
# def div():
#     a = request.args.get("a", type=int)
#     b = request.args.get("b", type=int)

#     if b == 0:
#         return "cannot divide by 0 please chose a posoitive number"
#     rest = a / b 

#     return str(rest)

@app.route('/math/<opreation>')
def opreation(opreation):
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)


    if opreation == "add":
        rest = a + b
    elif opreation == "sub":
        rest = a - b
    elif opreation == "mult":
        rest = a * b
    elif opreation == "div":
        if b == 0:
            return "pick a positiv number"
        rest = a / b
    else:
        return "<html><h1>Invalide Opreation</h1></html>"
    
    return str(rest)