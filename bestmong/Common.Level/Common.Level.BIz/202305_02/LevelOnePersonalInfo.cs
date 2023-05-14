using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_02
{
    public class LevelOnePersonalInfo
    {
        public List<int> Solution(string today, string[] terms, string[] privacies)
        {
            today = "2022.05.19";
            terms = new string[] { "A 6", "B 12", "C 3" };
            privacies = new string[] { "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C" };

            var todayDate = Convert.ToDateTime(today);
            var map = new Dictionary<string, int>();
            var answer = new List<int>();
            var info = new string[] { };
            foreach (var term in terms)
            {
                info = term.Split(" ");
                map.Add(info[0], Convert.ToInt32(info[1]));
            }

            var index = 0;
            var result = "";
            DateTime targetDate;
            foreach (var privacy in privacies)
            {
                info = privacy.Split(" ");
                targetDate = Convert.ToDateTime(info[0]).AddMonths(map[info[1]]).AddDays(-1);
                if(targetDate.Ticks < todayDate.Ticks)
                {
                  answer.Add(index + 1);
                }
                index++;
            }

            return answer;
        }
    }
}
