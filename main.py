from urllib.request import urlopen
from urllib.error import HTTPError
import json

USER = 'user'
KEY = 'key'
API_ACCOUNT_URL = "https://www.last.fm/api/account/create"
PATHS = {
    'key': "lastfm_key.txt",
    'user': "username.txt"
}


def print_author():
    info = '''
    Author:     Jakub Jonczyk
    Created at: 7.11.2019
    '''
    print(info)


def type_data(what: str):
    data = None
    while not data:
        data = input(f"It seems you don't have your {what} saved in {PATHS[what]} file. \n"
                     "Please, type it now: ")
    print("Thanks!")
    return data


def get_data(what: str):
    try:
        with open(PATHS[what]) as file:
            key = file.readline()
    except FileNotFoundError:
        print(f"{what} file not found")
        key = type_data(what)
    if key:
        return key
    else:
        print(f"Please, enter the {what} properly")
        get_data(what)


def weekly_album_chart(user, key, n):
    with urlopen(f"http://ws.audioscrobbler.com/2.0?method=user.getweeklyalbumchart&user={user}&api_key={key}&format=json") as file:
        text = file.read().decode("utf-8")
        obj = json.loads(text)["weeklyalbumchart"]["album"]
        rank = obj[n]["@attr"]["rank"]
        artist = obj[n]["artist"]["#text"]
        album = obj[n]["name"]
        playcount = obj[n]["playcount"]
        print(f"{rank}: {album} by {artist} | played {playcount} times")


def print_wait_screen(user):
    print(f"\nI've just asked last.fm for {user}'s favourite albums!")
    print("   Your weekly top scrobbled are:")

# --------------------------------------------
# ---------------- LAUNCH --------------------
# --------------------------------------------


username = get_data(USER)
my_key = get_data(KEY)
print_wait_screen(username)

try:
    for x in range(10):
        weekly_album_chart(username, my_key, x)
except HTTPError:
    print("Your data seems to be invalid - sorry, I have to close the app :(\n"
          f"If you don't have your last.fm API key, visit: {API_ACCOUNT_URL}")

print_author()
