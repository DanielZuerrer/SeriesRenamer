import json, requests
import logging as log
log.basicConfig(level=log.ERROR)

baseURL = 'http://api.tvmaze.com'

def getShowID(showTitle):
    response = requests.get(baseURL + '/search/shows?q=' + showTitle)
    data = json.loads(response.text)
    return data[0]["show"]["id"]

def getEpisodeTitle(showTitle, season, episode):
    showID = getShowID(showTitle)
    response = requests.get(baseURL + '/shows/{}/episodebynumber?season={}&number={}'.format(showID,season,episode))
    data = json.loads(response.text)
    episodeTitle = data["name"]
    return episodeTitle