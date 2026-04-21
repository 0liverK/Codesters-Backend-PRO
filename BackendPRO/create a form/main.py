from flask import Flask, render_template, request, redirect
import random

app = Flask(
	__name__, 
	template_folder='templates', 
	static_folder='static'
)

posts = []
authors = []

@app.route("/")
def index():
    return render_template('index.html', posts=posts, authors=authors)

@app.route("/new_post", methods=["GET"])
def new_post():
    return render_template('new_post.html', authors=authors)

@app.route("/new_post", methods=["POST"])
def new_post_create():
    author_value = request.values.get("post_author")

    post = {
        "id": len(posts) + 1,
        "title": request.values.get("post_title"),
        "author": author_value,  # no int() → prevents crash
        "content": request.values.get("post_content"),
        "picture": "https://picsum.photos/150?random=" + str(random.randint(0, 1000))
    }

    posts.append(post)
    return redirect('/')

@app.route("/post/<int:id>")
def single_post(id):
    for post in posts:
        if post['id'] == id:
            return render_template('single_post.html', post=post, authors=authors)
    return "Post not found", 404

@app.route("/authors")
def authors_list():
    return render_template('authors.html', authors=authors)

@app.route("/new_author", methods=["GET"])
def new_author():
    return render_template('new_author.html')

@app.route("/new_author", methods=["POST"])
def new_author_create():
    author = {
        "id": random.randint(1000, 9999),
        "name": request.values.get("author_name"),
        "posts": []
    }
    authors.append(author)
    return redirect('/authors')

@app.route("/authors/<int:id>")
def single_author(id):
    for author in authors:
        if author['id'] == id:
            return render_template('single_author.html', author=author, posts=posts, authors=authors)
    return "Author not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
    

@app.route("/post/<int:id>/delete", methods=["GET"])
def delete_post(id):
    for i in range(len(posts)):
        if posts[i]['id'] == id:
            del posts[i]
            return redirect('/')
    return "Post not found", 404
