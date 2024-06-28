def main():
    plist = []
    
    firstnum = int(input('Please input a number: '))
    
    # avoid error if first num is smaller than second
    while True:
        secondnum = int(input('Please enter a number smaller than the first: '))
        
        if(secondnum>=firstnum):
            print('Error, the second number must be smaller than the first')
            continue
        else:
            break
        
    # create list of all number in between the two values(inclusive)
    list = []
    for i in range(firstnum + 1 - secondnum):
        list.append(secondnum + i)
    
    print(list)

    return plist


if __name__ == '__main__':
    main()
