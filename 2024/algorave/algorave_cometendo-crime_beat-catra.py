
Clock.bpm = 120

Scale.default = "minor"

Root.default = "g"

Root.default -=12

Clock.set_time(-1)
Samples.addAPath('/home/diego/Music/samples')
s1 >> loop('pessoa-aleatoria', P[0:16], rate=1)

p1 >> pianovel(P(0,2,4,6) + P[0,3], dur=8, amp=0.5)
f3 >> play("V", sample=0,dur=8, room=1, mix=0.5, amp=0.7)
f4 >> play("x", sample=0,dur=8, room=1, mix=0.5, amp=0.7)
f5 >> play("X", sample=1,dur=8, room=1, mix=0.5, amp=0.7)


print(SynthDefs)


s1 >> loop('pessoa-aleatoria', P[0:16], rate=1)


s1 >> loop('pessoa-aleatoria', P[14,15,16,14,14,15,16], rate=1)


~s1 >> loop('pessoa-aleatoria', P[12,13])

s_all.stop()

d1 >> play("o", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.05, rate=1, amp=0.6)
d2 >> play("X", sample=1,dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.6)
s1 >> loop('pessoa-aleatoria', P[12])

d_all.stop()

p2 >> sitar(p1.pitch[0] + P[0,3,5,2], amp=0.2, dur=PDur(var([3,5], dur=4),8,1), drive=0.1)

s1.stop()

b1 >> bass(p1.pitch[0] + P[0,0,4], dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.2)

d_all.stop()
