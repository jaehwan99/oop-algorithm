using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_03
{
    public class QueueSumSearch
    {
        public long Solution(int[] queue11, int[] queue22)
        {
            long answer = 0;
            // var queue1 = queue11.ToList();
            //  var queue2 = queue22.ToList();
            var queue1 = new Queue<long>(queue11.Select(s => (long)s).ToList());
            var queue2 = new Queue<long>(queue22.Select(s => (long)s).ToList());
            var queue1Length = queue1.Count;
            var queue2Length = queue2.Count;

            long qu1Sum = queue1.Sum();
            long qu2Sum = queue2.Sum();
            long result = (qu1Sum + qu2Sum);
            if (result % 2 != 0)
                return -1;

            long searchVal = result / 2;

            while (true)
            {
                if (queue1.Count == 0 || queue2.Count == 0)
                    break;

                if (answer > queue1Length * 3)
                    break;

                if (qu1Sum == searchVal || qu2Sum == searchVal)
                    break;

                if (qu1Sum < searchVal)
                {
                    qu1Sum += queue2.First();
                    qu2Sum -= queue2.First();
                    queue1.Enqueue(queue2.First());
                    queue2.Dequeue();
                    answer++;
                }
                else if (qu2Sum < searchVal)
                {
                    qu2Sum += queue1.First();
                    qu1Sum -= queue1.First();
                    queue2.Enqueue(queue1.First());
                    queue1.Dequeue();
                    answer++;
                }
            }

            if (queue1.Count == 0 || queue2.Count == 0)
                return -1;

            if (qu1Sum != qu2Sum)
                return -1;

            return answer;
        }
    }
}
