# Smart-Media-Player

********************
***🧔:- Ayush Jaiswal<br>
📧:- ayushhjaiswal@gmail.com***
********************

**Here we create a smart media player using vlc and cv library of python which plays a video only when there is a viewer present in front of the screen.**
### Understanding the files of the code:-

#### Facedetect:-
* This python file contains the code for face detection using computer vision or cv library.
* It returns the length of 'faces' list which contains the number of faces detected.

#### Smart Media Player (main):-
* The first block of code is the face detection method which is later referenced before playing or pausing the video.
* The second block is controlling the flow of the video.
* First we check if a viewer is present or not by calling 'facedetect' function and play the video once presence of viewer is made sure.
* Then we thereby control the flow of video according to the suitable comments mentioned alongside in the code.
* We also include a waiting variable 'x' which starts incrementing once the viewer goes absent which in turn stops the media player.
* If the viewer returns to the screen before the waiting variable 'x' hits its pre-defined limit then the video continues and 'x' is again set to 0.
* The 'keyboard' library is used to check if the viewer wants to exit the player in middle of its course.
* We bind 'q' key to quit the player by using the 'is_pressed()' function of the 'keyboard' library.

### Additional comments:-
* This is just the basic code and concept that I have tried to implement here and will be delighted if someone links it to UI or just give their ideas to improve this code and logic overall.
* This is a public repository and therefore anyone can apply for pull requests if one has better ideas.
* Also, this code is actually a little slow since it periodically calls the 'facedetect' function, so if a viewer leaves the screen as soon as the 'facedetect' function call is made then it takes around 4-5 secs before it re-calls the 'facedetect' function and finds that there is no viewer and pauses the video, which is same when a viewer returns to the screen just after the 'facedetect' function call was made.
* If someone has a solution to the above issue kindly mail me at the given email-id.

********************
***🧔:- Ayush Jaiswal<br>
📧:- ayushhjaiswal@gmail.com***
********************
