counter = 0
def wrong_increment():
    counter += 1
    print(counter)
wrong_increment()
#output:
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value

