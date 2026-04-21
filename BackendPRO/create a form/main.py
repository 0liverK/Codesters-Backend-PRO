from flask import Flask, render_template

app = Flask(
	__name__, 
	template_folder='templates', 
	static_folder='static'
)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/new_post")
def new_post():
    return render_template('new_post.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)