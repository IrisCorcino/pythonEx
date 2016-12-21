number = int(input( "Type a number = "))
div = number / 10
mod = number % 10
number2 = 0
while div != 0:
    number2 += mod
    number2 = number2* 10
    div = div / 10
    mod = div % 10

if number2 == number:
    print '%i is a palidrom number' % number
