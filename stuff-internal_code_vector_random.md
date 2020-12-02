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
modified version for public reuse, some now meaningless vars in here from other
functions that have been removed
"""

import anki_vector
import random
name = "death"
words = "worderror"
place = "nowhere"
talk = "talkerror"
hello_store = []
phrase_store = []

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        def fire(store):
            global name
            global place
            global phrase_store
            global hello_store
            talk = store
            if place == "prayer":
                phrase_store.append(talk)

            elif place == "ketahi":
                hello_store.append(talk)
            else:
                print("fail fire function")

        def fireall():
            def ketahifire():
                global name
                global place
                name = "Z4T3"
                place = "ketahi"
                fire("Quote of the day for you is")
                fire("Hey Hey hey ")
                fire("Hello again")
            def prayerfire():
                global place
                place = "prayer"
                lord = "Lord my God"
                name = "Gratitude"
                fire("God, I call out your Name to praise you, you who have already helped me help myself.")
                fire("God, thank you for showering me in abundances of riches.")

            ketahifire()
            prayerfire()
        def ketahishot(): #used if next is hi
            shot = random.choice(hello_store)
            print(shot)
            return shot
        def prayershot():
            shot = random.choice(phrase_store)
            print(shot)
            return shot
        fireall()
        ketahishot()
        prayershot()

        print("Activate!")
        robot.behavior.say_text(ketahishot())  functions
        robot.behavior.say_text(prayershot())
if __name__ == "__main__":
    main()

```
{% include internalexternalstuffpage.html %}
