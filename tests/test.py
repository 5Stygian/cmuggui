from cmu_graphics import *

# TODO: fix relative import error
from ..src.cmuggui.cmuggui import *

# tests
if __name__ == "__main__":
    testMenu = cmuggui.Menu(
        0, 0,
        200, 400,
        fill=cmuggui.Colors.CSS3.aliceblue,
        border=cmuggui.Colors.darkerGray,
        borderWidth=5
    )
    print(testMenu.getData())

    def testFoo():
        print("im a boring button")

    testButton = cmuggui.Menu.Button(
        testMenu,
        testFoo,
        -20, 8,
        50, 30,
        fill=rgb(175,175,175),
        borderFill=rgb(120,120,120),
        borderWidth=1,
        textValue="Test"
    )
    print(testButton.getData())

    def testFoo2():
        print("im a cooler button")

    testButton2 = cmuggui.Menu.Button(
        testMenu,
        testFoo2,
        -30, 40,
        70, 40,
        fill=gradient("yellow", "white", start="right"),
        borderFill=gradient("blue", "green", "red", start="left"),
        borderWidth=4,
        textValue="test",
        textFill=gradient("red", "white"),
        textSize=15,
        textIsBold=True
    )
    print(testButton2.getData())
    
    def buttonPresetFoo():
        print("unpacking operator is my favorite python featrue")

    def buttonPreset(presetFoo):
        presetFoo=presetFoo
        return [testMenu, presetFoo, -40, 100, 70, 50]

    testPresetButton = cmuggui.Menu.Button( *buttonPreset(buttonPresetFoo), textValue="preset", textSize=22 )

    exitButton = cmuggui.Menu.Button(
        testMenu,
        cmuggui.Functions.QQUIT,
        -20, 365,
        40, 20,
        textValue="QUIT"
    )

    def onMousePress(x, y):
        testButton.addEventListener(x, y)
        testButton2.addEventListener(x, y)
        exitButton.addEventListener(x, y)
        testPresetButton.addEventListener(x, y)

    cmu_graphics.run() # type: ignore