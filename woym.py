
print 'Welcome TO Facebook WOYM Simplified By:Rasmoat'

import facebook

def main():
  graph = facebook.GraphAPI(access_token='put your access token', version='2.1')
  # Get access token from https://developers.facebook.com/tools/explorer/
  cfg = {
    "page_id"      : "your user id", 
    "access_token" : 'input access token again'
    }

  api = get_api(cfg)
  #Message and user select
  
  msg =raw_input("Please Write Your Post Here: ")
  graph.put_object("me", "feed", message=msg)

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  
if __name__ == "__main__":
main()
