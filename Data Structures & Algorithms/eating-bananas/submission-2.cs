public class Solution {
    public int MinEatingSpeed(int[] piles, int h)
    {

        int kmax = piles.Max();
        for (int k =1;  k  <= kmax; k++)
        {

        long ttime = 0; 

        foreach(int pile in piles)      
        {
            ttime += (int) Math.Ceiling((double) pile / k );
        }


        if( ttime <= h) return k;
        
        }




        return 0;
        }









    }

