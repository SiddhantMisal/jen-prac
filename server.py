from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
  return "welcome  to the  hula hula  app V3"

app.run(host="0.0.0.0", port=4000, debug=True)
