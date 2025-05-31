from video import initialize
from model import predict

if __name__ == '__main__':
    
    video_id = input("Enter id of yt video you wish to analyze 50 comments : ")
    max_result = 50  # Number of comments to retrieve (maximum 50 per API request)
    api_key ="AIzaSyC_4xZTiNuz1O-Qu5kYnlg82riP30KRIxY"  # Your YouTube API key
    df = initialize(video_id,api_key,max_result)

    
    df = initialize(video_id,api_key,max_result)  # Initialize the video module
    # df2 = df.drop(["Sentiment"],inplace=False)
    predict(df)