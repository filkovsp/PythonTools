import os
import io
import sys
import qrcode
import qrcode.image.svg as svg
import numpy as np
import math

fileName = "PyGame.py"
f = io.open(fileName, mode="r", encoding="utf-8")
fileText = f.readlines()
line_count = len(fileText)

# number of code lines per 1 SVG file.
line_max = 50

# number of code chunks (SVG files)
chunks = np.array_split(fileText, math.ceil(line_count/line_max))

i=0
for chunk in chunks:
    if len(chunks) > 1:
        img = qrcode.make("".join(chunk), image_factory=svg.SvgImage)
        img.save("{0}.{1}.svg".format(fileName,i))
        i+=1
    else:
        img = qrcode.make("".join(chunk), image_factory=svg.SvgImage)
        img.save("{0}.svg".format(fileName))

print("All done")
