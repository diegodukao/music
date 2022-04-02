Clock.set_time(-1)
d1 >> play("e", sample=var([0,1], 4), dur=PDur(var([9,5,4],2),16), rate=linvar([0.4,0.5]))

d2 >> play("  H ", sample=0, rate=1, amp=0.7, pan=0)

d3 >> play("x(.[.x])(x[xx])(.[.x])", amp=0.8)
d4 >> play("-(-[--][ - ][ -])--", amp=0.7, pan=-0.8)
b1 >> bass(var.r, sus=1/8, dur=PDur(var([9,5],[2,6]),16), amp=0.7)

var.r = var([0])
p1 >> pulse(var.r+P(0,3,6,8)-7, dur=8, sus=4, amp=0.2, pan=-0.4)

p2 >> nylon(var.r+P(0,3,6,8)-7, dur=PDur(var([9,5,4],2),16,2)*2, sus=1/8, pan=0.2, amp=0.7)
p1.stop()


