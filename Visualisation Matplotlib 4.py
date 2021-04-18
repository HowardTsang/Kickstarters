#1000117861	Ledr workbook: one tough journal!	Product Design	          Design	USD	08/10/2016	     1000	07/09/2016 13:14	47266	successful	549	US	11253	   47266	1000
#1366766769	:::Nadia Tykulsker/Spark(edIt) Arts 2014 Season:::	Dance	   Dance	USD	16/10/2013	     5500	16/09/2013 13:21	 5819	successful	123	US	5819	5819	5500
#1000120287	BB130A	Public Art	                                             Art	USD	24/03/2013	    25000	12/02/2013 01:07     1395	failed	     30	US	     1395	    1395	25000
#100012079	Chris Eger Band - New Nashville Record!	Music	               Music	USD	13/08/2014	    12000	14/07/2014 22:35	13260	successful	 92	US	13260	   13260	12000
#501846344	??????, n. Expat	Fiction	                              Publishing	USD	16/07/2011	    25000	03/06/2011 03:37	25385	successful	 41	US	25385	25385	25000
#451846041	??? CES!!! Geek Sputnik, going to CES 2013!! Webseries	Film & Video	USD	29/12/2012	     6000	03/12/2012 20:36	 6006	successful	 96	US	6006	6006	6000

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Film & Video','Publishing', 'Music', 'Art', 'Dance', 'Design'
backers = [96, 41, 92, 30, 123, 549]
explode = (0, 0, 0, 0.15, 0, 0)  # only "explode" the 4th slice (i.e. 'Art' - to show that it has the lowest backers as it is the only project that failed)

fig1, ax1 = plt.subplots()
ax1.pie(backers, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()