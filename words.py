from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime

def puttweet():

	twitter = OAuth1Session(os.environ["API_KEY"], 
                            os.environ["API_SECRET_KEY"], 
                            os.environ["ACCESS_TOKEN"], 
                            os.environ["ACCESS_TOKEN_SECRET"]
                            )

    q_year = random.randrange(25, 32)
    q_season = random.choice(('haru', 'aki'))
    q_num = random.randrange(1, 80)

	message = ("【１日１問】\n" +
               "本日の応用技術者試験過去問\n" +
               f"https://www.ap-siken.com/kakomon/{q_year}_{q_season}/{q_num}.html")

	params = {"status": message} 
	res = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)