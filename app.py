"""# API client library
from flask import Flask, jsonify

import googleapiclient.discovery
import requests
# API information
app=Flask(__name__)
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'AIzaSyDZnpOJ74ug59XBUvjgg_xcpWDL-6-ZjjA'
# API client
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY
        )
# Request body
file_path = "C:\\Users\\10140783\\Documents\\TestAPI\\RealtimeComments.csv"
@app.route("/")
def home():
   
    request = youtube.commentThreads().list(
      part="snippet",
      videoId='trsHTKqmZOk',
      maxResults=1000
      )
# Request execution
    output = request.execute()
    comments=[]
    for txt in output["items"]:
      comment=txt["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
      comments.append(comment)

    try:
      with open(file_path,"w") as f :
        f.write(str(comments))
       
      print(f"Successfully stored the response to the file {file_path}")

    except requests.exceptions.RequestException as e:
         print(f"An error occurred during the request: {e}")
    except IOError as e:
         print(f"An error occurred while writing to the file: {e}")    

    return comments

if __name__=='__main__':
   app.run()"""

from flask import Flask, jsonify
import googleapiclient.discovery
from googleapiclient.errors import HttpError
import csv

app = Flask(__name__)

# YouTube API config
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyDZnpOJ74ug59XBUvjgg_xcpWDL-6-ZjjA"

youtube = googleapiclient.discovery.build(
    api_service_name,
    api_version,
    developerKey=DEVELOPER_KEY
)

file_path = r"C:\Users\10140783\Documents\TestAPI\RealtimeComments.csv"

@app.route("/")
def home():
    try:
        yt_request = youtube.commentThreads().list(
            part="snippet",
            videoId="trsHTKqmZOk",
            maxResults=100
        )

        output = yt_request.execute()

        comments = [
            item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            for item in output.get("items", [])
        ]

        # Write proper CSV
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["comment"])
            for c in comments:
                writer.writerow([c])

        return jsonify({
            "count": len(comments),
            "comments": comments
        })

    except HttpError as e:
        return jsonify({"error": str(e)}), 500

    except IOError as e:
        return jsonify({"error": "File write failed", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
