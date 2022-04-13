myimage = images.create_image("""
# . . . .
# . . . .
# . . . .
# . . . .
# . . . .
""")

myimage.show_image(0)

def on_button_pressed_b():
    basic.pause(3000)
    while True:
        myimage.scroll_image(1,3000)
input.on_button_pressed(Button.B, on_button_pressed_b)

