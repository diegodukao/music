Root.default = "G"
Root.default -= 12
Clock.bpm =80
Scale.default = "harmonicMinor"

Clock.set_time(-1)
d1 >> play("x o[ x]xxo( x)")
d2 >> play("(----[---]---)", amp=[1,0.6])
p1 >> soft(P[4,0,1,0], dur=4,sus=1.25,amp=1, chop=5, pan=1)

p2 >> ripple(P(0-7,4,6-7,2+7)+p1.pitch, dur=1, amp=0.3, chop=4, pan=-0.6)
b1 >> bass(p1.pitch+ P[0], dur=[1.75,1/4,1/2,1/2,rest(1/2),1/2], amp=0.5)
~d4 >> bell(p1.pitch, dur=PDur(3,8)*2, amp=0.02)#.every(1, "offadd", var([-1,1], dur=8))

~d4 >> bell(p1.pitch, dur=PDur(3,8)*2, amp=0.4)#.every(1, "offadd", var([-1,1], dur=8))

~d4 >> bell(p1.pitch, dur=PDur(3,8)*2, amp=0.4).every(1, "offadd", var([-1,1], dur=8))


Group(p1,p2,d4).solo()
