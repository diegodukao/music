

require "~/Projects/livecoding/petal/petal.rb"

cps 1

#r = 1

r = "0.8 0.8 0.8 0.7"

d1 "bd ~ ~ [~ bd/2]", slow: 1, amp: 0.3

d2 "hh [~ hh] hh hh", amp: "0.8 0.6 0.4", slow: 1

d3 "~ [sn:1/8 sn:1/8 sn:1/8] sn:1 sn:1/4", amp: 0.2

d4 "sf(11,16)", slow: 2, rate: r, amp: 0.05, n: 0, pan: 0

d5 "birds:2(5,16) ~ ", slow: 8, amp: 0.1, rate: "0.8 0.6 0.4 0.6", pan: "rand -0.6 0.6"

##| d1 :silence
##| d2 :silence
# d3 :silence
d4 :silence

use_random_seed 200

d6 "~  crow(5,16) [~ [crow crow] ~] crow(7,16)", slow: 8, n: 3, amp: 0.1, pan: -0.8,rate: "rand 0.6 1"

#d6 :silence
