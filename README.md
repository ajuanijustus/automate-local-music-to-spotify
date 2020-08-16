# Automate Local Music Library to Spotify
Automating extraction of metadata from mp3 files in a desired file directory, finding the songs on Spotify and adding all the songs into a Spotify playlist of choice.

## Getting Started
For this project, you will need __Python__ installed on your system.

## Prerequisites
#### Technologies
1. [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
2. [Requests v2.24.0](https://requests.readthedocs.io/en/master/)
3. [eyeD3 v0.9.5](https://eyed3.readthedocs.io/en/latest/)
4. [urllib3 v1.24.3](https://urllib3.readthedocs.io/en/latest/)
#### Tokens/ID
1. Spotify Web API OAuth Token.
2. Spotify Playlist ID.
3. Path to directory.
  
## Local Setup
1. Install the dependencies.
<pre><code>pip install -r requirements.txt
</code></pre>
2. Collect your Spotify User ID, Playlist URI and Oauth Token From Spotify and add it to the env.bat file.
    * To get your Spotify User ID, visit [Spotify Account Overview](https://www.spotify.com/in/account/overview/):
    ![alt text](readme-images/user_id.png)
    * To get your Playlist ID, copy Spotify URI as in the screenshot:
    * To get your Oauth Token, visit this page: [Get Oauth](https://developer.spotify.com/console/post-playlist-tracks/) and click the Get Token button:
