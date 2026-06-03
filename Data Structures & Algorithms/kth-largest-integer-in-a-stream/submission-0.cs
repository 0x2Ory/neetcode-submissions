public class KthLargest {


    private PriorityQueue <int,int> heap; 
    private int k;
    public KthLargest(int k, int[] nums)
    {
        this.k = k; 
        this.heap = new PriorityQueue <int,int>();
        foreach (int num in nums)
        {
            heap.Enqueue(num,num);
            if(heap.Count > k)
            {
                heap.Dequeue();
            }
        }

    }
    
    public int Add(int val)
    {
        heap.Enqueue(val,val);
        if (heap.Count > k)
        {
            heap.Dequeue();
        }
        return  heap.Peek();
    }
}
