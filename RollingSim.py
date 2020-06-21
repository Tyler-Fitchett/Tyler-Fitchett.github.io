import sys
import time
import random
import pyodbc as pyodbc


conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-PUFFRBI;"
    "Database=Leaderboard;"
    "Trusted_Connection=yes;"
)

def read(conn):
    print("Leaderboard format, Name, Wins, Losses, Ties")
    cursor = conn.cursor()
    cursor.execute("select * from Leaderboard")
    for row in cursor:
        print(f'row = {row}')
    print()

def checkNameExist(conn, name, val):
    print("Checking")
    cursor = conn.cursor()
    if(val == 'Wins'):
        cursor.execute(
            'if exists(select * FROM Leaderboard WHERE Name = ?) BEGIN Update Leaderboard set Wins = Wins + 1 where Name = ?; END;',
        (name,name)
    )
    if(val == 'Ties'):
        cursor.execute(
            'if exists(select * FROM Leaderboard WHERE Name = ?) BEGIN Update Leaderboard set Ties = Ties + 1 where Name = ?; END;',
        (name,name)
    )
    if(val == 'Losses'):
        cursor.execute(
            'if exists(select * FROM Leaderboard WHERE Name = ?) BEGIN Update Leaderboard set Losses = Losses + 1 where Name = ?; END;',
        (name,name)
    )
    conn.commit()
    
    
def checkNameNotExist(conn, name,wins,losses,ties):
    print("Checking")
    cursor = conn.cursor()
    cursor.execute(
            'if not exists(select * from Leaderboard WHERE name = ?) BEGIN insert into Leaderboard(Name,Wins,Losses,Ties) values(?,?,?,?); END;',
        (name, name, wins, losses, ties)
    )
    conn.commit()


class DiceRollSim:
    def __init__(self, no_of_players, no_of_dies):
        self.players = self.assign_names(no_of_players)
        self.die_n = no_of_dies

    def assign_names(self, n):
        # Assigns names to 'n' players playing
        dict_players = {}

        # All members are indentified by name
        # and not number
        for i in range(n):
            dict_players[i + 1] = str(
                input("Name for player({}): ".format(i + 1)))
        
        return dict_players

    def roll_die(self):
        # Roll die n number of times 
        # In case playing with multiple dies
        return [random.randint(1, 6) for roll in range(self.die_n)]

    def play(self):
        # Main
        rounds = 0
        topRoll = 0
        winner = ''
        currentWinner = False
        tiedWins = False
        losers = []
        tiedWinners = []
        tie = 0
        winnercondition = 0
        losercondition = 0
        x = 0
        y = 0
        z = 0
        w = 0
        while True:
            # Continue playing until desired
            if str(input("\n\n[+]Continue [Y/n]? ")).strip().lower() == "y":
                print("\nRound-> %d" % rounds)

                # Print rolled die upper face number/s
                # for each player playing, along with sum for quick moves
                for player_num in self.players.keys():
                    rolled = self.roll_die()
                    print("  > Chance of player %s:  %s  total: %d" %
                          (self.players[player_num], rolled, sum(rolled)))
                          
                    if(sum(rolled) == topRoll):
                        tiedWinners.insert(w, self.players[player_num])
                        tie = 1
                        w += 1
                        if(currentWinner == True):
                            tiedWinners.insert(w, winner)
                            w+=1
                            currentWinner = False
                            tiedWins = True
                        topRoll = sum(rolled)
                    
                    if(sum(rolled) > topRoll):
                        if(currentWinner == True):
                            losers.insert(z, winner)
                        if(tiedWins == True):
                            losers.insert(z, tiedWinners)
                            tiedWins = False
                        winner = self.players[player_num]
                        topRoll = sum(rolled)
                        tie = 0
                        currentWinner = True
                        z+=1
                    if(sum(rolled) < topRoll):
                        losers.insert(z, self.players[player_num])
                        z+=1



                    # Delay for better user experience
                    time.sleep(5)

                # Update rounds played
                rounds += 1
                continue
            else:
                # Finished playing
                print("\n > Rounds played: %d" % rounds)
                if(tie == 1):
                    print("\n > The winners are: ")
                    print(*tiedWinners)
                    size = len(tiedWinners)
                    sizeL = len(losers)
                    while(winnercondition == 0):
                        checkNameExist(conn, tiedWinners[x], 'Ties')
                        checkNameNotExist(conn, tiedWinners[x], 0, 0, 1)
                        if(x == size):
                            winnercondition = 1
                        x+=1
                    while(loservondition == 0):                        
                        checkNameExist(conn, losers[y], 'Losses')
                        checkNameNotExist(conn, losers[y], 0, 1, 0)
                        y+=1
                        if(y == sizeL):
                            losercondition = 1
                        
                else:
                    print("\n > The winner is: %s !!!" % winner)
                    checkNameExist(conn, winner, 'Wins')
                    checkNameNotExist(conn, winner, 1, 0, 0)
                    sizeL = len(losers)
                    print(sizeL)
                    while(losercondition == 0):                        
                        print(losers[y])
                        checkNameExist(conn, losers[y], 'Losses')
                        checkNameNotExist(conn, losers[y], 0, 1, 0)
                        y+=1
                        if(y == sizeL):
                            losercondition = 1
                        
                break


def main_interface():
    count = 0
    # Indroductions
    print(" " * 7 + "| Dice Rolling Simulator | \n\n")

    # Initializations/Declarations
    players_n = abs(int(input("> How many players?  ")))
    die_n = abs(int(input("> Number of dies?  ")))
    print("\n\n")
    die_rolling_simulator = DiceRollSim(players_n, die_n)

    print("\nNumber of players playing -> %d\nWith %d dies." % (players_n, die_n))
    # And the game begins
    die_rolling_simulator.play()
    
    print("\n\nLeaderboard after update: ")
    read(conn)
    

    print("\n\nSee you at another game!")
    sys.exit(0)


main_interface()