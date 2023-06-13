using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_04
{
    public class MatrixSum
    {
        public int[,] Solution(int[,] arr1, int[,] arr2)
        {
            //int[,] arr1 = new int[,] { { 1, 2 }, { 2, 3 } };
            //int[,] arr2 = new int[,] { { 3, 4 }, { 5, 6 } };
            int[,] answer = new int[arr1.GetLength(0), arr1.GetLength(1)];

            for (var i = 0; i < arr1.GetLength(0); i++)
            {
                for (var j = 0; j < arr1.GetLength(1); j++)
                {
                    answer[i, j] = arr1[i, j] + arr2[i, j];
                }
            }
            return answer;
        }
    }
}
