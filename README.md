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

<p >
    <img
        align = "right"
        src = "assets/large-necronomicon-book-lovecraft-25.jpeg"
        alt = "Cthulhu Book"
        width = "250"
    />
</p>


_The Call of Cthulhu - Interactive Horror Game_ is a choose your own adventure game based on the book by H.P. Lovecraft. This is a text-based game and allows the user to make decisions which leads the user down different forks toward alternate endings of the story.

Source: _The Call of Cthulhu and Other Weird Stories_
<br> ISBN: 978-0-14-118234-6


__Some Context:__

About the Author:

Howard Phillips Lovecraft was an early 20th century horror writer. His childhood first began with his father getting committed to a psychiatric hospital after a mental breakdown. He died soon after which led to his mother's depression and him moving in with his maternal family. His grandfather Whipple Van Buren Phillips took on the role as his father figure and became the person Lovecraft felt closest to in his family. He exposed Lovecraft to literature and told him horror stories that he made up for his grandson's amusement. His grandfather's death however, came shortly before Lovecraft entered high school and left an emotional wound on Lovecraft that he never completely recovered from. Lovecraft called this the darkest point in his life and had thoughts of suicide along with nightmares and long nights of insomnia.

He never finished school due to the severity of his mental breakdowns. He was a progidy though and spent much of his time as a recluse just staying indoors and reading books. At the time, his works were published in _Weird Tales_ magazines and did not receive the amount of recognition that they do today. Nowadays, he is accredited as being the father of cosmic horror a.k.a. lovecraftian horror and known to have been one of the most influencial figures in the literary community for the horror genre.

Cosmic horror can be described as fear of the unknown or the unimaginable.  Often times, the root of fear in cosmic horror is of such a grand/cosmic scale that the mere revelation of their existence is enough to drive people into insanity. Furthermore, many of the creatures in the Cthulhu Mythos are actually thought to extend beyond such binary notions as good or evil but rather exist just as their own separate entities apart from mankind. This idea serves as the base to support his philosophy which involves reflecting upon the vastness of the universe and realising the insignificance of humanity in comparison.

Pop Culture Examples of Lovecraftian Themes:
 * The Thing (1982)
 * Bird Box (2018)
 * Junji Ito's works


__Some of the goals of this project are:__

Core Features:
- [ ] Dialogue displays on the screen gradually as user iterates through the game
- [X] Smooth transition between scenes
- [ ] Game Over screen allows user to select between Play Again or Quit
- [ ] If user selects Play Again it displays scenes traversed during the previous iteration of the game and allows the user to select a story point to revive from

Bonus Features:
- [ ] Click to pause
- [X] GUI window resizable
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

This game was made using `pygame.py` and organized into the following files:
```
main.py
initgame.py
gamefeatures.py
scenes.py
dialogue.txt
```
From `main.py`, the `main()` function first created an object of the class `Game_Features()` from `gamefeatures.py`. Then it just called the `scene_manager()` method, which had the story indexed into a binary tree, and used it to traverse between different nodes of the story.
```
Game_Features()
    .
    .
    scene_manager()
        .
        .
                                            1
                                           /
                                          2
                                         /
                                        3
                                       /
                                      4
                                     /
                                    5
                                   / \
                                  6   7
                                 /     \
                                8       9
                               / \
                              10  11
                             /     \
                            12      13
                           /
                          14
                         /
                        15
                       /
                      16
                     /
                    17
                   /
                  18
                 /  \
                19   20
               /
              21
             /
            22
           /  \
          23   24
         /      \
        25       26
        .
        .
```
_See also:_ [Cthulhu Decision Tree pdf](https://drive.google.com/file/d/1y-Ar-hCq-sWJkWkNjTRm8chB-Nbs8YqH/view?usp=sharing)

## Directions and Grading Rubric

>To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.
