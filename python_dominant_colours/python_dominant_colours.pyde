size(1500, 1000)

colorMode(HSB, 255)

# img = loadImage('hoth.png')
img = loadImage('city.jpg')
# img = loadImage('DJI_0028.JPG')
# img = loadImage('crayweed.jpeg')
colours = []
# img.loadPixels()
print 'pixels length:', len(img.pixels)
startingPixel = floor(random(len(img.pixels)))

colours.append({'red': red(img.pixels[startingPixel]), 'green': green(img.pixels[startingPixel]), 'blue': blue(img.pixels[startingPixel]), 'h': hue(img.pixels[
               startingPixel]), 's': saturation(img.pixels[startingPixel]), 'b': brightness(img.pixels[startingPixel]), 'col': color(img.pixels[startingPixel]), 'ranking': 1, 'firstColour': True})

maxRanking = 0
background(colours[0]['col'])
image(img, 0, 0)
for i in range(len(img.pixels)):
    # pixel = img.pixels[i]

    pixelCols = {'red': red(img.pixels[i]), 'green': green(img.pixels[i]), 'blue': blue(img.pixels[i]), 'h': hue(img.pixels[
        i]), 's': saturation(img.pixels[i]), 'b': brightness(img.pixels[i]), 'col': color(img.pixels[i]), 'ranking': 1, 'firstColour': False}

    newColour = True

    closestCol = {'index': 1337, 'distance': 900001}

    for j in range(len(colours)):
        d = dist(pow(pixelCols['red'], 2), pow(pixelCols['green'], 2), pow(pixelCols['blue'], 2), pow(
            colours[j]['red'], 2), pow(colours[j]['green'], 2), pow(colours[j]['blue'], 2))

        if d < closestCol['distance']:
            closestCol['index'] = j
            closestCol['distance'] = d

        if d < 15000:
            newColour = False
        else:
            if colours[j]['firstColour']:
                colours.pop(j)
    if newColour:
        colours.append(pixelCols)
        print "new colour found at index " + str(i)

    else:
        k = closestCol['index']

        colours[k]['ranking'] += 1
        if colours[k]['ranking'] > maxRanking:
            maxRanking = colours[k]['ranking']

        # c1 = colours[k]['col']
        # c2 = pixelCols['col']

        # c3 = lerpColor(c1, c2, .50)

        # colours[k]['h'] = hue(c3)
        # colours[k]['s'] = saturation(c3)
        # colours[k]['b'] = brightness(c3)
        # colours[k]['col'] = color(c3)

print 'there are ', len(colours), ' colours, and the max ranking is', maxRanking


finalColours = []
currentRanking = maxRanking
while currentRanking > (0.01 * maxRanking):
    for col in colours:
        if col['ranking'] == currentRanking and not col['firstColour']:
            finalColours.append(col)
    currentRanking -= 1

background(finalColours[0]['col'])

image(img, 0, 0)

for i in range(len(colours)):
    fill(colours[i]['col'])
    rect(20 * i, 10, 20, 20)


# numColoursWanted = 5
# counter = 0
# while len(finalColours) > numColoursWanted:
#     counter += 1
#     print 'loop:', i
#     for i in range(len(finalColours)):
#         newColour = True
#         if i < len(finalColours):
#             for j in range(len(finalColours)):
#                 if i == j:
#                     print 'identical', i
#                 else:
#                     c1 = finalColours[i]['col']
#                     c2 = finalColours[j]['col']
#                     c3 = lerpColor(c1, c2, .5)
#                     fill(c1)
#                     rect(15 + i * 20, 10 + counter * 120 + j * 8, 5, 5)
#                     fill(c2)
#                     rect(25 + i * 20, 10 + counter * 120 + j * 8, 5, 5)
#                     d = dist(hue(c1), saturation(c1), brightness(
#                         c1), hue(c3), saturation(c3), brightness(c3))
#                     print 'dist between: ', i, 'and', j, '=', d
#                     if d < 5 * counter:
#                         newColour = False
#                         print i, 'falsified', j
#                         fill(0, 255, 255)
#                         rect(35 + i * 20, 10 + counter * 120 + j * 8, 5, 5)

