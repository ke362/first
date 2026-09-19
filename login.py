from flask import Flask, render_template, request, redirect, url_for, session
app=Flask(__name__)             #_アンダースコアを前後に二つずつ！      #__name__は特殊変数。nameに実行されているファイル名が自動で入る
@app.route("/")                 #どのURLにアクセスした時にどの処理で返すか指定する仕組み(ルーティング)
def hello_world():              #ルーティングで返す関数の定義
    return "夜景を見るなら、断然夜をオススメしますよ  by小泉進次郎"
if __name__=="__main__":
    app.run(debug=True)