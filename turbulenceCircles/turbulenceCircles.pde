float power = 6; // Turbulence power
float d = 8; // Turbulence density
void setup () {
  colorMode(HSB);
  size(1920, 720);
  noStroke();
  strokeWeight(18);
}
void draw() {
  
  for (int y = 0; y < height; y+=20) {
    for (int x = 0; x < width; x+=20) {
      float total = 0.0;
      for (float i = d; i >= 1; i = i/2.0) {
        total += noise(x/d, y/d) * d;
      }
      float turbulence = 128.0 * total / d;
      float base = (x * 0.2) + (y * 0.12);
      float offset = base + (power * turbulence / 256.0);
      float c = abs(sin(offset + frameCount/4.0)) * 256.0;
      stroke(c);
      point(x, y);
    }
  }
}

