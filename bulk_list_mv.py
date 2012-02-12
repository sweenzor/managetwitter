import tweepy
import oauth

"""Script to move everyone you're following onto a list"""

api = oauth.create()

# pull list of friends
friends_list = api.friends_ids()
num_of_friends = len(friends_list)

# figure out how many lists you need
print 'number of friends: ', num_of_friends
num_of_lists = int(round(num_of_friends / 400.0))
print 'number of lists needed: ', num_of_lists

# init
root_name = 'Purge'
lists = [] #lol

# create enough twitter lists to hold all friends
for i in range(num_of_lists):
    lists.append(api.create_list(name=root_name+str(i), mode='private'))

# split friend list into a number of smaller lists
buckets_o_friends = [friends_list[i:i+400] for i in range(0, len(friends_list), 400)]

# print the counts of the sub-lists
for l in buckets_o_friends:
    print len(l)

fails = []
for i,friend_list in enumerate(buckets_o_friends):

    for friend in friend_list:

        try:
            api.add_list_member(lists[i].id, friend)
            print '%i added to %s' % (friend, lists[i].id)

        except:
            print '%i failed' % friend
            fails.append(friend)

print 'errors: ', fails
