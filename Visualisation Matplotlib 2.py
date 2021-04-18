#1490952056	:: OOQI grips :: The Hyper-Galactic Bike Handlebar Grips	Product Design	     Design	USD	09/07/2011	12000	30/05/2011 15:17	 5996	failed	    102	US	5996	5996	12000
#1741086920	:: Waxed canvas Tote to go Bag ::	Design	                                     Design	NOK	05/02/2017	3000	06/01/2017 04:48	17810	successful	 51	NO	411.09	2125.45	358.02

#998190126	: TO ERADICATE.	Narrative Film	                                           Film & Video	USD	08/12/2012	50000	08/11/2012 20:00	15613	failed	     34	US	15613	15613	50000
#404957358	::::MERKATO::::	Documentary	                                               Film & Video	USD	11/10/2011	12000	26/08/2011 13:52	14710	successful	224	US	14710	14710	12000

#1682472511	?????????????Tears of the moon at dawn?	Performances	                          Dance	CAD	12/09/2015	4000	16/07/2015 06:55	  168	failed	      7	CA	131.92	128.96	3070.55
#1366766769	:::Nadia Tykulsker/Spark(edIt) Arts 2014 Season:::	Dance	                      Dance	USD	16/10/2013	5500	16/09/2013 13:21	 5819	successful	123	US	5819	5819	5500

#829563049	??????????? MUSIC ????????? CAPSULE -- an odyssey in a box	Music	              Music	EUR	14/12/2014	34500	14/11/2014 23:26	 1740	failed	     32	NL	2164.74	2136.54	42362.48
#1388490444	:: Show some love to the Lyric Everly EP ::	Music	                              Music	USD	02/04/2011	5000	01/03/2011 06:44	 5420	successful	 43	US	5420	5420	5000


import matplotlib.pyplot as plt
import numpy as np

labels = ['Design', 'Film & Video', 'Dance', 'Music']
successful = [51, 34, 7, 32]
failed = [102, 224, 123, 43]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, successful, width, label='Successful Backers')
rects2 = ax.bar(x + width/2, failed, width, label='Failed Backers')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Amount of Backers')
ax.set_title('Backers by Main Category')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

