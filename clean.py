import pandas as pd
from operator import itemgetter

def loop(log,i,att):
    total = 0
    for i in range(0,i+1):
        total += log[i][att]
    return total

def clean(log):
    
    data = log
    i=0
    #while i <len(log)-1:
     #   if data[i][0] == data[i+1][0]:
      #      data.remove(data[i])
       # i=i+1

    #count of each step
    #for i in range(1,len(data)):
        #data[i][1] = data[i][1] - loop(data,i-1,1)
        #data[i][2] = data[i][2] - loop(data,i-1,2)
        
    data = sorted(data, key=itemgetter(0))
    
    #cumulative
    remove=[]
    for i in range(0,len(data)-1):
        if data[i][0] == data[i+1][0]:
            data[i+1][1] += data[i][1]
            data[i+1][2] += data[i][2]
            remove.append(i)
    remove.sort(reverse=True)
    for i in remove:
        data.pop(i)

    data = pd.DataFrame(data,columns=['file name','clicks','time'])
    for i in range(0,len(data)):
        if data['file name'][i] == '':
            data = data.drop(i)
    data['file cat']='others'

    data = data.reset_index()
    data = data.drop(columns=['index'])
    #data = file_type.get_file_type(data)
    
    #print(data) ##send to database

    return data