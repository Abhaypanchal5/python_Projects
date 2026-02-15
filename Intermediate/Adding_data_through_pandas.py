import pandas as pd

data = pd.read_csv("file path")  #enter the file in the place of file to access the file to read

#Create variable u want to insert into csv file using user input(i am using 3 varible in my case)

name = input("Enter your name: ")            
marks = input("Enter your marks: ")
city = input("Enter your city: ")

# farme the data according to your csv file 

newdata = pd.DataFrame({"name":[name],"marks":[marks],"city":[city]})

# concate the newdata with old data (if any) 

data = pd.concat([data,newdata],ignore_index=True)

# now push the new data to the file 

data.to_csv("File path",index=False)  # enter the file path if file is located else where or file name if in the same folder
 
print("data added!!!!") # print a conformation msg

