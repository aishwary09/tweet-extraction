#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:02:39 2020

@author: aishwary
"""
import src.getoldtweets3.GetOldTweets3 as got
import pandas as pd


banglore=["priyankaamber","RebelloAnil","discoversk","sri6060","Dwriteguy","pri_rao","ABhadrappa","kriti_kg","homie9007","trilobite_1970","bettaswamy0834"]
Mumbai= ["KhanzSuhail","Chetlur","BLoudST","moviesashish","AmritaW","aadirungta","mayankbhagwat","PawanKu54827606","latestly","manojsaxenaIN"]
Hydrabad=["sanchit_mdi","csmalapaka1","anuj_kh90","Hadihussain1711","lav4al"]
pune=["akash_3220","Ketan58640657","socially_manju","RiyajAhmad786","alishaikh3310","kukku1207"]
kolkata=["vikramdoogar","Subhadeep4India","ALOKGUHA2020","Abhadra7","Arindam99IT"]
Chennai=["shiva2607","SesaBalajiRB","sundarmail","Senthil80712625","manikhrm","aanandsivaraman","Ganeshkiran7","snehasa19805912"]
cities={  "pune":pune, "kolkata":kolkata, "Chennai":Chennai}

for key,value in cities.items():

    for person in value:
        print(person)
        tweetCriteria = got.manager.TweetCriteria().setUsername(person) \
            .setSince("2019-11-15") \
            .setUntil("2020-05-15")

        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        # for tweet in tweets:
        #     print(tweet.geo)
        users_locs = [[tweet.username, tweet.geo, tweet.text, tweet.date.strftime("%d %b, %Y"),tweet.date.strftime("%H:%M")] for tweet in tweets]
        tweet_text = pd.DataFrame(data=users_locs,
                                  columns=['user', "location", "tweet","tweet_day","tweet_timing"])
        name=str(key) +"/"+person+".csv"

        tweet_text.to_csv(name)

