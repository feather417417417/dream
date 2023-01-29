#変更範囲を確認
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# render_templateはhtmlファイルを読み込む為のモジュール
app = Flask(__name__)
# アプリケーションのインスタンス化
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
# db = SQLAlchemy(app)
# # データベースの生成　作成する決まり文句みたいなもの
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(30), nullable=False)
#     detail = db.Column(db.String(100))
#     due = db.Column(db.DateTime, nullable=False)
# データベースの設計

@app.route('/', methods=['GET', 'POST'])
# ホームページのルート GETとPOSTを受け付ける
# POST＝受け渡す(フォームなどを送信した場合)　GET＝もらう(サイトにアクセスする場合)
def index():
    if request.method == 'GET':
        posts = "大吉"
    #     # リクエストを送った時のメソッドがGETの場合
    #     posts = Post.query.all()
    #     # すべてのデータを取得
        return render_template('index.html', posts=posts)
    else:
    #     title = request.form.get('title')
    #     detail = request.form.get('detail')
    #     due = request.form.get('due')
    #     new_post = Post(title=title)
    #     # create.htmlで送信したnameの情報を取得
    #     due = datetime.strptime(due, '%Y-%m-%d')
    #     new_post = Post(title=title, detail=detail, due=due)
    #     # データベースに追加する準備
    #     db.session.add(new_post)
    #     db.session.commit()
        # add追加・commit保存

        return redirect('/')
        # トップページに戻る

@app.route('/create')
def create():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
