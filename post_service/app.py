from flask import Flask, request, jsonify,render_template
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://post.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db=SQLALchemy(app)
class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desc= db.Column(db.String(80), nullable=False)


@app.route('/creat_posts', methods=['POST','GET'])
def create_post():
        db.create_all()
        db.session.add_all([post(desc="description one"),post(desc="description two"),post(desc="description three")])
        db.session.commit()

@app.route('/posts', methods=['GET'])
def get_posts():
    posts= post.query.all()
    return jsonify({"posts": [{"id": post.id, "desc": post.desc} for post in posts]})
@app.route('/', methods=['GET'])
def get_posts():
    posts = post.query.all()
    return render_template('posts.html', posts=posts)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
