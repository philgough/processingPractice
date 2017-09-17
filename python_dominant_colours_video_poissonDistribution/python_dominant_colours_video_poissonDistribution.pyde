add_library('video')

add_library('PoissonPoints')

Y_AXIS = 1
X_AXIS = 2
video = None
colours = None
num_final_colours = 8

def setup():
    size(1920, 1080)
    global ppd
    ppd = PoissonPoints(this, 10000, 45, 25)
    # global ppd['ppLocations'] = []
    # ppd['ppLocations'] = pp.ppLocations
    # ppd['getPPLocation'] = pp.getPPLocation

    # print type(int(ppd['getPPLocation'](0).x))

    # len(ppd['ppLocations']))
    colorMode(HSB, 255)

    global video
 

    video = Movie(this, 'beach_1080_speed_blur_speed.mov')
    video.play()
    video.jump(0)
    video.pause()
    video.noLoop()
    # background(0)

    
    # video_frames = int(video.duration() * video.frameRate)
    global video_frames 
    video_frames = 10 + 12*25
    global pg, graphic_w, graphic_h
    graphic_w = 10000
    graphic_h = 6000
    pg = createGraphics(graphic_w, graphic_h)
    pg.colorMode(HSB, 255)
    pg.beginDraw()
    pg.background(0)
    pg.endDraw()
    
def draw():
   
    video.jump(frameCount/25.0)    

    video.play()
    image(video, 0, 200)
    
    video.pause()
    print('video.time():', video.time())
    getColours(video)
    # stroke(255)
    # strokeWeight(3)
    # for p in ppd.ppLocations:
    #     point(p.x, p.y)
    if frameCount + 10 > (video.duration()+1)*25:
        video.stop()
        pg.save("output.png")
        exit()
    

    
