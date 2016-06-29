import csv
import math
day_order=('M','T','W','R','F','S')
classes=('1','2','3','4','n','5','6','7','8','9','a','b','c','d')
classes_order=['M1', 'M2', 'M3', 'M4', 'Mn', 'M5', 'M6', 'M7', 'M8', 'M9', 'Ma', 'Mb', 'Mc', 'Md', 'T1', 'T2', 'T3', 'T4', 'Tn', 'T5', 'T6', 'T7', 'T8', 'T9', 'Ta', 'Tb', 'Tc', 'Td', 'W1', 'W2', 'W3', 'W4', 'Wn', 'W5', 'W6', 'W7', 'W8', 'W9', 'Wa', 'Wb', 'Wc', 'Wd', 'R1', 'R2', 'R3', 'R4', 'Rn', 'R5', 'R6', 'R7', 'R8', 'R9', 'Ra', 'Rb', 'Rc', 'Rd', 'F1', 'F2', 'F3', 'F4', 'Fn', 'F5', 'F6', 'F7', 'F8', 'F9', 'Fa', 'Fb', 'Fc', 'Fd', 'S1', 'S2', 'S3', 'S4', 'Sn', 'S5', 'S6', 'S7', 'S8', 'S9', 'Sa', 'Sb', 'Sc', 'Sd']
reverse_classes_order=['Sd', 'Sc', 'Sb', 'Sa', 'S9', 'S8', 'S7', 'S6', 'S5', 'Sn', 'S4', 'S3', 'S2', 'S1', 'Fd', 'Fc', 'Fb', 'Fa', 'F9', 'F8', 'F7', 'F6', 'F5', 'Fn', 'F4', 'F3', 'F2', 'F1', 'Rd', 'Rc', 'Rb', 'Ra', 'R9', 'R8', 'R7', 'R6', 'R5', 'Rn', 'R4', 'R3', 'R2', 'R1', 'Wd', 'Wc', 'Wb', 'Wa', 'W9', 'W8', 'W7', 'W6', 'W5', 'Wn', 'W4', 'W3', 'W2', 'W1', 'Td', 'Tc', 'Tb', 'Ta', 'T9', 'T8', 'T7', 'T6', 'T5', 'Tn', 'T4', 'T3', 'T2', 'T1', 'Md', 'Mc', 'Mb', 'Ma', 'M9', 'M8', 'M7', 'M6', 'M5', 'Mn', 'M4', 'M3', 'M2', 'M1']
mon_to_fri=['M1', 'M2', 'M3', 'M4', 'Mn', 'M5', 'M6', 'M7', 'M8', 'M9', 'Ma', 'Mb', 'Mc', 'Md', 'T1', 'T2', 'T3', 'T4', 'Tn', 'T5', 'T6', 'T7', 'T8', 'T9', 'Ta', 'Tb', 'Tc', 'Td', 'W1', 'W2', 'W3', 'W4', 'Wn', 'W5', 'W6', 'W7', 'W8', 'W9', 'Wa', 'Wb', 'Wc', 'Wd', 'R1', 'R2', 'R3', 'R4', 'Rn', 'R5', 'R6', 'R7', 'R8', 'R9', 'Ra', 'Rb', 'Rc', 'Rd', 'F1', 'F2', 'F3', 'F4', 'Fn', 'F5', 'F6', 'F7', 'F8', 'F9', 'Fa', 'Fb', 'Fc', 'Fd']

