using System;
using System.Collections.Generic;
using System.Linq;

namespace Common.Level.Biz._202305_01
{
    public class Players
    {

        public string[] Solution(string[] players, string[] callings)
        {
            var map = new Dictionary<string, int>();
            var index = 0;
            foreach (var player in players)
            {
                map.Add(player, index);
                index++;
            }

            var temp = "";
            var rank = 0;
            index = 0;
            foreach (var caller in callings)
            {
                rank = map[caller];
                temp = players[rank - 1];
                players[rank - 1] = caller;
                players[rank] = temp;
                map[caller] = rank - 1;
                map[temp] = rank;
            }

            // var temp = "";
            // var index = 0;
            // for (var i = 0; i < callings.Length; i++)
            // {
            //     temp = callings[i];

            //     index = Array.IndexOf(players, temp);
            //     players[index] = players[index -1];
            //     players[index -1] = temp;

            //     // for (var j = 1; j < players.Length; j++)
            //     // {
            //     //     if (temp.Equals(players[j]))
            //     //     {
            //     //         players[j] = players[j - 1];
            //     //         players[j - 1] = temp;
            //     //         break;
            //     //     }
            //     // }
            // }

            return players;
        }

        public string[] init()
        {

            var player = new string[] { "mumu", "soe", "poe", "kai", "mine" };
            var callings = new string[] { "kai", "kai", "mine", "mine" };
            var answer = Solution(player, callings);
            return answer;
        }

        // foreach(var call in callings){
        //     temp = call;
        //     foreach(var player in players.Select((value, index) => (value, index))){
        //         if(temp.Equals(player.value))
        //         {
        //             players[player.index] =  players[player.index -1];
        //             players[player.index -1] = temp;
        //             break;
        //         }
        //     }
        // }  


    }
}