Root.default = "c#"
Root.default -= 7
Clock.bpm = 120
Scale.default = "phrygian"
def liberta():
    notes = P[
        #1,4,5,1,4,5,1,4,
              6,1,5,4,4,5,6,
              7,6,5,4,
              3,0,3,7,6,4,
              0,4,7,4,
              4,7,4,7,4,4,7,4,
              4,7,4,7,4,7,4,4,5,3,3.5,
              5,8,7,6,7,8,3.5,
              9,8,7,6,5
              ]
    durs = P[
        #.5,.5,.5,.5,.5,.5,.5,.5,
             .5,.5,.5,1,.5,.5,.5,  # 4
             1,.5,1,1.5,  #4
             2,rest(.5),.5,.5,2,2.5, #8
             rest(2.5),.5,.5,.5, #5
             .5,.5,.5,.5,.5,.5,.5,.5,.5,.5,.5, #4
             .5,.5,.5,.5,.5,1,3,1, #8
             .5,1,.5,.5,.5,.5,.5, # 4
             .5,1,.5,.5,.5, #3
             ]
    ~p1 >> space(notes, dur=durs, oct=4, drive=0)
    ~p2 >> piano(p1.pitch+ P(0,2+7,4,6), dur=[8,8,rest(12),4,4,3,1], amp=0.7, oct=4)
    ~b1 >> bass(p2.pitch[0], dur=P[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], sus=1/2, amp=0.7).every(4, "stutter", 2, dur=2, amp=0.4)
def planet():
    d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4], pan=-0.6, amp=0.8)
    d2 >> play("X", sample=2, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.6)
    d3 >> play("O", sample=0,dur=[rest(1), 1], amp=0.35)
def cowbell():
    d4 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.3, pan=0.8)                         

Clock.set_time(-1)
p1 >> space(P[1,4,5,1, 4,5,1,5], oct=4,dur=1/2, drive=0)
Clock.schedule(liberta, Clock.now() + 80.75)


planet()
#
#

d4 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.3, pan=0.8)                         

d4.stop()
v1 >> viola(p1.pitch + P(0,2) + P[0,0,7,0,0,0], dur=[8,8,8,8,4,4], amp=0.3, pan=-0.4)
~p2 >> piano(p1.pitch+ P(0,2+7,4,6), dur=[8,8,8,4,4,4,4], amp=0.7, oct=4)
p1.amplify = 0

cowbell()

notes = P[
              6,1,5,4,4,5,6,
              7,6,5,4,
              7,6,5,4,
              9,8,7,6,5,4
              ]
durs = P[
             .5,.5,.5,1,.5,.5,.5,  # 4
             1,.5,1,1.5,  #4
             1,.5,1,1.5,
             .5,1,.5,.5,.5,1 #4
             ]
~p1 >> space(notes, oct=4,dur=durs, amplify=var([1,1], dur=8))#.every(4, "offadd",-3)



v1.stop()
notes = P[9,8,7,6,5]111
durs = P[.5,1,.5,.5,.5]
~p1 >> space(notes, oct=4,dur=durs, amplify=var([1,1], dur=8))#.every(4, "offadd",-3)
~p2 >> piano(p1.pitch+ P(0,2+7,4,6), dur=[8,4,4], amp=0.7, oct=4)

liberta()
p1.amplify=1
~p2 >> piano(p1.pitch+ P(0,2+7,4,6), dur=[8,4,4], amp=0.7, oct=4)


cowbell()

v_all.stop()

d2.stop()
d3.stop()

p_all.stop()

p1.amplify = 0
d4.stop()

Group(d1,d2).solo(0)
liberta()

v1.amplify=0

d2.amplify=1
d3.amplify=1

planet()

cowbell()

v1 >> viola(p1.pitch + P(0,2) + P[0,0,7,0,0,0], dur=[8,8,8,8,4,4], amp=0.3, pan=-0.4)

p1.amplify = 0

p_all.stop()

Group(d1,d2,p1,p2,b1).solo()

liberta()

p2.stop()

p1.stop()

d4.stop()

d_all.stop()

d4.stop()

p_all.stop()
v1.stop()

################# esta que ta aqui atras
def solta():
    Clock.set_time(-1)
    d1 >> play("o", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.05, rate=1)
    d2 >> play("X", sample=1,dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8)
    f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
    f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
    f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)
    s4.stop()

s_all.stop()
Samples.addPath('/home/diego/MusicProjects/algoclub-samples/export')
~s2 >> loop('chegou-o-momento-da-verdade', dur=[1.7, rest(2.3), rest(4)], rate=1, amp=0.8)

