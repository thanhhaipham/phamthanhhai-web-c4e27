from flask import *
from bike import Bikes 
from bson.objectid import ObjectId
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/newbike',methods=['GET','POST'])
def newbike():
    if request.method == 'GET':
        return render_template('bikebike.html')
    elif request.method == 'POST':
        form = request.form
        Model = form['Model']
        Dailyfee = form['Dailyfee']
        Image = form['Image']
        Year = form['Year']

if __name__ == '__main__':
  app.run(debug=True)
 