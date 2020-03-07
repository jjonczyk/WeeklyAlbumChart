from urllib.request import urlopen
import json

import pdb

def print_author():
    info = '''
    Author:     Jakub Jonczyk
    Created at: 7.11.2019
    '''
    print(info)


def enter_key():
    key = input('Enter your last.fm API key: ')
    print(key)
    return key


#get last.fm API key
def get_key():
    file = open("lastfm_key.txt")
    key = file.readline()
    file.close()
    if key:
        return key
    else:
        key = enter_key()
        return key

def get_user():
    user = input("type Your last.fm username: ")
    return user


def weekly_album_chart(user, key, n):
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

def print_wait_screen(user, key):
    print(f"\nI've just asked last.fm for {user}'s favourite albums! \nAPI key: {key}\n")
    print("   Your weekly top scrobbled are:")


username = get_user()
my_key = get_key()
print_wait_screen(username, my_key)

try:
    for x in range(10):
        weekly_album_chart(username, my_key, x)
except:
    print("Sorry, your data is invalid :(")

print_author()