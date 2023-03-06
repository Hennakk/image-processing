int i, j, k, n, l;
    int hist[256];  //밝기값 개수 저장 배열
    int N=256, max;
    for(int z=0; x<N; z++){
        hist[z]=0;
        sum_of_hist[z];
    }
    for(i=0; i<N; i++)
        for(j=0; j<N; j++){
            k=ORG[i][j];  //반복문을 통해 각 픽셀의 밝기값을 찾은 후
            hist[k]=hist[k]+1;  // 배열에 저장 
        } 
    for(i=0;i<256;i++)
        for(int j=0; j<256; j++){
            RESULT[i][j]=255;  //흰 배경으로 만들기
        }  
    max=hist[0];  //히스토그램 그래프를 256*256 사이즈안에 맞추기 위해
		    모든 그래프 성분을 최대값으로 나누어 준다.
    for(i=1;i<256;i++){
        if(hist[i]>max)
            max=hist[i]; //최대값 찾기
    } 
    for(n=0;n<256;n++){
        for(l=0;l<hist[n]/(max/255);l++){  //최대값을 픽셀값으로 나누어준다.
            RESULT[255-l][n]=300;  //그래프 그리기
        }
    }
    DrawResultImage();
