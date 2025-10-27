from cmu_graphics import *

from typing import Dict
from dataclasses import dataclass

@dataclass
class Colors:
    gray = rgb(200,200,200)
    darkgray = rgb(175,175,175)
    darkerGray = rgb(100,100,100)

class Menu(Rect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fill        = Colors.gray
        self.border      = Colors.darkerGray
        self.borderWidth = 2
        
        self.data = {
            "Class": f"{self.__class__}",
            "Dimensions": {
                "TopLeft": (self.left, self.top),
                "TopRight": (self.right, self.top),
                "BottomLeft": (self.left, self.bottom),
                "BottomRight": (self.right, self.bottom),
                "Width": self.width,
                "Height": self.height,
            },
            "BackgroundFill": self.fill,
            "BorderFill": self.border,
            "BorderWidth": self.borderWidth,
            "IsVisible": self.visible
        }
        
        self.toBack()

    def __updateData(self) -> None:
        self.data = {
            "Class": f"{self.__class__}",
            "Dimensions": {
                "TopLeft": (self.left, self.top),
                "TopRight": (self.right, self.top),
                "BottomLeft": (self.left, self.bottom),
                "BottomRight": (self.right, self.bottom),
                "Width": self.width,
                "Height": self.height,
            },
            "BackgroundFill": self.fill,
            "BorderFill": self.border,
            "BorderWidth": self.borderWidth,
            "IsVisible": self.visible
        }

    def getData(self) -> Dict:
        return self.data
    
    class Button:
        def __init__(self, parent, onclick,
                     horizontalAlign: int|float, verticalAlign: int|float,
                     width: int|float, height: int|float, fill = Colors.darkgray, borderFill = Colors.darkerGray, borderWidth: int|float = 2,
                     textValue: str = "", textFill = "black", textFont: str = "arial", textSize: int|float = 12,
                     textIsBold: bool = False, textIsItalic: bool = False, textIsVisible: bool = True):
            self.parent  = parent
            self.onclick = onclick
            
            self.horizontalAlign = horizontalAlign
            self.verticalAlign   = verticalAlign
            self.ArgWidth        = width
            self.ArgHeight       = height
            
            self.backgroundFill = fill
            self.borderFill     = borderFill
            self.borderWidth    = borderWidth
            
            self.boundingBox = Rect(
                parent.centerX+self.horizontalAlign,
                self.verticalAlign,
                self.ArgWidth,self.ArgHeight,
                fill=self.backgroundFill,
                border=self.borderFill,
                borderWidth=self.borderWidth
            )
            
            self.textValue = textValue
            self.textFill = textFill
            self.textFont = textFont
            self.textSize = textSize
            self.textIsBold = textIsBold
            self.textIsItalic = textIsItalic
            self.textIsVisible = textIsVisible
            self.text = Label(
                self.textValue,
                self.boundingBox.centerX,self.boundingBox.centerY,
                fill=self.textFill,
                font=self.textFont,
                size=self.textSize,
                bold=self.textIsBold,
                italic=self.textIsItalic,
                visible=self.textIsVisible
            )
            
            self.data = {
                "Class": f"{self.__class__}",
                "Parent": f"{self.parent}",
                "OnClickFunction": f"{self.onclick}",
                "BoundingBox": {
                    "Dimensions": {
                        "TopLeft": (self.boundingBox.left, self.boundingBox.top),
                        "TopRight": (self.boundingBox.right, self.boundingBox.top),
                        "BottomLeft": (self.boundingBox.left, self.boundingBox.bottom),
                        "BottomRight": (self.boundingBox.right, self.boundingBox.bottom),
                        "Width": self.boundingBox.width,
                        "Height": self.boundingBox.height
                    },
                    "BackgroundFill": self.boundingBox.fill,
                    "BorderFill": self.boundingBox.border,
                    "BorderWidth": self.boundingBox.borderWidth,
                    "IsVisible": self.boundingBox.visible
                },
                "Text": {
                    "Position": (self.text.centerX, self.text.centerY),
                    "Color": self.text.fill,
                    "Font": self.text.font,
                    "Size": self.text.size,
                    "IsBold": self.text.bold,
                    "IsItalic": self.text.italic,
                    "IsVisible": self.text.visible
                }
            }
            
            self.buttonGroup = Group( self.boundingBox, self.text )
        
        def __updateData(self) -> None:
            self.data = {
                "Class": f"{self.__class__}",
                "Parent": f"{self.parent}",
                "OnClickFunction": f"{self.onclick}",
                "BoundingBox": {
                    "Dimensions": {
                        "TopLeft": (self.boundingBox.left, self.boundingBox.top),
                        "TopRight": (self.boundingBox.right, self.boundingBox.top),
                        "BottomLeft": (self.boundingBox.left, self.boundingBox.bottom),
                        "BottomRight": (self.boundingBox.right, self.boundingBox.bottom),
                        "Width": self.boundingBox.width,
                        "Height": self.boundingBox.height
                    },
                    "BackgroundFill": self.boundingBox.fill,
                    "BorderFill": self.boundingBox.border,
                    "BorderWidth": self.boundingBox.borderWidth,
                    "IsVisible": self.boundingBox.visible
                },
                "Text": {
                    "Position": (self.text.centerX, self.text.centerY),
                    "Color": self.text.fill,
                    "Font": self.text.font,
                    "Size": self.text.size,
                    "IsBold": self.text.bold,
                    "IsItalic": self.text.italic,
                    "IsVisible": self.text.visible
                }
            }
        
        def getData(self) -> Dict:
            return self.data
        
        def addEventListener(self, event, x, y) -> None:
            if self.buttonGroup.contains(x, y):
                if event == "mouseDown":
                    self.onclick()
    
if __name__ == "__main__":
    # tests
    testMenu = Menu(
        0,0,
        200,400
    )
    print(testMenu.getData())

    def testFoo():
        print("im a boring button")

    testButton = Menu.Button(
        testMenu,
        testFoo,
        -20, 5,
        50, 30,
        fill=rgb(175,175,175),
        borderFill=rgb(120,120,120),
        borderWidth=1,
        textValue="Test"
    )
    print(testButton.getData())

    def testFoo2():
        print("im a cooler button")

    testButton2 = Menu.Button(
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
        textIsBold=True,
    )
    print(testButton2.getData())

    def onMousePress(x, y):
        testButton.addEventListener("mouseDown", x, y)
        testButton2.addEventListener("mouseDown", x ,y)

    cmu_graphics.run() # type: ignore