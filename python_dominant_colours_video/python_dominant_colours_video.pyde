add_library('video')

Y_AXIS = 1
X_AXIS = 2
video = None
colours = None
def setup():
    size(1500, 1000)
    
    colorMode(HSB, 255)
    
    
    global video
    
    video = Movie(this, 'port_kembla_1080_reversed_cropped.mov')
    video.play()
    video.noLoop()
    background(0)

    
def draw():
    print(frameCount)
    # image(video, 200, 200)
    # print(frameCount)
    # if video.playing() is False:
    if frameCount < width:
        video.pause();
        print(video.time())
        getColours(video)
        video.play()
    
def getColours(img):
    startingPixel = 0#floor(random(len(img.pixels)))
    colours = None
    colours = []
    colours.append({'red': red(img.pixels[startingPixel]), 'green': green(img.pixels[startingPixel]), 'blue': blue(img.pixels[startingPixel]), 'h': hue(img.pixels[
               startingPixel]), 's': saturation(img.pixels[startingPixel]), 'b': brightness(img.pixels[startingPixel]), 'col': color(img.pixels[startingPixel]), 'ranking': 1, 'firstColour': True})
    strokeWeight(1)
    maxRanking = 0
    # background(colours[0]['col'])
    # image(img, 0, 0)
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
    
            if d < 10000:
                newColour = False
            else:
                if colours[j]['firstColour']:
                    colours.pop(j)
        if newColour:
            colours.append(pixelCols)
            # print "new colour found at index " + str(i)
    
        else:
            k = closestCol['index']
    
            colours[k]['ranking'] += 1
            if colours[k]['ranking'] > maxRanking:
                maxRanking = colours[k]['ranking']
 
    finalColours = []
    currentRanking = maxRanking
    while currentRanking > (0.01 * maxRanking):
        for col in colours:
            if col['ranking'] == currentRanking and not col['firstColour']:
                finalColours.append(col)
        currentRanking -= 1
    
    # background(finalColours[0]['col'])
    
    # image(img, 0, 0)
    
    # for i in range(len(finalColours)):
    #     stroke(150, 255, 255)
    #     fill(finalColours[i]['col'])
    #     rect(20 * i, 35, 20, 20)
    
    counter = 0
    
    
    while len(finalColours) > 4:
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
    
    # for i in range(len(finalColours)):
    #     stroke(0, 255, 255)
    #     fill(finalColours[i]['col'])
    #     rect(20 * i, 60, 20, 20)
    #     print finalColours[i]
    
    # for j in range(len(finalColours)):
    #     i = 0
    #     # d = dist(pow(finalColours[i]['red'],2), pow(finalColours[i]['green'],2), pow(finalColours[i]['blue'],2), pow(finalColours[j]['red'],2), pow(finalColours[j]['green'],2), pow(finalColours[j]['blue'],2))
    #     # d = dist(pow(finalColours[i]['s'],2), pow(finalColours[i]['b'],2),  pow(finalColours[j]['s'],2), pow(finalColours[j]['b'],2))
    #     d = dist(pow(finalColours[i]['h'], 2), pow(finalColours[i]['b'], 2), pow(
    #         finalColours[j]['h'], 2), pow(finalColours[j]['b'], 2))
    #     print 'j:', j, ', dist:', d
    #     if d > biggestDist:
    #         biggestDist = dist
    #         standoutColour = j
    #     # if lowestRank > finalColours[i]['ranking']:
    #     #     standoutColour = i
    #     # d = dist(pow(finalColours[i]['red'],2), pow(finalColours[i]['green'],2), pow(finalColours[i]['blue'],2), pow(finalColours[j]['red'],2), pow(finalColours[j]['green'],2), pow(finalColours[j]['blue'],2))
    
    
    # strokeWeight(10)
    # stroke(finalColours[0]['col'])
    # fill(finalColours[standoutColour]['col'])
    # rect(20, 90, 40, 40)
 
    fc = frameCount * 1.0
    s = 5.0
    mh = 600.0
    x = 10.0 + fc * s
    h = mh/(len(finalColours)*1.0)
    w = s
    noStroke()
    for i in range(len(finalColours)-1):
        # fill(colours[i]['col'])
        c2 = finalColours[i]['col']
        c1 = finalColours[i+1]['col']
        y = 600.0 - (h * i) 
        
        # rect(x, y, w, h)
        setGradient(x, y, w, h, finalColours[i+1], finalColours[i], Y_AXIS)
        # rect(20 * i, 10, 20, 20)
        noStroke()
        fill(c1)
        rect(x, i * 5, 5, 5)
        fill(c2)
        rect(x, i * 5 + 5, 5, 5)
        
        
def setGradient(x, y, w, h, c1, c2, axis):
    noFill()
    if axis == Y_AXIS:  # Top to bottom gradient
        rang = int(y + h + 1)
        
        for i in range(int(y), rang):
            inter = map(i, y, y + h, 0, 1)
            
            # r = lerp(c1['red'], c2['red'], inter)
            # g = lerp(c1['green'], c2['green'], inter)
            # b = lerp(c1['blue'], c2['blue'], inter)
            c = lerpColor(c1, c2, inter)
            
            print(inter, r, g, b)
            
            c = color(r, g, b);
            stroke(c)
            line(x, i, x + w, i)
    elif axis == X_AXIS:  # Left to right gradient
        
        for i in range(int(x), int(x + w + 1)):
            inter = map(i, x, x + w, 0, 1)
            c = lerpColor(c1, c2, inter)
            stroke(c)
            line(i, y, i, y + h)
def movieEvent(m):
    m.read()