import re
import requests


class BlueRed:
    def __init__(self):
        self.blue_win_ranked = 0
        self.red_win_ranked = 0

        self.blue_win_flex = 0
        self.red_win_flex = 0

        self.aram_blue = 0
        self.aram_red = 0



def blueandredstats(stats):
    URL = "https://www.leagueofgraphs.com/fr/rankings/blue-vs-red"

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    res = requests.get(url = URL, headers = headers)

    tab = list(res.text.split(" "))
    compteur = -1


    f = open("demofilea.txt", "w")
    for i in tab:
        f.write(i)


        if ('%' in i):
            compteur += 1
            if (compteur == 0):
                stats.blue_win_ranked = i
            
            if (compteur == 1):
                stats.red_win_ranked = i
                
            if (compteur == 3):
                stats.blue_win_flex = i

            if (compteur == 4):
                stats.red_win_flex = i

            if (compteur == 6):
                stats.aram_blue = i

            if compteur == 7:
                stats.aram_red = i

    f.close()



stats = BlueRed()
blueandredstats(stats)

print(stats.blue_win_ranked)
print(stats.red_win_ranked)


print(stats.blue_win_flex)
print(stats.red_win_flex)

print(stats.aram_blue)
print(stats.aram_red)