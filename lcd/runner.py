import lcd_driver
from time import sleep

lcd_screen = lcd_driver.lcd()

lcd_screen.lcd_display_string('Hello World!', 1)

sleep(5)

lcd_screen.lcd_clear()

