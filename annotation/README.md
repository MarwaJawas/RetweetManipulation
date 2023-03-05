# The labeled process is performed based on two criteria.
First, categorizing the retweeter groups based on their behaviors in retweeting in hashtag. If the retweeter group is retweeting a large number of retweets,
the group is labeled as malicious. This feature can be measured by computing
weighted degree from retweeter graph. When the weighted degrees between
retweeters in group are high, this evidence to malicious retweeting behavior
among them.\n
Second, categorizing the retweeter groups by looking at the content of the
retweets. Twitter rules and policies were used as a reference for labeling process [8]. The group is labeled as malicious if their tweets content shows one of
the following:\n
• Multiple posts with similar promotions or similar tweet content.
• Their tweets’ content composite from text, hashtag, mention, URL, and
image.
• Their tweets contains similar URL to drive traffic to websites.
• Their tweets contains mentions of similar accounts.
