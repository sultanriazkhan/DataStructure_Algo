def remove_duplicates(lst):
   seen=set()
   result=[]
   for item in lst:
       if item not in seen:
           seen.add(item)
           result.append(item)
   return result
result=remove_duplicates([1,2,3,4,5,3,22,4,4,5,6])
print(result)