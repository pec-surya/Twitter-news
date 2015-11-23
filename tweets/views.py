from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template import RequestContext
from tweets.models import NewsChannel

from datetime import datetime
from twitter import *

# Create your views here.


def index(request):
	news = NewsChannel.objects.all()
	return render_to_response('tweets/index.html', {'news' : news})


def authenticate():
    token = "1335829488-wzLHStB2RYDgY9VAXmB2A8OGUlFHsSbLhm6AFcZ"      # info from the Twitter site.
    token_key = "T8Dz2gt3jad1AEyROp7zIKlstd4ZQMfntaQb2RkWehcio"
    con_secret = "nkSgT39MctaDCzqoLKrzhVuno"
    con_secret_key = "YaCmgAYxPxLk04gf4tXAttzcVT4eyhSkPeDqCLdmVntGA05iLm"

    twitter_access = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))   # oauth using creds

    return twitter_access

def getTweets(request, name):
	auth = authenticate()
	lastTweets = auth.statuses.user_timeline(screen_name=name, count=10)

	tweetsList = []
	for t in lastTweets:
		tweetsList.append(t["text"])

	return render_to_response('tweets/viewTweets.html', {'name' : name, 'tweets' : tweetsList})