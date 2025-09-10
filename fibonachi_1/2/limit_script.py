with open("limit_file.txt", "r") as file:
   line_one=file.readline()
   steps=file.readline()
   limit_start = file.readline()
   limit_end=file.readline()
line_one=line_one.split()

array=[float(i) for i in line_one]
steps=float(steps)
limit_end=float(limit_end)
limit_start=float(limit_start)
def fibonaci(steps, array, limit_end,limit_start):
    while steps > 0:
        next_number=array[-1]+array[-2]
        if next_number > limit_end:
            break
        array.append(next_number)
        steps-=1

    filtered = []
    for num in array:
        if num > limit_start:
            filtered.append(num)
    return filtered

with open("limit_result.txt", "w") as file:
    result = fibonaci(steps, array, limit_end, limit_start)
    file.write(str(result) + "\n")

