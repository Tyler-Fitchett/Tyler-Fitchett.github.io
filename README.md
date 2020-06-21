## Welcome to my ePortfolio

Here I will include all of the artifacts for the CS 499 Capstone class at Southern New Hampshire University


### Professional Self-assessment


```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

### Artifact Selection and Refinement Plan

```markdown

#Category One, Software design and engineering: 
For this category I am using an open source program that I found on GitHub. This program is a simple game 
program that will roll a die for a given number of players. This falls into the category of software design. 
My plan for this program is the enhance it by adding a leaderboard system in the form of a database that 
takes in the game results and stores them in a place that they can be accessed later. I think that making 
this improvement demonstrates the course outcome of using well-founded and innovative techniques. I believe 
that this will elevate this simple game into something that can be more advanced than just rolling a die 
over and over. Now it will be more like a game with the leaderboard system. There can also be even more 
added on later now that there is a leaderboard such as new games or incentives based on leaderboard position.

```

[Category 1 Refinement Plan](https://github.com/Tyler-Fitchett/Tyler-Fitchett.github.io/blob/master/img1.png)


```markdown

#Category Two, Algorithms and data structures:
For this category I am using an open source calculator program that I found on GitHub. This program in 
just a simple calculator that has add, subtract, multiply and mod functions. I plan to add new algorithms 
to the program that can perform more advanced math problems such as trig functions. I will also add in a 
new menu that is easier to use and showcases all the capabilities of the calculator. I believe this showcases 
my knowledge of using algorithmic principles to improve upon the quality of the work and to also increase 
the efficiency to make it a more professionally acceptable program.

```

[Category 2 Refinement Plan](https://github.com/Tyler-Fitchett/Tyler-Fitchett.github.io/blob/master/img2.png)

```markdown

#Category Three, Databases:
For this category I am going to use the final project from the most recent course I took at SNHU. 
This program has api calls for a mongodb database to run through the basic function for a market stocks 
database. The improvements that I plan to make on this project is to create an interface that can help a 
user go through the functions of create, read, add and delete within the database without having to input 
the curl functions themselves. I believe this showcases my ability to implement computer solutions to 
accomplish industry specific goals. The goals here being a functioning product that the average person 
can understand and use in a professional environment.

```

[Category 3 Refinement Plan](https://github.com/Tyler-Fitchett/Tyler-Fitchett.github.io/blob/master/img3.png)


### Informal Code Review

My code review will be included in a zip folder in my brightspace submission.


## Enhancements

### Enhancement 1, Software design and engineering:

```markdown

This artifact started out as an open source program for a coin flipping game. It is a fairly basic 
game that takes in a selected number of players, then rolls a selected amount of die for each player. 
The original program would output the results of the rolls and stop there. I decided to include this 
artifact in my portfolio because it was something that I believe everyone could wrap their head 
around. It was not too complicated in any area and it was a simple game to complete quickly. I 
chose to make improvements not on the core gameplay, but on the results of the game. What I did 
was to have the program be able to determine who was the winner, or in the case of multiple winner, 
decide who tied. The program would then upload the results to a SQL server database that tracked 
the leaderboard. If the winner had already been added to the leaderboard then the existing value 
would be updated, if they were not previously there the program would add them into the database 
and start their scores at zero. While completing this enhancement I found that what I was 
undertaking was slightly harder than I had originally anticipated. It really became difficult to 
track the winner as the number of users grew to larger numbers, but I believe I was able to get 
it right with my use of lists and if statements. I will be attaching a short video in the zip folder 
where I showcase the capabilities of the program. Since the database was hosted on my computer 
and the program was connecting to the local instance, it may not be possible to get the entire 
program working on a different computer at this time. This is why I will be including the video to 
show how it all works.  

```

[Here is a link to the original code](https://github.com/Tyler-Fitchett/Tyler-Fitchett.github.io/blob/master/diceRollerOriginal.py)
--
[Here is a link to the enhanced code](https://github.com/Tyler-Fitchett/Tyler-Fitchett.github.io/blob/master/RollingSim.py)


### Enhancement 2, Algorithms and data structures:
```markdown
This artifact was a simple calculator program that I found on an open source GitHub repository. 
This program was originally created on Jan 28, 2018. I chose this artifact to include in my 
portfolio because I think it is a simple program that anyone with beginners knowledge of python 
will be able to understand and recreate. I think the menu system is something that I used to 
struggle with understanding when I first started out programming and I think this is a good way 
to show how I have progressed throughout the program. The improvements I made to the program 
were simple, but significant. Firstly, I added in extra functions to the original calculator 
portion. The calculator can now perform simple trig functions such a Sine, Cosine and Tangent. 
The next thing I did was to add a second menu of options for converting numbers. Now there are 
three separate menus. The first menu was the main menu and the two submenus work as the calculator 
menu and the converter menu. I then went through and added different functions for converting 
numbers to different values. These conversions are what I figured would be the most used 
conversions and the most helpful to include in this calculator program. I feel that I did 
successfully meet the course objectives that I originally set out to meet. I changed my enhancement 
slightly because the original enhancement that I proposed would not successfully showcase my 
ability. What I had planned on doing was to make this calculator a standalone executable file, 
but what that involved was just importing functions that were created by other people and did 
not showcase what I could do. I learned while improving this artifact that even though some things 
may seem simple at first, there are ways to use experience to greatly enhance them to be much 
more. When I first started programming, I would have massively struggled to get the original 
calculator portion of this program working, now I am able to create multiple branches and submenus 
all with their own set of functions. This has been a great experience for me because I am now 
normally working with much more complex functions and I had forgotten what you can do to make 
these simple programs more advanced.

```

[Here is a link to the original code](https://github.com/Tyler-Fitchett/Tyler-Fitchett.github.io/blob/master/calculatorOriginal.py)
--
[Here is a link to the enhanced code](https://github.com/Tyler-Fitchett/Tyler-Fitchett.github.io/blob/master/Calculator.py)




