# boa tarde!!!! Algorave Brasil 2024


# MUITO OBRIGADO!!!!!

var.r = var(P[0,3,2], dur=[4,2,2])

p2 >> rlead(var.r + P[0:7], dur=4, spin=4, bend=0.5).penta().shuffle()



p2 >> pianovel(var.r + [P(0,2,4,0), P(0,2,4,6)], dur=8, shape=0.5, amp=0.4, formant=4).stop()

p3 >> pluck(var.r +P(0,2,4), dur=PDur(5,8)*2, sus=1/2, amp=0.05, shape=0.9, formant=1)

b1 >> bass(var.r, dur=1/2, amp=0.3, chop=2)

~b1 >> bass(var.r + P[0,4], dur=PDur(3,8), amp=0.4, chop=2, sus=0.5).every([6,2], "offadd",3)

~p5 >> karp(var.r + P[0,4], dur=PDur(3,8), amp=0.9, chop=2, sus=0.5).every([6,2], "offadd",3)

~p1 >> rlead(var.r + P[0,4], dur=PDur(3,8), amp=0.9, chop=2, sus=0.5, echo=0.5, echotime=2).every([6,2], "offadd",3)

Group(p2,b1).solo()

p4 >> nylon(b1.pitch, sus=0.2, dur=PDur(3,8), amp=0.4, drive=0.1, pan=linvar([-1,1], 8), fmod=linvar([-10,10],8)).stop()

p3.stop()

p3 >> pluck(fmod=linvar([-10,10], 8), dur=1/4, sus=1, amp=0.3, pan=linvar([-1,1], 8), bend=0.5, slide=0.5, formant=1)

b1.amplify = var([0,1], dur=PDur(7,8)/2)

Group(d4,p1, p2).solo()

~d4 >> donk(var.r + P[0,2,4,6], dur=PDur(var([3,5,8], dur=1),8)*2, amp=0.7, formant=0).shuffle().often("offadd",3).every(2, "stutter",3)

Group(d2,d3).stop()

d1 >> play("xs")
d2 >> play("  o ")


d3 >> play("[--]-[---]-", amp=[0.2, 0.8])
