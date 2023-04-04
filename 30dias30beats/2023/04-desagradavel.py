~p1 >> angst((0,2), dur=4, oct=4, amp=0.8)

Scale.default = "phrygian"

d1 >> donk(P[0,1,2] + P(0,2), dur=1/4, oct=4, drive=0.4, amp=0.6).every(4, "stutter", 3)
d3 >> play("#", dur=8, sample=[0], rate=[0.9,0.7], pan=[-0.5,0.5])

~b1 >> abass(P[0,1,2], dur=1/4, oct=3, amp=0.8, amplify=var([0,1], dur=4), pan=-0.7)

~d2 >> play("1345", sample=[2,0], rate=-0.3, dur=1/8, amp=0.3, pan=linvar([-1,1],4)).every(4, "shuffle")

~p3 >> bellmod(P[3,1,2,0], dur=PDur(5,8,1), amp=0.5, drive=0.2, pan=1, oct=4, amplify=var([1,0], dur=4)).every(2, "offadd",-1)
~p4 >> bellmod(P[3,1,2,0]+2, dur=PDur(5,8,1), amp=0.5, drive=0.2, pan=-1, oct=4, amplify=var([1,0], dur=4)).every(2, "offadd",-1)

Group(p1,d2,p3,p4).solo()

b1.stop()
Clock.bpm=80

