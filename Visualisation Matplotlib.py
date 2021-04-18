#100011318	My Moon - Animated Short Film	Animation	Film & Video	USD	03/05/2017	    50000	03/04/2017 17:11 57577.31	successful	840	US	10120	57577.31	50000
#1000115172	Daily Brew Coffee	Food Trucks	Food	GBP	31/03/2015	                         3500	01/03/2015 18:06	   21	failed	1	GB	    32.42	   31.09	5181.12
#1000117861	Ledr workbook: one tough journal!	Product Design	Design	USD	08/10/2016	     1000	07/09/2016 13:14	47266	successful	549	US	11253	   47266	1000
#1000120151	Feather Cast Furled Fly Fishing Leaders	Product Design	Design	AUD	22/08/2015	 2000	23/07/2015 03:09	 2000	successful	18AU  1473.62	 1427.35	1427.35
#1000120287	BB130A	Public Art	Art	USD	24/03/2013	                                        25000	12/02/2013 01:07     1395	failed	30	US	     1395	    1395	25000
#100012079	Chris Eger Band - New Nashville Record!	Music	Music	USD	13/08/2014	        12000	14/07/2014 22:35	13260	successful	92	US	13260	   13260	12000

import matplotlib.pyplot as plt
import numpy as np
pledged = [57577.31, 21, 47266, 2000, 1395, 13260]
goal = [50000, 3500, 1000, 2000, 25000, 12000]

plt.scatter(np.sort(pledged),np.sort(goal))

usd_pledged_real = [57577.31, 31.09, 47266, 1427.35, 1395, 13260]
usd_goal_real =  [50000, 5181.12, 1000, 1427.35, 25000, 12000]

plt.plot(np.sort(usd_pledged_real), np.sort(usd_goal_real), color = "red")

plt.title("Pledged vs Goal")
plt.xlabel("pledged values")
plt.ylabel("goal values")

plt.show()

