Clock.set_time(-1)
Clock.bpm=80
d2 >> play("..o.[ o].o( o)")
d1 >> play("x(x[xx]).x.[xx].( [ x])")
d3 >> play("------([- ][---])(-[- -])", amp=[1,0.6,0.8], pan=-8)

Scale.default = "chromatic"
var.r = var([0,1,-3,-2], dur=2)
b1 >> bass(var.r + P[0], dur=P[1, rest(3/4),1/4,1/2,1/2, rest(1)], amp=0.5, hpf=70)
p2 >> piano(var.r + P(-12,0,4,7), oct=4,dur=1, amp=0.5, pan=-0.6)

~p3 >> zap(var.r + P[-12,0,7,4], dur=1/2, oct=6, amp=2, drive=0, pan=0.6, sus=1/4, room=0.8, mix=0.5)

p2.stop()
Group(d1,d2,d3,p2).amplify = var([1,0], 1)

Group(d1,d2,d3,p2).amplify = var([1], 1)
p2 >> piano(var.r + P(-12,0,4,7), oct=4,dur=1, amp=0.5, pan=-0.6)



print(SynthDefs)
