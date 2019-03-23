from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'
@app.route('/about-me/')
def aboutme():
    about_me = {
        'name':'Phạm Thanh Hải',
        'work':'Student',
        'school':'MTA',
        'hobbies':'Gym,Bikes,Cars',
        'crush':'PVA'
    }
    return render_template('study.html',about_me=about_me)

@app.route('/school/')
def school():
    return redirect('http://techkids.vn')


if __name__ == '__main__':
  app.run(debug=True)
 