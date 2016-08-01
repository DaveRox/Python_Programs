largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
    	x = float(num)
    except:
        print 'Invalid input'
        continue
    for the_big in [num]:
        if largest is None:
            largest = the_big
        elif the_big > largest:
            largest = the_big
    for the_small in [num]:
        if smallest is None:
            smallest = the_small
        elif the_small < smallest:
            smallest = the_small
    
    
print "Maximum is", largest
print "Minimum is", smallest