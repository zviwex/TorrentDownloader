import os 
import urllib3
import sys
from pprint import pprint
import eztvit
import povies

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download_movie(name, quality=720):
    p = povies.Povies() 
    l_movies = p.search(name)
    p.download(l_movies[0]['id'])

def download_episode(series, season, episode):
    all_episotes = eztvit.EztvIt().get_episodes(series)
    episode = all_episotes[season][episode]
    episode = sorted(episode, key=lambda k: k['size_mb'])[-1]
    print("Downloading: {}, Size: {}".format(episode["release"], episode["size_mb"]))
    magnet = episode['download']['magnet']
    os.startfile(magnet)

  
def download_season(series, season):
    all_episotes = eztvit.EztvIt().get_episodes(series)
    season = all_episotes[season]
    for key, value in season.iteritems():
        episode = sorted(value, key=lambda k: k['size_mb'])[-1]
        print("Downloading: {}, Size: {}".format(episode["release"], episode["size_mb"]))
        magnet = episode['download']['magnet']
        os.startfile(magnet)

  
def download_series(series):
    all_episotes = eztvit.EztvIt().get_episodes(series)
    for key, value in all_episotes.iteritems():
        season = all_episotes[key]
        for key, value in season.iteritems():
            episode = sorted(value, key=lambda k: k['size_mb'])[-1]
            print("Downloading: {}, Size: {}".format(episode["release"], episode["size_mb"]))
            magnet = episode['download']['magnet']
            os.startfile(magnet)



def main():
    if len(sys.argv) < 3:
        print "Usage:"
        print "{} m <movie name> - for movies"
        print "{} e <tvshow name> <series number> <episode number> - for episodes"
        return

    if sys.argv[1][0] == "m":
        download_movie(sys.argv[2])
    else:
        download_episode(sys.argv[2].strip(), int(sys.argv[3]), int(sys.argv[4]))

main()