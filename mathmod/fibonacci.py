"""
TODO:
Remove logging, it goes in ParseFunc.
"""

#FIBONACCI
import time
import logging
def main(Comandeer):
    """
    TODO:
    Remove (the `Press control c to stop' can be put in parsefunc)
    """
    globals()['_'] = Commandeer

def CalculateFixedFibo(amount):
    """
    This is manual fibonacci mode -- that is, you choose how many numbers it does and returns a list of fibonacci up to that amount of calculations. Instead of it in a while loop and printing the numbers to the screen.
    Set `amount' to how many numbers of fibonacci you want to calculate.
    """
    if amount == 1:
        return [0,]
    if amount == 2:
        return [0,1]
    theList = [0, 1]
    num0 = 0
    num1 = 1
    hi = 0
    amount -= 2 #because we have already added the first two numbers
    for i in range(0, amount):
        num = num0 + num1 #set variable num to the sum of num0 and num1.
        if hi == 0:
            num0 = num
            hi = 1
        else: #every other time this loops it will run this instead of the previous block
            num1 = num # set num1 to num
            hi = 0 #next time it wont do this block it'll do the previous one
        theList.append(num)
    return theList

def CalculateLoopedFibo():
    """
    this is Looped fibo which is indefinite.
    """
    print(_("Press Control-C to stop."))
    print("0, 1", end=", ")
    try:
        num0 = 0
        num1 = 1
        hi = 0
        while True:
            num = num0 + num1 #set variable num to the sum of num0 and num1.
            if hi == 0:
                num0 = num
                hi = 1
            else: #every other time this loops it will run this instead of the previous block
                num1 = num # set num1 to num
                hi = 0 #next time it wont do this block it'll do the previous one
            print(num, end=", ", flush=True) #print the current number
            time.sleep(0.5)
    except KeyboardInterrupt: #if ctrl-c
        print(_("Thanks for using Palc's FIBONACCI function!"))
    except Exception as e: #if an error occurs
        print(_("An error occured."))
        logging.err("Exception %s in FIBONACCI" % e)

if __name__ == "__main__":
    def _(thestring):
        return thestring
    CalculateLoopedFibo()
