# cse210-06
Final Project

# El Pong Game
Pong was originally released in 1972 by Atari, we decided to recreate our improved version of the game by adding more difficulty to the game.

# Rules
- Player 1 moves with the keyboards “w” up and “s” down.
- Player 2 moves with the keyboards “up” up and “down” down.
- The ball randomly bounces to one side and the player uses a paddle to kick the ball to the other side. Player scores if the opponent does not hit the ball.
- The first to 11 points is declared the winner.
- If the points are tied at 10-10, a player then must strive for a two-point lead to win the game.

# Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```
```
python3 pong 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

# Project Structure

The project files and folders are organized as follows:
```
root                    (project root folder)
+-- pong                (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

# Requirements
- Python 3.8.0
- Raylib Python CFFI 3.7

# Contributors:

## Joseph Perez:
josephemilioperezpilier@gmail.com
- Game mockups [X]
- Removed bricks from the code [X]
- Added limits to rackets [X]
- Implemented simple score system [X]
- Added more speed to the ball [X]
- Change the collision to the top [X]
- Fixed Height and Width Contants to calculate the are of button [X]

## Daniel Parra:
par21002@byui.edu
- Added Player 2 Racket [X]
- Added Player 2 Score [X]
- Added both players controls [X]
- Added Menu on start [X]
- Added Menu Button action [X]
- Added Help button and Help scene [X]
- Added Credits button and Credits scene [X]
- Changed ball and racket sprites [X]
- Changed Player 1 and Player 2 racket start position [X]
- Changed both Score hud start position [X]
- Changed Ball start position [X]
- Changed Collide Border Action [X]
- Changed point system for both players [X]
- Created Button class [X]
- Created ChangeSceneClickAction [X]
- Created DrawButtonAction [X]

## Thomas Villalobos (Team Leader)
vil22003@byui.edu
- Readme File [X]
- Menu [X]
- Software Testing [X]
- Fixed the win with a two point lead [X]

## Gloria Rosado
ros21035@byu.edu
- Images [X]
- Menu [X]

## Jonathan Uribe
u266801382@byui.edu
- Quality Control [X]
