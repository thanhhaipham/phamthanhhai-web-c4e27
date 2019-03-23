from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Enter your weight and height'
@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    height = height/100
    BMI = weight/(height*height)
    return render_template('bmi.html',BMI = BMI)

if __name__ == '__main__':
  app.run(debug=True)
 