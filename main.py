import requests
import re 
import random

# Making a GET request

def getstats(URL):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    res = requests.get(url = URL, headers = headers)

    tab = list(res.text.split(' '))
    count  = 0
    is_open = False
    best_players_name = []
    best_players_winrate = []
    best_players_rank = []

    is_name_taken = False
    isrank_taken = False
    is_number_victory = False

    name = ""
    elo = ""
    winrate = ""


    
    rep ="lolg-cdn.porofessor.gg/img/d/summonerIcons"
    # f = open("alaide.txt", "w")

    for i in tab:
        # f.write(str(i))
        if (rep in i and is_open == False ):
            is_open = True
            count = 0 
        if(is_open == True):
            if ("alt" in i):
                is_name_taken = True
            if (is_name_taken == True):
                if ("title" in i):
                    is_name_taken =False
                    name = name.replace('alt="', "")
                    name = name[:-1]
                    best_players_name.append(name)
                    name = ""

                else:
                    name = name + i

            if ("summonerTier" in i):
                isrank_taken = True
            if (isrank_taken == True):
                if "wins" in i:
                    isrank_taken = False
                    elo = elo.replace('class="summonerTier">', "")
                    elo = elo[:-12]
                    elo = elo.strip()
                    elo= elo.rstrip()

                    tab = list(elo.split('\n'))
                    best_players_rank.append(tab)
                    elo = ""
                else:
                    elo = elo + i

            if "wins" in i:
                is_number_victory = True

            if(is_number_victory == True):
                if "</div>" in i:
                    is_number_victory = False
                    winrate = winrate.replace('class="wins">', "").replace("(","").replace("%)", "")
                    winrate = winrate[1:-5]
                    winrate = winrate.rstrip()
                    tab = list(winrate.split('<i>'))
                    

                    best_players_winrate.append(tab)
                    winrate = ""
                    

                else:
                    winrate = winrate + i

    return(best_players_name, best_players_rank, best_players_winrate)





def getbestplayers():
    url = 'https://www.leagueofgraphs.com/rankings/summoners'
    best_players_name = []
    best_players_rank = []
    best_players_winrate = []
    best_players_name2 = []
    best_players_rank2 = []
    best_players_winrate2 = []
    best_players_name3 = []
    best_players_rank3 = []
    best_players_winrate3 = []

    best_players_name, best_players_rank, best_players_winrate = getstats(url)
    url = "https://www.leagueofgraphs.com/fr/rankings/summoners/page-2"
    best_players_name2, best_players_rank2, best_players_winrate2 = getstats(url)

    url = "https://www.leagueofgraphs.com/fr/rankings/summoners/page-3"
    best_players_name3, best_players_rank3, best_players_winrate3 = getstats(url)

    best_players_name = best_players_name + best_players_name2 + best_players_name3
    best_players_rank = best_players_rank + best_players_rank2 + best_players_rank3
    best_players_winrate = best_players_winrate + best_players_winrate2 + best_players_winrate3


    delete = len(best_players_winrate) - len(best_players_name)
    del best_players_rank[-delete:]
    del best_players_winrate[-delete:]

    print(len(best_players_name))
    print(len(best_players_rank))
    print(len(best_players_winrate))

getbestplayers()