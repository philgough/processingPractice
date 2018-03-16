// this is what a nested for loop does
for (int i = 0; i < 10; i++) {
  for(int j = 0; j < i; j++) {
    int x = i;
    int y = j;
    rect(x*10, y*10, 10, 10);
  }
}