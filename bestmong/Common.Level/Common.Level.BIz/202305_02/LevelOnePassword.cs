using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_02
{
    public class LevelOnePassword
    {
        public string Solution(string s, string skip, int index)
        {
            var char_a = (int)'a';
            var char_z = (int)'z';
            var diff = char_z - char_a;

            var skipAlphabetList = new Dictionary<char, int>();
            var answer = "";
            var count = 0;
            for (var i = 0; i <= diff; i++)
            {
                if (skip.IndexOf((char)(char_a + i)) == -1)
                {
                    skipAlphabetList.Add((char)(char_a + i), count);
                    count++;
                }
            }

            var temp = 0;
            foreach (var i in s.ToCharArray())
            {
                temp = (skipAlphabetList[i] + index) % skipAlphabetList.Count;
                answer += skipAlphabetList.FirstOrDefault(x => x.Value == temp).Key;
            }
            return answer;
        }
    }
}
