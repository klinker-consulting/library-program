import sys
import os
sys.path.append(os.getcwd())

from flask import Flask
from lcd.lcd_driver import lcd

lcd_screen = lcd()

app = Flask(__name__)
@app.route('/lcd')
def print_to_lcd():
    lcd_screen.lcd_display_string('Hello World!', 1)
    return 'Printed'

@app.route('/clear')
def clear_lcd():
    lcd_screen.lcd_clear()
    return 'Cleared'

if __name__ == '__main__':
    app.run()
