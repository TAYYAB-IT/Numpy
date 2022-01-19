import numpy as np
#x=np.array([[1,3,5],[2,4,6],[3,6,9]])
#print(x)
#print(x.shape)          #return (no. of rows,no.of coloumns)
#print(x.diagonal())
#arr1=np.array([0,3,5,2])
#arr2=np.array([2,4,6,3])
#print(f"{arr1}+{arr2}=",arr1+arr2)
#print(arr1.reshape(2,2))
#arr3=arr1.astype('bool')
#print(arr3)
#arr4=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#print(arr4.shape)
#print(arr4.size)
#iterate an array of any dimantional
#for x in np.nditer(arr4):
#    print(x)
#iterate an array of any dimantional with its position
#for pos,x in np.ndenumerate(arr4):
#    print(pos,'::',x)
#z=np.where(arr4==5) #if found then return position else reuturn empty position
#print(z)
#print(np.where(arr4%2==0))
#arr5=np.array([1,2,3,4,6,7,9])
#x = np.searchsorted(arr5,7)    #work for one dimantonal sorted array  ,can also get position to insert a number in it
#print(x)
#arr6=np.array([[2,3,2,1,0],[6,5,4,1,3]])
#sort an array
#arr6=np.sort(arr6)
#print(arr6)
#arr7=arr6.copy()
#print(arr7)
#print(arr7.base)  #will return None
#arr8=arr6.view()
#print(arr8)
#print(arr8.base) #will return base array
#####Filter an array
#arr9=np.array([1,2,3,4,5,6,7,8,9,10])
#For even numbers
#filter_array=arr9%2==0
#print(filter_array)
#even_array=arr9[filter_array]
#print(even_array)
#ar=np.array([1,3,2,'Usman']) #it will cast the type to string array