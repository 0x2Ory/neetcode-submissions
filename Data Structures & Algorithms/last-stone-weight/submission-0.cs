public class Solution {
    public int LastStoneWeight(int[] stones)
    {
        PriorityQueue<int,int> heap = new PriorityQueue <int,int>();

        foreach(int stone in stones)
        {
            heap.Enqueue(stone, -stone);
        }


        while(heap.Count > 1)
        {
            int first = heap.Dequeue();
            int second = heap.Dequeue();
            if (first != second)
            {
                int rest = first - second;
                heap.Enqueue(rest,-rest);
            }
        }
        if(heap.Count == 1) return heap.Dequeue();
        else return 0;

        // ternärer Operator return heap.Count == 1 ? heap.Dequeue():0;

    }
}
