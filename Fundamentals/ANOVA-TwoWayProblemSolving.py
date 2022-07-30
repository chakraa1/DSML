"""
The illness caused due to a virus in a city concerning some restaurant inspectors is not consistent with their evaluations of the
cleanliness of restaurants. In order to rightly evaluate the situation, a restaurant chain owner directed the inspectors to grade
the cleanliness of his three restaurants. The gradings by inspector1 for restaurant (I,II,III) are (71,55,84) and by the four other
inspectors in the same order are (65,57,86), (70,65,77),(72,69,70) and (76,64,85).
Perform two-way ANOVA with 5% significance to verify any significant differences among inspectors and restaurants over the cleanliness scores.

H0I: mean(1)=mean(2)=mean(3)=mean(4)=mean(5) (its concerning Inspectors)
H0R: mean(I)=mean(II)=mean(III). (its concerning restaurants)
H1I: At least one mean is different from other inspectors.
H1R: At least one mean is different from other restaurants.

"""
import numpy as np
from scipy.stats import f_oneway


gradings_inspector1 = np.array([71,55,84])
gradings_inspector2 = np.array([65,57,86])
gradings_inspector3 = np.array([70,65,77])
gradings_inspector4 = np.array([72,69,70])
gradings_inspector5 = np.array([76,64,85])

print("inspectors ",f_oneway(gradings_inspector1, gradings_inspector2, gradings_inspector3,gradings_inspector4,gradings_inspector5))

restaurant1 = np.array([71,65,70,72,76])
restaurant2 = np.array([55,57,65,69,64])
restaurant3 = np.array([84,86,77,70,85])

print("restaurant ",f_oneway(restaurant1, restaurant2, restaurant3))



