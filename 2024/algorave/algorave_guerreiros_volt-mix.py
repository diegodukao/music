Scale.default = "minor"
Root.default = "d"
var.r = var([0,4,0,5],dur=8)

Clock.bpm =126

Clock.set_time(-1)



s3.stop()
f_all.stop()


d3 >> play("X", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], amp=0.6)
# volt mix 
d1 >> play("-", dur=1/2, pan=-0.8, amp=[0.8,0.5])
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.3)
d4 >> play("o", dur=[rest(1),1], amp=0.5)

d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=0.8, amp=0.9)

~b1 >> bass(var.r -7, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.3)



p1 >> saw(var.r + P(0,2+7,4,6) - 7, dur=PDur(3,8,1)*2, amp=0.3, sus=1/2, pan=0, room=1)

p2 >> soprano(var.r + P[0,2+7,4,6], dur=4, amp=0.2, pan=-0.7)

Group(p1,p2,b1,d1,d5).solo(0)

d3.amplify = 0
d4.amplify = 0

p_all.stop()

b_all.stop()

s_all.stop()

f_all.stop()

Samples.addAPath('/home/diego/Music/samples')

~s3 >> loop("guerreiros2", dur=[rest(8),rest(3.5), 4.5], beat_stretch=1, amp=0.2, room=1)

~s2 >> loop("voces-sacaram", dur=[4,3.4,rest(8.6)], amp=0.2)

s_all.stop()

s1 >> loop("sacaram", dur=[rest(4),rest(4),1,2,1,1,2,rest(1), ], amp=0.2, rate=1)

s1 >> loop("sacaram2", dur=[1, rest(7)], beat_stretch=1).stop()

~s2 >> loop("e-claro", dur=[2, rest(2)], amp=0.2, beat_stretch=1)

s4 >> loop("venham-aqui", dur=[2, rest(2)], amp=0.2).stop()

#############################################################
