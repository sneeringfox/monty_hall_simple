import random as r
def i():
    return r.randrange(2,4)
door = ["car","goat","goat"]
s = input("Pick a door 1 - 2 - 3 :")
if(s == 1):
    n = i()-1
    print "door %d has %s" % (n,door[n])
s = input("switch from %d" % (s) )
print "door you picked contains %s" % (door[s])
    
    
