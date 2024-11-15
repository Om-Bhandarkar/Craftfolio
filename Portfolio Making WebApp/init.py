from flask import Flask,render_template,request
import uuid,os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/templates')
def design():
    return render_template("designs.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route('/login', methods=["POST","GET"])
def upload():
    if request.method == 'POST':
        data = {
            "name" : request.form.get("firstname"),
            "lastname" : request.form.get("lastname"),
            "school" : request.form.get("school"),
            "college" : request.form.get("college"),
            "phone" : request.form.get("phone"),
            "email" : request.form.get("email"),
            "skill1" : request.form.get("skill1"),
            "skill2" : request.form.get("skill2"),
            "skill3" : request.form.get("skill3"),
            "skill4" : request.form.get("skill4"),
            "about" : request.form.get("about")
        }
        key = uuid.uuid1()
            # Image Uploading Method
        img = request.files['dp']
        img.save(f"static/image/{img.filename}")
        newImage = f"{key}{img.filename}"
        os.rename(f"static/image/{img.filename}",f"static/image/{newImage}")
    return render_template("portfolio.html",**data,img=newImage)

if __name__ == '__main__':
    app.run(debug=True)