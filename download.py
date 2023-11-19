from flask import Flask, request, render_template
from pytube import YouTube
from pytube.cli import on_progress

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") # this function renders the HTML file as a web page

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url") # this line gets the URL from the input element
    youtube_object = YouTube(url, on_progress_callback=on_progress) # this line creates a YouTube object with the URL and a progress callback function
    stream_object = youtube_object.streams.get_highest_resolution() # this line gets the highest resolution stream from the YouTube object
    try:
        stream_object.download(r'C:\Users\Krupa R M\Desktop\Linkedin cyber') # this line downloads the stream to the specified folder
        return "Download completed successfully" # this line returns a success message
    except Exception as e:
        return f"An error has occurred: {e}" # this line returns an error message

if __name__ == "__main__":
    app.run(debug=True) # this line runs the app in debug mode
