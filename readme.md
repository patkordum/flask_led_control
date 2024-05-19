# LED Control Flask App

This Flask application allows you to control an LED connected to a Raspberry Pi GPIO pin through a web interface.

## Features

- Turn the LED on or off with the click of a button.
- Simple and intuitive web interface.
- Responsive design for use on different devices.

## Requirements

- Raspberry Pi with GPIO pins.
- Python 3 installed.
- Flask and gpiozero Python libraries.

## Installation
Install the required Libraries:
- pip install flask gpiozero


Run the App
- python app.py

Open a web browser and navigate to http://localhost:5000 or http://<your_pi_ip_address>:5000 to access the LED control interface.


## Directory
led_control_flask/
├── app.py                # Flask application file
├── static/               # Directory for static files
│   └── styles.css        # CSS stylesheet
└── templates/            # Directory for HTML templates
    └── control_led.html  # HTML template for LED control interface
