import PoissonPoints.*;
PoissonPoints pp;
PGraphics bg;
// gradient background
void setup() {
  size(1280, 1280);

  bg = createGraphics(width, height);  
  bg.beginDraw();
  bg.loadPixels();

  for (int i = 0; i < bg.pixels.length; i++) {
    int y = i / width;
    int x = i - (y * width);
    float r = map(dist(x, y, width, 0), 0, width, 0, 255);
    float g = 180;
    float b = map(dist(x, y, 0, height), 0, height, 0, 200);
    bg.set(x, y, color(r, g, b));
  }
  bg.endDraw();


  pp = new PoissonPoints(this, 700, 55, 40);
}
void draw() {
  background(bg);
  fill(0);
  text(frameRate, 10, 10);

  stroke(255);
  //int[] closestMatch = new int[pp.ppLocations.length]; 
  for (int i = 0; i < pp.ppLocations.length; i++) {
    //strokeWeight(5);
    //point(pp.getPPLocation(i).x, pp.getPPLocation(i).y);
    //float disDist = 9000;
    //int nearest = i;

    for (int j = 0; j < pp.ppLocations.length; j++) {
      //float dis = min(disDist, dist(pp.getPPLocation(i).x, pp.getPPLocation(i).y, pp.getPPLocation(j).x, pp.getPPLocation(j).y));
      float dis = dist(pp.getPPLocation(i).x, pp.getPPLocation(i).y, pp.getPPLocation(j).x, pp.getPPLocation(j).y);

      if (j != i && dis < 65) {
        //disDist = dis;
        //nearest = j;
        strokeWeight(map(sin(radians(frameCount + j)), -1, 1, 0, 10));
        point(pp.getPPLocation(i).x, pp.getPPLocation(i).y);

        strokeWeight(map(sin(radians(frameCount + i)), -1, 1, 0, 3));

        line(pp.getPPLocation(i).x, pp.getPPLocation(i).y, pp.getPPLocation(j).x, pp.getPPLocation(j).y);
      } else 
      { 
        if (j != i && dis < 80) {
          //disDist = dis;
          //nearest = j;
          strokeWeight(map(sin(radians(frameCount + j)), -1, 1, 0, 8));          
          point(pp.getPPLocation(i).x, pp.getPPLocation(i).y);

          strokeWeight(map(sin(radians(frameCount + i)), -1, 1, 0, 1));
          line(pp.getPPLocation(i).x, pp.getPPLocation(i).y, pp.getPPLocation(j).x, pp.getPPLocation(j).y);
        } else 
        { 
          if (j != i && dis < 110) {
            //disDist = dis;
            //nearest = j;
            strokeWeight(map(sin(radians(frameCount + j)), -1, 1, 0, 5));
            point(pp.getPPLocation(i).x, pp.getPPLocation(i).y);

            strokeWeight(map(sin(radians(frameCount + i)), -1, 1, 0, .2));

            line(pp.getPPLocation(i).x, pp.getPPLocation(i).y, pp.getPPLocation(j).x, pp.getPPLocation(j).y);
          }
        }
      }
    }
  }
}