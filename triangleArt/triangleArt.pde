PImage startingImage;

int threshold = 10;

size(800, 500);
startingImage = loadImage("jack.jpg");

int sImgWidth = startingImage.width;
int sImgHeight = startingImage.height;

println("starting");
startingImage.loadPixels();
ArrayList<PVector> locations = new ArrayList();
for (int i = 0; i < startingImage.pixels.length-1; i++) 
{
  color p = startingImage.pixels[i];
  color q = startingImage.pixels[i+1];
  float d = dist(pow(red(p), 2),pow(green(p), 2),pow(blue(p), 2),pow(red(q), 2),pow(green(q), 2),pow(blue(q), 2));
 
  if (d > 1500)
  {
//    println("win");
//    append(locations, new PVector(i % sImgWidth, floor(i/sImgWidth)));
//    locations.append(new PVector(i % sImgWidth, floor(i/sImgWidth)));
    locations.add(new PVector(i % sImgWidth, floor(i/sImgWidth)));
  }
  
}
println(locations.size());

for (int i = 0; i < locations.size(); i++)
{
//  dist = 9001
//  for (int j = 0; j < locations.length; i++) {
//  }
  PVector loc = locations.get(i);
  point(loc.x/2, loc.y/2);
}
