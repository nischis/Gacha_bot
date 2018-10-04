import tweepy
import api_setting

def auth():

  CK = api_setting.CONSUMER_KEY
  CS = api_setting.CONSUMER_SECRET
  AT = api_setting.ACCESS_TOKEN
  AS = api_setting.ACCESS_TOKEN_SECRET

  auth = tweepy.OAuthHandler(CK, CS)
  auth.set_access_token(AT, AS)

  return auth


