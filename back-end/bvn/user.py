from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome'
@app.route('/user/<username>')
def user(username):
    users = {
        'duc': {
            'name': 'Đức Béo',
            'gender': 'Nam',
            'age': 21,
            'hobbies': 'Lừa đảo ',
        },
        'tung': {
            'name': 'Trần Công Tùng',
            'gender': 'Nam',
            'age': 21,
            'hobbies': 'Xàm loz ',
        },
        'ha':{
            'name':'Nguyễn Huy Anh',
            'gender':'Nam',
            'age':21,
            'hobbies':'Cà khịa',
        }
    }
    if username in users:  
        username = users[username]
        return render_template('user.html',username=username)
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)
 