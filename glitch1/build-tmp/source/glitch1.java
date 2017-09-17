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

public class glitch1 extends PApplet {

PImage glitch;

public void setup() {
	// size(472, 650);
	// colorMode(HSB, 360, 100, 100, 100);
	size(826, 853);
	glitch = loadImage("me.jpg");
	noLoop();

}



public void draw() {
	//background(0);
	image(glitch, 0, 0);
	loadPixels();

	for (int i = 0; i < pixels.length; i+= 1) {
		// pixels[i] /= sin(radians(i)) + pixels [int(sin(pow(i, 2)))];
		// println(pixels[i]);
		float x = asin(radians(pixels[i]/1000000));

		pixels[i] = PApplet.parseInt(sin(x + (0*PI+ radians(pow(i, x)))/*noise(i/100))*/) * 1000000);// + noise(i));
		// color c = int(noise(sin(radians(i)) + pixels [int(sin(pow(i, 2)))]));
		// fill(c);

		// rect(i%width, i % height, 40, 40);
	}
	updatePixels();
}
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "glitch1" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
