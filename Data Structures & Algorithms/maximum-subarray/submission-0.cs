public class Solution {
    public int MaxSubArray(int[] nums) {

        int n = nums.Length;
        int result = nums[0];

        for (int i = 0; i < n; i++) //durchlaufe ganzes array einmal
        {
            int current = 0; //Speiche arraysumme des derzeitgen subarrays

            for (int j = i; j < n; j++) //verkleinere das Array jedes Mal um alle möglichen SUbarray abzubilden
            {
                current += nums[j]; //berechne die Summe dieses Subarrays
                result = Math.Max(result,current); //speicher linksläufige subarray ergeebnisse und bilde ale restlichen ergebnisse ab
            }

        }
        return result;
    }
}