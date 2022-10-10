from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    the_joke = os.environ.get('JOKE')
    the_img = "https://images02.military.com/sites/default/files/2021-04/chucknorris.jpeg"
    img_size = 50
    if not the_joke:
        the_joke = 'Give me a Chuck-quote!'
        the_img = "https://cdn.iconscout.com/icon/free/png-256/emoji-95-433581.png"
        img_size = 10

    return render_template(
        'index.html',
        the_joke=the_joke,
        the_img=the_img,
        img_size=img_size)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)