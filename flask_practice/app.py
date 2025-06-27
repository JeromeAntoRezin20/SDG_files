
from flask import Flask, render_template,request,redirect
app=Flask(__name__)

@app.route('/')
def home():
    courses=['python','java','sql']
    return render_template("home.html",courses=courses)


@app.route('/course/<course_name>', methods=["Get","Post"])
def course_page(course_name):
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        return render_template('thank_you.html',name=name,course=course_name)
    return render_template("course.html", course_name=course_name)

@app.route('/about')
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(debug=True,port = 5015)
