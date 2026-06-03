public class Solution {
    public int[][] KClosest(int[][] points, int k) 
    {
    PriorityQueue <int[], int> maxHeap = new PriorityQueue <int[], int>();

    foreach (var point in points)
    {
        int dist = point[0] * point[0] + point[1] * point[1];
        maxHeap.Enqueue(point, -dist);
        if(maxHeap.Count  > k)
        {
            maxHeap.Dequeue();
        }
    }
    var res = new List<int[]>(); 
    while (maxHeap.Count > 0){
    res.Add(maxHeap.Dequeue());
    }
        return res.ToArray();
    }
}
