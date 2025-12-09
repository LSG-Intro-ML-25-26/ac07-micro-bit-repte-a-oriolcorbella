opcioCPU = 0

def on_button_pressed_a():
    global opcioCPU
    opcioCPU = randint(1, 3)
    if opcioCPU == 1:
        basic.show_icon(IconNames.DUCK)
    elif opcioCPU == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
        basic.pause(3000)    
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)
