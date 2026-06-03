public class Solution {
    public int[] TopKFrequent(int[] nums, int k) 
    {
        Dictionary<int,int> topdic = new Dictionary<int,int>();

        foreach (int vari in nums)
        {
            if (topdic.ContainsKey(vari))
            {
                topdic[vari]++;
            }
            else
            {
                 topdic[vari] = 1;
            }
        }

        PriorityQueue<int,int> heap = new PriorityQueue<int,int>();
        foreach (var entry in topdic)
        {
            heap.Enqueue(entry.Key, entry.Value);
            if(heap.Count > k) {
                heap.Dequeue();
            }
        }

        var res  = new int[k];

        for (int i = 0; i < k; i++)
        {
            res[i] = heap.Dequeue();
        }

        return res;
    }
}
