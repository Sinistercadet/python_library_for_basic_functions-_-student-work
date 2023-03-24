
def max(a):
    
	

    c = a[0]

    for q in range(1,len(a)):     # max value of list
    	

		
	    if a[q]>c:
	    	c = a[q]
	

      
    return c
		

def min(a):
	  
    c = a[0]
	  

    for q in range(1,len(a)):          #min value of list
    	
    	
		
	    if a[q]<c:
	    	
	    	c = a[q]
	
    return c
    
def Isort(a):
	newlist = []
	for i in range(0,len(a))  :                #Insertion sort
		num =0
		for j in range(0,len(newlist)):
			if a[i] > newlist[j]:
				num+=1
			else:
				break
		newlist.insert(num,a[i])
	print (newlist)

					
	
	
def insert(list,index,element):
	list.append('')
	for i in range(len(list)-1,index,-1):
		list[i]=list[i-1]
	list[index] = element
	print (list)
		
	
def insertl(list,index,elements_list):
	for i in range(0,len(elements_list)):
		insert(list,index+i,elements_list[i])
	print(list)
	
zv = 0
def rf(code,endv,updation = 1,loop_runner = zv):
	global zv
		
	if zv < endv:      #use zv variable for loop variable
		exec(code)
		zv=zv+updation
		rf(code,endv)
	else:
		print("Execution Successful.")
		zv = 0
		return 1
    

rf('''print("hello")''',9) #prefer docstring for code