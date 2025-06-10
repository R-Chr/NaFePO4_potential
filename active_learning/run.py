from vitrum.batch_active.learning import balace
import pickle
import os

try:
    ace.run()
except NameError:
    if os.path.isfile("balace.pickle"):
        file = open("balace.pickle",'rb')
        ace = pickle.load(file)
        ace.read_config()
    else:
        ace = balace()
    ace.run()
