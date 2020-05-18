h = int(input())

m = int(input())

time = ["zero", "one", "two", "three", "four",
"five", "six", "seven", "eight", "nine",
"ten", "eleven", "twelve", "thirteen",
"fourteen", "fifteen", "sixteen",
"seventeen", "eighteen", "nineteen",
"twenty", "twenty one","twenty two",
"twenty three", "twenty four",
"twenty five", "twenty six", "twenty seven",
"twenty eight", "twenty nine"]

if m==0:
    print(time[h], "o' clock")
if m==1:
    print(time[m],"minute past",time[h])
if m>1 and m<30 and m!=15:
    print(time[m],"minutes past",time[h])
if m==15:
    print("quater past",time[h])
if m>30 and m!=45 and m!=59:
    print(time[60-m],"minutes to",time[h+1])
if m==45:
    print("quarter to",time[h+1])
if m==30:
    print("half past",time[h])
if m==59:
    print(time[60-m], "minute to", time[h])