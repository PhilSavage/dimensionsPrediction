from sklearn import tree
import random

clf = tree.DecisionTreeClassifier()

X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]

Y = ['male','male','female','female','male','male','female','female','female','male','male']

clf = clf.fit(X,Y)

i = 1

numberpredictions = int(raw_input('How many predictions?'))

if numberpredictions > 0:
    while i <= numberpredictions:
        persondimension = random.randrange(150,190),random.randrange(50,90),random.randrange(37,48)
        prediction = clf.predict([persondimension])
        i +=1
        print persondimension
        print prediction

    if numberpredictions > 1:
        print('Here are '+str(numberpredictions)+' predictions')
    else:
        print('Here is ' + str(numberpredictions) + ' prediction')
else:
    print('Go on waste your time then!')
