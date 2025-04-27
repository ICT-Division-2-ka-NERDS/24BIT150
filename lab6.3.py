tup1=(6,1,2006)
tup2=(6,1,2008)
day1=tup1[0]+tup1[1]*30+tup1[2]*365
day2=tup2[0]+tup2[1]*30+tup2[2]*365
diff=abs(day2-day1)#abs stands for absolute value
print(diff)
