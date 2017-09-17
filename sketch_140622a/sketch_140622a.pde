boolean run = false;
float c = 0.0;

void setup() {
  size(600, 300);
  stroke(255);
  strokeWeight(4);
  noFill();
}


void draw() {
  background(0);

  if (run) {
    
    for (float i = 0.0; i < 50; i++) {
      arc(width/2, height-20, i*10, i*10, PI, PI + radians((i+(i*c/3.0)/10)%180));
    }
    c++;
  }
  
}


void mouseClicked() {
  run = true;
}

