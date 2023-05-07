using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.BIz.Level1
{
    public class Wallpaper
    {
        public int[] solution(string[] wallpaper)
        {
            var top = 0;
            var left = wallpaper.Length;
            var right = 0;
            var bottom = 0;

            var index = 0;
            var searchChar = "#";
            var currentValue = 0;
            foreach (var val in wallpaper)
            {
                currentValue = val.LastIndexOf(searchChar);
                if (currentValue > -1)
                {
                    top = index - top < 0 ? 0 : index - top;

                    if (left > currentValue)
                        left = currentValue;

                    if (right <= currentValue)
                        right = currentValue + 1;

                    bottom = index + 1;
                }
                index++;
            }

            int[] answer = new int[] { top, left, bottom, right };
            return answer;
        }
    }
}
