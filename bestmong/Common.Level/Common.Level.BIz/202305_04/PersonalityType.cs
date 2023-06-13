using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_04
{
    public class PersonalityType
    {
        public string Solution(string[] survey, int[] choices)
        {

            var dict = new Dictionary<char, int>();
            var characterType = new Dictionary<int, string>();
            var types = "RT|CF|JM|AN";

            var middleCount = 7 / 2 + 7 % 2;
            foreach (var type in types.ToCharArray())
            {
                if (type.Equals('|') == false)
                    dict.Add(type, 0);
            }

            var count = 0;
            foreach (var type in types.Split('|'))
            {
                characterType.Add(count++, type.ToString());
            }


            for (var i = 0; i < survey.Length; i++)
            {
                var surveyChar = survey[i].ToCharArray();
                var choice = choices[i];

                if (choice > middleCount)
                {
                    dict[surveyChar[1]] += choice % middleCount;
                }
                else if (choice < middleCount)
                {
                    dict[surveyChar[0]] += middleCount - choice;
                }
            }

            var answer = "";
            for (var i = 0; i < characterType.Count; i++)
            {
                var results = characterType[i].ToCharArray();
                answer += dict[results[0]] < dict[results[1]] ? results[1] : results[0];
            }
            return answer;
        }
    }
}
