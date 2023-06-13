using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Common.Level.Biz._202305_03
{
    public class Distance
    {
        public int[] Solution(string[,] places)
        {
            //places = new string[,]
            //{
            //    {"POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"},
            //    {"POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"},
            //    {"PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"},
            //    {"OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"},
            //    {"PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"},
            //};

            /// P 기준 상하좌우 -1 더하기
            /// -2 이상이면 거리두기 실패
            /// 1차원 배열로 데이터 저장 시 배열의 맨처음 마지막은 좌우가 없음 
            var answer = new int[5];
            Array.Fill(answer, -1);
            var result = new int[places.GetLength(0) * places.GetLength(1)];
            var distance = places.GetLength(0);
            for (var i = 0; i < places.GetLength(0); i++)
            {
                Array.Fill(result, 0);
                for (var j = 0; j < places.GetLength(1); j++)
                {
                    var charList = places[i, j].ToCharArray();
                    for (var z = 0; z < charList.Length; z++)
                    {
                        var index = j * distance + z;
                        switch (charList[z])
                        {
                            case 'P':
                                result[index] -= 1;
                                if (index != 0 && z != 0)
                                    result[index - 1] -= 1;

                                if (index < result.Length && z != charList.Length - 1)
                                    result[index + 1] -= 1;

                                if (index + distance < result.Length)
                                    result[index + distance] -= 1;

                                if (index > distance)
                                    result[index - distance] -= 1;
                                break;
                            case 'O':
                                result[index] += 0;
                                break;
                            case 'X':
                                result[index] += 10;
                                break;
                        }
                    }
                    if (result.Any(s => s <= -2))
                    {
                        answer[i] = 0;
                        break;
                    }
                }
                if (answer[i] == -1)
                {
                    answer[i] = 1;
                }
            }
            return answer;
        }
    }
}
