import numpy as np
import random
import datetime

import config

import time
import subprocess

# config list of sites to powershell recognizeable string
server_ls = "$('" + "', '".join([url for url in config.sites]) + "')"

# can call line below successfully -- cannot seem to loop it
# subprocess.call("powershell; ./.venv/Scripts/python3.exe bencode.py {0}".format(server_ls[0]))

while True:
    # subprocess.call("powershell C:/'Program Files (x86)'/NordVPN/NordVPN.exe -c -g 'United States';", shell=True)
    # time.sleep(10)
    for url in config.sites:
        print(url)
        subprocess.call("""
            powershell;
            ./.venv/Scripts/python3.exe bencode.py '{0}';
            echo "successful --- '{0}';
             """.format(url)
            , shell=True)

        time.sleep(20)
    # subprocess.call("""
    #     powershell; 
    #     C:/'Program Files (x86)'/NordVPN/NordVPN.exe -c -g "United States;
    #     for($i=0; $i-le {}.length-1; $i++) {
    #         ./.venv/Scripts/python3.exe bencode.py {}[$i];
    #         };
    #     echo "successful";
    #     Start-Sleep -s 5;""".format(server_ls)
    #     , shell=True)

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