from flask import Flask, render_template, request, flash
import uuid, os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

@app.route('/')
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        print(f"Error rendering homepage: {e}")
        flash("An error occurred while loading the homepage.")
        return render_template("error.html"), 500

@app.route('/templates')
def design():
    try:
        return render_template("designs.html")
    except Exception as e:
        print(f"Error rendering designs page: {e}")
        flash("An error occurred while loading the templates page.")
        return render_template("error.html"), 500

@app.route("/form")
def form():
    try:
        return render_template("form.html")
    except Exception as e:
        print(f"Error rendering form page: {e}")
        flash("An error occurred while loading the form page.")
        return render_template("error.html"), 500

@app.route('/login', methods=["POST", "GET"])
def upload():
    if request.method == 'POST':
        try:
            data = {
                "name": request.form.get("firstname"),
                "lastname": request.form.get("lastname"),
                "school": request.form.get("school"),
                "college": request.form.get("college"),
                "phone": request.form.get("phone"),
                "email": request.form.get("email"),
                "skill1": request.form.get("skill1"),
                "skill2": request.form.get("skill2"),
                "skill3": request.form.get("skill3"),
                "skill4": request.form.get("skill4"),
                "about": request.form.get("about"),
                "github": request.form.get("github"),
                "linkedin": request.form.get("linkedin")
            }
            key = uuid.uuid1()
            # Image Uploading Method
            img = request.files['dp']
            img_path = f"Portfolio Making WebApp/static/image/{img.filename}"
            img.save(img_path)
            
            # Renaming the image
            newImage = f"{key}_{img.filename}"
            new_img_path = f"Portfolio Making WebApp/static/image/{newImage}"
            os.rename(img_path, new_img_path)
            
            return render_template("portfolio.html", **data, img=newImage)
        except FileNotFoundError as fe:
            print(f"File error: {fe}")
            flash("An error occurred while uploading the image. Please try again.")
            return render_template("form.html"), 400
        except Exception as e:
            print(f"Error in upload route: {e}")
            flash("An unexpected error occurred. Please try again later.")
            return render_template("form.html"), 500

    try:
        return render_template("login.html")
    except Exception as e:
        print(f"Error rendering login page: {e}")
        flash("An error occurred while loading the login page.")
        return render_template("error.html"), 500

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Critical error starting the application: {e}")
