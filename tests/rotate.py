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

Functions.rotate(testGroup, 45, origin="origin_Custom", originX=267, originY=182)

cmu_graphics.run()
