from cmu_graphics import *
app.hovering = 0

from dataclasses import dataclass
from typing import Dict
import sys

@dataclass
class Colors:
    gray       = rgb(200,200,200)
    darkgray   = rgb(175,175,175)
    darkerGray = rgb(100,100,100)
    
    # CSS 3 colors
    @dataclass
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

    # colors used when debug=True
    @dataclass(frozen=True)
    class DEBUG:
        NORTHWEST_SOUTHEAST = rgb(255, 0 , 255) # CSS3: magenta
        NORTHEAST_SOUTHWEST = rgb(255, 255, 0)  # CSS3: yellow
        NORTH_SOUTH = rgb(255, 0, 0) # CSS3: red
        EAST_WEST   = rgb(0, 128, 0) # CSS3: green
        BORDER      = rgb(0, 0, 255) # CSS3: blue

class cmugguiError:
    class RangeError(Exception):
        def __init__(self, message):
            super().__init__(message)
            self.message = message
            
        def __repr__(self):
            return f"{self.message}"

class Functions:
    @staticmethod
    def NOFUNCTION() -> None: 
        pass

    @staticmethod
    def QUIT() -> None:
        sys.exit(0)

    @staticmethod
    def QQUIT() -> None:
        # im sorry
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
        if type(object) == Menu:
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
        elif type(object) == Menu.Button:
            match origin:
                case "object_Center":
                    object.rotate(degrees, object.centerX, object.centerY)
                    object.text.rotate(degrees, object.centerX, object.centerY)
                case "object_TopLeft":
                    object.rotate(degrees, object.left, object.top)
                    object.text.rotate(degrees, object.left, object.top)
                case "object_TopRight":
                    object.rotate(degrees, object.right, object.top)
                    object.text.rotate(degrees, object.right, object.top)
                case "object_BottomLeft":
                    object.rotate(degrees, object.left, object.bottom)
                    object.text.rotate(degrees, object.left, object.bottom)
                case "object_BottomRight":
                    object.rotate(degrees, object.right, object.bottom)
                    object.text.rotate(degrees, object.right, object.bottom)
                case "origin_Custom":
                    object.rotate(degrees, originX, originY)
                    object.text.rotate(degrees, originX, originY)

    # im sorry this is so long
    @staticmethod
    def hover(object, mode:str="darken", darkenModAmount:int|float=0.9, lightenModAmount:int|float=1.1, 
              hoverFill:bool=True, hoverBorder:bool=True, hoverText:bool=True) -> None:
        if darkenModAmount >= 1 or darkenModAmount < 0:
            raise cmugguiError.RangeError("darkenModAmount must be in range 0.0 to 1.0")
        
        if lightenModAmount <= 1:
            raise cmugguiError.RangeError("lightenModAmount must be greater than 1")
        
        if object.fill and hoverFill:
            if type(object.fill) == rgb:
                fill_r = object.fill.red
                fill_g = object.fill.green
                fill_b = object.fill.blue
            
                if app.hovering == 1:
                    match mode:
                        case "darken":
                            fill_r *= darkenModAmount
                            fill_g *= darkenModAmount
                            fill_b *= darkenModAmount
                            
                            fill_r = rounded(fill_r)
                            fill_g = rounded(fill_g)
                            fill_b = rounded(fill_b)
                            
                            if fill_r > 255: fill_r = 255
                            if fill_g > 255: fill_g = 255
                            if fill_b > 255: fill_b = 255
                            
                            object.fill = rgb(fill_r, fill_g, fill_b)
                                
                        case "lighten":
                            fill_r *= lightenModAmount
                            fill_g *= lightenModAmount
                            fill_b *= lightenModAmount
                            
                            fill_r = rounded(fill_r)
                            fill_g = rounded(fill_g)
                            fill_b = rounded(fill_b)
                                
                            if fill_r > 255: fill_r = 255
                            if fill_g > 255: fill_g = 255
                            if fill_b > 255: fill_b = 255
                            
                            object.fill   = rgb(fill_r, fill_g, fill_b)
                
            elif type(object.fill) == gradient:
                endFill = []
                
                if app.hovering == 1:
                    match mode:
                        case "darken":
                            for _ in range(len(object.fill.colors)):
                                fill_r = object.fill.colors[_].red
                                fill_g = object.fill.colors[_].green
                                fill_b = object.fill.colors[_].blue
                                
                                fill_r *= darkenModAmount
                                fill_g *= darkenModAmount
                                fill_b *= darkenModAmount
                                
                                fill_r = rounded(fill_r)
                                fill_g = rounded(fill_g)
                                fill_b = rounded(fill_b)
                                
                                endFill.append(rgb(fill_r, fill_g, fill_b))
    
                        case "lighten":
                            for _ in range(len(object.fill.colors)):
                                fill_r = object.fill.colors[_].red
                                fill_g = object.fill.colors[_].green
                                fill_b = object.fill.colors[_].blue
                                
                                fill_r *= lightenModAmount
                                fill_g *= lightenModAmount
                                fill_b *= lightenModAmount
                                
                                fill_r = rounded(fill_r)
                                fill_g = rounded(fill_g)
                                fill_b = rounded(fill_b)
                                
                                if fill_r > 255: fill_r = 255
                                if fill_g > 255: fill_g = 255
                                if fill_b > 255: fill_b = 255
                                
                                endFill.append(rgb(fill_r, fill_g, fill_b))
                
                    object.fill = gradient(*endFill, start=object.fill.start)
                    endFill.clear()
    
        if object.border and hoverBorder:
            if type(object.border) == rgb:
                border_r = object.border.red
                border_g = object.border.green
                border_b = object.border.blue
            
                if app.hovering == 1:
                    match mode:
                        case "darken":
                            border_r *= darkenModAmount
                            border_g *= darkenModAmount
                            border_b *= darkenModAmount
                            
                            border_r = rounded(border_r)
                            border_g = rounded(border_g)
                            border_b = rounded(border_b)    
                            
                            if border_r > 255: border_r = 255
                            if border_g > 255: border_g = 255
                            if border_b > 255: border_b = 255
                            
                            object.border = rgb(border_r, border_g, border_b)
                                
                        case "lighten":
                            border_r *= lightenModAmount
                            border_g *= lightenModAmount
                            border_b *= lightenModAmount
                            
                            border_r = rounded(border_r)
                            border_g = rounded(border_g)
                            border_b = rounded(border_b)    
                            
                            if border_r > 255: border_r = 255
                            if border_g > 255: border_g = 255
                            if border_b > 255: border_b = 255
                
                            object.border = rgb(border_r, border_g, border_b)
            
            elif type(object.border) == gradient:
                endBorder = []
                
                if app.hovering == 1:
                    match mode:
                        case "darken":
                            for _ in range(len(object.border.colors)):
                                border_r = object.border.colors[_].red
                                border_g = object.border.colors[_].green
                                border_b = object.border.colors[_].blue
                                
                                border_r *= darkenModAmount
                                border_g *= darkenModAmount
                                border_b *= darkenModAmount
                                
                                border_r = rounded(border_r)
                                border_g = rounded(border_g)
                                border_b = rounded(border_b)
                                
                                endBorder.append(rgb(border_r, border_g, border_b))
    
                        case "lighten":
                            for _ in range(len(object.border.colors)):
                                border_r = object.border.colors[_].red
                                border_g = object.border.colors[_].green
                                border_b = object.border.colors[_].blue
                                
                                border_r *= lightenModAmount
                                border_g *= lightenModAmount
                                border_b *= lightenModAmount
                                
                                border_r = rounded(border_r)
                                border_g = rounded(border_g)
                                border_b = rounded(border_b)
                                
                                if border_r > 255: border_r = 255
                                if border_g > 255: border_g = 255
                                if border_b > 255: border_b = 255
                                
                                endBorder.append(rgb(border_r, border_g, border_b))
                
                    object.border = gradient(*endBorder, start=object.border.start)
                    endBorder.clear()

        if object.text and hoverText:
            if type(object.text.fill) == rgb:
                text_r = object.text.fill.red
                text_g = object.text.fill.green
                text_b = object.text.fill.blue
                
                if app.hovering == 1:
                        match mode:
                            case "darken":
                                text_r *= darkenModAmount
                                text_g *= darkenModAmount
                                text_b *= darkenModAmount
                                
                                text_r = rounded(text_r)
                                text_g = rounded(text_g)
                                text_b = rounded(text_b)
                                
                                object.text.fill = rgb(text_r, text_g, text_b)
                        
                            case "lighten":
                                text_r *= lightenModAmount
                                text_g *= lightenModAmount
                                text_b *= lightenModAmount
                                
                                text_r = rounded(text_r)
                                text_g = rounded(text_g)
                                text_b = rounded(text_b)
                                
                                if text_r > 255: text_r = 255
                                if text_g > 255: text_g = 255
                                if text_b > 255: text_b = 255
                                
                                object.text.fill = rgb(text_r, text_g, text_b)
                        
            elif type(object.text.fill) == gradient:
                endText = []
                
                if app.hovering == 1:
                    match mode:
                        case "darken":
                            for _ in range(len(object.text.fill.colors)):
                                text_r = object.text.fill.colors[_].red
                                text_g = object.text.fill.colors[_].green
                                text_b = object.text.fill.colors[_].blue
                                
                                text_r *= darkenModAmount
                                text_g *= darkenModAmount
                                text_b *= darkenModAmount
                                
                                text_r = rounded(text_r)
                                text_g = rounded(text_g)
                                text_b = rounded(text_b)
                                
                                endText.append(rgb(text_r, text_g, text_b))
                
                        case "lighten":
                            for _ in range(len(object.text.fill.colors)):
                                text_r = object.text.fill.colors[_].red
                                text_g = object.text.fill.colors[_].green
                                text_b = object.text.fill.colors[_].blue
                                
                                text_r *= lightenModAmount
                                text_g *= lightenModAmount
                                text_b *= lightenModAmount
                                
                                text_r = rounded(text_r)
                                text_g = rounded(text_g)
                                text_b = rounded(text_b)
                                
                                if text_r > 255: text_r = 255
                                if text_g > 255: text_g = 255
                                if text_b > 255: text_b = 255
                                
                                endText.append(rgb(text_r, text_g, text_b))
                
                    object.text.fill = gradient(*endText, start=object.text.fill.start)
                    endText.clear()

