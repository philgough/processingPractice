void drawLine(float startX, float startY, float heading, float turn, float dist, float scale, int iter) {
  float endX = startX;
  float endY = startY;
  
  endX += cos(heading) * dist;
  endY += sin(heading) * dist;
  
  stroke((sin(radians(iter))*244+frameCount /2.0)% 360, 100, 100); 
  line(startX, startY, endX, endY);
  if (iter > 1) {
    drawLine(endX, endY,  heading + turn, turn, dist * scale, scale, iter-1);
  }
}

void setup() {
  size(1000, 1000);
  colorMode(HSB, 360, 100, 100, 100);
  drawLine(width/2, height/2, 0.0, radians(122), 10.0,1.05, 300);
  stroke(255);
  strokeWeight(2);
  noFill();
}

void draw() {
  background(0);

  drawLine(width/2, height/2, 0.0, radians(121 + (frameCount/115.0)%360), 10.0,1.05, 200);
}
