from flask import Flask,render_template,url_for,redirect,request,jsonify

app = Flask(__name__)

@app.route("/")
def category_sensor():
      return render_template("categorization_animate.html")
if __name__ == "__main__":

        app.run(debug=True,threaded=True,host="0.0.0.0",port=5778)
   
