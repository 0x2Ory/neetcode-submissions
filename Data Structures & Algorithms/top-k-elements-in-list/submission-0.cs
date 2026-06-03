public class Solution {
    public int[] TopKFrequent(int[] nums, int k) 
    {
       Dictionary<int, int> count =  new Dictionary<int, int>(); 

        foreach(int num in nums)
        {
            if (count.ContainsKey(num)) count[num]++;
            else count[num] = 1; 
        }

        PriorityQueue<int, int> container = new PriorityQueue<int, int> ();

        foreach(KeyValuePair<int, int> entry in count)
        {
            container.Enqueue(entry.Key, entry.Value);
            if(container.Count > k ) container.Dequeue();
        }

        int[] rescon = new int[k];

        for(int i = 0; i <k; i++) rescon[i] = container.Dequeue();
        return rescon; 
    }
}
