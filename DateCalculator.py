

def switch(h):
    return{
        0:"Saturday",
        1:"Sunday",
        2:"Monday",
        3:"Tuesday",
        4:"Wednesday",
        5:"Thursday",
        6:"Friday",

    }[h]
def DateCalculator(day,month,year):
    if (month==1):
        month=13
        year=year-1

    if(month==2):
       month=14
       year=year-1

    q=day
    m=month
    k=year%100
    j=year//100
    h=q+13*(m+1)//5+k+k//4+j//4+5*j
    h=h%7
    print(DateCalculator(h))

DateCalculator(1,5,2025)

