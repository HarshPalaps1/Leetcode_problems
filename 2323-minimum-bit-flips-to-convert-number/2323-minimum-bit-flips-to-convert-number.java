class Solution {

    public static int[] binary(int num ){
        int[] bi_num=new int[100]; 
        int position =0;
    
        while(num>0){
           bi_num[position]=num%2;
           num=num/2;
           position++; 
                   }
        
        
        return bi_num;
    }

    public int minBitFlips(int start, int goal) {
      int[] Start=binary(start);
      int[] Goal=binary(goal);
      int count=0;
      for(int i=0;i<Start.length;i++){
      if( Start[i]!=Goal[i]){
            count++;
      }
     
      
    } return count;}
}