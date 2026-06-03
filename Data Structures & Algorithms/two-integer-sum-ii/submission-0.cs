public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        // Texr in Ruhe lesen
        // was bekomen wir übergeben
        // was sollen wir übergeben
        // erstmal Brute forcen
        for (int i = 0; i < numbers.Length; i++)
        {
            for (int j = i+1; j < numbers.Length; j++)
            {
                if(numbers[i] + numbers[j] == target) 
                {
                    return new int[] {i+1, j+1 };
                }
            }
        }
        return new int[] {0,0};
    }
}