class Menu(Rect):
    MENUS   = []
    BUTTONS = []
    TITLES  = []
    
    def __init__(self, *args, fill=Colors.gray, border=Colors.darkerGray, borderWidth: int|float = 2, parent=None, debug: bool = False, **kwargs):
        super().__init__(*args, **kwargs, fill=fill, border=border, borderWidth=borderWidth)
        self.parent = parent
        if self.parent:
            if type(self.parent) != Menu:
                raise TypeError(f"type of self.parent must be Menu, not {type(self.parent)}")
            else:
                self.centerX = (parent.centerX - self.width/2) + self.centerX
                self.top = parent.top + self.centerY

        self.buttons = []
        self.buttonsData = []
        
        self.debug = debug
        if self.debug == True:
            self.widthFormula = 20*(self.width/self.height)
            self.dbNWSE = Line(
                self.left, self.top,
                self.right, self.bottom,
                fill=Colors.DEBUG.NORTHWEST_SOUTHEAST,
                lineWidth=self.widthFormula,
                opacity=55
            )
            self.dbNESW = Line(
                self.right, self.top,
                self.left, self.bottom,
                fill=Colors.DEBUG.NORTHEAST_SOUTHWEST,
                lineWidth=self.widthFormula,
                opacity=55
            )
            self.dbNS = Line(
                self.centerX, self.top,
                self.centerX, self.bottom,
                fill=Colors.DEBUG.NORTH_SOUTH,
                lineWidth=self.widthFormula,
                opacity=55
            )
            self.dbEW = Line(
                self.left, self.centerY,
                self.right, self.centerY,
                fill=Colors.DEBUG.EAST_WEST,
                lineWidth=self.widthFormula,
                opacity=55
            )
            self.dbBorder = Rect(
                self.left, self.top,
                self.width, self.height,
                fill=None,
                border=Colors.DEBUG.BORDER,
                borderWidth=self.widthFormula,
                #opacity=55
            )
            self.opacity = 0

        self.data = {
            "Class": f"{self.__class__.__name__}",
            "Parent": f"{self.parent}",
            "Debug": self.debug,
            "Dimensions": {
                "TopLeft": (self.left, self.top),
                "TopRight": (self.right, self.top),
                "BottomLeft": (self.left, self.bottom),
                "BottomRight": (self.right, self.bottom),
                "Width": self.width,
                "Height": self.height,
                "Center": (self.centerX, self.centerY)
            },
            "BackgroundFill": self.fill,
            "BorderFill": self.border,
            "BorderWidth": self.borderWidth,
            "IsVisible": self.visible,
            "Buttons": self.buttonsData
        }
        
        self.toBack()
    
    def __updateData(self) -> None:
        self.data = {
            "Class": f"{self.__class__.__name__}",
            "Parent": f"{self.parent}",
            "Debug": self.debug,
            "Dimensions": {
                "TopLeft": (self.left, self.top),
                "TopRight": (self.right, self.top),
                "BottomLeft": (self.left, self.bottom),
                "BottomRight": (self.right, self.bottom),
                "Width": self.width,
                "Height": self.height,
                "Center": (self.centerX, self.centerY)
            },
            "BackgroundFill": self.fill,
            "BorderFill": self.border,
            "BorderWidth": self.borderWidth,
            "IsVisible": self.visible,
            "Buttons": self.buttonsData
        }

        Menu.MENUS.append(self.data)
    
    def getData(self) -> Dict:
        return self.data

    def addEventListener(self, x, y) -> None:
        for button in self.buttons:
            if button.contains(x, y) and button.onclick is not None:
                button.onclick()
    
    class Button(Rect):
        def __init__(self, parent, *args, 
                     textValue: str = "", textFill = rgb(0,0,0), textSize: int|float = 12.0, textFont: str = "arial", textOpacity: int|float = 100,
                     textIsBold: bool = False, textIsItalic: bool = False, textIsVisible: bool = True,
                     onclick = None, debug: bool = False, **kwargs):
            super().__init__(*args, **kwargs)
            self.parent  = parent
            if type(self.parent) != Menu:
                raise TypeError(f"type of self.parent must be Menu, not {type(self.parent)}")
            
            self.onclick = onclick
            if callable(self.onclick) == False and self.onclick is not None:
                raise TypeError(f"onclick should be the name of a function, not {self.onclick.__class__.__name__}")
            
            # align with parent Menu
            self.centerX = (self.parent.centerX - self.width/2) + self.centerX
            self.top = self.parent.top + self.centerY
            
            self.textValue = textValue
            self.textFill  = textFill
            self.textSize  = textSize
            self.textFont  = textFont
            self.textIsBold = textIsBold
            self.textIsItalic = textIsItalic
            self.textOpacity = textOpacity
            self.textIsVisible = textIsVisible
            self.text = Label(
                self.textValue,
                self.centerX, self.centerY,
                fill=self.textFill,
                size=self.textSize,
                font=self.textFont,
                bold=self.textIsBold,
                italic=self.textIsItalic,
                opacity=self.textOpacity,
                visible=self.textIsVisible
            )

            self.debug = debug
            if self.debug == True:
                #self.widthFormula = 20*(self.boundingBox.width/self.boundingBox.height)
                self.widthFormula = 5
                self.dbNWSE = Line(
                    self.left, self.top,
                    self.right, self.bottom,
                    fill=Colors.DEBUG.NORTHWEST_SOUTHEAST,
                    lineWidth=self.widthFormula,
                    opacity=55
                )
                self.dbNESW = Line(
                    self.right, self.top,
                    self.left, self.bottom,
                    fill=Colors.DEBUG.NORTHEAST_SOUTHWEST,
                    lineWidth=self.widthFormula,
                    opacity=55
                )
                self.dbNS = Line(
                    self.centerX, self.top,
                    self.centerX, self.bottom,
                    fill=Colors.DEBUG.NORTH_SOUTH,
                    lineWidth=self.widthFormula,
                    opacity=55
                )
                self.dbEW = Line(
                    self.left, self.centerY,
                    self.right, self.centerY,
                    fill=Colors.DEBUG.EAST_WEST,
                    lineWidth=self.widthFormula,
                    opacity=55
                )
                self.dbBorder = Rect(
                    self.left, self.top,
                    self.width, self.height,
                    fill=None,
                    border=Colors.DEBUG.BORDER,
                    borderWidth=self.widthFormula,
                    #opacity=55
                )
                self.opacity = 0

            self.data = {
                "Class": f"{self.__class__.__name__}",
                "Parent": f"{self.parent}",
                "Debug": self.debug,
                "OnClickFunction": f"{self.onclick}",
                "BoundingBox": {
                    "Dimensions": {
                        "TopLeft": (self.left, self.top),
                        "TopRight": (self.right, self.top),
                        "BottomLeft": (self.left, self.bottom),
                        "BottomRight": (self.right, self.bottom),
                        "Width": self.width,
                        "Height": self.height,
                        "Center": (self.centerX, self.centerY)
                    },
                    "BackgroundFill": self.fill,
                    "BorderFill": self.border,
                    "BorderWidth": self.borderWidth,
                    "Opacity": self.opacity,
                    "IsVisible": self.visible
                },
                "Text": {
                    "Dimensions": {
                        "TopLeft": (self.text.left, self.text.top),
                        "TopRight": (self.text.right, self.text.top),
                        "BottomLeft": (self.text.left, self.text.bottom),
                        "BottomRight": (self.text.right, self.text.bottom),
                        "Width": self.text.width,
                        "Height": self.text.height,
                        "Center": (self.text.centerX, self.text.centerY),
                    },
                    "Value": self.text.value,
                    "Fill": self.text.fill,
                    "Font": self.text.font,
                    "Size": self.text.size,
                    "IsBold": self.text.bold,
                    "IsItalic": self.text.italic,
                    "Opacity": self.text.opacity,
                    "IsVisible": self.text.visible
                }
            }

            self.parent.buttons.append(self)
            self.parent.buttonsData.append(self.data)
            Menu.BUTTONS.append(self.data)
        
        def __updateData(self) -> None:
            self.data = {
                "Class": f"{self.__class__.__name__}",
                "Parent": f"{self.parent}",
                "Debug": self.debug,
                "OnClickFunction": f"{self.onclick}",
                "BoundingBox": {
                    "Dimensions": {
                        "TopLeft": (self.left, self.top),
                        "TopRight": (self.right, self.top),
                        "BottomLeft": (self.left, self.bottom),
                        "BottomRight": (self.right, self.bottom),
                        "Width": self.width,
                        "Height": self.height,
                        "Center": (self.centerX, self.centerY)
                    },
                    "BackgroundFill": self.fill,
                    "BorderFill": self.border,
                    "BorderWidth": self.borderWidth,
                    "Opacity": self.opacity,
                    "IsVisible": self.visible
                },
                "Text": {
                    "Dimensions": {
                        "TopLeft": (self.text.left, self.text.top),
                        "TopRight": (self.text.right, self.text.top),
                        "BottomLeft": (self.text.left, self.text.bottom),
                        "BottomRight": (self.text.right, self.text.bottom),
                        "Width": self.text.width,
                        "Height": self.text.height,
                        "Center": (self.text.centerX, self.text.centerY),
                    },
                    "Value": self.text.value,
                    "Fill": self.text.fill,
                    "Font": self.text.font,
                    "Size": self.text.size,
                    "IsBold": self.text.bold,
                    "IsItalic": self.text.italic,
                    "Opacity": self.text.opacity,
                    "IsVisible": self.text.visible
                }
            }
        
        def getData(self) -> Dict:
            return self.data
        
        def addEventListener(self, x, y, onclick = None, event: str = "mouseDown") -> None:
            if callable(onclick) == False:
                raise TypeError(f"onclick must be of type function, not {onclick.__class__.__name__}")
            
            if self.contains(x, y):
                if event == "mouseDown":
                    onclick()

    class Title(Label):
        def __init__(self, parent, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.parent = parent
            
            self.centerX = self.parent.centerX + self.centerX
            self.top = self.parent.top + self.centerY

            self.data = {
                "Class": f"{self.__class__.__name__}",
                "Parent": f"{self.parent}",
                "Dimensions": {
                    "TopLeft": (self.left, self.top),
                    "TopRight": (self.right, self.top),
                    "BottomLeft": (self.left, self.bottom),
                    "BottomRight": (self.right, self.bottom),
                    "Width": self.width,
                    "Height": self.height,
                    "Center": (self.centerX, self.centerY)
                },
                "Color": self.fill,
                "Value": self.value,
                "Fill": self.fill,
                "Font": self.font,
                "Size": self.size,
                "IsBold": self.bold,
                "IsItalic": self.italic,
                "Opacity": self.opacity,
                "IsVisible": self.visible
            }

            Menu.TITLES.append(self.data)
    
        def __updateData(self):
            self.data = {
                "Class": f"{self.__class__.__name__}",
                "Parent": f"{self.parent}",
                "Dimensions": {
                    "TopLeft": (self.left, self.top),
                    "TopRight": (self.right, self.top),
                    "BottomLeft": (self.left, self.bottom),
                    "BottomRight": (self.right, self.bottom),
                    "Width": self.width,
                    "Height": self.height,
                    "Center": (self.centerX, self.centerY)
                },
                "Color": self.fill,
                "Value": self.value,
                "Fill": self.fill,
                "Font": self.font,
                "Size": self.size,
                "IsBold": self.bold,
                "IsItalic": self.italic,
                "Opacity": self.opacity,
                "IsVisible": self.visible
            }

        def getData(self):
            return self.data

class Topbar(Menu):
    def __init__(self, *args, borderBottomWidth=3, fill=None, **kwargs):
        super().__init__(*args, fill=fill, **kwargs)
        
        self.borderBottomWidth = borderBottomWidth
        self.borderBottom = Line(
            self.left, self.bottom,
            self.right, self.bottom,
            lineWidth=self.borderBottomWidth
        )

class VerticalTitle(Menu.Title):
    def __init__(self, *args, spacing=0, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.spacing = self.size + spacing
        
        self.__valueList = list(self.value)
        self.chars = Group()
        
        for _ in range(len(self.__valueList)):
            self.chars.add(
                Menu.Title(
                    self.parent,
                    self.__valueList[_],
                    0, self.centerY+self.spacing*_,
                    fill=self.fill,
                    size=self.size,
                    font=self.font,
                    bold=self.bold,
                    italic=self.italic,
                    opacity=self.opacity,
                    visible=self.visible
                )   
            )
        
        self.chars.centerX = self.centerX
        
        self.visible = False
        
        self.data = {
            "Class": f"{self.__class__.__name__}",
            "Parent": f"{self.parent}",
            "Position": (self.chars.centerX, self.chars.centerY),
            "Value": self.value,
            "Color": f"{self.fill}",
            "Font": self.font,
            "Size": self.size,
            "IsBold": self.bold,
            "IsItalic": self.italic,
            "Opacity": self.opacity,
            "IsVisible": self.visible
        }
    
    def getData(self) -> Dict:
        return self.data

# tests
if __name__ == "__main__":
    testMenu = Menu(
        0, 0,
        200, 400,
        fill=Colors.CSS3.aliceblue,
        border=Colors.darkerGray,
        borderWidth=5
    )
    menuData = testMenu.getData()

    def testFoo():
        print("im a boring button")

    testButton = Menu.Button(
        testMenu,
        0, 12,
        50, 30,
        fill=rgb(175,175,175),
        border=rgb(120,120,120),
        borderWidth=1,
        textValue="Test"
    )
    tbData = testButton.getData()
    print(tbData)

    def testFoo2():
        print("im a cooler button")

    testButton2 = Menu.Button(
        testMenu,
        0, 50,
        70, 40,
        fill=gradient("yellow", "white", start="right"),
        border=gradient("blue", "green", "red", start="left"),
        borderWidth=4,
        textValue="t e s t",
        textFill=gradient("red", "white", start="right"),
        textSize=20,
        textIsBold=True
    )
    tb2Data = testButton2.getData()
    print(tb2Data)

    exitButton = Menu.Button(
        testMenu,
        0, 365,
        40, 20,
        fill=Colors.CSS3.slategray,
        textValue="QUIT"
    )

    testTitle = Menu.Title(
        testMenu,
        "test",
        0, 100
    )

    def onMousePress(x, y):
        testButton.addEventListener(x, y, onclick=testFoo)
        testButton2.addEventListener(x, y, onclick=testFoo2)
        exitButton.addEventListener(x, y, onclick=Functions.QQUIT)

    def onMouseMove(x, y):
        if testButton2.contains(x, y):
            app.hovering += 1
            Functions.hover(testButton2)
        else:
            testButton2.fill      = tb2Data["BoundingBox"]["BackgroundFill"]
            testButton2.border    = tb2Data["BoundingBox"]["BorderFill"]
            testButton2.text.fill = tb2Data["Text"]["Fill"]

            app.hovering = 0

    cmu_graphics.run() # type: ignore
