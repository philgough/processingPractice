size(400, 400);
background(0);
stroke(255);
for (int i = 0; i < width; i++) {
  for (int j = 0; j < height; j++) {
    float d = dist(i, j, width/2, height/2);
    if (floor(d) == 150) {
      point(i, j);
    }
  }
}
