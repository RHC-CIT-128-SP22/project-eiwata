[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6908356&assignment_repo_type=AssignmentRepo)
# The Call of Cthulhu - Interactive Horror Game

>CIT 128 Student Directed Project


## Student Info

>Add your Name, CRN, and Semester Year here using unordered bullets in Markdown.

* Erika Iwata
* CRN: 37902
* Spring 2022


## Program Description

>Describe your individual project program and include the goals of the program.

<p
    align = "center"
>
<img
    src = "assets/Cthulhu Book.gif"
    alt = "Cthulhu Book"
    style = "display: inline-block; max-width: 100 px"
>
</p>

The Call of Cthulhu - Interactive Horror Game is a choose your own adventure game based on the book by H.P. Lovecraft. This is a text-based game and allows the user to make decisions which leads the user down different forks toward alternate endings of the story.

Some of the goals of this project are:

Core Features:
- [ ] Dialogue displays on the screen gradually as user iterates through the game
- [X] Smooth transition between scenes
- [ ] Game Over screen allows user to select between Play Again or Quit
- [ ] If user selects Play Again it displays scenes traversed during the previous iteration of the game and allows the user to select a story point to revive from

Bonus Features:
- [ ] Click to pause
- [ ] GUI window size is adjustable
- [ ] Allow user to choose the dialogue speed (slow 1x, medium 1.5x, fast 2x)
- [ ] Decision timer (12 sec) or else it autoselects decision A over decision B

### Video Demonstration

>Add a Link to your video demonstration

### Install Instructions

>Add any install instructions, if needed. This includes how to install included modules or libraries as well as configurations. You may remove this section if no special instructions are required.

- Python3
    - How to install: `brew install python3`
- Pygame
    - How to install: `pip install pygame`

## Software Engineering

>Describe the software engineering techniques used for the design and development of this program.

This game was made using `pygame.py` and organized into the following user - defined modules:
```
main.py
initgame.py
gamefeatures.py
scenes.py
dialogue.py
```
From `main.py`, the `main()` function first created an object of the class `Game_Features()` from `gamefeatures.py`. Then it just called the `scene_manager()` method, which had the story indexed into a binary search tree, and used it to traverse between different nodes of the story.
```
Game_Features()
    .
    .
    scene_manager()
    .
    .
```

## Directions and Grading Rubric

>To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.
