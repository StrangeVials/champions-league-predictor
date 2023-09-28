import random

group_A = ["Bayern", "Manchester United", "Copenhagen", "Galatasaray"]
group_B = ["Sevilla", "Arsenal", "PSV", "Lens"]
group_C = ["Napoli", "Real Madrid", "Braga", "Union Berlin"]
group_D = ["Benfica", "Inter Milan", "Salzburg", "Real Sociedad"]
group_E = ["Feyenoord", "Atletico Madrid", "Lazio", "Celtic"]
group_F = ["PSG", "Dortmund", "Newcastle", "AC Milan"]
group_G = ["Manchester City", "Leipzig", "Crvena Zvezda", "Young Boys"]
group_H = ["Barcelona", "Porto", "Shakhtar Donetsk", "Antwerp"]

ro16teams = []
quarterfinals = []
semiquarterfinals = []
finals = []
empty = []
valid_inputs = {"A": group_A, "B": group_B, "C": group_C, "D": group_D, "E": group_E, "F": group_F, "G": group_G, "H": group_H}


def question(statement):  # this function will change the question depending on what stage of the program you are in
    if statement == 1:
        a = input("Enter the group you want (Type any letter from A-H): ").capitalize()
        return a
    if statement == 2:
        b = input("Enter the bracket you want (Type any number from 1-8): ")
        return b
    if statement == 3:
        c = input("Enter the bracket you want (Type any number from 1-4): ")
        return c
    if statement == 4:
        d = input("Enter the bracket you want (Type any number from 1-2): ")
        return d


def randomizer(teams,number_of_winners,counter):  # main function that selects teams at random
    query = question(counter)
    if valid_inputs == {}:
        counter += 1
    if valid_inputs != {}:
        while valid_inputs != {}:
            while query == "":
                query = question(counter)

            if query not in valid_inputs:
                while query not in valid_inputs:
                    query = question(counter)

            if query in valid_inputs:
                x = random.sample(valid_inputs[query], number_of_winners)  # parameter is number_of_winners
                print(x)
                teams.extend(x)  # parameter is teams
                valid_inputs.pop(query)


def separator(start,end,teams):  # previous winners that were placed in one list will be assigned in random brackets
    teams = list(set(teams))
    for x in range(start, end, 2):
        print(teams[x:x + 2])
        empty.append(teams[x:x + 2])
    counter = 1
    for y in empty:
        valid_inputs[str(counter)]=y
        counter += 1
    empty.clear()


randomizer(ro16teams,2,1)  # type letters A-H
print("The brackets for the round of 16 are:")
separator(0,16,ro16teams)
print("")

randomizer(quarterfinals,1,2)  # type numbers 1-8
print("The brackets for the quarter finals are:")
separator(0,8,quarterfinals)
print("")

randomizer(semiquarterfinals,1,3)  # type numbers 1-4
print("The brackets for the semi-quarter finals are:")
separator(0,4,semiquarterfinals)
print("")

randomizer(finals,1,4)  # type numbers 1-2
print("The bracket for the finals are:")
separator(0,2,finals)
print("")

print("The winner of the Champions League 2023/24 Season is:")
x = random.choice(finals)
print(x)

