import feedparser
import webbrowser

data = {}
feed_url = 'https://help.zscaler.com/rss-feed/zscaler-client-connector/client-connector-app-release-summary-2021/Windows'
#feed_url = 'https://help.zscaler.com/rss-feed/zscaler-client-connector/client-connector-app-release-summary-2021/macOS'
feed = feedparser.parse(feed_url)
for i in range(len(feed.entries)):
    data[feed.entries[i].version] = feed.entries[i].link

version = max(data)
version_link = data[version]
webbrowser.open(version_link)
