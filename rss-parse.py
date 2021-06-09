import os
import feedparser
print("Test")

def RSSParser(rss_url):
    return feedparser.parse(rss_url)

RSSParser("https://help.zscaler.com/rss-feed/zscaler-client-connector/client-connector-app-release-summary-2021/Windows")


