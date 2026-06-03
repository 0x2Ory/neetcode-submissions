public class Solution {
    public bool IsValidSudoku(char[][] board) 
    {
     int n_rows = board.Length;
     int n_cols  = board[0].Length; // Länge spalten dsa dei rieh eund spalten gleich sein mpssne 

    // row
    for( int i = 0;  i < n_rows; i++)
    {
    HashSet<char> contai = new HashSet<char>();
    for(int j = 0 ; j < n_cols; j++)
    {
        if(board[i][j] == '.') continue; 
        if(contai.Contains(board[i][j]) ) return false;
        contai.Add(board[i][j]);
    }
    }

    // column -
    for(int i = 0; i < n_rows; i++)
    {
     HashSet<char> contai = new HashSet<char>();
     for(int j =0; j <n_cols; j++)
     {
        if(board[j][i] == '.') continue; 
        if(contai.Contains(board[j][i])) return false;
        contai.Add(board[j][i]);
     }
    }


   // 9 quadrate zum durhclaufen 
   for ( int quadrate = 0; quadrate < 9; quadrate ++ )
   {
        HashSet<char> cont = new HashSet<char>();
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                int row = (quadrate / 3) * 3 + i;
                int col = (quadrate % 3) * 3 + j; 
                if (board[row][col] == '.') continue; 
                if (cont.Contains(board[row][col])) return false; 
                cont.Add(board[row][col]);
            }
        }
   }

return true;
}
}