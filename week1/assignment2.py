import numpy as np
#Array manipulation

arr= np.arange(25).reshape(5,5)
print(arr)
print('================')
print(arr[:,-1])
print('================')
print(arr[::2])
print('================')
mask = arr%2 == 0
print(arr[mask])

#Conditional repalcement
temps = np.random.randint(-10, 40, (7, 24))  # Week of hourly temps
#Replace all temps below 0 with 0
print(temps)
print('=================')
positive = np.where(temps > 0 , temps , 0)
print(positive)

#Replace all temps above 35 with 35

print('====================')
above_thiry_five = np.where(temps< 35,temps ,35)
print(above_thiry_five)

#Create mask for "pleasant" temps (18 - 25)

mask2 = (temps >= 18 ) & (temps <=35)
print(temps[mask2])


#Golf scores
np.random.seed(42)
scores = np.random.randint(70,100,(10,18))
print('========================')
print(scores)
best_score_per_hole = scores.min(axis=0) #axis=0 mean doewn the row
print('=========================')
print(best_score_per_hole)
print('===========================')
print(best_score_per_hole.shape)

print('=================')
worst = scores.sum(axis=1)
print(worst)
print('=================')
worst_player = worst.argmax() #the index
print(worst_player)
print('===============')
worst_player_result = worst.max()
print(worst_player_result)
print('===================')
holes_below_80 = np.all(scores<80,axis=0)
print(holes_below_80)