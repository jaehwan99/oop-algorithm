using System;

namespace Coding.Test.Level1
{
    public class Painting
    {
        public int solution(int n, int m, int[] section)
        {
            var currentValue = 0;
            var last = section[section.Length - 1];
            var count = 0;

            for (var i = 0; i < section.Length; i++)
            {

                if (currentValue >= last)
                    break;
                if (currentValue < section[i])
                {
                    currentValue = section[i] + m - 1;
                    count++;
                }
            }
            int answer = count;
            return answer;
        }

        public int Init()
        {
            // var n = 8;
            // var m = 4;
            // var section = new int[] { 2, 3, 6 };

            // var n = 5;
            // var m = 4;
            // var section = new int[] { 1,3 };

            var n = 100;
            var m = 2;
            var section = new int[] { 2, 4, 10, 11, 14, 17, 40 };

            var answer = solution(n, m, section);
            return answer;
        }
    }
}