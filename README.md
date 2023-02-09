# spotify-recommendation-system

Description:

Our package is a locally hosted webapp that leverages the strength of the Spotify API and the d3 Javascript plugin to provide a unique music recommendation experience. Users will be able to login to Spotify as a group and view the attributes of their music taste. Once everyone is authenticated, users can receive a recommendation that is tailor-made to the overall tastes of the group, ensuring that everyone can enjoy the playlist together.

We utilized Python’s Flask module to host our app directly on a user’s computer. User’s will be able to see their music taste visualized on the webpage using d3 visualizations. The ability to compare tastes and find music that the whole group can enjoy is what makes Groupify unique!

Installation:

To install our package, open requirements.txt and ensure that all needed python modules have been installed.

Execution:
To run our package, navigate to the root folder, and execute “python run.py” from the command line or terminal. 
Then, navigate to http://localhost:5000/ using a Firefox or Chrome browser. 
Click on the “Visualizations” tab, and wait until the page finishes loading. This might take around 20 seconds.  
You can see the distribution of the clusters broken down by two features on the first plot. Each dot represents a song. Hover over a dot to see the song name, artist name, and its values for the two features selected. 
You can select another pair of features through the dropdown list on the top.  
Click on the "Authenticate" button to authenticate your group's Spotify accounts. You will be redirected to a Spotify login page and you will need to login with your Spotify credentials. You will need to authenticate your group’s accounts one by one.
Click on the "Visualize and Recommend" button after you are done with authentication. This will visualize your group's songs and generate recommendations based on your group's listened songs. The second graph on the page will show the distribution of the features of each user’s songs. The third graph on the page will show the distribution of the recommended songs for the user group. You will see the list of recommended songs and their Spotify link at the bottom of the page. 
If you wish to reset all users’ data and recommended songs, click on the “Reset” button. 
Note that we currently only support a group of at most 5 individuals. If you input data for more than 5 users, we will only consider the songs for the first 5 users for visualization and generating recommendations.

