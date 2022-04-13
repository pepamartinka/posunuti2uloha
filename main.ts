let myimage = images.createImage(`
# . . . .
# . . . .
# . . . .
# . . . .
# . . . .
`)
myimage.showImage(0)
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.pause(3000)
    while (true) {
        myimage.scrollImage(1, 3000)
    }
})
