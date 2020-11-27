---
layout: noheader
---
```python
#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
#author: james bytes
https://jamesbyt.es
"""
# /usr/bin/python3
# /usr/bin/python3

import anki_vector
import json
import requests
from time import sleep

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
                                   #####################################################
        targetbuyPrice = 14444.44  #<<<<<<<<<<<<#value for the usd price to buy BTC ####
        targetsellPrice = 24444.44 #<<<<<<<<<<<<#value for the usd price to sell BTC ###
                                   #####################################################
        print("Raise Vector's head...")
        robot.motors.set_head_motor(5)

        print("make vector spin...")
        robot.motors.set_wheel_motors(50, -50)
        print("Hello_Bitcoin script initiating..")

        def getBitcoinPrice():
            URL = "https://www.bitstamp.net/api/ticker/"
            try:
                r = requests.get(URL)
                priceFloat = float(json.loads(r.text)["last"])
                return priceFloat
            except requests.ConnectionError:
                print("Error querying Bitstamp API")
        def lastPrice():
            moneyyy = "Bitcoin last price was " + str(getBitcoinPrice()) + "USD" #space after was may cause issue with output, test
            return moneyyy
        def differencebuyPrice():
            diff = btcPrice - mybuyPrice
            return diff
        def differencesellPrice():
            diff = mysellPrice - btcPrice
            return diff
        mybuyPrice = int(targetbuyPrice)
        stringmybuyPrice = str(targetbuyPrice)
        btcPrice = int(getBitcoinPrice())
        stringBtcPrice = str(getBitcoinPrice())
        mysellPrice = int(targetsellPrice)
        stringmysellPrice = str(targetsellPrice)

        def buy():
            if ( btcPrice > mybuyPrice ):
                robot.behavior.say_text("Hello Master! I have an update for you.")
                sleep(1)
                robot.behavior.say_text(lastPrice())
                sleep(1)
                robot.behavior.say_text("BTC value is currently greater than your set buy price of " + stringmybuyPrice)
                sleep(0.5)
                robot.behavior.say_text("That's " + str(differencebuyPrice()) + " dollars away from your target!")
                sleep(1)
                robot.behavior.say_text("Do not buy any bitcoin today!")
            elif ( btcPrice < mybuyPrice ):
                robot.behavior.say_text("Master! Critical update!")
                sleep(1)
                robot.behavior.say_text(lastPrice())
                sleep(1)
                robot.behavior.say_text("BTC value is lower than your set buy price of " + stringmybuyPrice)
                sleep(0.5)
                robot.behavior.say_text("That's " + str(differencebuyPrice()) + " dollars lower than your target!")
                sleep(1)
                robot.behavior.say_text("Acquire bitcoin you must!")
            elif ( btcPrice == mybuyPrice ):
                robot.behavior.say_text("beep beep beep Master! Critical update!")
                sleep(1)
                robot.behavior.say_text(lastPrice())
                sleep(1)
                robot.behavior.say_text("BTC is exactly your target price. This is inconceivable. A miracle.")
                "Life is a lie! Reality is a dream! Self destruct initiating in T minus 10 billion years"
        def sell():
            sleep(2)
            if ( btcPrice > mysellPrice ):
                robot.behavior.say_text("Attention! Critical update!")
                sleep(1)
                #robot.behavior.say_text(lastPrice())
                #sleep(1)
                robot.behavior.say_text("BTC is currently greater than your set sell price of " + stringmysellPrice)
                sleep(0.5)
                robot.behavior.say_text("That's " + str(differencesellPrice()) + " dollars above your sell target!")
                sleep(1)
                robot.behavior.say_text("Sell bitcoin you must!")
            elif ( btcPrice < mysellPrice ):
                robot.behavior.say_text("Next Update.")
                sleep(1)
                #robot.behavior.say_text(lastPrice())
                #sleep(1)
                robot.behavior.say_text("BTC is currently lower than your set sell price of " + stringmysellPrice)
                sleep(1)
                robot.behavior.say_text("That's " + str(differencesellPrice()) + " dollars away from your sell target!")
                sleep(0.5)
                robot.behavior.say_text("Do not sell any bitcoin today!")
            elif ( btcPrice == mysellPrice ):
                robot.behavior.say_text("Critical update!")
                sleep(1)
                #robot.behavior.say_text(lastPrice())
                #sleep(1)
                robot.behavior.say_text("BTC is exactly your target price. This is inconceivable. A miracle.")
                sleep(1)
                robot.behavior.say_text("Life is a lie! Reality is a dream! Self destruct initiating in T minus 10 billion years")
        buy()
        sell()
        sleep(1)
        robot.motors.set_wheel_motors(0, 0) #stop wheels

        robot.behavior.say_text("beep beep beep. yay money money!")
        robot.anim.play_animation_trigger('ComeHereSuccess')
'''
================================================================================
      ======================== EXTRA FUNCTIONS ===========================
================================================================================
        def getBitcoinHigh():
            URL = "https://www.bitstamp.net/api/ticker/"
            try:
                r = requests.get(URL)
                priceFloat = float(json.loads(r.text)["high"])
                return priceFloat
            except requests.ConnectionError:
                print("Error querying Bitstamp API")
        def getBitcoinLow():
            URL = "https://www.bitstamp.net/api/ticker/"
            try:
                r = requests.get(URL)
                priceFloat = float(json.loads(r.text)["low"])
                return priceFloat
            except requests.ConnectionError:
                print("Error querying Bitstamp API")

        def getBitcoinVolume():
            URL = "https://www.bitstamp.net/api/ticker/"
            try:
                r = requests.get(URL)
                priceFloat = float(json.loads(r.text)["volume"])
                return priceFloat
            except requests.ConnectionError:
                print("Error querying Bitstamp API")

        robot.behavior.say_text("Bitcoin high price was")
        robot.behavior.say_text(str(getBitcoinHigh()) + "USD")
        sleep(1)
        robot.behavior.say_text("Bitcoin trading volume is at")
        robot.behavior.say_text(str(getBitcoinVolume()) + "USD")
        sleep(1)
'''

if __name__ == "__main__":
    main()

```
