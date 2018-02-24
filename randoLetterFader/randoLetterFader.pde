Grid[][] grid;
int gridX, gridY;

void setup()
{
  size(1000, 1000);
  gridX = width/20;
  gridY = height/20;

  grid = new Grid[gridX][gridY];

  for (int i = 0; i < gridX; i++) 
  {
    for (int j = 0; j < gridY; j++)
    {
      grid[i][j] = new Grid(i * width/gridX, j * height/gridY);
    }
  }
  fill(0);
  noStroke();
}


void draw()
{

  background(0);
  for (int i = 0; i < gridX; i++) 
  {
    for (int j = 0; j < gridY; j++)
    {
      if (frameCount % 3 == 0) 
      {
        grid[i][j].run();
      }
      grid[i][j].drawMe();
    }
  }
}

class Grid 
{
  float x;
  float y;
  char s;
  float a = 0;
  float reducto = 7.5;

  Grid(float tx, float ty)   
  {
    s = getChar();
    x = tx;
    y = ty;

  }


  char getChar() 
  {
    return (char) floor(random(87, 123));
  }


  void run() 
  {

    s = getChar();

  }
  void drawMe() 
  {


    if (dist(x, y, mouseX, mouseY) < 100) 
    {
      a = 255;
    }
    else {
      a = max(a - reducto, 0);
      
    }
    fill(255, a);
    text(s, x, y);    
  }
}