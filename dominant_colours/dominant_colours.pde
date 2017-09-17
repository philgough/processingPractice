PImage img;
color colour;
void setup() 
{
  size(1000, 1000);
  colorMode(HSB, 360, 100, 100, 100);
  img = loadImage("lego.png");

  colour = color(170, 100, 100);

  background(colour);

  img.loadPixels();
  
  int[] colours = {color(0), color(0), color(0)};
  
  int[] frameColours = 
  
  for (int i = 0; i < img.pixels.length; i++)
  {
    
    int pixel = img.pixels[i];
    int hue = Math.round(hue(pixel));
    float sat = saturation(pixel);
    float lum = brightness(pixel);
    
      
  }
  
  
  image(img, 0, 0, 50, 50);
}