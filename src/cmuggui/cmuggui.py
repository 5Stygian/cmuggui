from cmu_graphics import *

from typing import Dict

class Colors:
    gray       = rgb(200,200,200)
    darkgray   = rgb(175,175,175)
    darkerGray = rgb(100,100,100)
    
    # CSS 3 colors
    class CSS3:
        aliceblue            = rgb(240, 248, 255)
        antiquewhite         = rgb(250, 235, 215)
        aqua                 = rgb(0, 255, 255)
        aquamarine           = rgb(127, 255, 212)
        azure                = rgb(240, 255, 255)
        beige                = rgb(245, 245, 220)
        bisque               = rgb(255, 228, 196)
        black                = rgb(0, 0, 0)
        blanchedalmond       = rgb(255, 235, 205)
        blue                 = rgb(0, 0, 255)
        blueviolet           = rgb(138, 43, 226)
        brown                = rgb(165, 42, 42)
        burlywood            = rgb(222, 184, 135)
        cadetblue            = rgb(95, 158, 160)
        chartreuse           = rgb(127, 255, 0)
        chocolate            = rgb(210, 105, 30)
        coral                = rgb(255, 127, 80)
        cornsilk             = rgb(255, 248, 220)
        cornflowerblue       = rgb(100, 149, 237)
        crimson              = rgb(220, 20, 60)
        cyan                 = rgb(0, 255, 255)
        darkblue             = rgb(0, 0, 139)
        darkcyan             = rgb(0, 139, 139)
        darkgoldenrod        = rgb(184, 134, 11)
        darkgray             = rgb(169, 169, 169)
        darkgreen            = rgb(0, 100, 0)
        darkgrey             = rgb(169, 169, 169)
        darkkhaki            = rgb(189, 183, 107)
        darkmagenta          = rgb(139, 0, 139)
        darkolivegreen       = rgb(85, 107, 47)
        darkorange           = rgb(255, 140, 0)
        darkorchid           = rgb(153, 50, 204)
        darkred              = rgb(139, 0, 0)
        darksalmon           = rgb(233, 150, 122)
        darkseagreen         = rgb(143, 188, 143)
        darkslateblue        = rgb(72, 61, 139)
        darkslategray        = rgb(47, 79, 79)
        darkslategrey        = rgb(47, 79, 79)
        darkturquoise        = rgb(0, 206, 209)
        darkviolet           = rgb(148, 0, 211)
        deeppink             = rgb(255, 20, 147)
        deepskyblue          = rgb(0, 191, 255)
        dimgray              = rgb(105, 105, 105)
        dimgrey              = rgb(105, 105, 105)
        dodgerblue           = rgb(30, 144, 255)
        firebrick            = rgb(178, 34, 34)
        floralwhite          = rgb(255, 250, 240)
        forestgreen          = rgb(34, 139, 34)
        fuchsia              = rgb(255, 0, 255)
        gainsboro            = rgb(220, 220, 220)
        ghostwhite           = rgb(248, 248, 255)
        gold                 = rgb(255, 215, 0)
        goldenrod            = rgb(218, 165, 32)
        gray                 = rgb(128, 128, 128)
        green                = rgb(0, 128, 0)
        greenyellow          = rgb(173, 255, 47)
        grey                 = rgb(128, 128, 128)
        honeydew             = rgb(240, 255, 240)
        hotpink              = rgb(255, 105, 180)
        indianred            = rgb(205, 92, 92)
        indigo               = rgb(75, 0, 130)
        ivory                = rgb(255, 255, 240)
        khaki                = rgb(240, 230, 140)
        lavender             = rgb(230, 230, 250)
        lavenderblush        = rgb(255, 240, 245)
        lawngreen            = rgb(124, 252, 0)
        lemonchiffon         = rgb(255, 250, 205)
        lightblue            = rgb(173, 216, 230)
        lightcoral           = rgb(240, 128, 128)
        lightcyan            = rgb(224, 255, 255)
        lightgoldenrodyellow = rgb(250, 250, 210)
        lightgray            = rgb(211, 211, 211)
        lightgreen           = rgb(144, 238, 144)
        lightgrey            = rgb(211, 211, 211)
        lightpink            = rgb(255, 182, 193)
        lightsalmon          = rgb(255, 160, 122)
        lightseagreen        = rgb(32, 178, 170)
        lightskyblue         = rgb(135, 206, 250)
        lightslategray       = rgb(119, 136, 153)
        lightslategrey       = rgb(119, 136, 153)
        lightsteelblue       = rgb(176, 196, 222)
        lightyellow          = rgb(255, 255, 224)
        lime                 = rgb(0, 255, 0)
        limegreen            = rgb(50, 205, 50)
        linen                = rgb(250, 240, 230)
        magenta              = rgb(255, 0, 255)
        maroon               = rgb(128, 0, 0)
        mediumaquamarine     = rgb(102, 205, 170)
        mediumblue           = rgb(0, 0, 205)
        mediumorchid         = rgb(186, 85, 211)
        mediumpurple         = rgb(147, 112, 216)
        mediumseagreen       = rgb(60, 179, 113)
        mediumslateblue      = rgb(123, 104, 238)
        mediumspringgreen    = rgb(0, 250, 154)
        mediumturquoise      = rgb(72, 209, 204)
        mediumvioletred      = rgb(199, 21, 133)
        midnightblue         = rgb(25, 25, 112)
        mintcream            = rgb(245, 255, 250)
        mistyrose            = rgb(255, 228, 225)
        moccasin             = rgb(255, 228, 181)
        navajowhite          = rgb(255, 222, 173)
        navy                 = rgb(0, 0, 128)
        oldlace              = rgb(253, 245, 230)
        olive                = rgb(128, 128, 0)
        olivedrab            = rgb(107, 142, 35)
        orange               = rgb(255, 165, 0)
        orangered            = rgb(255, 69, 0)
        orchid               = rgb(218, 112, 214)
        palegoldenrod        = rgb(238, 232, 170)
        palegreen            = rgb(152, 251, 152)
        paleturquoise        = rgb(175, 238, 238)
        palevioletred        = rgb(216, 112, 147)
        papayawhip           = rgb(255, 239, 213)
        peachpuff            = rgb(255, 218, 185)
        peru                 = rgb(205, 133, 63)
        pink                 = rgb(255, 192, 203)
        plum                 = rgb(221, 160, 221)
        powderblue           = rgb(176, 224, 230)
        purple               = rgb(128, 0, 128)
        red                  = rgb(255, 0, 0)
        rosybrown            = rgb(188, 143, 143)
        royalblue            = rgb(65, 105, 225)
        saddlebrown          = rgb(139, 69, 19)
        salmon               = rgb(250, 128, 114)
        sandybrown           = rgb(244, 164, 96)
        seagreen             = rgb(46, 139, 87)
        seashell             = rgb(255, 245, 238)
        sienna               = rgb(160, 82, 45)
        silver               = rgb(192, 192, 192)
        skyblue              = rgb(135, 206, 235)
        slateblue            = rgb(106, 90, 205)
        slategray            = rgb(112, 128, 144)
        slategrey            = rgb(112, 128, 144)
        snow                 = rgb(255, 250, 250)
        springgreen          = rgb(0, 255, 127)
        steelblue            = rgb(70, 130, 180)
        tan                  = rgb(210, 180, 140)
        teal                 = rgb(0, 128, 128)
        thistle              = rgb(216, 191, 216)
        tomato               = rgb(255, 99, 71)
        turquoise            = rgb(64, 224, 208)
        violet               = rgb(238, 130, 238)
        wheat                = rgb(245, 222, 179)
        white                = rgb(255, 255, 255)
        whitesmoke           = rgb(245, 245, 245)
        yellow               = rgb(255, 255, 0)
        yellowgreen          = rgb(154, 205, 50)

