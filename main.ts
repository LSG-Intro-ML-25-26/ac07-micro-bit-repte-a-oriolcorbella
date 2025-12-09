let opcioCPU = 0
input.onButtonPressed(Button.A, function () {
    opcioCPU = randint(1, 3)
    if (opcioCPU == 1) {
        basic.showIcon(IconNames.Duck)
    } else if (opcioCPU == 2) {
        basic.showIcon(IconNames.Square)
    } else {
        basic.showIcon(IconNames.Scissors)
    }
    basic.pause(2000)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
