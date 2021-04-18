#Below is the selection of two Film & Video categories that are successful and with a high number of backers.
#The function is to illustrate the backers status of how many backers there are for successful projects in the Film & Video category.
#The below information was used in this function.
#1000104688	Permaculture Skills	            Webseries	Film & Video	successful	571
#100011318	My Moon - Animated Short Film	Animation	Film & Video	successful	840



def backers_status(x1, x2):
    result = x1 + x2
    return result

x1 = 571
x2 = 840

result = backers_status(x1, x2)
print("The sum amount of backers for these two projects are", result)


#As a result I have used functions to create reusable code for the data check of the backers status of the two successful projects in the Film & Video Category.