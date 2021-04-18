#100011318	My Moon - Animated Short Film	Animation	            Film & Video	USD	03/05/2017	    50000	03/04/2017 17:11 57577.31	successful	840	US	10120	57577.31	50000
#1000115172	Daily Brew Coffee	Food Trucks	                                Food	GBP	31/03/2015	     3500	01/03/2015 18:06	   21	failed	1	GB	    32.42	   31.09	5181.12
#1000117861	Ledr workbook: one tough journal!	Product Design	          Design	USD	08/10/2016	     1000	07/09/2016 13:14	47266	successful	549	US	11253	   47266	1000
#1366766769	:::Nadia Tykulsker/Spark(edIt) Arts 2014 Season:::	Dance	   Dance	USD	16/10/2013	     5500	16/09/2013 13:21	 5819	successful	123	US	5819	5819	5500
#1000120287	BB130A	Public Art	                                             Art	USD	24/03/2013	    25000	12/02/2013 01:07     1395	failed	30	US	     1395	    1395	25000
#100012079	Chris Eger Band - New Nashville Record!	Music	               Music	USD	13/08/2014	    12000	14/07/2014 22:35	13260	successful	92	US	13260	   13260	12000



usd_pledged_real = [57577.31, 31.09, 47266, 1427.35, 1395, 13260]
usd_goal_real =  [50000, 5181.12, 1000, 1427.35, 25000, 12000]


import matplotlib.pyplot as plt


labels = ['Film & Video', 'Food', 'Design', 'Dance', 'Art', 'Music']
pledged = [57577.31, 21, 47266, 5819, 1395, 13260]
goal = [50000, 3500, 1000, 5500, 25000, 12000]
pledged_std = [2, 3, 4, 1, 2, 4]
goal_std = [3, 5, 2, 3, 3, 7]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, pledged, width, yerr=pledged_std, label='Pledged')
ax.bar(labels, goal, width, yerr=goal_std, bottom=pledged,
       label='Goal')

ax.set_ylabel('Total Amount')
ax.set_title('Total Amount by Pledged vs Goal')
ax.legend()

plt.show()