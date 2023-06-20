from flask import Flask, render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    decs = db.Column(db.String(500))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, decs=desc)
        db.session.add(todo)
        db.session.commit()
    alltodos = Todo.query.all()

    return render_template('index.html', alltodos=alltodos)


@app.route('/show')
def product():
    alltodo = Todo.query.all()
    print(alltodo)
    return 'Welcome to second app'




@app.route('/delete/<int:sno>')
def delete(sno):
    query= Todo.query.filter_by(sno=sno).first()
    db.session.delete(query)
    db.session.commit()

    return redirect ('/')



if __name__ == "__main__":
    app.run(debug=True, port=8000)
