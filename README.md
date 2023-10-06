# champions-league-predictor

v3.1 - added fancy display of all the group stages and removed some unneccesary code

This is a simple game that will predict the winner of the 2023/24 Champions League season.

There are 8 predetermined lists based on the actual group stages that were drawn in real life. 

The program will ask you to enter any group stage. This will give you the winners of that group stage. For example, if you enter group F, the program will randomly select 2 teams as the winner. The program will then store these two teams in the ro16teams list. Note that you cannot make the program return two new strings from the same list after entering that group; for example, if winners from group F have already been selected, you cannot make the randomizer function grab another two new strings from F.

After winners from all group stages have been chosen, the program will take all the winners stored in the ro16teams list and place the list in the separator function. At this point in the program, there are 16 teams. The separator function will create 8 new lists with 2 teams each. Note that which team will be paired with which is randomized.

Then, the process will repeat like before, but this time, only 1 team will be selected as the winner. There will be 8 winners in total. The separator function will create 4 lists with 2 teams each from the 8 winners, and this process will keep on repeating until 1 team has been selected as the champion.

The question function's purpose is to help the user identify which inputs are valid, as well as at what stage of the competition they are in.
