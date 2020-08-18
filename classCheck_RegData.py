import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from collections import defaultdict
 
def getSlots(start, end): 
	beg=int(str(start)[0:2])
	fin=int(str(end)[0:2])
	if(beg<8) :
		beg+=12
	if(fin<8) :
		fin+=12
	beg-=7
	fin-=7
	if str(end)[3:5] == "00":
		fin-=1
	slots=[i for i in range(beg,fin+1)]
 
	return slots

def getCourse(sub,cat,a,b,c):
	if a=="nan" :
		a=""
	if b=="nan" :
		b=""
	if c=="nan" :
		c=""
	
	return sub+cat+a+b+c
 
def getDays(days):
	res = []
	for i in days:
		res+=[str(i)]
		if(i=='H'):
			res.pop()
			res[-1]+="H"
	return res
 
def remspace(temp):
    res=''
    j=0;
    for i in temp:
        j=j+1
        if i<='A' or i>='Z':
            return res[0:j]
    return res
 
#df = pd.read_excel('timetable.xls',sheet_name=0)
#stu = pd.read_excel('clash.xlsx',sheet_name=0)
 
df = pd.read_excel('timetable.xls',sheet_name=0)
stu = pd.read_excel('student.xls',sheet_name=0)
 
timemap = defaultdict(list)
classnmbr_map = {}
for i in df.index:
    classnmbr_map[df['Subject'][i]+df['Catalog'][i].strip()+df['Section'][i]]=df['Class Nbr'][i]
for i in df.index:
	if pd.isnull(df.loc[i, 'Class Pattern']) == False:
		if (df['Class Pattern'][i],getSlots(str(df['Mtg Start'][i]),df['End time'][i])) in timemap[df['Subject'][i]+df['Catalog'][i]+df['Section'][i]]:
			dfdfd=1
		else:
			timemap[df['Subject'][i]+df['Catalog'][i]+df['Section'][i]].append((df['Class Pattern'][i],getSlots(str(df['Mtg Start'][i]),df['End time'][i]))) 
# timemap = {df['Subject'][i]+df['Catalog'][i]+df['Section'][i]:(df['Class Pattern'][i],getSlots(str(df['Mtg Start'][i]),df['End time'][i])) for i in df.index if not pd.isnull(df.loc[i, 'Class Pattern'])}
'''
for keys,values in timemap.items():
    print(keys)
    print(values)
'''
 
kids=[]
for i in stu.index:
	if pd.isnull(stu.loc[i,'Project Section No']) and pd.isnull(stu.loc[i,'Thesis section']) and pd.isnull(stu.loc[i,'Graded Component']):
		kids+=[(stu['ID'][i],getCourse(str(stu['Subject'][i]),str(stu['Catalog'][i]),str(stu['Lecture Section No'][i]),str(stu['Practical Section No'][i]),str(stu['Tutorial Section No'][i])))] 
kids.sort()
 
# kids = sorted((stu['ID'][i],getCourse(str(stu['Subject'][i]),str(stu['Catalog'][i]),str(stu['Lecture Section No'][i]),str(stu['Practical Section No'][i]),str(stu['Tutorial Section No'][i]),str(stu['Project Section No'][i]),str(stu['Thesis section'][i]) )) for i in stu.index)
 
#print kids
itr = 0
while itr<len(kids):
	stu_id = kids[itr][0]
	 
	
	ttable = {}
	while itr<len(kids) and kids[itr][0] == stu_id:
		
		#print(kids[itr][1])
		timemap_list = timemap[kids[itr][1]] 
		for days , slots in timemap_list:
			days = getDays(days)
			for i in days:
				for j in slots:
					if(i,j) in ttable:
						ttable[(i,j)] += [kids[itr][1]]
					else :
						ttable[(i,j)] = [kids[itr][1]] 
		itr += 1	
	
	free = 1
	
	uni = []		
	for i in ttable:
		if len(ttable[i]) > 1:
			free = 0
			#print ("On Day : " + str(i[0]) + " during slot : "+str(i[1]))
			if ttable[i] not in uni:
				uni.append(ttable[i])
			#print (ttable[i])
	if free==False:
		print ("For student ID: " + str(stu_id))
		for x in uni:
			t = x[0].split()
			u = x[1].split()
			print(str(classnmbr_map[t[0]+t[1]])+" "+t[0]+" "+t[1]+" , "+str(classnmbr_map[u[0]+u[1]])+" "+u[0]+" "+u[1])
			#print(x[0]+" , "+x[1])
		print ("--------------------------------------\n" )
	#else:
		#print ("For student ID: " + str(stu_id)) 
 
'''	print "For student ID: " + str(stu_id) + "\n"
	print "-------------------------------" 
	for i in ttable:
		print i
	print "-------------------------------" 
'''
