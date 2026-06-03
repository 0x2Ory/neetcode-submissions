public class Solution {
    public int MaxArea(int[] heights)
    {
     int start = 0; 
     int end = heights.Length -1; 
     int result = 0; 
    while (start < end)
    {
     int store = Math.Min(heights[start],heights[end]) * (end - start);
     if( heights[start] < heights[end] ) start++; 
     else end--;
     result = Math.Max(result,store);
    }

    return result; 



    }
}
