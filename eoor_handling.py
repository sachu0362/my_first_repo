while True:
    try:
        age = input('enter your age')
        10/int(age)
    except ValueError:
        print('Please enter a number')
    except ZeroDivisionError:
        print('Please do not enter 0 for god sake')
    else:
        print('Thank you..!!')
        break
    finally:
        print('Ok... i am done finally')