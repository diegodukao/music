Scale.default = "minor"

Clock.bpm=120

Clock.set_time(-1)
f2 >> play("k", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.04)

f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)

~p1 >> pluck(P[0,1,2, 3,4,5, 6,7,4, 2,3,2] -7, dur=PDur(3,8)*2, drive=0.2, amp=0.1, room=1, mix=0.5, pan=0.8).every(4, "stutter", 3)
p1.amplify = 0
~b1 >> jbass(p1.pitch +7, dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8, lpf=73, hpf=0)

d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.1, pan=-0.8)

Group(p1,b1,f3,f4,f5).solo()

Group(p1, b1,f3,f4,f5).solo(-1)
f2 >> play("k", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.04)
d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])
d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.2, pan=-0.8).stop()
d3 >> play("o", dur=[rest(1), 1])
d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])
~b1 >> jbass(p1.pitch +7, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.8, lpf=73, hpf=0)


~p1 >> pluck(P[0,1,2, 3,4,5, 6,7,4, 2,3,2] -7, dur=PDur(3,8)*2, drive=0.2, amp=0.1, room=1, mix=0.5, pan=PWhite(-0.3,0.3)).every(4, "stutter", 3)
p1.amplify = 1


d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.1, pan=-0.8)

d2.stop()

# Beatbox do Catra 

f1 >> play("X", dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8)
~b1 >> jbass(p1.pitch +7, dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8, lpf=73, hpf=0)
d_all.stop()

p1.amplify =0


j1 >> donk([1,0,0, 1,0,0, 1,0,0, 1,1], dur=[1/2,1/4,1/4, 1/2,1/4,1/4, 1/2,1/4,1/4, 1/2,1/2], pan=0.8, amp=0.3)

j1.stop()

b1.stop()

p1.amplify = 0

d_all.stop()



