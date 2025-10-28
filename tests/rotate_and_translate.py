from cmu_graphics import *

from ..src.cmuggui.cmuggui import Functions.translate, Functions.rotate

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

Functions.rotate(testGroup, 70, origin="object_TopRight")
Functions.translate(testGroup, 20, 40)

cmu_graphics.run()
