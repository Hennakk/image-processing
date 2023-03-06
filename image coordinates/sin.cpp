    int i, j, k;
    double pi=3.14159265;
    double temp, x, y, xi, yi;
    double theta=45*pi/180.0; //θ=45일때
    n=(int)125+100*cos(theta);
    for(k=1; k<360;k++){
        x=(double)k;
        xi=125+100*cos(2*pi*x/360);
        yi=125+100*sin(2*pi*x/360);
        i=(int)xi;
        j=(int)yi;
        RESULT[i][j]=0;
        RESULT[125][j]=300;  //x축
        RESULT[i][125]=300;  //y축
        RESULT[j][n]=0;
    }
        for(r=0;r<100;r++){
            xx=(int)125-r*sin(theta);
            yy=(int)125+r*cos(theta);
            RESULT[xx][yy]=300; //빗금 r
	    RESULT[xx][n]=300;  // sinθ
        }
    DrawResultImage();
