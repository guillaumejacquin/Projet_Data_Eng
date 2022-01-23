import requests
import re 
import random

# Making a GET request
url = 'https://www.leagueofgraphs.com/rankings/summoners'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

res = requests.get(url = url, headers = headers)

tab = list(res.text.split(' '))
count  = 0
is_open = False
tab_var = []
rep = 'lolg-cdnlolg-cdn.porofessor.gg'

for i in tab:
    print(i)
    f = open("alaide.txt", "a")
    f.write(str(i))
    f.close()
    # if(i in rep and is_open == False ):
    #     is_open = True
    #     count = 0 
    # if(is_open == True):
    #     print(i)
    #     count += 1
    #     if(count >= 30):
    #         is_open = False
    #         print('--------------------------------------------------------------------------------------------------------------')





# f = open("zizi.txt", "a")
# f.write(str(res.content))
# f.close()