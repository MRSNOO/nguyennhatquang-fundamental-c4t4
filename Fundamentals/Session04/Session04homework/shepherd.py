sheepsize=[5,16,28,68,90,149,178,250,350,500]
print("""
Hello, my name is Quang and these are my sheep sizes:
""")
max1= max(sheepsize)
print(sheepsize)
monthnow=1
print("Now my biggest sheep has size {0} lets shear it".format(max1))
for i in range (len(sheepsize)):
    if sheepsize[i] == max1:
            sheepsize[i]=8
print("After shearing here is my flock")
print(sheepsize)
n = int(input("Number of Months"))
s=0

while monthnow<=n:
    print ("""
    Month{0}:
One month has passed, now here is my flock
    """.format(monthnow))
    for i in range (len(sheepsize)):
        sheepsize[i]+=50
    print(sheepsize)
    max2 = max(sheepsize)
    max2=int(max2)
    print("Now my biggest sheep has size {0} lets shear it".format(max2))
    for i in range (len(sheepsize)):
        if sheepsize[i] == max2:
            sheepsize[i]=8
    print("After shearing here is my flock")
    print(sheepsize)
    for i in range(len(sheepsize)):
        s=s+sheepsize[i]

    monthnow+=1
print()
print("My flock has size in total:",s)
print("I would get {0}*2$ = ".format(s),s*2,"$")