    int i, j, k;
    double pi=3.14159265;
    double temp, x, y, xi, yi;
    for(i=0; i<256;i++)
        for(j=0; j<256;j++){
            RESULT[i][j]=200;
        }
    for(k=1; k<255;k++){
        x=(double)k;
        xi=k;
        yi=100*cos(2*pi*x/120);
        i=125+(int)yi;  //중간 x축을 기준으로 그래프가 그려져야하므로 125를 더함
        j=(int)k;
        RESULT[i][j]=300;
        RESULT[125][j]=150; //x축
        RESULT[j][10]=150;  //y축
    }
    DrawResultImage();
