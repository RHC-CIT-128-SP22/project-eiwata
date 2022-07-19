[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6908356&assignment_repo_type=AssignmentRepo)


<img
    src = "assets/icon.png"
    align = "right"
    width = "65 px"
/>


# The Call of Cthulhu - Interactive Horror Game

>CIT 128 Student Directed Project


## Student Info

>Add your Name, CRN, and Semester Year here using unordered bullets in Markdown.

* Erika Iwata
* CRN: 37902
* Spring 2022


## Program Description

>Describe your individual project program and include the goals of the program.

_The Call of Cthulhu - Interactive Horror Game_ is a choose your own adventure game based on the book by H.P. Lovecraft. This is a text-based game and allows the user to make decisions which leads them down different forks toward alternate endings of the story.

Source: _The Call of Cthulhu and Other Weird Stories_
<br> ISBN: 978-0-14-118234-6


__Some Context:__

About the Author:

Howard Phillips Lovecraft was an early 20th century horror writer. At the time, his works were published in _Weird Tales_ magazines and did not receive the amount of recognition that they do today. Because of this, he lived much of his life in poverty and this was actually one of the main causes for his depression. Nowadays, he is accredited as being the father of cosmic horror a.k.a. lovecraftian horror and known to have been one of the most influencial figures in the literary community for the horror genre.

Cosmic horror can be described as fear of the unknown or the unimaginable. Often times, the root of fear in cosmic horror is of such a grand/cosmic scale that the mere revelation of their existence is enough to drive people into insanity. Furthermore, many of the creatures in the Cthulhu Mythos are not known to be evil. They just exist as their own separate entities apart from mankind. Lovecraft's philosophy was a weird mix of anthropocentrism and nihilism and his works involved reflecting upon the vastness of the universe and realising the insignificance of humanity in comparison.

Pop Culture Examples of Lovecraftian Themes:
 * The Thing (1982)
 * Bird Box (2018)
 * Junji Ito's works

__Some of the goals of this project are:__

Core Features:
- [X] Dialogue displays on the screen gradually as user iterates through the game
- [X] Click to continue
- [X] Start screen and Game Over screen

Bonus Features:
- [X] Resizable GUI window
- [X] Smooth transition between scenes
- [X] Decision timer (10 sec) or else it autoselects decision A over decision B
- [ ] If user selects Continue, on the Game Over screen, it displays scenes traversed during the previous iteration of the game and allows the user to select a story point to revive from

### Video Demonstration

>Add a Link to your video demonstration
<div align = "left">
        <a href = "https://youtu.be/CT-vGxStvVk">
        <img src = assets/youtube.png width = 600>
        </a>
</div>

## Install Instructions

>Add any install instructions, if needed. This includes how to install included modules or libraries as well as configurations. You may remove this section if no special instructions are required.

- Python3
    - How to install: `brew install python3`
- Pygame
    - How to install: `pip install pygame`

## Software Engineering

>Describe the software engineering techniques used for the design and development of this program.

This game was made using `pygame.py` and organized into the following files:
```
main.py
initgame.py
gamefeatures.py
scenes.py
narrator.py
dialogue.txt
```
From `main.py`, the `main()` function first creates an object of the class `Game_Features()` from `gamefeatures.py`. Then it just calls the `scene_manager()` method and uses it to traverse between different scenes of the story.

Additionally, the class `Scene_Tracker()` from `scene.py` generates a binary tree for the story. The class `Display_Scene()` also from `scene.py` inherits `Scene_Tracker()` and creates an object of the class called `story = Scene_Tracker('A')` and proceeds to add in nodes as it traverses through different scenes. 
At the end of the game, the Game Over screen will display and give the user the option to select between Continue and Exit. If the user selects Continue, it goes to the `play_again()` method in `Display_Scene()` which looks at the nodes in the binary tree for the previous iteration of the game and displays some of the scenes that were traversed during the last game play to allow the user to select a story point to revive from.
```
Scene_Tracker():
    .
       A
        \
         B
          \
           C
            \
             D
              \
               E
              / \
             e   F
                  \
                   G
                  / \
                 g   H
                /     \
               f       I
                        \
                         J
                          \
                           K
                            \
                             L
                              \
                               M
                                \
                                 N
                                  \
                                   O
                                 /  \
                                o    P
                                      \
                                       Q
                                        \
                                         R
                                       /  \
                                      r    S
    .
    .
Display_Scene(Narrator, Scene_Tracker):
    .
    story = Scene_Tracker('A')
    .
    def scene_B(self):
        self.story.insert('B')
        .
    def scene_C(self):
        self.story.insert('C')
        .
    def play_again(self):
        .
           A
            \
             B
              \
               C
                \
                 D
                  \
                   E
                  /
                 e
        .
        .
```
_See also:_ [Cthulhu Decision Tree pdf](https://drive.google.com/file/d/1ljiRw9f8k8uvD437W7veBSKKvOAo-qb_/view?usp=sharingg)

## Directions and Grading Rubric

>To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.
