public class Solution {
    public int Trap(int[] height) 
    {
        int left =0 , res  = 0; 
        int right  = height.Length  -1; 
        int lefth = height[left];
        int righth = height[right];
        if((height.Length == 0) || height == null) return 0; 
        // immer die keliner Höhe bewegen
        // wenn beide gleich sonderfall
        // Menge berechnen wir:
        // was ist größer ? wir nehmen dei anderen seite 
        // weil uns größte nicht interessiert es nicht ausausshclaggebend 
        // für den stantd ist sodnern nur der kleine
        // zwei sachen wissen wir nun nach rehctsoderlinks
        // hin wird das wasser getrap also müssen wir auf der
        //kleinen seite heasufinden wie viel dableinbt 
        // wir nehmen hier das maximum beider i +1 
        // und szbtrahieren durch die größe

        while (left < right)
        {

            if(lefth < righth)
            {
                left++;
                lefth = Math.Max(lefth, height[left]);
                res += lefth - height[left];
            }
            else
            {
                right--; 
                righth =Math.Max(righth, height[right]);
                res += righth - height[right];
            }


        }







        return res; 
    }
}