s2.stop()

s2 >> loop('chegou-o-momento-da-verdade', dur=[4, rest(4)], rate=1)

s2.stop()
Group(d4,d3,p1,p2,b1,s1,f3,f4,f5).stop()
~s4 >> loop('qual-voce-acha-que-e', dur=[4, rest(4)], rate=0.8)


#planet()
Clock.set_time(-1)
Group(f3,f4,f5,d2,b1).stop()
s_all.stop()
~s4 >> loop('bom-pra-mim-e-esta-que-ta-aqui-atras', dur=[6,rest(10)], rate=0.8)
Clock.schedule(solta, Clock.now() + 5)


~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(4),rest(1.8),2.2], rate=0.8)

~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(2),1.1,rest(0.9),1.1,rest(0.8),2.1], amp=0.8, rate=0.8)

~s4 >> loop('qual', dur=[1, rest(7)], rate=0.8, amp=0.4)

s3.stop()

s_all.stop()


s_all.stop()

~s4 >> loop('bom-pra-mim-e-esta-que-ta-aqui-atras', dur=[2,rest(2)], rate=0.8)

s1.stop()

s_all.stop()

~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(2),2], amp=0.6)

s3 >> loop('eh-esta-que-ta-aqui-atras', dur=[rest(2),2], rate=1).stop()

s2 >> loop('qual-voce-acha-que-e', dur=[4, rest(2), 0.75, rest(0.25), 0.75, rest(0.25), 4, rest(4)], beat_stretch=0, rate=0.8)

s2.stop()

s_all.stop()


print(dir(Scale))

solta()

s_all.stop()
p_all.stop()

############## frank fito
Root.default = "c"
Scale.default = "major"
var.r= var(P[0,0.5,1,0.8],dur=[1.5,1,0.5,1])
def pancada():
    f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
    f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
    f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)

s_all.stop()

p1 >> pluck(var.r +P[0]-7, dur=[1/2,1/2, rest(1/2),1/2, 1/2,1/4,1/4, 1/2,1/2,
                      rest(1/2),1/2, 1/2,1/2, 1/2,1/4,1/4, 1/2,1/2,], pan=0, amp=0.7)
b1 >> bass(var.r + P[0], dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),    3/4,rest(1/4), rest(1),1/2,1/2, 1/2,rest(1/2),], sus=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),    3/4,rest(1/4), rest(1),1/2,1/2, 1,rest(1/2),], amp=0.5, lpf=0)

d1 >> play("o", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.05, rate=1)
d2 >> play("X", sample=1,dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8)
f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)

p2 >> play("[ss]", amplify=var([1,0], dur=[4,2,1,1]), pan=0.4, amp=0.5)

p_all.stop()

p1.stop()
p3 >> bell(var.r + P[0], dur=PDur(var([5,3,4],1),8)*2, sus=1/4, amp=0.2, pan=[-0.7])

p_all.stop()

p4 >> saw(var.r + P[0:7], dur=b1.dur*8, amp=0.3, pan=linvar([-1,1]), chop=linvar(40)).penta().every(3,"offadd",-1)

p4 >> saw(var.r+ P[0:7], dur=b1.dur*8, amp=0.4, chop=linvar(40), pan=0.8).penta().every(3, "offadd",-1)

p2.stop()

Group(d1,d2,b1).solo()

p_all.stop()
b1.stop()
#############################

Scale.default = "minor"

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

~b1 >> bass(var.r -7, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.4)



p1 >> saw(var.r + P(0,2+7,4,6) - 7, dur=PDur(3,8,1)*2, amp=0.3, sus=1/2, pan=0, room=1)

p2 >> soprano(var.r + P[0,2+7,4,6], dur=4, amp=0.2, pan=-0.7)

Group(p1,p2,b1,d1,d5).solo(0)

d3.amplify = 0
d4.amplify = 0

p_all.stop()

b_all.stop()

s_all.stop()

f_all.stop()

Samples.addPath('/home/diego/MusicProjects/algoclub-samples/export')
~s3 >> loop("guerreiros2", dur=[rest(8),rest(3.5), 4.5], beat_stretch=1, amp=0.4)

~s2 >> loop("voces-sacaram", dur=[4,3.4,rest(8.6)], amp=0.2)

s_all.stop()

s1 >> loop("sacaram", dur=[rest(4),rest(4),1,2,1,1,2,rest(1), ], amp=0.2, rate=1)

s1 >> loop("sacaram2", dur=[1, rest(7)], beat_stretch=1).stop()

~s2 >> loop("e-claro", dur=[2, rest(2)], amp=0.2, beat_stretch=1)

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

