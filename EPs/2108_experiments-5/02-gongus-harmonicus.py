Scale.default = "harmonicMinor"
Root.default = "E"
Root.default -= 12
Clock.bpm = 110

var.r = var([0,2], dur=16)

var.r = var([0], dur=16)

var.r = var([3,1], dur=8)

var.r = var([3,-1], dur=8)

var.r = var([0], dur=16)

Clock.set_time(-1)
var.r = var([0,2], dur=16)
p2 >> gong(P[7,4,6,2] + var.r +7, dur=[1/4, 1/4, rest(1/4), 1/4], amp=0.5, drive=0.2, pan=0.4).every(4, "offadd", 3)

p1 >> gong(P[P(0,2,4), P(0,2,4), P(0,2,4), P(0,2,4)] + var.r, dur=8, drive=0.1, pan=-0.4, amp=0.3)

p2.amplify = var([0,1], dur=2)

d1 >> donk(var.r - 7, dur=PDur(3,8,2), drive=0, pan=0.8, amp=0.3)
d2 >> donk(P[7,4,6,2] + var.r -7, dur=[1/4, 1/4, rest(1/4), 1/4], amp=0.3, pan=-0.6).every(4, "offadd", 3)
d2.amplify = var([1,0], dur=PDur(3,4))

p2.solo()

p2.solo(0)
p2.amplify = var([0,1], dur=2)
var.r = var([0], dur=16)
b1 >> bass(p1.pitch[0]+7, dur=[2,2,1/8,rest(1/8),1/4,rest(1/2),1,rest(1/4),1/4,1/2,3/4,1/4], sus=[1/2,1/2,1/8,1/8,1/4,1/2,1/2,1/2,1/4,1/2,1/2,1/4], amp=0.4)
var.metal = var([2])
~a1 >> play("X(X )( X)( X) ", dur=P[1/4,1/4,1/8,1/8,1/4]*var.metal, amp=0.6)
~a2 >> play("   O", sample=0, dur=P[1/4]*var.metal, amp=0.6)
~a3 >> play(" - -", dur=P[1/4]*var.metal)
~a4 >> play("#", dur=16, pan=0.6)

a2.stop()

Group(a2,a4,q1,b1).stop()
d_all.stop()

q1 >> quin(P[7,5,4,2,5,3,2][:16]+ var.r -7, dur=PDur(9,16)/2, amp=0.7, pan=PWhite(-1,1))

