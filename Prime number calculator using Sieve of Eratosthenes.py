def userinput() :
    userinput_function = eval(input())
    return userinput_function
def prime_number_list_maker(par1,par2) :
    prime_list = []
    for x in range(par1,par2+1,1) :
        prime_list = prime_list + [x]
    return prime_list
def prime_numbers_finder(par1,par2,par3) :
    list1 = par3[:]
    for diviser in range(2,par2+1,1) :
        index = 0
        for dividend in list1 :
            if dividend != 0 :
                if diviser < dividend :
                    remainder = dividend % diviser
                    if remainder == 0 :
                        list1[index] = 0
            index = index + 1
    result = []
    for x1 in list1 :
        if x1 > 1 :
            result = result + [x1]
    return result
def main() :
    print('================================================================+')
    print('* Please enter a positive integer : ',end = '')
    userinput1 = userinput()
    print('* Please enter another positive integer : ',end = '')
    userinput2 = userinput()
    if userinput1 > userinput2 :
        smaller_number = userinput2
        userinput2 = userinput1
        userinput1 = smaller_number
    print()
    print('>> Calculating, please wait...',end='')
    start_time = time()
    prime_number_list = prime_number_list_maker(userinput1,userinput2)
    user_result = prime_numbers_finder(userinput1,userinput2,prime_number_list)
    finish_time = time()
    print()
    print()
    print('>> PRIME NUMBERS : ',user_result)
    print()
    print('>> Total time taken for calculation : ',finish_time - start_time,'second/s')
    print()
    print('>> Total number of prime numbers between',userinput1,'and',userinput2,': ',len(user_result))
    print('================================================================+')
    print()
from time import time
done = False
print()
print('  +-------------------    PRIME NUMBER CALCULATOR   ---------------------+')
print('                        Using Sieve of Eratosthenes')
print()
while not done :
    done2 = False
    main()
    while not done2 :
        userinputx = input('* Press C to Continue or Press E to Exit : ')
        if userinputx == 'c' or userinputx == 'C' :
            done2 = True
            print()
        elif userinputx == 'e' or userinputx == 'E' :
            done = True
            done2 = True
            print()
        else :
            print()
            print('                     >>>>  WRONG INPUT !  <<<<')
            print()
