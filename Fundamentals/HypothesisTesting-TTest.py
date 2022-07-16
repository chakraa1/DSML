"""
There are 8 females and 12 males in a coaching class. After a practice test, the coach wants to know whether the average
score of females is greater than the average score of males. Given data describes the scores of females and males.
Check whether the assumption of the coach is significant or not at a 5% of significance level?

female_scores=[25,30,45,49,47,35,32,42]
male_scores=[45,47,25,22,29,32,27,28,40,49,50,33]

"""
female_scores=[25,30,45,49,47,35,32,42]
male_scores=[45,47,25,22,29,32,27,28,40,49,50,33]

mean_f = np.mean(female_scores)
mean_m = np.mean(male_scores)

sd_f = np.std(female_scores)
sd_m = np.std(male_scores)

