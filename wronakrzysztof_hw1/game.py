# -*- coding: utf-8 -*-
import random
import time
import sys
import os


class Player:  # contains player stats.
    money = 200
    year = 1
    money_per_turn = 0
    lose_turn = False

    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id

    def status(self):  # shows stats of a player
        print("Player", self.player_id, ": ", self.name, " has", self.money, "money.", self.year, " year student")

    def turn(self):  # every time its player's turn, this method will be called to do all new player's turn actions
        self.money += self.money_per_turn

    def increase_year(self):  # increases year stat of player and return true if player has won
        end = False
        self.year += 1
        if self.year > 5:
            print("You have finished your studies and won the game!")  # print when won the game
            end = True
        else:
            print("You have become a ", self.year, " year student")
        return end


def start():  # main function, contains main game loop.
    option = menu()  # displays menu and gets input of chosen option
    if option == 1:  # user chose to play the game
        players = num_of_players()  # get number of players from the user
        players_list = players_creation(players)  # create list of player objects
        end = False
        i = 0
        while end is False:  # main game loop
            end = turn(players_list, i)
            i += 1
    elif option == 2:
        print("Cya!")
        quit()
    else:
        print("An error has occurred, application will be closed now.")
        quit()


def menu():  # displays menu when application starts, returns number of option chosen by player.
    print("AGH STUDENT")  # Name of the game
    print("1. New game")
    print("2. Quit")
    choice = get_choice(2)  # get number from 1 to 2 from input
    return choice


def num_of_players():  # gets input of how many players are going to play the game
    players = 0
    while players < 2 or players > 4:  # keep asking for number from 2 to 4
        print("Number of players (2-4):")
        players = nat(input())  # get natural number
    return players


def players_creation(players):  # creates Player objects and returns a list of them
    players_list = []
    print("Creating game for ", players, " players")
    players_list = [Player(ask_name(i, players_list), i) for i in range(1, players + 1)]
    return players_list


def nat(string):  # converts string to natural number, returns -1 if conversion is impossible
    try:
        return int(string)
    except ValueError:
        return -1


def ask_name(player, players_list):  # asks for player name during game creation. player variable is number of player.
    player_name = ""
    while len(player_name) < 5 or len(player_name) > 10:
        print("Player ", player, "name, from 5 to 10 characters:")
        player_name = input()
    return player_name


def turn(players_list, i):  # this function is called every turn.
    print()
    print()
    how_many_players = len(players_list)
    print("Turn :", int(i / how_many_players + 1))  # prints which turn of current player is it
    current_player = players_list[i % how_many_players]  # get current player from players list
    current_player.turn()  # do all stuff related to new turn of current player
    current_player.status()  # show status of current player
    event_number = random.randint(0, 10)  # picks a random number
    print()
    end = event(current_player, event_number)  # do event related stuff. returns true if game ends because of event
    time.sleep(5)
    return end  # returns true if game should end because of event which happened during current turn


def get_choice(max):
    choice = nat(input())  # gets player's input
    while choice < 1 or choice > max:  # in case of incorrect string
        print("Incorrect number, please try again:")
        choice = nat(input())  # gets player's input
    return choice


def roll(good, all_chances):  # returns true with a chance of good / all_chances
    rolled = random.randint(1, all_chances)
    if rolled <= good:
        return True
    else:
        return False


