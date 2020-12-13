var maxArea = function(height) {
    var maxA,i,j;
    maxA = 0;
    i = 0;
    j = height.length -1;
    
    while (i < j){
        maxA = Math.max(maxA,Math.min(height[i],height[j]) * (j-i));
        
        if (height[i] < height[j]){
            i+=1;
        }
        else{
            j-=1;
        }
        
    }
    return maxA
};
