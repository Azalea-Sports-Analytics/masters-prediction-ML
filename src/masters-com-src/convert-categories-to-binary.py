"""
Task for Srinath

Create a function that takes in the invitees to the Masters from a given year and converts the Qualification and the #*^ at start of names to binary columns.

I will explain this in more detail using the "data\masters-com-data\2025-invites.csv"

In the "Invitees" column the players name may start with # * or ^
    - # Denotes first Masters appearance
    - * Denotes the player is an amateur
    - ^ Dentes that the Masters committee has invited this player as their discretion who would have not other wise qualified.

Remove this symbol and instead have a binary columns "amatuer" (*), "firstMasters" (#), "invite" (^). 
If the player has a * infront of their name then the "amateur" column should be 1 else 0.

The next part to this function should then conver the players Qualifaction cateogires to binary columns. 
QUALIFICATIONS FOR INVITATION
1. Masters Tournament Champions (Lifetime)
2. U.S. Open Champions (Honorary, non-competing after five years)
3. The Open Champions (Honorary, non-competing after five years)
4. PGA Champions (Honorary, non-competing after five years)
5. Winners of the Players Championship (Three years)
6. Current Olympic Gold Medalist (One Year)
7-A. Current U.S. Amateur Champion (7-A) (Honorary, non-competing after one year)
7-B. Runner-up (7-B) to the current US Amateur Champion
8. Current The Amateur Champion (Honorary, non-competing after one year)
9. Current Asia-Pacific Amateur Champion (One year)
10. Current Latin America Amateur Champion (One year)
11. Current U.S. Mid-Amateur Champion (One year)
12. Current NCAA Division I Men's Individual Champion (One year)
13. The first 12 players, including ties, in the previous year's Masters Tournament
14. The first 4 players, including ties, in the previous year's U.S. Open
15. The first 4 players, including ties, in the previous year's The Open Championship
16. The first 4 players, including ties, in the previous year's PGA Championship
17. Individual winners of PGA Tour events that award a full-point allocation from previous Masters to current Masters
18. Those qualifying and eligible for the previous year's season-ending Tour Championship
19. The 50 leaders on the final Official World Golf Ranking for the previous calendar year
20. The 50 leaders on the final Official World Golf Ranking published during the week prior to the current Masters Tournament

headers = [
    "qual_1",
    "qual_2",
    "qual_3",
    "qual_4",
    "qual_5",
    "qual_6",
    "qual_7_A",
    "qual_7_B",
    "qual_8",
    "qual_9",
    "qual_10",
    "qual_11",
    "qual_12",
    "qual_13",
    "qual_14",
    "qual_15",
    "qual_16",
    "qual_17",
    "qual_18",
    "qual_19",
    "qual_20"
]

Whichever, Qualification categries that player is part of I would expect a 1 in that column and a 0 in all other. 

As an example from the data\masters-com-data\2025-invites.csv I would expect "Beck, Ewan" to have the following:

Invitees,Country,qual_1,qual_2,qual_3,qual_4,qual_5,qual_6,qual_7_A,qual_7_B,qual_8,qual_9,qual_10,qual_11,qual_12,qual_13,qual_14,qual_15,qual_16,qual_17,qual_18,qual_19,qual_20,amateue,firstMasters,invite
Beck, Ewan,United States,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0

This is because Ewan Beck is playing his first Masters, is an amateur, and qualified through category 11. 


I expect the function to be able to do the same process to any csv that looks like this.


Input: File Path to the json
Output: Dataframe as outlined above.

The idea of this function is that this process is repeatable for 2023 and 2024 invite list.
"""

import json
import pandas as pd
import os


# Now use the relative path from project_root
file_path = "data/masters-com-data/invitees-2025.json"

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the invitees list and convert to DataFrame
invitees_data = data["invitees"]
invitees_df = pd.DataFrame(invitees_data)
print(invitees_df.head())