from app import app
from flask import render_template


@app.route('/')
def hello_world():
    return render_template('index.html', name = "Keith")


@app.route('/favorite5sports')
def get_favorite_sports():
    sports = ["baseball", "basketball", "football", "track", "boxing"]
    title = "Hello, my name is Keith and here are my five favorite sports:"
    for i, sport in enumerate(sports, 1):
        title += f"\t{i}. {sport}"
    return title

@app.route('/test')
def favorite_five_test():
    return 'This is a test!!!'

from app import routes