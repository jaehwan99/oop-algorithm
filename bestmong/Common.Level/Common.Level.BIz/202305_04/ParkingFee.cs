using OOP.Algorithm.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_04
{
    public class ParkingFee
    {
        public List<int> Solution(int[] fees, string[] records)
        {
            //    //int[] fees = new int[] { 120, 0, 60, 591 };
            //    //string[] records = new string[] { "16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN" };

            //    int[] fees = new int[] { 180, 5000, 10, 600 };
            //    string[] records = new string[] { "05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT" };
            List<int> answer = new List<int>();

            var defaultTime = fees[0];
            var defaultFee = fees[1];
            var unitMin = fees[2];
            var unitRate = fees[3];


            var p_info = new Dictionary<int, Parking>();
            foreach (var data in records)
            {
                var dataArr = data.Split(' ');
                var currentTimeArr = dataArr[0].Split(':');
                var currentTime = new TimeSpan(Convert.ToInt32(currentTimeArr[0]), Convert.ToInt32(currentTimeArr[1]), 00);
                var key = Convert.ToInt32(dataArr[1]);
                if (dataArr[2] == "IN")
                {
                    if (p_info.ContainsKey(key))
                    {
                        p_info[key].IsOut = false;
                        p_info[key].CurrentInOutTime = currentTime;
                    }
                    else
                    {
                        p_info.Add(key, new Parking()
                        {
                            CurrentInOutTime = currentTime,
                            AccumulateMin = 0,
                            IsOut = false,
                        });
                    }
                }
                else
                {
                    p_info[key].IsOut = true;
                    p_info[key].AccumulateMin += (currentTime - p_info[key].CurrentInOutTime).TotalMinutes;
                    p_info[key].CurrentInOutTime = currentTime;
                }
            }

            var keys = p_info.Keys.OrderBy(s => s).ToList();
            var lastOutTime = new TimeSpan(23, 59, 00);
            foreach (var key in keys)
            {
                var infos = p_info[key];
                var accumulateMin = infos.AccumulateMin + (infos.IsOut == false ? (lastOutTime - infos.CurrentInOutTime).TotalMinutes : 0);
                var result = GetParkingRate(defaultFee, defaultTime, accumulateMin, unitMin, unitRate);
                answer.Add(result);
            }
            return answer;
        }

        public int GetParkingRate(int defaultFee, int defaultTime, double accumulateMin, int unitMin, int unitRate)
        {
            var calMin = accumulateMin - defaultTime < 0 ? 0 : accumulateMin - defaultTime;
            defaultFee = accumulateMin == calMin ? 0 : defaultFee;
            var useTime = Math.Ceiling(calMin / unitMin);
            return (int)(defaultFee + (useTime * unitRate));
        }
    }
}