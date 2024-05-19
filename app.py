from flask import Flask, render_template, request
from gpiozero import LED

# Initialize the LED
led = LED(23)

# Create the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def control_led():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'on':
            led.on()
        elif action == 'off':
            led.off()
    return render_template('control_led.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