file={'M':{'M1':[],'M2':[],'M3':[],'M4':[],'Mn':[],'M5':[],'M6':[],'M7':[],'M8':[],'M9':[],'Ma':[],'Mb':[],'Mc':[],'Md':[]},'T':{'T1':[],'T2':[],'T3':[],'T4':[],'Tn':[],'T5':[],'T6':[],'T7':[],'T8':[],'T9':[],'Ta':[],'Tb':[],'Tc':[],'Td':[]},'W':{'W1':[],'W2':[],'W3':[],'W4':[],'Wn':[],'W5':[],'W6':[],'W7':[],'W8':[],'W9':[],'Wa':[],'Wb':[],'Wc':[],'Wd':[]},'R':{'R1':[],'R2':[],'R3':[],'R4':[],'Rn':[],'R5':[],'R6':[],'R7':[],'R8':[],'R9':[],'Ra':[],'Rb':[],'Rc':[],'Rd':[]},'F':{'F1':[],'F2':[],'F3':[],'F4':[],'Fn':[],'F5':[],'F6':[],'F7':[],'F8':[],'F9':[],'Fa':[],'Fb':[],'Fc':[],'Fd':[]},'S':{'S1':[],'S2':[],'S3':[],'S4':[],'Sn':[],'S5':[],'S6':[],'S7':[],'S8':[],'S9':[],'Sa':[],'Sb':[],'Sc':[],'Sd':[]}}
accumulated_file={'M':{'M1':[],'M2':[],'M3':[],'M4':[],'Mn':[],'M5':[],'M6':[],'M7':[],'M8':[],'M9':[],'Ma':[],'Mb':[],'Mc':[],'Md':[]},'T':{'T1':[],'T2':[],'T3':[],'T4':[],'Tn':[],'T5':[],'T6':[],'T7':[],'T8':[],'T9':[],'Ta':[],'Tb':[],'Tc':[],'Td':[]},'W':{'W1':[],'W2':[],'W3':[],'W4':[],'Wn':[],'W5':[],'W6':[],'W7':[],'W8':[],'W9':[],'Wa':[],'Wb':[],'Wc':[],'Wd':[]},'R':{'R1':[],'R2':[],'R3':[],'R4':[],'Rn':[],'R5':[],'R6':[],'R7':[],'R8':[],'R9':[],'Ra':[],'Rb':[],'Rc':[],'Rd':[]},'F':{'F1':[],'F2':[],'F3':[],'F4':[],'Fn':[],'F5':[],'F6':[],'F7':[],'F8':[],'F9':[],'Fa':[],'Fb':[],'Fc':[],'Fd':[]},'S':{'S1':[],'S2':[],'S3':[],'S4':[],'Sn':[],'S5':[],'S6':[],'S7':[],'S8':[],'S9':[],'Sa':[],'Sb':[],'Sc':[],'Sd':[]}}
maxcurrent_file={'M':{'M1':[],'M2':[],'M3':[],'M4':[],'Mn':[],'M5':[],'M6':[],'M7':[],'M8':[],'M9':[],'Ma':[],'Mb':[],'Mc':[],'Md':[]},'T':{'T1':[],'T2':[],'T3':[],'T4':[],'Tn':[],'T5':[],'T6':[],'T7':[],'T8':[],'T9':[],'Ta':[],'Tb':[],'Tc':[],'Td':[]},'W':{'W1':[],'W2':[],'W3':[],'W4':[],'Wn':[],'W5':[],'W6':[],'W7':[],'W8':[],'W9':[],'Wa':[],'Wb':[],'Wc':[],'Wd':[]},'R':{'R1':[],'R2':[],'R3':[],'R4':[],'Rn':[],'R5':[],'R6':[],'R7':[],'R8':[],'R9':[],'Ra':[],'Rb':[],'Rc':[],'Rd':[]},'F':{'F1':[],'F2':[],'F3':[],'F4':[],'Fn':[],'F5':[],'F6':[],'F7':[],'F8':[],'F9':[],'Fa':[],'Fb':[],'Fc':[],'Fd':[]},'S':{'S1':[],'S2':[],'S3':[],'S4':[],'Sn':[],'S5':[],'S6':[],'S7':[],'S8':[],'S9':[],'Sa':[],'Sb':[],'Sc':[],'Sd':[]}}
normalized_file={'M':{'M1':[],'M2':[],'M3':[],'M4':[],'Mn':[],'M5':[],'M6':[],'M7':[],'M8':[],'M9':[],'Ma':[],'Mb':[],'Mc':[],'Md':[]},'T':{'T1':[],'T2':[],'T3':[],'T4':[],'Tn':[],'T5':[],'T6':[],'T7':[],'T8':[],'T9':[],'Ta':[],'Tb':[],'Tc':[],'Td':[]},'W':{'W1':[],'W2':[],'W3':[],'W4':[],'Wn':[],'W5':[],'W6':[],'W7':[],'W8':[],'W9':[],'Wa':[],'Wb':[],'Wc':[],'Wd':[]},'R':{'R1':[],'R2':[],'R3':[],'R4':[],'Rn':[],'R5':[],'R6':[],'R7':[],'R8':[],'R9':[],'Ra':[],'Rb':[],'Rc':[],'Rd':[]},'F':{'F1':[],'F2':[],'F3':[],'F4':[],'Fn':[],'F5':[],'F6':[],'F7':[],'F8':[],'F9':[],'Fa':[],'Fb':[],'Fc':[],'Fd':[]},'S':{'S1':[],'S2':[],'S3':[],'S4':[],'Sn':[],'S5':[],'S6':[],'S7':[],'S8':[],'S9':[],'Sa':[],'Sb':[],'Sc':[],'Sd':[]}}
class_importance={}

f = open('103summerv3.csv', 'r')


#print file

print('CSV FILE:')
'''
for row in csv.reader(f):
        print(row[0],':',row[1])
f.seek(0)
'''




#put +-value to the first and the last class

