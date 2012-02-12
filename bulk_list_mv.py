import tweepy
import oauth

api = oauth.create()

friends_list = api.friends_ids()
num_of_friends = len(friends_list)

print 'number of friends: ', num_of_friends
num_of_lists = int(round(num_of_friends / 400.0))
print 'number of lists needed: ', num_of_lists

root_name = 'Purge'
lists = [] #lol

for i in range(num_of_lists):
    lists.append(api.create_list(name=root_name+str(i), mode='private'))

buckets_o_friends = [friends_list[i:i+400] for i in range(0, len(friends_list), 400)]

for l in buckets_o_friends:
    print len(l)

fails = 0
for i,friend_list in enumerate(buckets_o_friends):

    for friend in friend_list:

        try:
            api.add_list_member(lists[i].id, friend)
            print '%i added to %s' % (friend, lists[i].id)

        except:
            print '%i failed' % friend
            fails += 1

print 'error count: ', fails
