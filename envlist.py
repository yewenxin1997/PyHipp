#!/data/miniconda3/envs/env1/bin/python

from filelock import FileLock
import hickle
import sys

# set constants
file_path = "/data/picasso/envlist.hkl"
<<<<<<< HEAD
lock_path = "/data/picasso/envlist.hkl.lock"
=======
lock_path = "/data/picasso/envlist.khl.lock"
>>>>>>> upstream/master
time_out_secs = 60

# program modes
READ_MODE = 0
WRITE_MODE = 1
RESET_MODE = 2

# get number of arguments
nargs = len(sys.argv)
if nargs > 3:
    print('Usage: envlist; envlist env; envlist envprefix nenvs')
    exit
elif nargs > 2:
<<<<<<< HEAD
    # creates or re-creates the list of environments
    pmode = RESET_MODE
    # get prefix for environment name
    envprefix = sys.argv[1]
    # get number of environments to create
    nenvs = sys.argv[2]
elif nargs > 1:
    # returns env to the list of environments
    pmode = WRITE_MODE
    # get name of environment to return
    env = sys.argv[1]
else:
    # gets name of an environment to use
    pmode = READ_MODE

# creates a lock for the file so it can only be accessed one at a time
=======
    pmode = RESET_MODE
    envprefix = sys.argv[1]
    nenvs = sys.argv[2]
elif nargs > 1:
    pmode = WRITE_MODE
    env = sys.argv[1]
else:
    pmode = READ_MODE

>>>>>>> upstream/master
lock = FileLock(lock_path, timeout=time_out_secs)

with lock:
    if pmode == RESET_MODE:
<<<<<<< HEAD
        # create a list (named clist) of nevns environments with the 
        # prefix envprefix
        # add code here
        clist = ['cenv'+ str(i) for i in range(0,64)]
=======
        clist1 = [*range(0,int(nenvs),1)]
        clist = [envprefix + str(s) for s in clist1]
>>>>>>> upstream/master
    else:
        # load hickle file
        clist = hickle.load(file_path)

        if pmode == WRITE_MODE:
<<<<<<< HEAD
            # append env to the clist
            # add code here
            clist.append(env)
        else:
            # get and remove env from clist
            # add code here
            # return env name
            env = clist[0]
            del clist[0]
=======
            # append item to end of list
            clist.append(env)
        else:    
            # pop first item off list
            env = clist.pop(0)
            # return env name
>>>>>>> upstream/master
            print(env)

    # save hickle file
    hickle.dump(clist, file_path, mode="w")
