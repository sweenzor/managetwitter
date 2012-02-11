import tweepy
import oauth

api = oauth.create()

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

print len(api.friends_ids())

