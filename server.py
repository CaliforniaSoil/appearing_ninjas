from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html')
@app.route('/ninja')
def ninjas():
  return render_template('ninjas.html')
@app.route('/ninja/blue')
def blue():
  return render_template('blue.html')
@app.route('/ninja/orange')
def orange():
  return render_template('orange.html')
@app.route('/ninja/purple')
def red():
  return render_template('purple.html')
@app.route('/ninja/red')
def purple():
  return render_template('red.html')
@app.route('/back')
def back():
  return render_template('404.html')




app.run(debug=True)
