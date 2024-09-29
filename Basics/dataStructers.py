#set
days={'sunday','monday','monday','tuesday','monday'}
print(days)
print('monday' in days)
days.add('thursday')
print(days)

#dictionary
grades={'sam':92,'beth':82}
print(grades)
grades['fred']=95
print(grades)
del grades['fred']
print(grades)
print(grades.keys())
print(list(grades.keys()))
print(list(grades.values()))