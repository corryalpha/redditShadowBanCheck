import requests
import random
import time


def isShadowbanned(user):
    while True:

        agent = ""

        for x in range(5):
            agent = str(agent + str(random.randint(0, 9)))

        r = requests.get(f"https://reddit.com/u/{user}.json", headers={"User-Agent":agent})

        if r.status_code == 404:
            return True
        elif r.status_code == 200:
            return False
        elif r.status_code == 409:
            time.sleep(3)
            continue