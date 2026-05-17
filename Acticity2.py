# Program to check if a number is power of 4

def powerOf4(number):

    count = 0

    #if only 1 set bit exist
    if (number %(~(number &(number - 1)))):

        #count 0 bits 1 set bit
        while(number > 1):
            number >>=1
            count += 1

    # If count is even return true else false
    if(count % 2 == 0):
        return True
    else:
        return False
    
number = int(input("Enter your number : "))
if(powerOf4(number)):
    print(number, 'is a power of 4')
