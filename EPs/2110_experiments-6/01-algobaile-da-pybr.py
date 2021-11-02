Clock.bpm = 126
Root.default = "E"
Scale.default = "minor"

var.r = var([0],dur=8)

s3 >> play('b', sample=[3,4,3,3,4,4,5,6], dur=[1/2], rate=P[1,1,1,1,1,rest(1),rest(2),rest(2)], drive=0.2, amplify=1, amp=0.6)

s3.stop()

d3 >> play("x", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)], amp=0.8)

# volt mix 
d1 >> play("-", dur=1/2, pan=-0.8)
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.3)
d4 >> play("o", dur=[rest(1),1], amp=0.6)
b1 >> bass(var.r - 7, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.5)

d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=0.8, amp=0.6)


# samples custom
~s2 >> play('b', sample=[3,4,3,3,4,4,5,6], dur=[1/2], rate=P[1,1,2,2,1,1,2,2]*2, drive=0.2, amplify=var([0,1], dur=1/2), amp=0.5)

s3.stop()

s3 >> play('b', sample=[3,4,3,3,4,4,5,6], dur=[1/2], rate=P[1,1,1,1,1,1,1,1,1], drive=0.2, amplify=1, amp=0.5)


s3 >> play('b', sample=[3,4,3,3,4,4,5,6], dur=[1/2], rate=P[1,1,1,1,1,rest(1),rest(2),rest(2)], drive=0.2, amplify=1, amp=0.5)

s3.stop()

s3 >> play('b', sample=[4,4,5,6,3,4,3,3,], dur=[1/2], rate=P[1,1,1,1,rest(1),rest(1),rest(2),rest(2)], drive=0.2, amplify=1, amp=0.5)

~s4 >> play('b', sample=[3,4,3,3,4][:8], dur=PDur(3,8), rate=1, drive=0.2).stop()

p2.stop()

var.r = var([0,2,0,3], dur=8)

p1 >> piano(var.r + P(0,2,4+7,6,9) -7, dur=8, amp=0.5, pan=-0.5)

~p2 >> piano(var.r + P[0,2,4,6,7,8], dur=PDur(var([5,3,7], dur=[3,2,3]),8)*2, amp=0.5, pan=0.5).shuffle()

Group(d1,d2,d3,d4,b1).stop()


s2 >> play('b', sample=[3,4,3,3,4,4,5,6], dur=[1/4], rate=P[1,1,2,2,1,1,2,2]*var([2,1], dur=1/4), drive=0.2, amplify=var([0,1], dur=1/2), amp=0.6)

