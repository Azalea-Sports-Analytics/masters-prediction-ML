# Research on ML in Golf

## https://datagolf.com/predictive-model-methodology/
### Intro
Built a predicitive model that predicts a prob. dist'n for each players score then simulates the tournaments to get a % for winning, top 10, etc.
Models each golfer's adjusted SG in a round so that they can then compare across courses. They believe accurately estimating probabilties of the SG dist'n relative to some benchmark, then they can accurately predict the estimate of probabilities of a certain event happening in a tournament. 

### Adjusting Scores
\( S_{ij} = \mu_i(t) + \delta_j + \epsilon_{ij} \)