def event(player, event_number):  # Very long function, called every turn. All events are described here.
    end = False  # changes its value if game is supposed to end because of current event
    if player.lose_turn is True:  # lose a turn event
        print("You lose a turn")
        player.lose_turn = False

    elif event_number == 0:  # apply for a job event
        print("There's a job offer.")
        print("Do you want to apply for the job? You have to spend 30 money to apply.")
        print("1.Apply.")
        print("2.Don't apply.")
        choice = get_choice(2)
        cost = 30
        if choice == 1:
            if player.money >= cost:  # check if player has enough money
                player.money -= cost
                if roll(1, 5):
                    print("You got a job! From now on you will be getting 5 money per turn")
                    player.money_per_turn += 5
                else:
                    print("You didn't manage to get a job.")
            else:
                print("You don't have enough money!")
                choice = 2
        if choice == 2:
            print("You didn't apply for the job.")

    elif event_number == 1:  # WDI failed event
        print("You have failed WDI exam.")
        print(" Do you want to pay 50 money course retake fee or repeat a year?")
        print("1. Pay.")
        print("2. Repeat a year.")
        choice = get_choice(2)
        if choice == 1:
            if player.money >= 50:  # check if player has enough money
                print("You paid 50 money for course retake")
                player.money -= 50  # player loses money.
            else:
                print("You don't have enough money!")
                choice = 2  # no money, player is forced to choose option 2
        if choice == 2:
            print("You have to repeat a year of study, you will lose next turn")
            player.lose_turn = True  # player loses a turn

    elif event_number == 2:  # exam coming event
        print("An exam is coming.")
        print("Do you want to get the books for 50 money?")
        print("1.Yes")
        print("2.No")
        choice = get_choice(2)
        if choice == 1:
            if player.money >= 50:  # check if player has enough money
                print("You paid 50 money for the books")
                player.money -= 50  # player loses money.
                if roll(1, 2):  # 50% of passing the exam
                    print("You have passed your exam!")
                    end = player.increase_year()
                else:
                    print("Unfortunately, you didn't pass your exam")
            else:
                print("You don't have enough money!")
                choice = 2  # player is forced to choose option 2
        if choice == 2:
            print("You didn't buy the books")

    elif event_number == 3:  # parents send you random amount of money from 1 to 100
        money = random.randint(1, 100)
        print("Parents sent you ", money, " money.")
        player.money += money
        print("You now have ", player.money, " money")

    elif event_number == 4:  # internship event. Lose a turn and get 100 money or nothing.
        print("You can go for an internship abroad.")
        print("Do you want to go?")
        print("1. Yes")
        print("2. No")
        choice = get_choice(2)
        if choice == 1:
            player.money += 100  # player gets money
            player.lose_turn = True  # player loses next turn
            print("You have awesome time on internship and earn 100 money, but you will lose next turn.")
        if choice == 2:
            print("You chose to stay and study. Nothing happens.")

    elif event_number == 5:  # join AGH science club. Free +1 year
        print("You can join one of AGH science clubs.")
        print("Do you want to join?")
        print("1. Yes")
        print("2. No")
        choice = get_choice(2)
        if choice == 1:
            print("You learn a lot. You passed all exams and become a pass a year.")
            end = player.increase_year()
        if choice == 2:
            print("Nothing happens.")

    elif event_number == 6:  # Forgot group number event.
        print("PhD Grydrych wants you to write a number of your group on calculus exam, but you have no clue what's the number.")
        print("You can ask a friend, but PhD Grydrych might catch you.")
        print("Do you want to try?")
        print("1. I'm brave.")
        print("2. I can manage myself.")
        choice = get_choice(2)
        if choice == 1:
            if roll(3, 4):  # 75% chance of passing the exam if player picks risky choice
                print("You managed to get a number of your group and passed your exam")
                end = player.increase_year()
            else:
                print("You have been caught. You lose a turn.")
                player.lose_turn = True
        if choice == 2:
            if roll(1, 5):  # 20% chance of passing the exam if player doesn't play risky
                print("Somehow you managed to pass the exam. You are a next year student!")
                player.increase_year()
            else:
                print("You didn't pass the exam.")

    elif event_number == 7:  # meeting with football fans event. Lose a turn, 50 money, or both.
        print("Football fans surrounded you in the park at 2 AM")
        print("They keep on asking: Wisla czy Cracovia?")
        print("1. Wisla")
        print("2. Cracovia")
        print("3. Sorry, I don't speak polish")
        choice = get_choice(3)
        if choice == 1:
            print("You end up in a hospital. You lose next turn.")
            player.lose_turn = True
        if choice == 2:
            if player.money > 50:
                print("You managed to escape, but you lost 50 money.")
            else:
                print("You managed to escape, but you lost all your money.")
        if choice == 3:
            if player.money > 50:
                print("You wake up in a hospital. You lose next turn and you lose 50 money.")
            else:
                print("You wake up in a hospital. You lose next turn and you lose all your money.")

    elif event_number == 8:  # party is coming event. become a next year student with 25% chance or do play WoW.
        print("A party is coming. You can go to party or not.")
        print("What do you choose?")
        print("1. Let's party.")
        print("2. Let's study.")
        print("3. I will make my own party.")
        choice = get_choice(3)
        if choice == 1:
            print("Nobody invited you. You end up studying anyway.")
            choice = 2
        if choice == 2:
            if roll(1, 4):
                print("You became a next year student!")
                player.increase_year()
            else:
                print("You didn't manage to pass the exam anyway.")
        if choice == 3:
            print("You make your own party in World of Warcraft.")
            print("You are a level 90 paladin now.")

    elif event_number == 9:  # old man on the street event. lose 100 money or nothing
        print("An old man on the street asks you for 100 money.")
        print("Do you want to give it to him?")
        print("1. Yes")
        print("2. No")
        choice = get_choice(2)
        if choice == 1:
            if player.money >= 100:
                print("You give a man the money.")
                player.money -= 100
                time.sleep(2)
                print("What did you expect to happen? Nothing happens.")
            else:
                print("You don't have that much money!")
        if choice == 2:
            print("You don't give a man the money.")

    elif event_number == 10:  # forgot to push to repo event. All hope is lost.
        print("You forgot your to push your python project to remote repository in time.")
        print("What do you do?")
        print("1. Beg for forgiveness.")
        print("2. Say you had to attend to twelve funerals last week.")
        print("3. Do nothing.")
        choice = get_choice(3)
        print("It doesn't matter, all hope is lost.")

    return end  # end is true if game is supposed to end because of current event.

try:
	start()  # start main function and handle keyboard interruptions.
except (KeyboardInterrupt, EOFError):
	print()
	print("Bye bye")
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)
pass