def getColours(img):
    # startingPixel = 0#floor(random(len(img.pixels)))
    colours = None
    colours = []
    # colours.append(
    # i = len(ppd['ppLocations']) - 1
    loc = ppd.getPPLocation(0)
    x = loc.x
    y = loc.y

    # print(img.get(int(x), int(y)))

    colours.append({'red': red(img.get(int(x), int(y))),
                    'green': green(img.get(int(x), int(y))),
                    'blue': blue(img.get(int(x), int(y))),
                    'h': hue(img.get(int(x), int(y))),
                    's': saturation(img.get(int(x), int(y))),
                    'b': brightness(img.get(int(x), int(y))),
                    'col': color(img.get(int(x), int(y))),
                    'ranking': 1,
                    'firstColour': True})
    # strokeWeight(1)
    # print(len(colours))
    maxRanking = 0
    # background(colours[0]['col'])
    # image(img, 0, 0)
    # for i in range(len(img.pixels)):
    # pixel = img.pixels[i]
    theRange = len(ppd.ppLocations) - 1
    # print("theRange:", theRange)
    for i in range(1, theRange):
        loc = ppd.getPPLocation(i)
        x = loc.x
        y = loc.y
        pixelCols = {'red': red(img.get(int(x), int(y))),
                    'green': green(img.get(int(x), int(y))),
                    'blue': blue(img.get(int(x), int(y))),
                    'h': hue(img.get(int(x), int(y))),
                    's': saturation(img.get(int(x), int(y))),
                    'b': brightness(img.get(int(x), int(y))),
                    'col': color(img.get(int(x), int(y))),
                    'ranking': 1,
                    'firstColour': False}
        # print pixelCols
        newColour = True
        
        closestCol = {'index': 1337, 'distance': 900001}

        for j in range(len(colours)):
            d = dist(pow(pixelCols['red'], 2), pow(pixelCols['green'], 2), pow(pixelCols['blue'], 2), pow(
                colours[j]['red'], 2), pow(colours[j]['green'], 2), pow(colours[j]['blue'], 2))

            if d < closestCol['distance']:
                closestCol['index'] = j
                closestCol['distance'] = d

            if d < 6000:
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
    # print(colours)
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

    while len(finalColours) > num_final_colours:
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
        # print finalColours[i]

    # for j in range(len(finalColours)):
    #     i = 0
    # d = dist(pow(finalColours[i]['red'],2), pow(finalColours[i]['green'],2), pow(finalColours[i]['blue'],2), pow(finalColours[j]['red'],2), pow(finalColours[j]['green'],2), pow(finalColours[j]['blue'],2))
    # d = dist(pow(finalColours[i]['s'],2), pow(finalColours[i]['b'],2),  pow(finalColours[j]['s'],2), pow(finalColours[j]['b'],2))
    #     d = dist(pow(finalColours[i]['h'], 2), pow(finalColours[i]['b'], 2), pow(
    #         finalColours[j]['h'], 2), pow(finalColours[j]['b'], 2))
    #     print 'j:', j, ', dist:', d
    #     if d > biggestDist:
    #         biggestDist = dist
    #         standoutColour = j
    # if lowestRank > finalColours[i]['ranking']:
    # standoutColour = i
    # d = dist(pow(finalColours[i]['red'],2), pow(finalColours[i]['green'],2), pow(finalColours[i]['blue'],2), pow(finalColours[j]['red'],2), pow(finalColours[j]['green'],2), pow(finalColours[j]['blue'],2))

    # strokeWeight(10)
    # stroke(finalColours[0]['col'])
    # fill(finalColours[standoutColour]['col'])
    # rect(20, 90, 40, 40)
    # print(finalColours)
    fc = frameCount * 1.0
    s = 15.0
    mh = graphic_h * 1.00000001
    x = 10.0 + fc * s
    h = mh / 8.0
    w = s
    pg.beginDraw()
    pg.noStroke()
    # for i in range(len(finalColours) - 1):
    for i in range(len(finalColours)):
        # print(i)
        # fill(colours[i]['col'])
        c2 = finalColours[i]['col']
        # c1 = finalColours[i + 1]['col']
        # y = mh - (h * i)
        y = map(i, 0, num_final_colours, 0, graphic_h)
        # rect(x, y, w, h)
        # pg.beginDraw()
        # setGradient(x, y, w, h, finalColours[i + 1], finalColours[i], Y_AXIS)
        
        # pg.endDraw()
        # rect(20 * i, 10, 20, 20)
        pg.fill(c2)
        pg.rect(x, y , w, h)
        
        noStroke()
        fill(c2)
        rect(10.0 + fc * 5, i * 5, 5, 5)
        # fill(c2)
        # rect(x, i * 5 + 5, 5, 5)

    pg.endDraw()
    
    
    
    
def setGradient(x, y, w, h, c1, c2, axis):
    pg.noFill()
    if axis == Y_AXIS:  # Top to bottom gradient
        rang = int(y + h + 1)

        for i in range(int(y), rang):
            inter = map(i, y, y + h, 0, 1)

            # r = lerp(c1['red'], c2['red'], inter)
            # g = lerp(c1['green'], c2['green'], inter)
            # b = lerp(c1['blue'], c2['blue'], inter)
            # print c1['col']
            # print c2['col']
            c = lerpColor(c1['col'], c2['col'], inter)

            # print(inter, r, g, b)

            # c = color(r, g, b)
            pg.stroke(c)

            pg.line(x, i, x + w, i)

    elif axis == X_AXIS:  # Left to right gradient

        for i in range(int(x), int(x + w + 1)):
            inter = map(i, x, x + w, 0, 1)
            c = lerpColor(c1, c2, inter)
            stroke(c)
            line(i, y, i, y + h)
def movieEvent(m):
    m.read()
    
    
    

# def setFrame(n): 
#   video.play();
    
#   # The duration of a single frame:
#   frameDuration = 1.0 / video.frameRate()
    
#   # We move to the middle of the frame by adding 0.5:
#   where = (n + 0.5) * frameDuration; 
    
#   # Taking into account border effects:
#   diff = video.duration() - where;
#   if diff < 0:
#     where += diff - 0.25 * frameDuration;
  
    
#   video.jump(where);
#   video.pause();  

def keyReleased():
    # global value
    if key == ' ':
       video.stop()
       pg.save("output.png")
       exit()
    