r=0
for row in csv.reader(f):
        r=0
        for x in range(int((len(row[0])-2)/2)):
            if row[0][0]!=row[0][2*(x+1)]:
                file[row[0][2*x+2]][row[0][2*x+2:2*x+4]].append(float(row[1]))
                file[row[0][2*x]][row[0][2*x:2*x+2]].append(-float(row[1]))
                if len(row[0])-(2*x+2)==2:
                    file[row[0][0]][row[0][0:2]].append(float(row[1]))
                    file[row[0][len(row[0])-2]][row[0][len(row[0])-2:len(row[0])]].append(-float(row[1]))
                    r=1
                if 2*x==0:
                        file[row[0][0]][row[0][0:2]].append(float(row[1]))
                        file[row[0][len(row[0])-2]][row[0][len(row[0])-2:len(row[0])]].append(-float(row[1]))
                        r=1
                break
        if r==0:
                file[row[0][0]][row[0][0:2]].append(float(row[1]))
                file[row[0][len(row[0])-2]][row[0][len(row[0])-2:len(row[0])]].append(-float(row[1]))

'''
for each_class in classes_order:
    print(each_class,":",file[each_class[0]][each_class])
'''

print("ACCUMULATING.....")






#accumulating all the positives and negatives

for days_in_week in file.keys():
    for key, valuelist in file[days_in_week].items():
        negative_value=0
        positive_value=0
        for value in valuelist:
            if value<0:
                negative_value+=value
            else:
                positive_value+=value
        if negative_value!=0:
            accumulated_file[days_in_week][key].append(negative_value)
        if positive_value!=0:
            accumulated_file[days_in_week][key].append(positive_value)

'''
for each_class in classes_order:
    print(each_class,":",accumulated_file[each_class[0]][each_class])
'''
print('REDIRECTING.....')




#redirect all the negatives to next classes

for key in reverse_classes_order:
        if key[1]!='d':
                for each_value in accumulated_file[key[0]][key]:
                        if each_value<0:
                                if key[1]=='1':
                                    nextclass='2'
                                if key[1]=='2':
                                    nextclass='3'
                                if key[1]=='3':
                                    nextclass='4'
                                if key[1]=='4':
                                    nextclass='n'
                                if key[1]=='n':
                                    nextclass='5'
                                if key[1]=='5':
                                    nextclass='6'
                                if key[1]=='6':
                                    nextclass='7'
                                if key[1]=='7':
                                    nextclass='8'
                                if key[1]=='8':
                                    nextclass='9'
                                if key[1]=='9':
                                    nextclass='a'
                                if key[1]=='a':
                                    nextclass='b'
                                if key[1]=='b':
                                    nextclass='c'
                                if key[1]=='c':
                                    nextclass='d'
                                newkey=key[0]+nextclass
                                accumulated_file[newkey[0]][newkey].append(each_value)
                                accumulated_file[key[0]][key].remove(each_value)

'''
for each_class in classes_order:
    print(each_class,":",accumulated_file[each_class[0]][each_class])
'''
print('CALCULATING MAX CURRENT.....')





#find the max in the list for the max current in each class breaktime

templist=[]
for each_class in classes_order:
        templist=[]
        for each_value in accumulated_file[each_class[0]][each_class]:
                templist.append(int(math.fabs(each_value)))
        if len(accumulated_file[each_class[0]][each_class])!=0:
                maxcurrent_file[each_class[0]][each_class].append(max(templist))

'''
for each_class in classes_order:
    print(each_class,":",maxcurrent_file[each_class[0]][each_class])
'''
print('NORMALIZATION.....')




#nornalize data from Monday to Friday

maxvalue=0
for key in mon_to_fri:
        for value in maxcurrent_file[key[0]][key]:
                if value>maxvalue:
                        maxvalue=value
print('maxvalue=',maxvalue)
for key in mon_to_fri:
        for value in maxcurrent_file[key[0]][key]:
                normalized_file[key[0]][key].append(1/((value/maxvalue)*4+1))
     
'''
for each_class in classes_order:
    print(each_class,":",normalized_file[each_class[0]][each_class])
'''

'''
total=0
for key in mon_to_fri:
        for value in normalized_file[key[0]][key]:
                total+=value
print('total=',total)                
'''

#calculate importancy for each class in every weeks
for each_class in classes:
        sum_of_class=0
        for key in mon_to_fri:
                if key[1]==each_class:
                        for value in maxcurrent_file[key[0]][key]:
                                sum_of_class+=value
        class_importance[each_class]=sum_of_class
        #print(each_class,':',sum_of_class)





#CHECKING:
'''
for each_class in classes_order:
        print(each_class,":",file[each_class[0]][each_class],accumulated_file[each_class[0]][each_class],maxcurrent_file[each_class[0]][each_class])
'''

nf = open('heartbeat.txt', 'w', encoding = 'UTF-8')
for key in mon_to_fri:
        for value in normalized_file[key[0]][key]:
                nf.write(str(value)+'\n')
nf.close()
