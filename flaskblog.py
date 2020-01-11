from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Khushboo Verma',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_created': 'April 22, 2019'
    },
    {
        'author': 'Kartik Verma',
        'title': 'Blog Post Copy',
        'content': 'I copied didis post',
        'date_created': 'May 25, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    #return "<h1>Welcome to Home Page!</h1>"
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    #return "<h1>Welcome to About Page!</h1>"
    return render_template('about.html', title = 'About')

if __name__ == "__main__":
    app.run(debug=True)