# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Working with pickle and error handling
# Companion file is datafile.txt which should be included in the same file path
# ChangeLog (Who,When,What):
# JGrove 11.21.19 created file
# ------------------------------------------------------------------------ #

import pickle

##See all the data you imported
fh=open('datafile.txt','rb')
teamlist=pickle.load(fh)
fh.close()
#pickle.load(positionlist,fh)

#Select the section you would like to see reprinted
strOpt=input ("Press Y if you would like to see the team list. Press N if you would like to exit")
try:
    if strOpt.lower() is "y":
        print(teamlist)
    elif strOpt is "N":
        exit()
    else:
        raise
except: print("Please Pick Y or N")




