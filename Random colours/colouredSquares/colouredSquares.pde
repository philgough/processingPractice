//

int colourRange = 8;
void setup() 
{
  size(2000, 2000);
  colorMode(HSB, colourRange, 100, 100, 100);
  rectMode(CENTER);
  noStroke();
  
  int gridSize = width/40;

  int numX = width/gridSize;

  int numY = height/gridSize;

  Grid[][] grid = new Grid[width/numX][height/numY];

  background(colourRange);

  for (int i = 0; i < numX; i++)
  {
    for (int j = 0; j < numY; j++)
    {
      grid[i][j] = new Grid(i, j, gridSize);
    }
  }
  //

  PVector temp = new PVector(0, 0);
  float d = dist(width/2, height/2, 0, 0);

  for (int i = 0; i < numX; i++) 
  {
    for (int j = 0; j < numY; j++)
    {

      grid[i][j].drawGrid(temp, d);
    }
  }
  //
  //
}

class Grid
{
  int x, y, s; 
  boolean drawMe;
  

  Grid(int xPos, int yPos, int gridSize)  
  {
    s = gridSize;
    x = s*xPos + s/2;
    y = s*yPos + s/2;
  }

  void drawGrid(PVector t, float d) 
  {



    t.set(x, y);

    float r  = randomGaussian();
    // percent of location as per d
    float p = dist(width/2, height/2, t.x, t.y)/d;


    if (p < r/3)
    {
      fill(int(random(colourRange)), 30 + random(15), 80 + random(20));
    } else
     fill(colourRange); 
    {
    }
    rect(x, y, s - 4, s - 4 );
    fill(0);
//    text(p, x, y);
  }
}