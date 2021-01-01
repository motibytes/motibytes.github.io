it tries to long if price hits the bottom, take profit at the middle of channel, take profit at the top.

it tries to short if price hits the top, take profit at the middle of channel, take profit at the bottom.

mine using channels, looking for cycles in the channel

that bot has four types of order: entry, tp, stop, close
Jump






bot

def Entry():
    a
def Take_Profit():
    a
stop loss

close


" price action is a trading technique that allows a trader to read the market
and make subjective trading decisions based on the recent and actual price movements,
rather than relying solely on technical indicators. "

I do not close because:
- if price breaks downwards I will have perfect short from the top.
- if price breaks upwards I will have the perfect long from the bottom

currentprice = reee
greenLongPP = 0
greenCounter = 0
def Execute():
    global greenCounter
    global blueCounter
   if (greenLongPP = currentPrice):   #if price hits green long, set stop loss
        greenCounter++
        price = greenLongPP
        Entry(price)
        Stop_Loss_Long(price = price + price * 0.1)
        #no close
        
        #while Counters < 10?
        if (greenLongPP == PRedShort):            #if price hits red take profit, short, set stop loss
            redprice = price
            amount = 0.5
            Take_Profit(price, amount)
            Open_Short(price)
            Stop_Loss_Short(price = price - price * 0.1)
        if (greenLongPP == PBlueMiddle && BlueCounter == 0):        #if price hits blue take profit
            blueCounter++
            blueprice = price
            amount = 0.25
            Take_Profit_Short(price, amount)
        if (greenLongPP == PBlueMiddle && BlueCounter == 2):      #if price hits blue again, price rejected, take profit
            blueprice = price
            amount = 0.25
    else:
        Close()
#blue middle counter needs to be reset to 0

If price hits green I long and then if price hits blue I take profit and then if
price hits red I take profit and open a short.
If price hits blue again(if price is rejected from top)
I take profit from my shorts and still do not touch longs.
When price hits green again I increase the long positions



so best way to trade this channels is
- long from bottom
- take profit at pivot level but keep it open
- take profit at top keep it open

- short from top
- take profit at pivot level but keep it open
- take profit at bottom but keep it open

- when the price hits the bottom again, increase the contract size of previous long
- when the price hits the top again, increase the contract size of previous short
this is for major positions

abusing horizontal channels until it doesn't work anymore = shortcut to richness
at one point it won't work out and it will mean that channel is broken
