# importing the module
import tweepy
import sys, getopt


# personal details
consumer_key ="BI1CIAeXxXmQ6ufUvdzHkpWRh"
consumer_secret ="quPUszNXLuDy1SHtZXjh25pU896zcWpfkA6VyOXksDjaAOrQla"
access_token ="1163343849818853376-sgrhKCY7yVYdR8bJBjOAsmM3xlX34b"
access_token_secret ="4NNA9IuQ5v5AzFEMZ6yPZLnocCxJMgDNx5OgYBUBzbAF8"

# authentication f consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update the status
# api.update_status(status ="Hello Everyone !")

def main(argv):
   message = ''
   imageurl = ''
   try:
      opts, args = getopt.getopt(argv,"hm:i:",["msg=","img="])
   except getopt.GetoptError:
      print 'test.py -m Message -i imageURL'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print '\nPost on twitter usin API in a very simple way using tweepy'
         print 'version 0.01\n'
         print 'You can add Message and image (to be implemented)\n'
         print 'Simple usage: '
         print 'test.py -m Message -i imageURL\n'
         sys.exit()
      elif opt in ("-m", "--message"):
         message = arg
      elif opt in ("-i", "--img"):
         imageurl = arg
   if message:
       print 'Tweet Message: ', message
       api.update_status(status =message)
   if imageurl:
      print 'Image: ', imageurl
      print 'Sorry It is not implemented yet'

if __name__ == "__main__":
   main(sys.argv[1:])


