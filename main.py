import json,random
from PIL import Image, ImageDraw
from PIL import ImageFont


class MapPy:
    def __init__(self, file):
        self.file = file
        self.imageFile = file + ".png"
        self.metafile = file + ".json"
        json_data = open(self.metafile).read()
        self.data = json.loads(json_data)
        self.im = Image.open(self.imageFile)
        self.rgb = self.im.convert('RGB')
        self.imgData = self.im.load()
        self.width, self.height = self.im.size

        self.startRed = 255
        self.startGreen = 0
        self.startBlue = 0

        self.endRed = 0
        self.endGreen = 0
        self.endBlue = 0

        self.max = 20

        self.scaleMin = 4
        self.scaleMax = 9

        self.fnt = ImageFont.truetype('font.ttf', 18)

    def run(self):
        self.values = {}
        for x in self.data:
            name = x['name']
            value = input("Value for " + name + ": ")
          #  value = random.uniform(self.scaleMin,self.scaleMax)
            self.values[name] = value
        self.steps = {}
        for area in self.data:
            value = self.values[area['name']]
            i = (((float(value) - self.scaleMin)) / (self.scaleMax - self.scaleMin)) * self.max
            self.steps[area['name']] = i
        self.title = "Youth Crime By Region of England"
        self.subTitle = "Data From Year\nEnding March 2016"
        self.scaleSubText = "Youths Cautioned Or Sentenced\nPer 10,000 People"
        self.process()
        self.drawScale()
        self.drawTitle()
        self.im.show()

    def process(self):

        for x in range(0, self.width):
            for y in range(0, self.height):
                r, g, b = self.rgb.getpixel((x, y))
                hexValue = self.rgbToHex(r, g, b)
                for area in self.data:
                    if area['color'] == hexValue:
                        r = int(self.interpolate(self.startRed, self.endRed, self.steps[area['name']], self.max))
                        g = int(self.interpolate(self.startGreen, self.endGreen, self.steps[area['name']], self.max))
                        b = int(self.interpolate(self.startBlue, self.endBlue, self.steps[area['name']], self.max))
                        self.imgData[x, y] = (r, g, b)
                        break

    def drawScale(self):
        scaleWidth = int(self.width * 0.4)
        scaleHeight = int(scaleWidth * 0.3)
        scaleArea = Image.new("RGB", (scaleWidth, scaleHeight), (140, 140, 140))
        img = Image.new("RGB", (self.max, 1))
        iData = img.load()
        for i in range(0, self.max):
            r = int(self.interpolate(self.startRed, self.endRed, i, self.max))
            g = int(self.interpolate(self.startGreen, self.endGreen, i, self.max))
            b = int(self.interpolate(self.startBlue, self.endBlue, i, self.max))
            iData[i, 0] = (r, g, b)
        img = img.resize((int(scaleWidth - ((scaleWidth * 0.1) * 2)), int((scaleHeight / 10))), Image.ANTIALIAS)
        iW, iH = img.size
        scaleX = int(scaleWidth / 2 - iW / 2)
        scaleY = int(scaleHeight * 0.15)
        scaleArea.paste(img, (scaleX, scaleY))
        d = ImageDraw.Draw(scaleArea)

        d.text((scaleX -(scaleX/4),scaleY + iH), str(self.scaleMin), font=self.fnt, fill=(255, 0, 0, 255))
        d.text((scaleX + iW, scaleY + 5), str(self.scaleMax), font=self.fnt, fill=(255, 0, 0, 255))

        textWS, textHS = d.textsize(self.scaleSubText, font=self.fnt)
        d.multiline_text((scaleWidth/2 - textWS/2,iH * 3 + scaleY), self.scaleSubText, font=self.fnt, fill=(0, 0, 0, 255),
                         align="center")
        self.im.paste(scaleArea, (self.width - scaleWidth, self.height - scaleHeight))

    def drawTitle(self):
        titleWidth = int(self.width * 0.4)
        titleHeight = int(titleWidth * 0.3)
        titleArea = Image.new("RGB", (titleWidth, titleHeight), (140, 140, 140))
        d = ImageDraw.Draw(titleArea)
        textW, textH = d.textsize(self.title, font=self.fnt)
        d.text((titleWidth/2 - textW/2,5),self.title,font=self.fnt,fill=(0,0,0,255))
        d.line([titleWidth/2 - textW/2,5 + textH,(titleWidth/2 - textW/2) + textW,5 + textH], fill = (0,0,0,255),width = 4)
        textWS, textHS = d.textsize(self.subTitle, font=self.fnt)
        d.multiline_text((titleWidth / 2 - textWS / 2, textH + 10), self.subTitle, font=self.fnt, fill=(0, 0, 0, 255),align="center")
        self.im.paste(titleArea, (self.width - titleWidth,0))

    def interpolate(self, startValue, endValue, stepNumber, lastStepNumber):
        return (endValue - startValue) * stepNumber / lastStepNumber + startValue

    def rgbToHex(self, r, g, b):
        return '%02X%02X%02X' % (r, g, b)


MapPy("map").run()
