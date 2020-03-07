from urllib.request import urlopen
import json

def print_author():
    info = '''
    Author: Jakub Jonczyk
    Date:   7.11.2019
    '''
    print(info)

#get last.fm API key
def get_key():
    file = open("lastfm_key.txt")
    key = file.readline()
    file.close()
    return key

def get_user():
    user = input("type Your last.fm username: ")
    return user

def weekly_album_chart(user, key, n):
    user = username
    key = get_key()
    with urlopen(f"http://ws.audioscrobbler.com/2.0?method=user.getweeklyalbumchart&user={user}&api_key={key}&format=json") as file:
        try:
            text = file.read().decode("utf-8")
            object = json.loads(text)["weeklyalbumchart"]["album"]
            rank =  object[n]["@attr"]["rank"]
            artist = object[n]["artist"]["#text"]
            album = object[n]["name"]
            playcount = object[n]["playcount"]
            print(f"{rank}: {album} by {artist} | played {playcount} times")
        except:
            raise ConnectionError

def print_wait_screen():
    print(f"\nI've just asked last.fm for {username}'s favourite albums! \nAPI key: {get_key()}\n")
    print("   Your weekly top scrobbled are:")

username = get_user()
counter = 0;
print_wait_screen()
for x in range(10):
    weekly_album_chart(username, get_key(), x)
print_author()