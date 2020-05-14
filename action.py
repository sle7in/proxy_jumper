import numpy as np
import random
import datetime

def submit_form(website):
    """navigate to feature, select radio button, then submit form.
    assume all sites have identical xml content"""
    # ie, request get website (url)
    # select radio button with "Glass Cases" ( or grab button id )
    # submit form
    # determine between submission response: "Thank you, we have already counted your vote." or "Thank you for voting! " to guage votes submitted
    pass








# get time between 1 hour and 2 hours from now
new_time = datetime.datetime.now() + datetime.timedelta(seconds = random.randint(3600, 7200))