# lab3task2
# All created operations take place in the main.py function. There I described the stages of the passage into the json file.
# The hidden.py file contains a function that returns the user's keys and tokens from the developer account.
# The oauth.py module handles user authentication via the API
# The twitter2.py module contains a function that returns .json information about friends on Twitter.
# The program is launched from the main.py module
# Example of work after module is run:
# +++++++++++++++
# Retrieving https://api.twitter.com/1.1/friends/list.json?oauth_consumer_key=ca5oZNU2YPkRHWkQmSt85TOoA&oauth_timestamp=1614108260&oauth_nonce=87816539&oauth_version=1.0&screen_name=%40AKernytska&count=5&oauth_token=1362494612896698372-Nyn0Bxc2CUKuvnIUOwTSQK4565QMWB&oauth_signature_method=HMAC-SHA1&oauth_signature=Mj2CbDw2rkBIPL9FyiuLpKK%2FFjA%3D
# Remaining 12
# Info:
# --- users: [...]
# --- next_cursor: 0
# --- next_cursor_str: 0
# --- previous_cursor: 0
# --- previous_cursor_str: 0
# --- total_count: None
# 
# Inner info:
# 1. users
# 
# Enter: 1
# We have 2 data blocks inside.
# 
# Pick which to show: 2
# Info:
# --- id: 1320076697421647872
# --- id_str: 1320076697421647872
# --- name: yushka
# --- screen_name: Yushka19
# --- location: Україна
# --- description: 
# --- url: None
# --- entities: {...}
# --- protected: False
# --- followers_count: 4
# --- friends_count: 14
# --- listed_count: 0
# --- created_at: Sat Oct 24 18:56:46 +0000 2020
# --- favourites_count: 2
# --- utc_offset: None
# --- time_zone: None
# --- geo_enabled: False
# --- verified: False
# --- statuses_count: 2
# --- lang: None
# --- status: {...}
# --- contributors_enabled: False
# --- is_translator: False
# --- is_translation_enabled: False
# --- profile_background_color: F5F8FA
# --- profile_background_image_url: None
# --- profile_background_image_url_https: None
# --- profile_background_tile: False
# --- profile_image_url: http://pbs.twimg.com/profile_images/1320419824867119104/7Sa4-Dht_normal.jpg
# --- profile_image_url_https: https://pbs.twimg.com/profile_images/1320419824867119104/7Sa4-Dht_normal.jpg
# --- profile_banner_url: https://pbs.twimg.com/profile_banners/1320076697421647872/1603647278
# --- profile_link_color: 1DA1F2
# --- profile_sidebar_border_color: C0DEED
# --- profile_sidebar_fill_color: DDEEF6
# --- profile_text_color: 333333
# --- profile_use_background_image: True
# --- has_extended_profile: True
# --- default_profile: True
# --- default_profile_image: False
# --- following: True
# --- live_following: False
# --- follow_request_sent: False
# --- notifications: False
# --- muting: False
# --- blocking: False
# --- blocked_by: False
# --- translator_type: none
# 
# Inner info:
# 1. entities
# 2. status
# 
# Enter: 1
# Info:
# --- description: {...}
# 
# Inner info:
# 1. description
# 
# Enter: 1
# Info:
# --- urls: [...]
# 
# Inner info:
# 1. urls
# 
# Enter: 1
# Empty.
# Json file is ended.
