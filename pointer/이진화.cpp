    int i, j, k, n, l;
    int N=256, Threshold=100;
    for(i=0;i<N;i++){
        for(int j=0; j<N; j++){
            if(ORG[i][j]>=Threshold){
                RESULT[i][j]=255;
            }
            else RESULT[i][j]=0;
        }
    }
    DrawResultImage();
