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


