# Hand_Gesture_Recognition
In this project we Have Implemented Hand Gesture Recognition using the packages [opencv](https://pypi.org/project/opencv-python/) and [mediapipe](https://pypi.org/project/mediapipe/)  
Used Hand Model Detection Module and made two hand gestures controller
   1. Volume Controller : 
  In this, we have have made proper and accurate hand gesture.
  The volume increases and lowers in accordance with adjustments made to the tips of the thumb and index fingers.
  It not only shows on the us on the running window, but we can have a look on change of volume level on the device. 
  The Python Core Audio Windows Library, or [Pycaw package](https://github.com/AndreMiras/pycaw), which we utilised, is compatible with Python 2 and Python 3.


   2. Virtual Keyboard Controller : 
  In this, we have made Virtual Keyboard interface which can be operated by colliding index and middle finger together. 
  After doing this, the required text is typed simultaneously.
  With this virtual keyboard, you may type anywhere, just like we type on a notepad.
  For the virtual keyboard to function in any program, we utilised the [pynput package](https://github.com/moses-palmer/pynput).
  

# Requirements
  1. [GitHub Id](https://github.com/)
  2. Python Setup
  3. IDE   (eg. VScode,Pycharm)

# Working On Project
Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

Replace ( ) with given message

  1. Fork this Project In Your GitHub Account.
  2. Pull the Project In Your Local Machine
```
  git clone (URL OF the Project from your forked Repo)
```
  3. Suggested to create a seperate Python Environment and activate it .
```
py -m venv (Environment Name)
```
  4. Install Required packages/library from the requirements.txt
```
pip install -r requirements.txt
```
  5. Do necessary changes in the project.
  6. Then add your changes to staging area
```
  git add (file/folder name)
```
  6. Then commit your changes
```
git commit -m "(Your Commit message)"
```
  7. Then push your project
```
git push (Remote Name) (Branch Name)
```
```
For Eg : git push origin master
```
  8. Create pull Request(PR) From GitHub
  9. Now Wait to Get your PR accepted
  10. Done 😊


# Demo
# Volume Controller
It can be controll using index finger and thumb finger to controll volume and to lock the volume pinky finger should be down
1. **Image when volume is mute , when volume is at 0% then there will be red dot for indication**
  ![](/image/img1.png)


2. **Image when volume is at x level , when volume is at x % then there will be yellow dot for indication**
  ![](/image/img3.png)

3. **Image when volume is at full , when volume is at 100 % then there will be green dot for indication**
  ![](/image/img2.png)

# Virtual Keyboard Controller
It can be controll using Index finger when distance between index and middle finger will be less than 30 then text will be typed
1. **When nothing is typed using these Controller**
  ![](/image/img4.png)

2. **When Context is typed using these Controller**
  ![](/image/img5.png)

# Issues
  Feel free to submit issues and enhancement requests.

# Contributor 
[Me](https://github.com/rapid-killer-9) and my buddy [Vedika](https://github.com/evil-queen28) had collaboratively completed this project, and we are still eager to add new features anytime we come up with the addition concept.

# Licences
  [MIT LICENSE](LICENSE)
