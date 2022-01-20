##integer reversion 


def integer_reverse(num):
    
    remainder = 0
    reverse_number = 0

    while num>0:
        remainder = num%10
        reverse_number = reverse_number*10 + remainder
        num = num//10

    return reverse_number

if __name__=="__main__":
    print(integer_reverse(123456))