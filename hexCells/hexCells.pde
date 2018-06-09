Hex[][] hex;

float _w = 20;
float _h = sin(radians(60)) * _w;
int columns, rows;

void setup() {
  size(600, 600);
  
  columns = width/int(_w*3);
  rows = height/int(_h);
  hex = new Hex[columns][rows];
  for (int i = 0; i < columns; i++) {
     for (int j = 0; j < rows; j++) {
       if (j % 2 == 0) hex[i][j] = new Hex(i * _w * 3, j * _h, _w);
       else hex[i][j] = new Hex(i*_w*3+_w+_w/2, j*_h, _w);
     }
  }
}


void draw() {
  background(255);
  for (int i = 0; i < columns; i++) {
    for (int j = 0; j < rows; j++) {
      hex[i][j].display();
      
    }
  }
}


class Hex {
  float x, y, r;
  float xoff, yoff;

  Hex(float x_, float y_, float r_) {
    x = x_;
    y = y_;
    r = r_;
    xoff = r_/2;
    yoff = sin(radians(60)) * r_;

  }
  void display() {
    //print(x, y, r);
    fill(200, 0, 250);
    stroke(0);
    pushMatrix();
    translate(x - r/4, y - r/2);
    beginShape();
    vertex(0, yoff);
    vertex(xoff, 0);
    vertex(xoff+r, 0);
    vertex(2*r, yoff);
    vertex(xoff+r, 2*yoff);
    vertex(xoff, 2*yoff);
    vertex(0, yoff);
    endShape();
    
    popMatrix();
  }
}