# finalColours[j]['h'] = hue(c3)
# finalColours[j]['s'] = saturation(c3)
# finalColours[j]['b'] = brightness(c3)
# finalColours[j]['col'] = color(c3)

#             if not newColour:
#                 print newColour
#                 finalColours
#                 finalColours.pop(j)
#                 print 'pop!', i, 'remaining:', len(finalColours)
#                 if len(finalColours) <= numColoursWanted:
#                     print 'done'


for i in range(len(finalColours)):
    stroke(150, 255, 255)
    fill(finalColours[i]['col'])
    rect(20 * i, 35, 20, 20)

counter = 0


while len(finalColours) > 3:
    counter += 1
    f = len(finalColours) - 1
    # print
    markedColours = []
    for i in range(f):
        j = i + 1
        # d = dist(finalColours[i]['h'], finalColours[i]['s'], finalColours[j]['h'], finalColours[j]['s'])
        # d = dist(finalColours[i]['h'], finalColours[i]['s'], finalColours[i]['b'], finalColours[j]['h'], finalColours[j]['s'], finalColours[j]['b'])
        d = dist(pow(finalColours[i]['red'], 2), pow(finalColours[i]['green'], 2), pow(finalColours[i]['blue'], 2), pow(
            finalColours[j]['red'], 2), pow(finalColours[j]['green'], 2), pow(finalColours[j]['blue'], 2))

        if d < 10 * counter:
        # c3 = lerpColor(finalColours[i]['col'], finalColours[j]['col'], .5)
        # finalColours[i]['col'] = color(c3)
        # finalColours[i]['h'] = hue(c3)
        # finalColours[i]['s'] = saturation(c3)
        # finalColours[i]['b'] = brightness(c3)
        # finalColours.pop(j)
            markedColours.append(j)
    for i in range(len(markedColours)):

        j = markedColours[len(markedColours) - (i + 1)]
        finalColours.pop(j)
        print 'popped colour at', j, ',', f, 'colours remain, counter:', counter

lowestRank = 900000
standoutColour = 0

biggestDist = 0

for i in range(len(finalColours)):
    stroke(0, 255, 255)
    fill(finalColours[i]['col'])
    rect(20 * i, 60, 20, 20)
    print finalColours[i]

for j in range(len(finalColours)):
    i = 0
    # d = dist(pow(finalColours[i]['red'],2), pow(finalColours[i]['green'],2), pow(finalColours[i]['blue'],2), pow(finalColours[j]['red'],2), pow(finalColours[j]['green'],2), pow(finalColours[j]['blue'],2))
    # d = dist(pow(finalColours[i]['s'],2), pow(finalColours[i]['b'],2),  pow(finalColours[j]['s'],2), pow(finalColours[j]['b'],2))
    d = dist(pow(finalColours[i]['h'], 2), pow(finalColours[i]['b'], 2), pow(
        finalColours[j]['h'], 2), pow(finalColours[j]['b'], 2))
    print 'j:', j, ', dist:', d
    if d > biggestDist:
        biggestDist = dist
        standoutColour = j
    # if lowestRank > finalColours[i]['ranking']:
    #     standoutColour = i
    # d = dist(pow(finalColours[i]['red'],2), pow(finalColours[i]['green'],2), pow(finalColours[i]['blue'],2), pow(finalColours[j]['red'],2), pow(finalColours[j]['green'],2), pow(finalColours[j]['blue'],2))


strokeWeight(10)
stroke(finalColours[0]['col'])
fill(finalColours[standoutColour]['col'])
rect(20, 90, 40, 40)

print 'completion time:', millis()