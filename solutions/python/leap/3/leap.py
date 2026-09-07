def leap_year(year):
    '''This function returns a bool value based on if the year passed in the parameter is      a leap year or not.
    parameter(int): The year you want to check if it's a leap year or not.
    return(bool): returns a bool value.
    '''
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False
