print('This line was executed')


class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, 12, 4, 17, 3])  # try to use [1, 'a', 4, 17, 3]
ml.sort()
print(ml)  # correct answer [1, 3, 4, 12, 17]


# Other type of mistakes
def f():
    x = [1, 2, 3]
    print(x[2])  # try x[4]


f()  # correct answer 3


# Other type of mistakes
try:
    x = [1, 2, 'a', 7]
    x.sort()
    print(x)
except TypeError:
    print('It is type error!')

print('I can catch the exception')


# Other types of mistakes
def f(x, y):
    try:
        return x / y
    except TypeError:
        print('Type error occurred!')
    #except ZeroDivisionError:
        #print('Division by zero!')


try:
    print(f(5, 0))
except ZeroDivisionError:
    print('Division by zero!')


# Other types of mistakes
def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError):
        print('Type error occurred!')


print(f(5, 0))
print(f(5, []))


# Other types of mistakes
def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


print(f(5, 0))
print(f(5, []))


# Other types of mistakes
def f(x, y):
    try:
        return x / y
    except:
        print('Error!')


print(f(5, 0))
print(f(5, []))

# Method resolution order
# Checking in which order the instance of class will go through namespaces of inherited classes
print(ZeroDivisionError.mro())


# Other types of mistakes
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('Division by zero!')
    except TypeError:
        print('Type error!')
    else:
        print('Result is', result)
    finally:
        print('Finally')


divide(2, 1)
divide(2, 0)
divide(2, [])


# Implementing the task
def foo(x, y):
    return x / y


try:
    foo(5, 0)
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')


# Other methods to through exceptions
def greet(name):
    if name[0].isupper():
        return 'Hello,' + name
    else:
        raise ValueError(name + ' is inappropriate name')


print(greet('Anton'))
# print(greet('anton'))

while True:
    try:
        name = input('Please enter your name: ')
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print('Please try again')
    else:
        break


# Implementing the task
# Creating new custom exception
class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            # Through the exception
            raise NonPositiveError('NonPositiveError occured!')


x = PositiveList()
x.extend([1, 2, 3, 4, 5])
print(x)
x.append(1)
print(x)
x.append(-1)



