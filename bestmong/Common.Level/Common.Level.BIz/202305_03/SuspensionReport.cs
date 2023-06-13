using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_03
{
    public class SuspensionReport
    {
        public List<int> Solution(string[] id_list, string[] report, int k)
        {
            //["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"] 2
            //["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"] 3

            //string[] id_list = new string[] { "muzi", "frodo", "apeach", "neo" };
            //string[] report = new string[] { "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi" };

            //string[] id_list = new string[] { "con", "ryan" };
            //string[] report = new string[] { "ryan con", "ryan con", "ryan con", "ryan con" };

            //string[] id_list = new string[] { "muzi", "frodo", "apeach", "neo" };
            //string[] report = new string[] { "muzi frodo", "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi" };
            //int k = 2;
            var result = new Dictionary<string, int>();
            var banUsers = new Dictionary<string, string>();

            foreach (string id in id_list)
            {
                result.Add(id, 0);
            }

            foreach (string id in report)
            {
                var data = id.Split(' ');

                var reporter = banUsers.Count == 0 ? "" : banUsers.ContainsKey(data[1]) ? banUsers[data[1]] : "";
                /// reporter.contains 로 사용 시 비슷한 이름이 있을 경우 검증오류
                ///report=["frodo muzisung", "frodo muzi", "apeach neo", "muzi neo"]
                if (string.IsNullOrEmpty(reporter) || reporter.Split(",").Any(s => s == data[0]) == false)
                {
                    if (banUsers.ContainsKey(data[1]))
                        banUsers[data[1]] += "," + data[0];
                    else
                        banUsers.Add(data[1], data[0]);
                }
            }

            foreach (string id in banUsers.Keys)
            {
                var reporters = banUsers[id].Split(',');
                if (reporters.Length >= k)
                {
                    foreach (var reporter in reporters)
                    {
                        result[reporter] += 1;
                    }
                }
            }

            var answer = new List<int>();
            foreach (var item in result)
            {
                answer.Add(item.Value);
            }

            return answer;
        }
    }
}
