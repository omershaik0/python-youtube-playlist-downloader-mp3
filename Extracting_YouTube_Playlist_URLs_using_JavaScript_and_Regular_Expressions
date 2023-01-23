# Extracting YouTube Playlist URLs using JavaScript and Regular Expressions

1. Go to the page of a YouTube playlist.
2. Open the browser's developer tools (using the "Inspect" option) and navigate to the console.
3. In the console, run the following script to automatically scroll down the page to load more videos in the playlist. 
`var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);` 
4. Once the desired number of videos have been loaded, stop the script by running the following commands:
`window.clearInterval(scroll); console.clear();`
5. Next, extract all the URLs of the videos on the page by running the following script:
`urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title"){console.log(v.href)}});`
6. The extracted URLs will be logged to the console.
7. Copy the output from the console and paste it into a text editor like Sublime Text.
8. Use the following regular expression pattern to filter out the URLs and save them to a text file:
`https://www.youtube.com/watch\?v=.+`
Note: The above steps are assuming that you are able to access the browser's developer tools, and use the javascript in the console.
