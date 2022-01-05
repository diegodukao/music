p2 >> karp(var.ch + P[0:7].loop(3)|P[0], dur=PDur(5,8), amp=0.7, oct=5).every(4,"offadd", 4).penta().shuffle().every(8,"shuffle")

print(SynthDefs)

p_all.stop()






Scale.default = "mixolydian"
Root.default = "e"
Root.default -= 12


# var.ch = var([0, -1, 3, -1, 0], dur=[4, 4, 3, 1, 4])


Clock.set_time(-1)
p2 >> gong(var.ch + P[0:7], dur=1/2, amp=0.8).every(4,"offadd", 4).penta().shuffle().every(4, "stutter", 3, pan=[-1,1]).every(4, "offadd", 3)
var.ch = var([0])

var.ch = var([0,2,3], dur=[24,4,4])

p1 >> piano(var.ch + P(0-7,2+7,4,6), dur=PDur(3,8)*2, amp=0.65, pan=-0.5).every(4,"offadd",4)

p1.stop()

p2.stop()
p0.stop()

p2.amplify = var([1,0], dur=PDur(3,8))

d0.stop()

p1.stop()

p2.amplify = var([1,0], dur=PDur(3,8))
d1 >> play('XXo(X[ X])', amp=0.6, dur=1/2)
d2 >> play('- -- - -- ', dur=1/4, pan=-0.7, amp=0.8).every(8, "stutter", 4)
b1 >> bass(var.ch, dur=P[1/2,1/2,rest(1), 1/4,1/4,1/2,1/2,rest(1/2), 1/2], lpf=600, amp=0.5)
d4.stop()

d4 >> play("[ss]", dur=var([1/2,1,1/2],4), amp=0.5, pan=0.7)

p0 >> pulse(var.ch + P[0, 7, 0, 12], dur=[rest(1),1], pan=0.5, amp=0.2).every(4,"offadd",4)

p2.stop()

var.ch = var([4, -1, 3, -1, 0], dur=[4, 4, 3, 1, 4])
d1 >> play('XXo(X[ X])', amp=0.6, dur=1)

p0.stop()

var.ch = var([0])
p1.dur = 4
p1.amp = 0.5
#p1 >> piano(var.ch + P(0-7,2+7,4,6), dur=PDur(3,8)*2, amp=0.5, pan=-0.5).every(4,"offadd",4)
#p1 >> piano(var.ch + P[0,2+7,4,6], dur=PDur(var([3,6,5], dur=[1.5,1,1.5]),8)*2, amp=0.6, pan=-0.5).every(3, "stutter", 1).every(4,"offadd",4)
d1 >> play('XXo(X[ X])', amp=0.6, dur=1/2)
#p2.stop()
#p0.stop()
#p0 >> pulse(var.ch + P[0, 7, 0, 12], dur=[rest(1),1], pan=1, amp=0.15).every(4,"offadd",4)
p3 >> sitar(var.ch + P[0,2,4,6,7], dur=PDur(5,8,2)*4, pan=-1, amp=0.3).shuffle().every(8, "offadd", 3)
p4 >> sitar(var.ch + P[0,2,4,6,7] + 2, dur=PDur(5,8,2)*4, pan=1, amp=0.3).shuffle().every(8, "offadd", 3)

p3.stop()
p4.stop()

p2.stop()


p1 >> piano(var.ch + P(0-7,2+7,4,6), dur=PDur(3,8)*2, amp=0.5, pan=0.5).every(4,"offadd",4)

p0 >> piano(var.ch + P[0,2+7,4,6], dur=PDur(var([3,6,5], dur=[1.5,1,1.5]),8)*2, amp=0.5, pan=0.3).every(3, "stutter", 1).every(4,"offadd",4)


var.ch = var([0,2,3], dur=[24,4,4])

p2.stop()

p1.stop()

d_all.stop()
b_all.stop()






b1 >> bass(var.ch + P[0].loop(3)|P[3], dur=PDur(5,8), amp=0.8, lpf=300).stop()

Group(p3,p4,p1,p2).stop()
