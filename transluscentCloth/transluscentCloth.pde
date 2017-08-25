float shapeSeed;
float xSeed, ySeed;

void setup(){
  size(800,600);
  colorMode(HSB, 360, 255, 255, 255);
  background(360);
  stroke(random(360), 100, 200, 50);
  strokeWeight(2);
  noFill();
  shapeSeed = random(80);
  xSeed = random(100, 200);
  ySeed = random(100, 200);
}

void draw(){
    //for (int j = 0; j < width; j++) {
      pushMatrix();
      translate(frameCount - 150, height/4);
      beginShape();
      for (int i = 0 ; i < 360; i++) {
        noiseSeed(4);
        float inc = noise(i/shapeSeed);
        noiseSeed(3);
        float xpos = (250 * noise(frameCount/xSeed)) * sin(radians(i)) * inc;
        noiseSeed(2);
        float ypos = ((height/2) * noise(frameCount/ySeed)) + 250 * cos(radians(i)) * inc;
        //println(xpos, ypos);
        vertex(xpos, ypos);
      }
      endShape(CLOSE);
      popMatrix();
  //}
  ////
}