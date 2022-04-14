require "~/Projects/livecoding/petal/petal.rb"

cps 0.5



d1 "bd ~ ~ [~ bd/2]", slow: 1, amp: 0.3

d2 "hh [~ hh] hh hh", amp: "1 0.8", slow: 1

# d3 "~ sn:1 [~ ~ sn:1/2 sn:1] sn:1*2", amp: 0.1

d3 "~ [sn:1/8 sn:1/8 sn:1/8] sn:1 sn:1/4", amp: 0.2

d4 "tech(11,16)", slow: 2, rate: 0.8, amp: 0.7, n: "2", pan: 0.8

d5 "birds:2(5,16)", slow: 8, amp: 0.1, rate: "0.8 0.6 0.4 0.6", pan: "rand -0.6 0.6"

##| d1 :silence
##| d2 :silence
##| d3 :silence
##| d4 :silence

d6 "feel(3,16,2) feel(3,16)", slow:2, amp: 0.4, rate: "rand 0.6 1"

#d4 :silence

#d5 :silence

#d6 :silence