class Functions:
    @staticmethod
    def QUIT() -> None:
        raise KeyboardInterrupt

    @staticmethod
    def toggleVisibility(object) -> None:
        object.visible = not(object.visible)

    @staticmethod
    def translate(object, translateX: int|float, translateY: int|float) -> None:
        object.centerX += translateX
        object.centerY += translateY
    
    @staticmethod
    def rotate(object, degrees: int|float, origin: str="object_Center", originX: int|float|None=None, originY: int|float|None=None) -> None:
        match origin:
            case "object_Center":
                object.rotate(degrees, object.centerX, object.centerY)
            case "object_TopLeft":
                object.rotate(degrees, object.left, object.top)
            case "object_TopRight":
                object.rotate(degrees, object.right, object.top)
            case "object_BottomLeft":
                object.rotate(degrees, object.left, object.bottom)
            case "object_BottomRight":
                object.rotate(degrees, object.right, object.bottom)
            case "origin_Custom":
                object.rotate(degrees, originX, originY)



class Menu(Rect):
    def __init__(self, *args, fill=Colors.gray, border=Colors.darkerGray, debug: bool = False, **kwargs):
        super().__init__(*args, **kwargs, fill=fill, border=border)
        self.fill       = fill
        self.border     = border

        self.debug = debug
        if self.debug:
            self.debugLineNS = Line(
                self.centerX, self.top,
                self.centerX, self.bottom,
                fill=Colors.CSS3.red,
                lineWidth=5,
                opacity=55
            )
            self.debugLineEW = Line(
                self.left, self.centerY,
                self.right, self.centerY,
                fill=Colors.CSS3.blue,
                lineWidth=5,
                opacity=55
            )
            self.debugBorder = Rect(
                self.left, self.top,
                self.width, self.height,
                fill=None,
                border=Colors.CSS3.yellow,
                borderWidth=5,
                opacity=55
            )
        
        self.data = {
            "Class": f"{self.__class__.__name__}",
            "Debug": self.debug,
            "Dimensions": {
                "TopLeft": (self.left, self.top),
                "TopRight": (self.right, self.top),
                "BottomLeft": (self.left, self.bottom),
                "BottomRight": (self.right, self.bottom),
                "Width": self.width,
                "Height": self.height,
            },
            "BackgroundFill": (self.fill.red, self.fill.green, self.fill.blue),
            "BorderFill": (self.border.red, self.border.green, self.border.blue),
            "BorderWidth": self.borderWidth,
            "IsVisible": self.visible
        }
        
        self.toBack()

    def __updateData(self) -> None:
        self.data = {
            "Class": f"{self.__class__.__name__}",
            "Debug": self.debug,
            "Dimensions": {
                "TopLeft": (self.left, self.top),
                "TopRight": (self.right, self.top),
                "BottomLeft": (self.left, self.bottom),
                "BottomRight": (self.right, self.bottom),
                "Width": self.width,
                "Height": self.height,
            },
            "BackgroundFill": (self.fill.red, self.fill.green, self.fill.blue),
            "BorderFill": (self.border.red, self.border.green, self.border.blue),
            "BorderWidth": self.borderWidth,
            "IsVisible": self.visible
        }

    def getData(self) -> Dict:
        self.__updateData()
        return self.data
    
    class Button:
        def __init__(self, parent, onclick,
                     horizontalAlign: int|float, verticalAlign: int|float,
                     width: int|float, height: int|float, fill = Colors.darkgray, borderFill = Colors.darkerGray, borderWidth: int|float = 2,
                     textValue: str = "", textFill = "black", textFont: str = "arial", textSize: int|float = 12,
                     textIsBold: bool = False, textIsItalic: bool = False, textIsVisible: bool = True,
                     debug: bool = False):
            self.parent = parent
            self.onclick = onclick
            self.debug = debug

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
            
            self.buttonGroup = Group( self.boundingBox, self.text )

            if self.debug:
                self.debugLineNS = Line(
                    self.boundingBox.centerX, self.boundingBox.top,
                    self.boundingBox.centerX, self.boundingBox.bottom,
                    fill=Colors.CSS3.red,
                    lineWidth=5,
                    opacity=55
                )
                self.debugLineEW = Line(
                    self.boundingBox.left, self.boundingBox.centerY,
                    self.boundingBox.right, self.boundingBox.centerY,
                    fill=Colors.CSS3.blue,
                    lineWidth=5,
                    opacity=55
                )
                self.debugBorder = Rect(
                    self.boundingBox.left, self.boundingBox.top,
                    self.boundingBox.width, self.boundingBox.height,
                    fill=None,
                    border=Colors.CSS3.yellow,
                    borderWidth=5,
                    opacity=55
                )

            self.data = {
                "Class": f"{self.__class__.__name__}",
                "Parent": f"{self.parent}",
                "Debug": self.debug,
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
                    "BackgroundFill": (self.boundingBox.fill),
                    "BorderFill": (self.boundingBox.border),
                    "BorderWidth": self.boundingBox.borderWidth,
                    "IsVisible": self.boundingBox.visible
                },
                "Text": {
                    "Position": (self.text.centerX, self.text.centerY),
                    "Fill": (self.text.fill),
                    "Font": self.text.font,
                    "Size": self.text.size,
                    "IsBold": self.text.bold,
                    "IsItalic": self.text.italic,
                    "IsVisible": self.text.visible
                }
            }
        
        def __updateData(self) -> None:
            self.data = {
                "Class": f"{self.__class__.__name__}",
                "Parent": f"{self.parent}",
                "Debug": self.debug,
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
                    "BackgroundFill": (self.boundingBox.fill),
                    "BorderFill": (self.boundingBox.border),
                    "BorderWidth": self.boundingBox.borderWidth,
                    "IsVisible": self.boundingBox.visible
                },
                "Text": {
                    "Position": (self.text.centerX, self.text.centerY),
                    "Fill": (self.text.red, self.text.green, self.text.blue),
                    "Font": self.text.font,
                    "Size": self.text.size,
                    "IsBold": self.text.bold,
                    "IsItalic": self.text.italic,
                    "IsVisible": self.text.visible
                }
            }
        
        def getData(self) -> Dict:
            return self.data
        
        def addEventListener(self, x, y, event="mouseDown") -> None:
            if self.buttonGroup.contains(x, y):
                if event == "mouseDown":
                    self.onclick()

# tests
if __name__ == "__main__":
    testMenu = Menu(
        0, 0,
        200, 400,
        fill=Colors.CSS3.aliceblue,
        border=Colors.darkerGray,
        borderWidth=5
    )
    print(testMenu.getData())

    def testFoo():
        print("im a boring button")

    testButton = Menu.Button(
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
        textIsBold=True
    )
    print(testButton2.getData())

    exitButton = Menu.Button(
        testMenu,
        Functions.QUIT,
        -20, 365,
        40, 20,
        textValue="QUIT"
    )

    def onMousePress(x, y):
        testButton.addEventListener(x, y)
        testButton2.addEventListener(x, y)
        exitButton.addEventListener(x, y)

    cmu_graphics.run() # type: ignore
