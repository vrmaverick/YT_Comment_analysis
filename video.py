import pandas as pd
import requests
from textblob import TextBlob

def get_comment_sentiment(comment):
    analysis = TextBlob(comment)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"
    
def initialize(video_id,api_key,max_result):
  video_info_url = f"https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id={video_id}&key={api_key}"
  video_info_response = requests.get(video_info_url)
  video_info_data = video_info_response.json()
  comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={api_key}&videoId={video_id}&part=snippet&maxResults={max_result}"
  comments_response = requests.get(comments_url)
  comments_data = comments_response.json()
  df = pd.DataFrame(comments_data['items'])
  df1 = pd.DataFrame(df['snippet'])
  txt=""
  comments = []
  for i in range(0,10):
      df2 = pd.DataFrame(df['snippet'][i])
      txt = df2['topLevelComment']['snippet']['textOriginal']
      comments.append(txt)


  comment_list = []
  sentiment_list = []
  for comment in comments:
      sentiment = get_comment_sentiment(comment)
      comment_list.append(comment)
      sentiment_list.append(sentiment)
      print(f"{comment} : {sentiment}")
  sentiment_df = pd.DataFrame({"Comments": comment_list, "Sentiment": sentiment_list})
  return sentiment_df