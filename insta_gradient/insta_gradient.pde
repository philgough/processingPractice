

size(1680, 500);
 
for (int i = 0; i < width; ++i) {
        for (int j = 0; j < 720; ++j) {
                float redVal = map(i, 0, width, 150, 255);
                float greenVal = map(j, 0, height, 100, 222);
                float blueVal = map(i, 0, width, 220, 100);
                stroke(redVal, greenVal, blueVal);
                point(i, j);
                
        }
        
}

save("output.png");
 
