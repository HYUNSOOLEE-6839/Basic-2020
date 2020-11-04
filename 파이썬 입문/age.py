import datetime
datetime.datetime.now()

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

birth_year, birth_month, birth_day = map(int,input('생일입력>').split())

if current_month > birth_month: 
    age = current_year - birth_year
elif current_month < birth_month : 
    age = current_year - birth_year - 1
else:            
    if current_day < birth_day:  
        age = current_year - birth_year -1
    elif current_day < birth_day:  
        age = current_year - birth_year - 1
    else:
        age = current_year - birth_year
print('만 나이는 %d 입니다.' %age)