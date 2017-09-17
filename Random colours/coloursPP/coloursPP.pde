size(2000, 2000);
import PoissonPoints.*;
int maxNumPoints = width * 3;
int sparseness = width/75;
int numTests = width/100;

PGraphics background = createGraphics (width, height);

PGraphics foreground = createGraphics(width, height); 


PoissonPoints pp;


pp = new PoissonPoints(this, maxNumPoints, sparseness, numTests);
colorMode(HSB, 360, 100, 100, 100);

background.beginDraw();
foreground.beginDraw();

background.colorMode(HSB, 360, 100, 100, 100);
foreground.colorMode(HSB, 360, 100, 100, 100);
//background(360);
//stroke(255);
//strokeWeight(20);
//

boolean[] hasBeenDrawnOntoTheImage = new boolean[pp.numLocations()]; 

PVector[] locations = new PVector[pp.numLocations()];

// distance
float d = dist(width/2, height/2, 0, 0);
//println(d);


PVector temp = new PVector(0, 0);
foreground.rectMode(CENTER);



PVector start = new PVector(0, 0);
PVector finish = new PVector(0, 0);
background.strokeWeight(1);
background.stroke(150);
background.background(0, 0, 100);

for (int i = 1; i < pp.ppLocations.length; i++) {
  int parentID = pp.getParentPoint(i);
  start.set(pp.getPPLocation(parentID));

  finish.set(pp.getPPLocation(i));
  background.line(start.x, start.y, finish.x, finish.y);
}
background.filter(BLUR, 6);
background.strokeWeight(4);
background.stroke(200);


float h = 0;
float s = 0; 
float b = 0;
for (int i = 0; i < pp.ppLocations.length; i++) {
  //  locations[i] = pp.getPPLocation(i);
  //  point(pp.getLocation(i).x, pp.getlocation(i).y);
  temp.set(pp.getPPLocation(i));
  // random number
  float r  = randomGaussian();
  // percent of location as per d
  float p = dist(width/2, height/2, temp.x, temp.y)/d;

  if (p < r/1.5) {
    //    println("win");

    hasBeenDrawnOntoTheImage[i] = true;

    int parentID = pp.getParentPoint(i);
    //println(parentID);
    PVector parentLocation = pp.getPPLocation(parentID); 

    //println(hasBeenDrawnOntoTheImage[parentID]);
    foreground.strokeCap(PROJECT);

    if (hasBeenDrawnOntoTheImage[parentID]) {
      background.line(temp.x, temp.y, parentLocation.x, parentLocation.y);
      foreground.strokeCap(ROUND);
    }

    foreground.beginDraw();
    foreground.strokeWeight(width/100);
    h = (pow(i, pow(r, p))%50 + 220) % 360;
    s = 40 + 2*r;
    b = r * 50 + 50;
    foreground.stroke(h, s, b);
    foreground.point(temp.x, temp.y);
  } else {
    foreground.strokeCap(ROUND);
    foreground.stroke(360);
    foreground.strokeWeight(width/300);
    foreground.point(temp.x, temp.y);
    foreground.stroke(200 + p*160);
    foreground.strokeWeight(width/500);
    foreground.strokeCap(PROJECT);
    foreground.point(temp.x, temp.y);
    hasBeenDrawnOntoTheImage[i] = false;
  }
}
background.endDraw();
foreground.endDraw();


image(background, 0, 0);

image(foreground, 0, 0);