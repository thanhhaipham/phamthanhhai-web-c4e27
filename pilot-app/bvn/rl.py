from flask import Flask, render_template
from pymongo import MongoClient
from mlab import rivers

app = Flask(__name__)


@app.route('/river')
def river():
    riverlist = rivers.find()
    return render_template('river.html',all_rivers = riverlist)
@app.route('/river/length')
def length():
  lengthlist = rivers.find()
  return render_template('length.html',lengths = lengthlist)


if __name__ == '__main__':
  app.run(debug=True)
 