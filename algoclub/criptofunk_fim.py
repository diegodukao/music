# Fazendo Funk com Programação - Criptofunk 2022
# @diegodukao e @thaisnviana

Clock.bpm = 120


# volt mix 
d1 >> play("-", dur=1/2)
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4])
d3 >> play("x", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)])
d4 >> play("o", dur=[rest(1),1])
d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2]).stop()

# planet rock
d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])
d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.5)
d3 >> play("o", dur=[rest(1), 1])
d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])

Group(d1, p2, d2, p1).solo(0)

var.raiz = var([0,0,2,2], dur=4)

p1 >> keys(P(0,2,4) + var.raiz, drive=0.1, dur=4)

p2 >> pluck(P[0,1,4,5] + var.raiz, dur=PDur(5,8)*2, drive=0.3) 

b1 >> bass(P[0] + var.raiz, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)], sus=1/2, drive=0.1)


# planet rock
d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])
d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.5)
d3 >> play("o", dur=[rest(1), 1])
d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])
d5.stop()



d1 >> play("X", dur=[3/4, rest(1/4), rest(1), 1/2, 1/2, rest(3/4), 1/4], amp=1.5)
d2 >> play("o", dur=[rest(3/4), 1/4, rest(1/2), 1/2, rest(1), 1])

Group(p1, d2).solo(0)

Scale.default = "minor"

~p1 >> pluck(P(0,2,4) + P[0,0,0,1,-1,2,0], amp=1, dur=1)

b1 >> bass([0], dur=4, amp=1)

print(SynthDefs)















#############################
Scale.default = "minor"
var.r = var([0,4,0,5],dur=8)
Clock.bpm =126
Clock.set_time(-1)



s3.stop()
f_all.stop()


Group(p1,p2,p3,b1,d1).solo(0)
d3 >> play("X", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], amp=0.6)
# volt mix 
d1 >> play("-", dur=1/2, pan=-0.8, amp=[0.8,0.5])
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.3)
d4 >> play("o", dur=[rest(1),1], amp=0.5)
d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=0.8, amp=0.9)
~b1 >> bass(var.r -7, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.4)

d5.stop()
p1 >> saw(var.r + P(0,2+7,4,6) - 7, dur=PDur(3,8,1)*2, amp=0.4, sus=1/2, pan=0, room=1)
p3 >> karp(var.r + P[0,2,4,6], dur=1/4, amp=0.7,pan=linvar(-1,1)).shuffle().every(3, "offadd",-1)
p3.amplify = var([0,1], dur=PDur(5,8))

Group(d2,d3,d4,b1,d1).stop()
p3.stop()
p2 >> soprano(var.r + P[0,2+7,4,6], dur=4, amp=0.4, pan=-0.7)

p1.stop()
p3.stop()
p2.stop()

d3.amplify = 0
d4.amplify = 0

p_all.stop()

b_all.stop()

s_all.stop()

f_all.stop()

f_all.stop()

Samples.addPath('/home/diego/MusicProjects/algoclub-samples/export')
~s3 >> loop("guerreiros2", dur=[rest(8),rest(3.5), 4.5], beat_stretch=1, amp=1)

~s2 >> loop("voces-sacaram", dur=[4,3.4,rest(8.6)], amp=1)

s_all.stop()

~s3 >> loop("sacaram", dur=[rest(4),rest(4),1,2,1,1,2,rest(1)], amp=0.2, rate=1)

s1 >> loop("sacaram2", dur=[1, rest(7)], beat_stretch=1).stop()

~s2 >> loop("e-claro", dur=[2, rest(2)], amp=0.2, beat_stretch=1).stop()

s4 >> loop("venham-aqui", dur=[2, rest(2)], amp=0.2).stop()

#############################################################

Scale.default = "dorian"
Root.default = "A"
Root.default -= 12

b1 >> bass(P[0:7],dur=PDur(7,16,2)*2, sus=1/4, amp=0.4).shuffle().penta()

Clock.bpm = 200

var.r = var([0,4], dur=4)

var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])

Clock.set_time(-1)

d1 >> play("x", dur=[1/2,rest(1),1/2], amp=0.5)
d2 >> play("t", sample=3, dur=PDur(7,16,2)*2, amp=1.2)
d3 >> play("-", amp=[0.8,0.3], pan=-0.8)

p1 >> piano((0,2,4), dur=PDur(7,16)*2, amp=0.2)

Clock.schedule(start, Clock.now() + 16)

def start():
    Clock.clear()
    Clock.set_time(-1)
    var.r = var([0,4], dur=4)
    var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
    p1 >> piano(var.r + var.f, dur=PDur(7,16,2)*2, amp=0.45, pan=-0.4)
    b1 >> bass(
        P[0,4,4,0,   4-7,8-7,13-7,11-7,8-7],
        dur=P[1.5, 0.5, 1, 1,    1, 0.5, 0.5, 1,1],
        sus=P[1.5, 0.5, 1, 1,    1, 0.4, 0.3, 0.9,1],
        lpf=800, amp=0.4)
    d1 >> play("x", dur=[1/2,rest(1),1/2], amp=0.5)
    d2 >> play("t", sample=3, dur=PDur(7,16,2)*2, amp=1.2)
    d3 >> play("-", amp=[0.8,0.3], pan=-0.8)
    

p2 >> quin(P[7, 9, 11, 6, 8,   -3+7, 6, 8, 10][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)


~p2 >> quin(P[7, 9, 11, 6, 8,   -3+7, 6, 8, 10][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)
var.r = var([0,4], dur=4)
var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
b1 >> bass(
    P[0,4,4,0,   4-7,8-7,13-7,11-7,8-7],
    dur=P[1.5, 0.5, 1, 1,    1, 0.5, 0.5, 1,1],
    sus=P[1.5, 0.5, 1, 1,    1, 0.4, 0.3, 0.9,1],
    lpf=800, amp=0.45)
~s1 >> play("#", dur=1, pan=0.6, amplify=var([1,0], dur=[1,2]), room=1, mix=0.5)

s1.stop()

p2.stop()



p2 >> quin(P[12, 14, 16-7, 11, 13,   0+7, 9, 11, 13][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)
p2.amplify = var([0,1], dur=[1,1,0.5,1.5])
var.r = var([5,3], dur=[4])
var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
b1 >> bass(
    P[5-7,9-7,5-7,9-7,8-7,        3, 1, 2, 3, 2, 1],
    dur=P[1.5,0.5, 0.5, 0.5, 1,   0.75, 0.75, 0.5, 1, 0.5, 0.5],
    sus=P[1.5,0.5, 0.5, 0.5, 1,   0.7, 0.7, 0.4, 1, 0.4, 0.4],
    lpf=800, amp=0.45)
~s1 >> play("#", dur=1, pan=0.6, amplify=var([1,0], dur=[1,2]), room=1, mix=0.5)



p1 >> piano([0,1,2,3,4,5,6,], dur=[1/2,1/4,1/8]).shuffle().every(2, "offadd", -1)
