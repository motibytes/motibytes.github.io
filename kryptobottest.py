greenCounter = 0
blueCounter = 1

greenlongPP = 10 #round this
currentPrice = 10 #then convert to int

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#def execute(greenlongPP, currentPrice):
#    global greenCounter
#    global blueCounter

#    if greenLongPP == currentPrice:   #if price hits green long, set stop loss
#        greenCounter++
#        price = greenLongPP
#        print("I should start entry at " + price)
#execute()
#        Entry(price)
#        Stop_Loss_Long(price = price + price * 0.1)
        #no close

        #while Counters < 10?
#        if (greenLongPP == PRedShort):            #if price hits red take profit, short, set stop loss
#            redprice = price
#            amount = 0.5
#            Take_Profit(price, amount)
#            Open_Short(price)
#            Stop_Loss_Short(price = price - price * 0.1)
#        if (greenLongPP == PBlueMiddle && BlueCounter == 0):        #if price hits blue take profit
#            blueCounter++
#            blueprice = price
#            amount = 0.25
#            Take_Profit_Short(price, amount)
#        if (greenLongPP == PBlueMiddle && BlueCounter == 2):      #if price hits blue again, price rejected, take profit
#            blueprice = price
#            amount = 0.25
#    else:
#        Close()
