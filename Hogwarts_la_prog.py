#Hogwarts_report
#extra_function_to_calc_grade
def gv(x):
        if x=="A":
                return(10)
        if x=="AB":
                return(9)
        if x=="B":
                return(8)
        if x=="BC":
                return(7)
        if x=="C":
                return(6)
        if x=="CD":
                return(5)
        if x=="D":
                return(4)

#dictionaries_to_be_used_later
grade_sum={}
course_count={}
name={}

#Course_Input
course=input()
course_d=input()
break_input=input()
while (break_input!="Students"):
    break_input=input()
    
#Student_Input
roll,stu_name=input().split('~')
name[roll]=stu_name
grade_sum[roll]=0
course_count[roll]=0
break_input=input()
while('~' in break_input):
    roll,stu_name=break_input.split('~')
    name[roll]=stu_name
    grade_sum[roll]=0
    course_count[roll]=0
    break_input=input()
    
#Grades_Input
code,sem,year,r,grade=input().split('~')
if r in grade_sum.keys():
    grade_sum[r]=grade_sum[r]+gv(grade)
    course_count[r]+=1
break_input=input()
while (break_input!="EndOfInput"):
    code,sem,year,r,grade=break_input.split('~')
    if r in grade_sum.keys():
        grade_sum[r]=grade_sum[r]+gv(grade)
        course_count[r]+=1
    break_input=input()
    
#Final_result
srt_r=sorted(name)
for key in srt_r:
    if grade_sum[key]!=0:
        ans=round((grade_sum[key]/course_count[key]),2)
        print(key+"~"+name[key]+"~"+str(ans))
    else:
        print(key+"~"+name[key]+"~"+"0")