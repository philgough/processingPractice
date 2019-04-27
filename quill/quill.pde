PVector[] targetVecs;
PVector orig;
float targetRad = 100;

void setup() {
  size(400, 400);
  noFill();
  stroke(255);
  //stroke(255, 0, 0);

  //background(0);
  targetVecs = new PVector[180]; 
  //println("create origin");
  orig = new PVector(width/2, height/2); 

}

void draw() {
  background(0);
  stroke(255);
  
  text(frameRate, 10, 10);
  //noFill();
  
  //target.endShape();
  //shape(target, 0, 0);
  //println("draw origin");
  //int m = millis();

  for (int i = 0; i < targetVecs.length; i+= 1) {
    float rads = radians(i * 2 + frameCount);



    float x = orig.x + targetRad * cos(rads + frameCount/100.0);  
    float y = orig.y + targetRad * sin(rads + frameCount/50.0);

    targetVecs[i] = new PVector(x, y);
    //target.vertex(x, y);
  }

  for (float l = 1.0; l > 0; l -= 0.15) {
    stroke(255, 255 - 255 * l, 0);
    //println("l:", l);
    beginShape();
    for (int i = 0; i < targetVecs.length; i+=1) {
      //float rads = radians(i);

      PVector loc = PVector.lerp(orig, targetVecs[i], l);
      //float y = orig.y + targetRad * sin(rads * 2);

      //targetVecs[i] = new PVector(x, y);
      //println(l, dist(loc.x, loc.y, orig.x, orig.y));
      vertex(loc.x, loc.y);
    }
    endShape(CLOSE);
  }
  //println(millis()-m);
}