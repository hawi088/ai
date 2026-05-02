import pandas as pd
#Data from dictionary
data = {
    "Name": ['SpongeBob', 'Patrick' , 'Squidbird'], #column 1
    "Age"  : [30 ,35 , 50] #column 2 

}

df  = pd.DataFrame(data)

# print(df.iloc[1])
print(df)
print("===========================")
list_data = [10,20,30,40,50]
series = pd.Series(list_data)
print(series)