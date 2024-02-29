import feedparser

nytimes_feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/Health.xml")
reuters_feed = feedparser.parse("https://reutersagency.com/feed/?best-topics=health&post_type=best")
politico_feed = feedparser.parse("https://rss.politico.com/healthcare.xml")

def nytimes():
    
    for entry in nytimes_feed.entries:
        print("<< " + entry.title + " >>")
        print(entry.summary)
        print()


def reuters():

    for entry in reuters_feed.entries:
        print("<< " + entry.title + " >>")
        print(entry.summary.split("[&#8230;]")[0].replace('<p>', '') + "...")
        print()


def politico():

    for entry in politico_feed.entries:
        print("<< " + entry.title + " >>")
        print(entry.summary)
        print()

while True:

    print("what we've got:")
    print("(0) QUIT\n(1) NYTimes\n(2) Reuters\n(3) Politico")
    choice = int(input("what you'll have: "))

    if choice == 1:
        print()
        nytimes()
        continue
    
    elif choice == 2:
        print()
        reuters()
        continue

    elif choice == 3:
        print()
        politico()
        continue
    
    elif choice == 0:
        print("see ya!")
        break
