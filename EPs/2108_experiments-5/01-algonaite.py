Scale.default = "minor"
Root.default = "A"
Root.default -= 12

Clock.bpm = 120


Clock.set_time(-1)
var.chords2 = var(P[
    P(0, 4+7,2+7,6)-7,
    P(0,4-7,2+7,6)-7, # D
    P(0,2-7, 2,6,8)-7, # F
    P(0,2-7,2,6, 0+7)-7, # E
    P(0,2, 0+7,6, 2+7)-7, # B   
], [4,4,4,2,2])
var.s = var(P[0,3,5,2,1], dur=[4, 4, 4, 2, 2])
b1 >> bass(0, dur=PDur(5,16)*2, sus=1/4, amp=0.8, pan=0.3)
b2 >> sawbass(0, dur=PDur(5,16,2)*2, sus=1/4, amp=0.8, pan=-0.3)
p1 >> piano(var.chords2 + var.s, dur=[4, 4, 4, 2, 2], pan=0, amp=0.7)

d4 >> play(" =", sample=[0,2], dur=16, pan=[0.3, -0.3], amp=[1,0.5])

d1 >> play("XXXX", dur=1)

d4 >> play("#=", sample=[0,2], dur=16, pan=[0.3, -0.3], amp=[1,0.5])
d2 >> play(" H H", dur=1, pan=0.2)
d3 >> play("---- ------- ---", dur=1/4, amp=P[0.3,0.3,0.8,0.8]-0.2, pan=-0.6)

p3 >> space(var.chords2[-1] +var.s,dur=[4, 4, 4, 2, 2], pan=[0.7, -0.7, 0, 0.7, -0.7], amp=0.8)

~p2 >> pluck(P[0,4,2,6, 6,4,2,0, 4-7,0,6,2, 7,4,2,6, 6,4,6,2,  2,0,4,0, 0,6,4,2,  4,7,6,4,] -7 + var.s, dur=PDur(7,16,3)*2, pan=0.2, amp=0.8, room=0.8, mix=0.6, drive=0.17)
Group(p1,p2,p3,d2).solo()

Group(p1,p2,p3,d2).solo(0)

~n1 >> nylon(var.s + P[7,2,0,8], dur=PDur(5,16), pan=-0.6, drive=0, amp=0.2)

~n1 >> nylon(var.s + P[7,2,0,8], dur=PDur(var([5,7], dur=[12,4]),16), pan=-0.5, amp=0.2)

b1 >> bass(n1.pitch, dur=PDur(5,16)*2, sus=1/4, amp=0.6, pan=0.3)
b2 >> sawbass(n1.pitch, dur=PDur(5,16,2)*2, sus=1/4, amp=0.6, pan=-0.3)
p_all.stop()
n1.amplify=0

~p2 >> pluck(P[0,4,2,6, 6,4,2,0, 4-7,0,6,2, 7,4,2,6, 6,4,6,2,  2,0,4,0, 0,6,4,2,  4,7,6,4,] -7 + var.s, dur=PDur(7,16,3)*2, pan=0.2, amp=0.8, room=0.8, mix=0.6, drive=0.17)

d3.stop()

p2.solo()

p2.solo(0)
d3 >> play("---- ------- ---", dur=1/4, amp=P[0.3,0.3,0.8,0.8]-0.2, pan=-0.6)
b1 >> bass(0, dur=PDur(5,16)*2, sus=1/4, amp=0.8, pan=0.3)
b2 >> sawbass(0, dur=PDur(5,16,2)*2, sus=1/4, amp=0.8, pan=-0.3)
p3 >> space(var.chords2[-1] +var.s,dur=[4, 4, 4, 2, 2], pan=[0.7, -0.7, 0, 0.7, -0.7], amp=0.8)
p1 >> piano(var.chords2 + var.s, dur=[4, 4, 4, 2, 2], pan=0, amp=0.7)

Group(p1,p3,p2).solo()


