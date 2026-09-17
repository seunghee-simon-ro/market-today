import feedparser
import pandas as pd


RSS_URL = "https://www.cnbc.com/id/100003114/device/rss/rss.html"


def categorize_news(title):
    title_lower = title.lower()

    if any(
        keyword in title_lower
        for keyword in [
            "fed",
            "interest rate",
            "inflation",
            "central bank",
            "bank of england",
            "rate hike",
            "rate cut",
            "yield"
        ]
    ):
        return "Interest Rates & Economy"

    elif any(
        keyword in title_lower
        for keyword in [
            "oil",
            "crude",
            "gold",
            "copper",
            "iron ore",
            "commodity",
            "fuel"
        ]
    ):
        return "Commodities"

    elif any(
        keyword in title_lower
        for keyword in [
            "ai",
            "artificial intelligence",
            "openai",
            "technology",
            "tech",
            "data center",
            "hyperscaler"
        ]
    ):
        return "Technology"

    elif any(
        keyword in title_lower
        for keyword in [
            "japan",
            "china",
            "korea",
            "asia",
            "australia",
            "india",
            "yen",
            "yuan"
        ]
    ):
        return "Asia & Australia"

    elif any(
        keyword in title_lower
        for keyword in [
            "stock",
            "stocks",
            "market",
            "shares",
            "nasdaq",
            "s&p 500",
            "dow"
        ]
    ):
        return "Markets"

    else:
        return "Global Economy"


feed = feedparser.parse(RSS_URL)


results = []

for article in feed.entries[:20]:

    title = article.get("title", "")

    results.append({
        "Title": title,
        "Category": categorize_news(title),
        "Published": article.get("published", ""),
        "Link": article.get("link", "")
    })


news_df = pd.DataFrame(results)


print("\n==============================")
print("        MARKET NEWS")
print("==============================\n")

print(news_df.to_string(index=False))


news_df.to_csv(
    "data/news_snapshot.csv",
    index=False
)


print("\nSaved:")
print("data/news_snapshot.csv")