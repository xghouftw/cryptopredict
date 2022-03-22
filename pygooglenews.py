pip install pygooglenews
pip install pandas
pip install datetime

import pandas as pd
from pygooglenews import GoogleNews
import datetime

gn = GoogleNews()

def get_news(search):
    stories = []
    start_date = datetime.date(2020,2,6)
    end_date = datetime.date(2022,2,6)
    delta = datetime.timedelta(days=1)
    date_list = pd.date_range(start_date, end_date).tolist()

    for date in date_list[:-1]:
        result = gn.search(search, from_=date.strftime('%Y-%m-%d'), to_=(date+delta).strftime('%Y-%m-%d'))
        newsitem = result['entries']

        for item in newsitem:
            story = {
                'title':item.title,
                'link':item.link,
                'published':item.published
            }
            stories.append(story)

    return stories

df = pd.DataFrame(get_news('bitcoin'))

print(df)
