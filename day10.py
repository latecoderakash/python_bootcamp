#function with ouput

# def format_name(f_name,l_name):
#     format_1=f_name.title()
#     format_2=l_name.title()
#     return f"{format_1} {format_2}"

# print(format_name("Aash", "KUMAR"))

#leap year program

def is_leap_year(year):

    if year % 4 != 0:
        return False

    elif year % 100 != 0:
        return True

    elif year % 400 == 0:
        return True

    else:
        return False


print(is_leap_year(2400))
