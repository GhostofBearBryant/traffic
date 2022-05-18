# Traffic.py
Be notified of traffic spikes in subreddits.

Traffic.py is a script that works with Submanager to monitor traffic spikes on your subreddit.  

It's currenly configured to notify is the number of user joins crosses a preset threshold of 500 for tier one subreddits and 250 for tier 2 subreddits. 
It's currently configured to run once per day as a linux cronjob.  The script will check your subreddit list via r/mod once per day.  It has two tiers for defining what constitutes a spike.  For tier one subs, the threshold is 500, for tier 2, it's 250.  You can change these numbers in the script.  You will also need to define what your tier one subs are.  

Note that this script is highly customized for usage on the current subreddit list.
