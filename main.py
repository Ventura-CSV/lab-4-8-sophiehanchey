def main():
    firstnum = int(input('Please input a number: '))
    
    # avoid error if first num is smaller than second
    while True:
        secondnum = int(input('Please enter a number larger than the first: '))
        
        if(secondnum<=firstnum):
            print('Error, the second number must be larger than the first')
            continue
        else:
            break
    
    # determine the prime numbers
    plist = []   
    for i in range(firstnum,secondnum+1):
        prime = True
        for j in range(2, i):
            quotient = i/j
            if quotient == int(quotient):
                prime = False
        
        if prime:
            plist.append(i)

    print(plist)
    return plist

if __name__ == '__main__':
    main()
