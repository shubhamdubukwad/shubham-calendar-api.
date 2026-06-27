import feedparser
import urllib.parse
import json
from datetime import datetime

def fetch_and_save():
    search_query = "महाराष्ट्र सुट्टी जाहीर" 
    encoded_query = urllib.parse.quote(search_query)
    news_url = f"https://news.google.com/rss/search?q={encoded_query}&hl=mr&gl=IN&ceid=IN:mr"
    
    feed = feedparser.parse(news_url)
    today_str = datetime.today().strftime('%Y-%m-%d')
    
    holidays_list = [
        {"date": "2026-07-15", "title": "मुसळधार पावसामुळे पुणे जिल्ह्यात सुट्टी"},
        {"date": "2026-09-14", "title": "गणेश चतुर्थी स्थानिक सुट्टी"}
    ]
    
    for entry in feed.entries[:10]:
        title = entry.title
        if any(kw in title for kw in ["सुट्टी", "जिल्हाधिकारी", "शाळा बंद"]):
            clean_title = title.split("-")[0].strip()
            new_entry = {"date": today_str, "title": clean_title}
            if new_entry not in holidays_list:
                holidays_list.append(new_entry)
                
    with open("holidays.json", "w", encoding="utf-8") as f:
        json.dump(holidays_list, f, ensure_ascii=False, indent=2)
    print("✅ JSON फाईल यशस्वीरीत्या अपडेट झाली!")

if __name__ == "__main__":
    fetch_and_save()
