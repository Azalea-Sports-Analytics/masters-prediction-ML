# List of Potential Data Sources

## List of Tours
### PGA Tour
The PGA Tour is the tour where most of the players in this event play year-round. 72 hole golf tournaments. 
It seems that data can easily be extracted from here as a .csv
[Link to PGA TOUR stats website](https://www.pgatour.com/stats)

### LIV Golf
This is a tour formed in 2021. It is fairly unconventional as tournaments are played over 54 holes (as opposed to the usual 72) in a shotgun start format.
[Link to LIV stats website](https://www.livgolf.com/stats)

Note: The PGA Tour has banned players who compete in LIV events from playing in PGA TOUR events.

### DP World Tour
Previously known as the European Tour. LIV players can play on this tour, but do receive a fine. A lot of the European players on the LIV tour will sacrifice fine money as these events are important for qualifying for the Ryder Cup (a matchplay event every 2yrs where 12 players from Europe take on 12 from USA). 72 hole golf touurnaments. 
[Link to DP Tour Stats website](https://www.europeantour.com/dpworld-tour/stats/)

It seems there in no button to download data on this website.

### Asian Tour
A lesser known tour, but some of the LIV players will play in these events. 72 hole golf tournaments.
[Link to Asian Tour Stats website](https://www.asiantour.com/stats?id=2025)

### PGA Champions Tour
This is the seniors tour for players age 50 and over. There will be a small number of players in the Masters 2025 field who are regularly play events here. This appears to work the same way as PGA Tour website - data is downloadable as csv. 
[Link to Champions Tour Stats website](https://www.pgatour.com/pgatour-champions/stats)



## Player Ranking Systems

### Official World Golf Rankings (OWGR)
Eligible tournaments from the leading professional golf tours, Major Championships (excluding LIV GOLF) and competitions around the world are included in the Official World Golf Ranking.

Any player competing in Eligible Tournaments will receive Ranking Points subject to their respective finishing position. 

Ranking Points are derived from each Eligible Tournament's Field Rating.

The OWGR System is run over rolling Ranking Periods. Ranking Points are maintained at full value for a 13-week period from the relevant Ranking Date on which they were awarded to place additional emphasis on recent performances. Ranking Points are then reduced in equal decrements for the remaining 91 weeks of the relevant Ranking Period.

Each player is then ranked according to their average points during the Relevant Ranking Period, which is determined by dividing a player's Total Points by the number of Eligible Tournaments they have played during that Ranking Period, subject to the minimum and maximum divisors set out below.

There is a minimum divisor of 40 Eligible Tournaments over the Ranking Period, with no more than the most recent 52 Eligible Tournaments that the player concerned has played in during the relevant Ranking Period counting towards a player's position in the Official World Golf Ranking.

It seems that historic data can be downloaded as a PDF (the rankings are updated weekly). This may be a task for someone to see how easy it is to automate extracting data from a PDF.

[Link to OWGR website](https://www.owgr.com/current-world-ranking)

### Data Golf Rankings 
This is an unoffical ranking website that aims to capture the rankings of any golfer that plays in OWGR-sanctioned events, LIV events, or WAGR-sanctioned (WORLD AMATUER GOLF RANKING) amateur events is eligible.

The rankings are determined by averaging the field strength-adjusted scores of each golfer, with recent rounds receiving more weight. The index listed on the page—the DG Index—is this weighted average (plus some adjustments for the overall recency of a player's data), and should be interpreted as our expectation for a golfer's next performance in units of strokes-gained relative to an average PGA Tour field (update: we've made our SG baseline tour-independent). That is, if a player has a value for the DG Index of +2, that means we currently expect them to beat a PGA Tour field by 2 strokes per round. Approximately the last 150 rounds that a golfer has played contribute to their DG Index. Finally, to be included in the rankings, a golfer must have played at least 40 rounds in the last 2 years and at least 1 round in the last 6 months.

My inituition is that this will prove more useful to us that OWGR since it does not discard LIV players and includes amateur players.

Seem to be able to download historic records as a csv.

[Link to DataGolf website](https://datagolf.com/datagolf-rankings)


## The Major Championships
There are 4 Major events played every year. These are where the best players in the world from all the different tours come together and compete. They are not operated by any of the touring organisations.

### The Masters
This is the tournament that we are trying to predict the result of for this year 2025. 72 hole tournament. Top 50 players and ties after 36 holes advance to play the final 36 holes (score does NOT reset after cut).
This is always played at Augusta National Golf Course in the 2nd week of April. This has the smallest field of the majors with about 85-100 players competing depending on qualification status.

[Link to Masters website](https://www.masters.com/index.html)

### PGA Championship
This is usually played in May at a different course in the US every year. This is not to be confused with the PGA Tour - separate to this. Cut: Top 70 and ties

From first inspection from website we may need to source historic data from elsewhere.

[Link to PGA website](https://www.pgachampionship.com/)

### US Open
This is played over Father's day weekend. 72 hole tournament. Different course each year in the US.  Cut: Top 60 and ties
[Link to US open website](https://www.usopen.com/)
[Link to historical stats](https://victory.usopen.com/history-landing/scoring-and-stats/scoring.html#!&y=2024)

## The Open
Played in July. 72 holes. Different course from a rota each year in the UK. Cut: Top 70 and ties. 
Data from the website seems limited. May need to source elsewhere.
[Link to OPen Website](https://www.theopen.com/leaderboard)


