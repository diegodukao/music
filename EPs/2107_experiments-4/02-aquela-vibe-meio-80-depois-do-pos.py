Clock.bpm = 120
Scale.default = "minor"

var.d_dur = var([2])

Clock.set_time(-1)
d1 >> play("-----.-.-----.--", dur=1/4*var.d_dur, amp=P[0.9,0.6,0.4,0.8]-0.2, pan=-0.8)
d0 >> play(".....s.s.....s..", dur=1/4*var.d_dur, amp=P[0.8]-0.2, pan=-0.8)
d2 >> play("x.x.......x..x..", dur=1/4*var.d_dur)

d6 >> play(".......K.K.KK..K.......K.K.KK..K.......K.K.KK..K.K.KK..K.K.KK..K", dur=1/4, amp=0.7, sample=0, room=0.3, pan=0.8)

~p1 >> pluck(P[7,6,4,5,4,2,3][:12], dur=P[1.0, 0.5, 1.0, 0.5, 0.5, 0.5], drive=0.2, room=0.8, mix=0.5, pan=0.3, amp=0.3)

p2 >> pluck(P[7,6,4,5,4,2,3][:12] + 3, dur=P[1.0, 0.5, 1.0, 0.5, 0.5, 0.5], drive=0.2, room=0.8, mix=0.5, pan=0.6, amp=0.4, amplify=var([0,1], dur=8)).offbeat(1)

p_all.solo()

p2 >> pluck(P[7,6,4,5,4,2,3][:12] + 3, dur=P[1.0, 0.5, 1.0, 0.5, 0.5, 0.5], drive=0.2, room=0.8, mix=0.5, pan=0.6, amp=0.4, amplify=var([0,1], dur=8)).offbeat([])

d1 >> play("-----s-s-----s--", dur=1/4*var.d_dur, amp=P[0.9,0.6,0.4,0.8]-0.2, pan=-0.8)
d2 >> play("x.x.......x..x..", dur=1/4*var.d_dur)
d3 >> play("....O.......O...", dur=1/4*var.d_dur, amp=0.55)
d4 >> play(".......o.o.o...o.......o.o.o...o.......o.o.o...o.o.o...o.o.o...o", amp=0.6, dur=1/4)
c1 >> play("=#", dur=16, sample=2, pan=[-0.8, 0.5], amp=[0.6, 1])
~b1 >> bass(P[0,0,0,0].loop(3)|P[5,4,2,3,4,4,5,3, 4,3,4,3,2,4,2,3].loop(1), dur=P[0.5, 0.5, 0.5, 0.25, 0.75, 0.5, 0.5, 0.5]*var.d_dur, room=0.2, mix=0.4, sus=1/4)

d3.stop()



b1.stop()

d_all.stop()

Group(p1, k1).stop()

p_all.stop()

d_all.stop()

p1.stop()

k1 >> keys(var([0, 3], dur=8) + P(0,2,4,6), dur=PDur(3,8)*2, drive=0.1, sus=1/2, amp=0.2, pan=-0.7)

x1 >> piano(var([0, 3], dur=8) + P[0,2,4,6], dur=PDur(var([5,3,4],dur=1),8)*2, pan=0.2, amp=0.8).every(4, "offadd", 4)

x2 >> piano(var([0, 3], dur=8) + P(0,2,4,6), dur=P[8], pan=0, sus=4, oct=4, amp=0.8)

p1.stop()
p2.stop()
k1.stop()


d_all.stop()

b_all.stop()

