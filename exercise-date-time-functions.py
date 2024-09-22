def num_check():
    while True:
        try:
            num_in= int(input("\ninput an integer between 1 & 10: "))
            if (num_in >= 1 and num_in <= 10):
                break
        # integer check (integers can be positive or negative)
        except ValueError:
            print("input is NOT an integer, please try again!")
            continue
        # else executed if: 
        # (1) try didn't break 
        # (2) ValueError exception was not thrown 
        else:
            print("input is an integer, but not in the correct range, please try again!")

def add(x, y):
    print(f"{x}+{y}={x+y}")

def subtract(x, y):
    print(f"{x}-{y}={x-y}")

def divide(x, y):
    print(f"{x}/{y}={x/y}")

def multiply(x, y):
    print(f"{x}*{y}={x*y}")

##### ----- MAIN -----#####
if __name__ == "__main__":
    from random import randrange

    # Task 1: count from 0 to 20
    print("\ncounting from 0 to 20")
    num = 0 
    while num <=  20:
        print(f"{num:02d} ",end="")
        num += 1    # NB: like i++ in JS

    # Task 2: count from 0 to 20
    print("\n\ncounting from 20 to 0")
    num = 20 
    while num >=  0:
        print(f"{num:02d} ", end="")
        num -= 1    # NB: like i-- in JS

    # Task 3: match generated random number via while loop
    num = 1
    randNum = randrange(21) # generate 20 random numbers
    print(f"\n\nrandom value is {randNum} ")
    while num <= 20:
        print(f"{num:02d} ", end="")
        if (num == randNum):
            print(f"\nnum={num} and randNum={randNum}... break ")
            break
        num += 1

    # Task 4: date and time
    """
    import datetime
    # print out the current date and time using datetime module
    dateTime = datetime.datetime.now()
    print("\ncurrent date and time is: " + dateTime.strftime("%H:%M:%S"))

    # print an auto incrementing real time clock (date and time) to the terminal
    while True:
        # '\r' is like '\n' but it starts on the current line, not the next line
        # 'end=' specifies how to end the print statement (default is end="\n")
        print("real-time clock: " + datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    """

    # Task 5: error handling subroutine
    num_check()

    # Task 6: subroutines
    print("\nsimple calculations:")
    add(2,3)
    subtract(10,2)
    divide(21,3)
    multiply(5,5)