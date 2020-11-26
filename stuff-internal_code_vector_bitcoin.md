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

import anki_vector
import json
import requests
from time import sleep
def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        print("Raise Vector's head...")
        robot.motors.set_head_motor(5)
        print("Hello Bitcoin")

        def getBitcoinPrice():
            URL = "https://www.bitstamp.net/api/ticker/"
            try:
                r = requests.get(URL)
                priceFloat = float(json.loads(r.text)["last"])
                return priceFloat
            except requests.ConnectionError:
                print("Error querying Bitstamp API")

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
        robot.behavior.say_text("Hello Master! I have an update for you.")
        sleep(1)
        robot.behavior.say_text("Bitcoin last price was")
        sleep(1)
        robot.behavior.say_text(str(getBitcoinPrice()) + "USD")
        sleep(1)
        robot.behavior.say_text("Bitcoin high price was")
        robot.behavior.say_text(str(getBitcoinHigh()) + "USD")
        sleep(1)
        robot.behavior.say_text("Bitcoin trading volume is at")
        robot.behavior.say_text(str(getBitcoinVolume()) + "USD")
        sleep(1)
        robot.behavior.say_text("beep boop beep yay money!")
        robot.anim.play_animation_trigger('ComeHereSuccess')
        #V2:
        #bitcoin price is above your target price of 14.4444! Don't buy bitcoin yet!

if __name__ == "__main__":
    main()

```
