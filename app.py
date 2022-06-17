from flask import Flask, render_template
import os


app=Flask(__name__)

# strona główna
@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html")

#  strona z kateegoriami
@app.route("/category")
def category():
    return render_template("category.html")

#  strona do kontaktu
@app.route("/contact")
def contact():
    return render_template("contact.html")
# pojedyńczy wpis
# podziękowania zapisania na newsletter
# podziękowania za wysłanie wiadomości
    
if __name__=="__main__":
    app.run()
