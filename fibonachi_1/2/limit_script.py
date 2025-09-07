with open("limit_file.txt", "r") as file:
   line_one=file.readline()
   steps=file.readline()
   limit=file.readline()
array=[]
line_one=line_one.split()
for i in line_one:
    array.append(i)
    array=[float(i) for i in array]
for i in steps and limit:
    steps=float(steps)
    limit=float(limit)
def fibonaci(steps, array, limit):
    if steps==0:
        return array
    if(limit>= array[-1]):
     array.append(array[-1]+ array[-2])
     steps-=1
    elif(limit<array[-1]):
        array.pop(-1)
        return array
    return fibonaci(steps, array,limit)
with open("limit_result.txt", "w") as file:
    file.write(str(fibonaci(steps, array,limit)))
    file.write("\n")
