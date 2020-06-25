import tweepy
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Hello World").sheet1
row = ["Text","Geolocation","Coordinates","Location","TimeStamp","Username","Tweet Id","Media Type","Media Url1","Media Url2","Extended Media type","Extended Media Url","Hashtag1","Hashtag2","Hashtag3","Website1","Website2","Mention1","Mention2","Mention3","Media Url3","Media Url4"]
sheet.insert_row(row)
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        text = status.text
        if text.startswith("RT @") == True:
            return
        loc = status.user.location
        coords = status.coordinates
        geo = status.geo
        name = status.user.screen_name
        id_str = status.id_str
        created = status.created_at
        created = json.dumps(created, indent=4, sort_keys=True, default=str)
        if(status.truncated):
            text = status.extended_tweet["full_text"]
            try:
                hash = status.extended_tweet["entities"]["hashtags"][0]["text"]
            except:
                hash = None
            try:
                hash1 = status.extended_tweet["entities"]["hashtags"][1]["text"]
            except:
                hash1 = None
            try:
                hash2 = status.extended_tweet["entities"]["hashtags"][2]["text"]
            except:
                hash2 = None
            try:
                website = status.extended_tweet["entities"]["urls"][0]["expanded_url"]
            except:
                website = None
            try:
                website1 = status.extended_tweet["entities"]["urls"][1]["expanded_url"]
            except:
                website1 = None
            try:
                mention = status.extended_tweet["entities"]["user_mentions"][0]["screen_name"]
            except:
                mention = None
            try:
                mention1 = status.extended_tweet["entities"]["user_mentions"][1]["screen_name"]
            except:
                mention1 = None
            try:
                mention2 = status.extended_tweet["entities"]["user_mentions"][2]["screen_name"]
            except:
                mention2 = None
            try:
                media_url =  status.extended_tweet["entities"]["media"][0]["media_url"]
            except:
                media_url = None
            try:
                media_url1 =  status.extended_tweet["entities"]["media"][1]["media_url"]
            except:
                media_url1 = None
            try:
                media_url2 =  status.extended_tweet["entities"]["media"][2]["media_url"]
            except:
                media_url2 = None
            try:
                media_url3 =  status.extended_tweet["entities"]["media"][3]["media_url"]
            except:
                media_url3 = None
            try:
                m_type = status.extended_tweet["entities"]["media"][0]["type"]
            except:
                m_type = None
            try:
                mediae_url = status.extended_tweet["extended_entities"]["media"][0]["video_info"]["variants"][0]["url"]
            except:
                mediae_url = None
            try:
                me_type = status.extended_tweet["extended_entities"]["media"][0]["type"]
            except:
                me_type = None
            if geo is not None:
                geo = json.dumps(geo)
            if coords is not None:
                coords = json.dumps(coords)
            if hash is not None:
                hash = json.dumps(hash)
            if hash1 is not None:
                hash1 = json.dumps(hash1)
            if hash2 is not None:
                hash2 = json.dumps(hash2)
            if website is not None:
                website = json.dumps(website)
            if website1 is not None:
                website1 = json.dumps(website1)
            if mention is not None:
                mention = json.dumps(mention)
            if mention1 is not None:
                mention1 = json.dumps(mention1)
            if mention2 is not None:
                mention2 = json.dumps(mention2)
            if media_url is not None:
                media_url = json.dumps(media_url)
            if media_url1 is not None:
                media_url1 = json.dumps(media_url1)
            if media_url2 is not None:
                media_url2 = json.dumps(media_url2)
            if media_url3 is not None:
                media_url3 = json.dumps(media_url3)
            if m_type is not None:
                m_type = json.dumps(m_type)
            if mediae_url is not None:
                mediae_url = json.dumps(mediae_url)
            if me_type is not None:
                me_type = json.dumps(me_type)
        else:
            try:
                hash = status.entities["hashtags"][0]["text"]
            except:
                hash = None
            try:
                hash1 = status.entities["hashtags"][1]["text"]
            except:
                hash1 = None
            try:
                hash2 = status.entities["hashtags"][2]["text"]
            except:
                hash2 = None
            try:
                website = status.entities["urls"][0]["expanded_url"]

            except:
                website = None
            try:
                website1 = status.entities["urls"][1]["expanded_url"]
            except:
                website1 = None
            try:
                mention = status.entities["user_mentions"][0]["screen_name"]
            except:
                mention = None
            try:
                mention1 = status.entities["user_mentions"][1]["screen_name"]
            except:
                mention1 = None
            try:
                mention2 = status.entities["user_mentions"][2]["screen_name"]
            except:
                mention2 = None
            try:
                media_url =  status.entities["media"][0]["media_url"]
            except:
                media_url = None
            try:
                media_url1 =  status.entities["media"][1]["media_url"]
            except:
                media_url1 = None
            try:
                media_url2 =  status.entities["media"][2]["media_url"]
            except:
                media_url2 = None
            try:
                media_url3 =  status.entities["media"][3]["media_url"]
            except:
                media_url3 = None
            try:
                m_type = status.entities["media"][0]["type"]
            except:
                m_type = None
            try:
                mediae_url = status.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
            except:
                mediae_url = None
            try:
                me_type = status.extended_entities["media"][0]["type"]
            except:
                me_type = None
            if geo is not None:
                geo = json.dumps(geo)
            if coords is not None:
                coords = json.dumps(coords)
            if hash is not None:
                hash = json.dumps(hash)
            if hash1 is not None:
                hash1 = json.dumps(hash1)
            if hash2 is not None:
                hash2 = json.dumps(hash2)
            if website is not None:
                website = json.dumps(website)
            if website1 is not None:
                website1 = json.dumps(website1)
            if mention is not None:
                mention = json.dumps(mention)
            if mention1 is not None:
                mention1 = json.dumps(mention1)
            if mention2 is not None:
                mention2 = json.dumps(mention2)
            if media_url is not None:
                media_url = json.dumps(media_url)
            if media_url1 is not None:
                media_url1 = json.dumps(media_url1)
            if media_url2 is not None:
                media_url2 = json.dumps(media_url2)
            if media_url3 is not None:
                media_url3 = json.dumps(media_url3)
            if m_type is not None:
                m_type = json.dumps(m_type)
            if mediae_url is not None:
                mediae_url = json.dumps(mediae_url)
            if me_type is not None:
                me_type = json.dumps(me_type)
        data = [text,geo,coords,loc,created,name,id_str,m_type,media_url,media_url1,me_type,mediae_url,hash,hash1,hash2,website,website1,mention,mention1,mention2,media_url2,media_url3]
        sheet.insert_row(data)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

auth = tweepy.OAuthHandler("K8wEhUHEhr9TaL8B91Yo6kLYo", "bIWSDSqH06YYKIfC3uc2UAEGNbA8KhjihytBzlL3Bko20uwmCA")
auth.set_access_token("1256234655172431872-oO3d96pRfLfRLUljguv9jN9sO8hjT7", "1C4sxjAwVXshhnGmnC8hON21fxyiWyBTjumsyxVAthRn3")
api = tweepy.API(auth)
tracklist = ['#DilBecharaOnBigScreen']
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track = tracklist)
