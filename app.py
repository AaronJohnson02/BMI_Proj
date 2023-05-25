from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing.html', bmi=None)

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = calculate_bmi_value(height, weight)
    return render_template('landing.html', bmi=bmi)

def calculate_bmi_value(height, weight):
    bmi = weight / (height ** 2) * 10000

    if bmi < 18.5:
        message = "BMI: {s:.2f}, You are underweight".format(s=bmi)
    elif 18.5 <= bmi <= 24.9:
        message = "BMI: {s:.2f}, You are healthy".format(s=bmi)
    elif 25 <= bmi <= 29.9:
        message = "BMI: {s:.2f}, You are overweight".format(s=bmi)
    else:
        message = "BMI: {s:.2f}, You are obese".format(s=bmi)

    return message

if __name__ == '__main__':
    app.run()
