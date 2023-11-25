# Sampleando a Vida Adoidado
# @diegodukao

# https://algoravebrasil.gitlab.io/entre/

Clock.bpm = 120

Clock.set_time(-1)
Samples.addPath('/home/diego/Dropbox/palestras')
s1 >> loop('pessoa-aleatoria', P[0:16], rate=1)

p1 >> piano(P(0,2,4,6) + P[0,3], dur=8, amp=0.5)
f3 >> play("V", sample=0,dur=8, room=1, mix=0.5, amp=0.7)
f4 >> play("x", sample=0,dur=8, room=1, mix=0.5, amp=0.7)
f5 >> play("X", sample=1,dur=8, room=1, mix=0.5, amp=0.7)

s1 >> loop('pessoa-aleatoria', P[0:16], rate=1)    

s1 >> loop('pessoa-aleatoria', P[12])
d1 >> play("o", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.05, rate=1, amp=0.6)
d2 >> play("X", sample=1,dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.6)


Scale.default = "minor"

d_all.stop()
p2 >> sitar(p1.pitch[0] + P[0,3,5,2], amp=0.2, dur=PDur(var([3,5], dur=4),8,1), drive=0.1)

b1 >> bass(p1.pitch[0] + P[0,0,4], dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.6)

d_all.stop()
