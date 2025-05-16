from flask import Flask, render_template, request
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('Bmical.html')
@app.route('/submit', methods=['POST'])
def submit():
    Height=float(request.form['Height'])
    Weight=float(request.form['Weight'])
    BMI= Weight/ (Height * Height)

    return f"Your body Mass Index is {BMI}"
if __name__ == '__main__':
    app.run(debug=True)