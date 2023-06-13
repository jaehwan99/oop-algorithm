using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_04
{
    public class Uniform
    {
        public int Solution(int n, int[] lost, int[] reserve)
        {
            /*5	[2, 4]	[3]*/
            /*3	[1]	[3]*/
            var max = 30;
            var temp = lost.Where(s => reserve.Contains(s) == false).ToArray();
            reserve = reserve.Where(s => lost.Contains(s) == false).ToArray();
            lost = temp.OrderBy(s => s).ToArray();
            reserve = reserve.OrderBy(s => s).ToArray();


            var answer = n - lost.Length;
            var dict = new Dictionary<int, int>();
            for (int i = 1; i <= max; i++)
            {
                dict[i] = 0;
            };

            foreach (int i in reserve)
            {
                dict[i] = 1;
            };

            foreach (int i in lost)
            {
                if (i != 1 && dict[i - 1] == 1)
                {
                    answer++;
                    dict[i - 1] = 0;
                }
                else if (i != max && dict[i + 1] == 1)
                {
                    answer++;
                    dict[i + 1] = 0;
                }
            }
            return answer;
        }
    }
}
