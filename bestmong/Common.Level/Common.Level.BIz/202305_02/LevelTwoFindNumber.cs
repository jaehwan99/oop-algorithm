using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_02
{
    public class LevelTwoFindNumber
    {
        public int[] Slution(int[] numbers)
        {
            var answer = new int[numbers.Length];
            Array.Fill(answer, -1);

            var count = 1;
            for (var i = numbers.Length - 2; i >= 0; i--)
            {
                for (var j = i + 1; j <= i + count; j++)
                {
                    if (numbers[j] > numbers[i])
                    {
                        answer[i] = numbers[j];
                        break;
                    }

                    if (answer[j] == -1)
                    {
                        answer[i] = -1;
                        break;
                    }

                    if (answer[j] > numbers[i])
                    {
                        answer[i] = answer[j];
                        break;
                    }
                }
                count++;
            }
            return answer;
        }
    }
}
