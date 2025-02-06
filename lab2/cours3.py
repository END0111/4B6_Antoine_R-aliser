from flask import Flask, request, render_template
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("RPi.GPIO module not found. Running in simulation mode.")
    class GPIO:
        BCM = BOARD = OUT = IN = HIGH = LOW = None
        PUD_UP = PUD_DOWN = None
        @staticmethod
        def setmode(mode): pass
        @staticmethod
        def setup(pin, mode, pull_up_down=None): pass
        @staticmethod
        def output(pin, state): pass
        @staticmethod
        def input(pin): return 0
        @staticmethod
        def cleanup(): pass

app = Flask(__name__)

# GPIO setup
LED_PIN = 17
BUTTON_PIN = 27
led_state = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global led_state
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'turn_on':
            led_state = 1
            GPIO.output(LED_PIN, GPIO.HIGH)
        elif action == 'turn_off':
            led_state = 0
            GPIO.output(LED_PIN, GPIO.LOW)
    
    button_state = 1 if led_state == 0 else 0  # Simulated button state
    return render_template('index.html', led_state=led_state, button_state=button_state)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        GPIO.cleanup()
