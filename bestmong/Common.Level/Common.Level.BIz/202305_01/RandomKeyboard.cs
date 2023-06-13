using System;
using System.Collections.Generic;
using System.Linq;

namespace Common.Level.Biz._202305_01
{
    public class RandomKeyboard
    {
        public int[] Solution(string[] keymap, string[] targets)
        {
            int[] answer = new int[targets.Length];
            var map = new Dictionary<char, int>();
            var index = 0;

            foreach (var key in keymap)
            {
                var temp = key.ToCharArray();
                index = 1;
                foreach (var i in temp)
                {
                    if (map.ContainsKey(i) == false || map[i] > index)
                    {
                        map[i] = index;
                    }
                    index++;
                }
            }

            index = 0;
            foreach (var target in targets)
            {
                var temp = target.ToCharArray();
                var count = 0;
                foreach (var i in temp)
                {
                    if (map.ContainsKey(i) == false)
                    {
                        count = -1;
                        break;
                    }
                    else
                        count += map[i];
                }
                answer[index] = count;
                index++;
            }

            return answer;
        }

        public int[] Init()
        {
            // var keyArray = new string[] { "ABACD", "BCEFD" };
            // var targets = new string[] { "ABCD", "AABB" };

            var keyArray = new string[] { "AGZ", "BSSS" };
            var targets = new string[] { "ASA", "BGZ" };
            return Solution(keyArray, targets);
        }
    }
}