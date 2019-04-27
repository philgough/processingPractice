float[] offset;
int iterations = 1;
void setup() {
  size(300, 800);
  offset = new float[height*iterations];
  for (int i = 0; i < offset.length; i++) {
    offset[i] = random(1, 1.2);
  }
}

void draw() {
  fill(0, 70);
  noStroke();
  rect(0, 0, width, height);
  stroke(255);

  for(int i = 0; i < height*iterations; i++) {
    float xPos = width/2 + cos(radians(frameCount/(2 * offset[i%height]) + (i%height)/4.0)) * width/2;
    float yPos = i%height;
    point(xPos, yPos);
  }
  
}
