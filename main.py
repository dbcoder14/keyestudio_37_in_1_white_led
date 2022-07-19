def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

val = 0
led.enable(False)

def on_forever():
    global val
    while val < 1024:
        val = val + 1
        pins.analog_write_pin(AnalogPin.P0, val)
        basic.pause(5)
    while val > 0:
        val = val - 1
        pins.analog_write_pin(AnalogPin.P0, val)
        basic.pause(5)
basic.forever(on_forever)
