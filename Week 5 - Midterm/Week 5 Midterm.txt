# Tristan Knott
# Week 5 Midterm
#
# Variables Used:
# total_hits            adds and stores hits from all characters   
# average_hits          devides the total hits by number of characters to find average hit
# player_name           stores names of characters into list
# player_race           stores race of characters in list
# player_character      stores the character in list
# number_of_hits        stores number of hits per character in list
# file                  stores read csv file
# report                stores file broken down into a list
#
# ==========================================================================================
import csv

def find_hits():
    print('{:<15}{:<15}{:<20}{:<15}'.format("Player Name", "Player Race", "Player Character", "Number of Hits"))
    for i in range(0, len(player_name)):
        if int(number_of_hits[i])>=40:
            print('{:<15}{:<15}{:<20}{:<15}'.format(player_name[i], player_race[i], player_character[i], number_of_hits[i]))

def hit_average():
    total_hits=0
    for i in range(0, len(player_name)):
        total_hits+=float(number_of_hits[i])
    average_hits=float(total_hits/len(player_name))
    print(f"\nThe average number of hits to all players is: {average_hits}\n")

def print_lists():
    print('{:<15}{:<15}{:<20}{:<15}'.format("Player Name", "Player Race", "Player Character", "Number of Hits"))
    for i in range(0, len(player_name)):
        print('{:<15}{:<15}{:<20}{:<15}'.format(player_name[i], player_race[i], player_character[i], number_of_hits[i]))

player_name = []
player_race = []
player_character = []
number_of_hits = []

with open(r"Week 5 - Midterm\Midterm.csv") as f:
    character_counter = 0
    file = csv.reader(f)
    report = list(file)
    for row in report:
        character_counter+=1
        player_name.append(row[0])
        player_race.append(row[1])
        player_character.append(row[2])
        number_of_hits.append(row[3])
        
find_hits()
hit_average()
print_lists()