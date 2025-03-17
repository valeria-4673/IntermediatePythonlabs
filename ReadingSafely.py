def read_int(prompt, min, max):
    
    v = input(prompt)
    try:
        assert(min <= int(v) <= max)
        print('The number is: ', int(v))
    except ValueError:
        print('Error: wrong input')
        read_int(prompt, min, max)
    except AssertionError:
        print('Error: the value is not within permitted range (min..max)')
        read_int(prompt, min, max)
        
v = read_int("Enter a number from -10 to 10: ", -10, 10)
