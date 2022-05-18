import praw
import trafficconfig
import time
from time import localtime, timezone
from datetime import datetime, date
import json





try:
    reddit = praw.Reddit(
                        username = trafficconfig.username,
                        password = trafficconfig.password,
                        client_id = trafficconfig.client_id,
                        client_secret = trafficconfig.client_secret,
                        user_agent= trafficconfig.user_agent)

except Exception as e:
        print("You broke something.")
        print(e)    

print(f"Logged in as: {reddit.user.me()}")


tier_one_subs = trafficconfig.tier_one_subs
currentSysTime = time.localtime()
print(time.strftime("%a, %B %d, %Y | %H:%M:%S", currentSysTime))

for subreddit in reddit.redditor("ghostofbearbryant").moderated():
    try:
        sub_name = subreddit.display_name
        stats = reddit.subreddit(sub_name).traffic()
        daily_data = stats["day"]
        previous_day = daily_data[2]
        previous_day_stats = (  previous_day[0], 
                                previous_day[1], 
                                previous_day[2],
                                previous_day[3]
                        )

        (time_created, pageviews, uniques, subscriber_count) = previous_day_stats
        time_stamp = datetime.fromtimestamp(int(time_created)).strftime("%a, %b %d, %Y")
        submit_sub = "ghostofbearbryant"
        title = f"Traffic spike in r/{sub_name}. {subscriber_count} subscribers joined  on {time_stamp}"
        selftext = f"Subreddit: [r/{sub_name}](http://reddit.com/r/{sub_name}/about/traffic)\n\nSubscribers: {subscriber_count}\n\nWhen: {time_stamp}.\n\nPageviews: {pageviews}\n\nUnique visits: {uniques}"
        reddit.validate_on_submit = True

        # If you want to print and evaluate the raw traffic data, uncomment the following two lines.
        #raw_stats = json.dumps(stats, indent=4)
        #print(raw_stats)

        if sub_name not in tier_one_subs:
            if subscriber_count >= 250:
                print(f"{subscriber_count} number of subscribers in {sub_name}")
                reddit.subreddit(submit_sub).submit(title, selftext)
        else:
            if subscriber_count >= 500:
                print(f"{subscriber_count} number of subscribers in {sub_name}")
                reddit.subreddit(submit_sub).submit(title, selftext)

    except Exception as e:
        print("You broke something.")
        print(e)
