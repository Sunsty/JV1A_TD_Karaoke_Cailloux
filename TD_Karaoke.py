# Import



# Classes

class Player:

    def __init__(self,strName,intScore1,intScore2,intScore3,intScore4,intScore5):

        self.__name = strName
        self.__averageScore = 0
        self.__totalScore = 0
        self.__bestSong = 0
        self.__worstSong = 0
        self.__score1 = intScore1
        self.__score2 = intScore2
        self.__score3 = intScore3
        self.__score4 = intScore4
        self.__score5 = intScore5
        self.__listScore = {1:self.__score1,2:self.__score2,3:self.__score3,4:self.__score4,5:self.__score5}

    def getName(self):
        return self.__name
    
    def getAverageScore(self):

        self.__averageScore = (self.__score1+self.__score2+self.__score3+self.__score4+self.__score5)//5

        return self.__averageScore
    
    def getTotalScore(self):

        self.__totalScore = (self.__score1+self.__score2+self.__score3+self.__score4+self.__score5)

        return self.__totalScore
    
    def getBestSong(self):

        for i in range(1,(len(self.__listScore))):
            if( self.__listScore[i+1] > self.__listScore[i] ):
                self.__bestSong = i+1

        return self.__bestSong
    
    def getWorstSong(self):

        for i in range(1,(len(self.__listScore))):
            if( self.__listScore[i+1] < self.__listScore[i] ):
                self.__worstSong = i+1

        return self.__worstSong
    
    def getListScore(self):
        return self.__listScore

    def setScore(self,newScore,nbrSong):

        if newScore > self.__listScore[nbrSong]:
            self.__listScore[nbrSong] = newScore
            print(f"\n### Good Job {self.__name} !! New record !! ###\n")

    def displayScore(self):

        print(f"\nWelcome {self.__name}\n")
        print(f"Your total score is {self.getTotalScore()} points")
        print(f"Your average score is {self.getAverageScore()} points")
        print(f"Your best song is song n°{self.getBestSong()} with {self.__listScore[self.getBestSong()]} points")
        print(f"Your worst song is song n°{self.getWorstSong()} with {self.__listScore[self.getWorstSong()]} points")


class Song:

    def __init__(self,strName):

        self.__name = strName

    def getName(self):
        return self.__name
    

class Karaoke:

    def __init__(self,listPlayers,listSongs):

        self.__listPlayers = listPlayers
        self.__listSongs = listSongs

    def getListPlayers(self):
        return self.__listPlayers
    
    def getListSongs(self):
        return self.__listSongs
    
    def addPlayer(self,player):

        self.__listPlayers.append(player)
        print(f"{player.getName()} was added")

    def removePlayer(self,nbrPlayer):

        if len(self.__listPlayers) != 1:
            print(f"{self.__listPlayers[nbrPlayer].getName()} has been removed")
            self.__listPlayers.pop(nbrPlayer)

        else:
            print("You cannot remove more players")

    def diplayBestScore(self,nbrSong):
        nbrPlayer = 0
        bestPlayer = self.__listPlayers[nbrPlayer].getName()
        for i in range(len(self.__listPlayers)-1):
            if( self.__listPlayers[i+1].getListScore()[nbrSong] > self.__listPlayers[i].getListScore()[nbrSong] ):
                bestPlayer = self.__listPlayers[i+1].getName()
                nbrPlayer = i+1

        print(f"Best score for {self.__listSongs[nbrSong].getName()} is {self.__listPlayers[nbrPlayer].getListScore()[nbrSong]} by {bestPlayer}")

    def displayBestTotalScore(self):
        nbrPlayer = 0
        bestPlayer = self.__listPlayers[nbrPlayer].getName()
        for i in range(len(self.__listPlayers)-1):
            if( self.__listPlayers[i+1].getTotalScore() > self.__listPlayers[i].getTotalScore() ):
                bestPlayer = self.__listPlayers[i+1].getName()
                nbrPlayer = i+1

        print(f"Best total score is {self.__listPlayers[nbrPlayer].getTotalScore()} by {bestPlayer}")

    def displayBestAverageScore(self):
        nbrPlayer = 0
        bestPlayer = self.__listPlayers[nbrPlayer].getName()
        for i in range(len(self.__listPlayers)-1):
            if( self.__listPlayers[i+1].getAverageScore() > self.__listPlayers[i].getAverageScore() ):
                bestPlayer = self.__listPlayers[i+1].getName()
                nbrPlayer = i+1

        print(f"Best average score is {self.__listPlayers[nbrPlayer].getAverageScore()} by {bestPlayer}")

    def displayMaximumScore(self):
        nbrPlayer = 0
        bestPlayer = self.__listPlayers[nbrPlayer].getName()
        for i in range(len(self.__listPlayers)-1):
            if( self.__listPlayers[i+1].getListScore()[self.__listPlayers[i+1].getBestSong()] > self.__listPlayers[i].getListScore()[self.__listPlayers[i].getBestSong()] ):
                bestPlayer = self.__listPlayers[i+1].getName()
                nbrPlayer = i+1

        print(f"Maximum score is {self.__listPlayers[nbrPlayer].getListScore()[self.__listPlayers[nbrPlayer].getBestSong()]} by {bestPlayer} on {self.__listSongs[self.__listPlayers[nbrPlayer].getBestSong()].getName()}")


# Functions



# Variables



# Main Code


karaoke = Karaoke([Player("Dan",65,50,89,0,74),Player("Sam",87,78,98,74,65),Player("Zoe",60,0,50,0,100)],
                  {1:Song("\"Paranoia - Heartsteel\""),2:Song("\"GODS - New Jeans\""),3:Song("\"VILLAIN - K/DA\""),4:Song("\"POP/STARS - K/DA\""),5:Song("\"Legends never die - Against the current\"")})

print("")

karaoke.diplayBestScore(1)
karaoke.diplayBestScore(2)
karaoke.diplayBestScore(3)
karaoke.diplayBestScore(4)
karaoke.diplayBestScore(5)
karaoke.displayBestTotalScore()
karaoke.displayBestAverageScore()
karaoke.displayMaximumScore()

print("")

karaoke.removePlayer(1)
karaoke.addPlayer(Player("John",53,55,57,60,50))

print("")

karaoke.diplayBestScore(1)
karaoke.diplayBestScore(2)
karaoke.diplayBestScore(3)
karaoke.diplayBestScore(4)
karaoke.diplayBestScore(5)
karaoke.displayBestTotalScore()
karaoke.displayBestAverageScore()
karaoke.displayMaximumScore()

print("")