#!/usr/bin/env python

import routes
import routefs
import twitter
import sys

# Helper functions

# From: http://code.activestate.com/recipes/466341-guaranteed-conversion-to-unicode-or-byte-string/
def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

# Main class
class TwitterRFS(routefs.RouteFS):
    """ Basic Twitter-RouteFS to display tweets from the queried users """
    
    def __init__(self, *args, **kwargs):
        super(TwitterRFS, self).__init__(*args, **kwargs)
        self.twitterapi = twitter.Api()
        self.user_cache = {}
        self.tweet_cache = {}

    def make_map(self):
        m = routes.Mapper()
        m.connect('/', controller='list_users')
        m.connect('/{user}', controller='list_tweets')
        m.connect('/{user}/{id}', controller='get_tweet')
        return m

    def list_users(self, **kwargs):
        """ List known usernames """
        return [user
                for user, tweet in self.user_cache.iteritems()
                if tweet]

    def list_tweets(self, user, **kwargs):
        """ List tweet IDs in within the user's directory """
        if user not in self.user_cache:
            try:
                self.user_cache[user] = self.twitterapi.GetUserTimeline(user)
                for tweet in self.user_cache[user]:
                    self.tweet_cache[tweet.id] = tweet
            except:
                self.user_cache[user] = None
        return [str(tweet.id) for tweet in self.user_cache[user]]

    def get_tweet(self, user, id, **kwargs):
        """ Tweet text displayed as file content"""
        tweettext = safe_str(self.tweet_cache[int(id)].text)+'\n'
        return tweettext
    
if __name__ == '__main__':
    routefs.main(TwitterRFS)
