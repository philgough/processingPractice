import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class YouthCouncils extends PApplet {

int _w = 1920;
int _h = 720;
int _numY;
int _numX;
int _gridSize = 30;
float _ticker = 0;
float _tickRate = 0.05f;
int _numCells;
Cell[][] grid;
int _xGroup = 0;
int _yGroup = 0;
int _groupChanger = 45;
int _numPoints = 6;
int _sat = 100;
int _bri = 75;
float hue = 0;

int CYCLE = 0;
int RED = 1;
int ORANGE = 2;
int YELLOW = 3;
int GREEN = 4;
int BLUE = 5;
int INDIGO = 6;
int VIOLET = 7;

int backgroundColour = CYCLE;
float backgroundSelector = CYCLE;

int _flashMode = 1;
float[] _pointX = new float[10];
float[] _pointY = new float[10];

public void setup() {
  size(_w, _h);
  colorMode(HSB, 360, 100, 100, 100);
  //stroke(360, 10);
  noStroke();
  fill(360, 50);
  strokeWeight(6);
  smooth();
  goCell();
  instructions();
  noCursor();
}

public void goCell() {
  _numCells = 0;
  _numY = floor(_h/_gridSize);
  _numX = floor(_w/_gridSize);

  grid = new Cell[_numY][_numX];

  for (int y = 0; y < _numY; y ++) {
    for (int x = 0; x < _numX; x ++) {
      Cell newCell = new Cell(y, x, _numCells);
      _numCells++;
      grid[y][x] = newCell;
    }
  }
}

public void instructions () {
  //println("a/z to change global ticker rate");
  //println("h = cycle hues, or ROYGBIV for background");
  //println("s/x to change background saturation");
  //println("d/c to change background brightness");
  //println(",/. to change the rate of group effects");
  //println("-/= to change the number of points rendered (e.g., triangles -> circles)");
}

public void draw() {
  //backgroundSelection();
  //hue = 0;
  runBackground();

  for (int y = 0; y < _numY; y++) {
    for (int x = 0; x < _numX; x++) {
      grid[y][x].run();
    }
  }
  _ticker+= _tickRate;
  movePoints();
  groupChange();
}

public void movePoints() {
  for (int i = 1; i < _pointX.length; i++) {
    _pointX[i] = (sin(((i%2 *4 - 1)  * -1) * _ticker/10 + i)) * _w/10 * i + _w/2;
    _pointY[i] = (cos(((i%2 *2 - 1)  * -1) * _ticker/10 + i)) * _h/10 * i + _h/2;
  }
}

public void groupChange () {
  if (frameCount % _groupChanger == 1) {
    _xGroup = PApplet.parseInt(floor(random(_w)));
    _yGroup = PApplet.parseInt(floor(random(_h)));
  }
}

public void runBackground() {
  hue = 0;
  if (backgroundColour == CYCLE) {
    hue = (frameCount % 360);
  }
  else {
    if (backgroundColour == RED) {
      hue = 0 + (sin(_ticker/3) * 20);
    }
    else { 
      if (backgroundColour == ORANGE) {
        hue = 30 + (sin(_ticker/3) * 20);
      }
      else { 
        if (backgroundColour == YELLOW) {
          hue = 60 + (sin(_ticker/3) * 20);
        }
        else { 
          if (backgroundColour == GREEN) {
            hue = 120 + (sin(_ticker/3) * 20);
          }
          else { 
            if (backgroundColour == BLUE) {	
              hue = 180 + (sin(_ticker/3) * 20);
            }
            else { 
              if (backgroundColour == INDIGO) {
                hue = 240 + (sin(_ticker/3) * 20);
              }  
              else { 
                if (backgroundColour == VIOLET) {
                  hue = 300 + (sin(_ticker/3) * 20);
                }
              }
            }
          }
        }
      }
    }
  }
  
  fill(hue, _sat, _bri, 25);
  //fill(fillColor);
  rect (0, 0, width, height);
  // background(hue, _sat, _bri);
}




public void keyPressed() {
  switch (key) {
  case 'h' :
    backgroundColour = CYCLE;
    //println("cycle hues");
    break;	
  case 'r' :
    backgroundColour = RED;
    //println("reds");
    break;	
  case 'o' :
    backgroundColour = ORANGE;
    //println("oranges");
    break;	
  case 'y' :
    backgroundColour = YELLOW;
    //println("yellows");
    break;	
  case 'g' :
    backgroundColour = GREEN;
    //println("greens");
    break;	
  case 'b' :
    backgroundColour = BLUE;
    //println("blues/cyans");
    break;	
  case 'i' :
    backgroundColour = INDIGO;
    //println("indigo/blues");
    break;	
  case 'v' :
    backgroundColour = VIOLET;
    //println("violets/magenta");
    break;
  case '1' :
    _flashMode = 1;
    //println("random flashes");
    break;	
  case '2' :
    _flashMode = 2;
    //println("sparkles");
    break;	
  case '3' :
    _flashMode = 3;
    //println("group flashes");
    break;
  case '4' :
    _flashMode = 4;
    //println("block flashes");
    break;	
  case '5' :
    _flashMode = 5;
    //println("flashLight");
    break;	
  case '6' :
    _flashMode = 6;
    //println("Circle Wave Effect");
    break;		
  case 'a' :
    _tickRate += .005f;
    //println("tickRate: " + _tickRate);
    break;	
  case 'z' :
    if (_tickRate > 0.005f) {
      _tickRate -= .005f;
      //println("tickRate: " + _tickRate);
    }
    else {
      //println("too slow!");
    }
    break;	
  case 's' :
    _sat += 5;
    //println("saturation: " + _sat);
    break;	
  case 'x' :
    _sat -= 5;
    //println("saturation: " + _sat);
    break;	
  case 'd' :
    _bri += 5;
    //println("brightness: " + _bri);
    break;	
  case 'c' :
    _bri -= 5;
    //println("brightness: " + _bri);
    break;	
  case '.' :
    if (_groupChanger > 10) {
      _groupChanger -= 5;
      //println("groupChanger: " + _groupChanger);
    }
    else {
      //println("too fast, baby!");
    }
    break;	
  case ',' :
    _groupChanger += 5;
    //println("groupChanger: " + _groupChanger);
    break;	
  case '-' :
    if (_numPoints > 2) {
      _numPoints--;
      //println("_numPoints: "+_numPoints);
    }
    else {
      //println("you need more points");
    }
    break;	
  case '=' :
    if (_numPoints < _gridSize/1.7f) {
      _numPoints++;
      //println("_numPoints: "+_numPoints);
    }
    else {
      //println("this seems a little pointless...");
    }		
    break;
  }
}

class Cell {
  int x;
  int y;
  int index;
  float xPos, yPos;
  float shiftX, shiftY;
  float randomNum;
  int colour;

  Cell(int tempY, int tempX, int i) {
    x = tempX;
    y = tempY;
    index = i;
    xPos = x * _gridSize;
    yPos = y * _gridSize;
    colour = color(0, 100, 100, 10);
    randomNum = random(500);
  }

  public void run() {
    colourChooser();
    render();
  }

  public void render() {
    pushMatrix();
    translate(xPos + _gridSize/2, yPos + _gridSize/2);
    //ellipse(0, 0, _gridSize -2, _gridSize - 2);
    beginShape();
    for (int i = 0; i <= 360; i += (360/_numPoints)) {
      vertex(sin(radians(i)) * _gridSize/2.5f, cos(radians(i)) * _gridSize/2.5f);
    }
    endShape(CLOSE);
    fill(360, 80);
    ellipse(shiftX, shiftY, _gridSize/10, _gridSize/10);
    popMatrix();
  }

  public void colourChooser() {
    shiftX = 0;
    shiftY = 0;
    switch (_flashMode) {

    case 1 : 
      if (frameCount % _groupChanger * 3 == 0) {
        randomNum = random(500);
      }
      if (randomNum > 490) {
        colour = color(360, 90);
      }
      else {
        colour = color(360, 3);
      }
      break;

    case 2 :
      if (random(100) > 75) {
        colour = color(360, 90);
      }
      else {
        colour = color(360, 3);
      }
      break;	
    case 3 :
      colour = color(360, 3);

      for (float i = 0.5f; i < 16; i *= 2) {
        if ((index * i) % _numCells == frameCount % _numCells) {
          colour = color(360, 100);
        }
      }
      break;
    case 4 :
      colour = color(360, 3);
      if (abs(xPos - _xGroup) < 250) {
        if (abs(yPos - _yGroup) < 250) {
          colour = color(360, 35);
        }
      }
      break;
    case 5 :
      colour = color(360, 3);
      for (int i = 1; i < _pointX.length; i++) {
        if (dist (_pointX[i], _pointY[i], xPos, yPos) < 10 * i/2) {
          colour = color(360, 55);
        }
      }
      break;	
    case 6 :
      colour = color(360, 5); 
      shiftX = sin(_ticker /2 + index * 30) * _gridSize;// + index;
      shiftY = cos(_ticker /2 + index * 30) * _gridSize;// + index;	
      break;
    }
    fill(colour);
  }
}

  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "YouthCouncils" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
