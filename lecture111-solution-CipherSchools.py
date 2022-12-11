def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print('you cannot divide a number by zero')
        print(err)
    except TypeError as err:
        print("numbers must be int or floats")
    except:
        print("unexcepted error")