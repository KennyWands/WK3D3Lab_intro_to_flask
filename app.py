from flask import Flask

app = Flask(__name__)
#creates app object of class Flask
from controllers import controller

if __name__ == "__main__":
    app.run(debug=True)
# name is predefined variable and sets main as the module in which flask 
# is used. app.run then is the controller module