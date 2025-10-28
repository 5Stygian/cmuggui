from cmu_graphics import *

from ..src.cmuggui.cmuggui import Functions

testRect = Rect(
    100,100,
    50,50
)

testLabel = Label(
    "test",
    testRect.centerX, testRect.centerY,
    fill="white",
    size=20
)

testGroup = Group( testRect, testLabel )

Functions.translate(testGroup, 50, -10)
Functions.translate(testLabel, -5, -5)
Functions.translate(testRect, 0, 5)

cmu_graphics.run()
