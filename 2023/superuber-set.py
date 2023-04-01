d1 >> play("x-", amp=0.7)
d2 >> play("..o.", amp=0.7)
d3 >> play("-", dur=1/2, amp=0.7)

var.r = var([0])

b1 >> bass(P[0] + var.r, dur=PDur(5,8,2)*2, sus=[0.1])
p1 >> karp(P[0,6,8,2] + P[0,0,0,-2] + var.r, dur=[1/2,1/4,1,1/4])
p2 >> piano(P(0,2,4) + P[0,0,0,-2] + var.r, dur=2, amp=0.7)

Clock.bpm = 120

Scale.default = "minor"


Scale.default = "dorian"
Root.default = "E"
Root.default -= 12
Clock.bpm = 100

var.ch = var([0],dur=8)

d1 >> play("-[--]", dur=1/2)

b1 >> bass(var.ch +P[0,2,4], amp=0.8, dur=PDur(3,8), sus=[0.6, 0.4, 0.4])

d2 >> play("[V ]V", dur=PDur(3,8), amp=0.3)

d3 >> play("XKK", dur=PDur(3,8), amp=0.4)

Group(d1,b1,p2).solo(0)
p1 >> piano(var.ch + P(0,2+7,4,6,8-7) + var([0,2],dur=1), dur=PDur(5,8)*4, amp=0.4).every(8, "stutter", 3, pan=0.5, amp=0.4)

d4 >> play("[ K]", dur=var([2,1,1,1/8], dur=P[14,1,3/4,1/4]), delay=1/2, amp=0.4, drive=0.03)

p2 >> space(var.ch + P[0, 2+7, 4, 6, 8-7] + var([0,2], dur=1), crush=0.2, drive=0.2, dur=1/4, amp=0.4,
    amplify=(var([1,0], dur=PDur(7,8))), pan=linvar([-1,1])).every(3, "offadd", -2)

Group(p2, d1, d3, d4, b1).solo(0)

p2.stop()

var.ch = var([0],dur=8)







Clock.bpm = 120

p1.stop()

def planet():
    d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4], pan=-0.6, amp=0.8)
    d2 >> play("X", sample=2, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.6)
    d3 >> play("O", sample=0,dur=[rest(1), 1], amp=0.35)
def cowbell():
    d4 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.3, pan=0.8)                         

~d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4], pan=-0.6, amp=0.8)

d2 >> play("X", sample=2, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.4)
d3 >> play("O", sample=0,dur=[rest(1), 1], amp=0.35)


~b1 >> sawbass(0, dur=P[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], sus=1/2, amp=0.7).every(4, "stutter", 2, dur=2, amp=0.35)

p_all.stop()

d4 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.15, pan=0.9)

b1.stop()

################# 
def solta():
    Clock.set_time(-1)
    d1 >> play("o", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.05, rate=1)
    d2 >> play("X", sample=1,dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8)
    f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
    f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
    f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)
    s4.stop()

p_all.stop()

s_all.stop()

Samples.addPath('/home/diego/MusicProjects/algoclub-samples/export')
~s3 >> loop('chegou-o-momento-da-verdade', dur=[1.7, rest(2.3), rest(4)], rate=1, amp=0.5)

s2.stop()

s3 >> loop('chegou-o-momento-da-verdade', dur=[4, rest(4)], rate=1)

s3.stop()
Group(d4,d3,p1,p2,b1,s1,f3,f4,f5).stop()
~s4 >> loop('qual-voce-acha-que-e', dur=[4, rest(4)], rate=0.8, amp=0.6)


#planet()
Clock.set_time(-1)
Group(f3,f4,f5,d2,b1).stop()
s_all.stop()
~s4 >> loop('bom-pra-mim-e-esta-que-ta-aqui-atras', dur=[6,rest(10)], rate=0.8)
Clock.schedule(solta, Clock.now() + 5)

~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(4),rest(1.8),2.2], rate=0.8, amp=0.6)

~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(2),1.1,rest(0.9),1.1,rest(0.8),2.1], amp=0.7, rate=-0.8, pan=0)

~s3 >> loop('qual', dur=[1, rest(7)], rate=-0.8, amp=0.4)

s3.stop()

p1.stop()

planet()

s_all.stop()

~s4 >> loop('bom-pra-mim-e-esta-que-ta-aqui-atras', dur=[2,rest(2)], rate=[0.8, 0.8,0.8, 0.8, -0.8,-0.8, -0.8,-0.8], amp=0.7, pan=-0.7)

s1.stop()

~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(2),2], amp=0.6).stop()

s3 >> loop('eh-esta-que-ta-aqui-atras', dur=[rest(2),2], rate=1).stop()

s2 >> loop('qual-voce-acha-que-e', dur=[4, rest(2), 0.75, rest(0.25), 0.75, rest(0.25), 4, rest(4)], beat_stretch=0, rate=0.8, amp=0.6).stop()

s2.stop()

s_all.stop()

solta()

planet()

p4.stop()

s_all.stop()

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

~d1 >> play("o", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.05, rate=1, amp=0.5)
d2 >> play("X", sample=1,dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8)
f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)

p2 >> play("[ss]", amplify=var([1,0], dur=[4,2,1,1]), pan=0.4, amp=0.5)


d1 >> play("x.........x....(.x)", dur=1/4)
d2 >> play("...p..p.........", dur=1/4, sample=1)
d3 >> play("....!.......!...", dur=1/4, sample=0, amp=0.4, rate=0.7).stop()
d4 >> play("..............m.", dur=1/4, sample=0)
d5 >> play("...o..o.....o...", dur=1/4, sample=0, amp=0.5)
d6 >> play("s..s..ss..s..s.s", dur=1/4, sample=0, amp=0.5)


p_all.stop()

p1.stop()

p3 >> bell(var.r + P[0], dur=PDur(var([5,3,4],1),8)*2, sus=1/4, amp=0.2, pan=[-0.7]).stop()

s_all.stop()

p_all.stop()

p4 >> saw(var.r + P[0:7], dur=b1.dur*8, amp=0.4, pan=linvar([-1,1]), chop=linvar(40)).penta().every(3,"offadd",-1)

p4 >> saw(var.r+ P[0:7], dur=b1.dur*8, amp=0.2, chop=linvar(40), pan=0.8).penta().every(3, "offadd",-1).stop()

planet()

p2.stop()

Group(d1,d2,b1).solo(0)

p_all.stop()
b1.stop()
#############################


s_all.stop()
Scale.default = "minor"
p4.stop()
var.r = var([0,4,0,5],dur=8)

Clock.bpm = 126

Clock.set_time(-1)


s3.stop()
f_all.stop()

p_all.stop()

f_all.stop()
~b1 >> sawbass(var.r -7, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.8)

d3 >> play("X", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], amp=0.9)
# volt mix 
d1 >> play("-", dur=1/2, pan=-0.8, amp=[0.7,0.5])
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.7)
d4 >> play("o", dur=[rest(1),1], amp=0.8)

d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=0.8, amp=1, drive=0.1)#.stop()


p3.stop()

p1 >> saw(var.r + P(0,2+7,4,6) - 7, dur=PDur(3,8,1)*2, amp=0.35, sus=1/2, pan=0, room=1)
p2 >> soprano(var.r + P[0,2+7,4,6], dur=4, amp=0.8, pan=-0.5, room=1, mix=0.5)

Group(p1,p2,b1,d1,d5,s1).solo(0)

d3.amplify = 0
d4.amplify = 0

p_all.stop()

b_all.stop()

s_all.stop()

f_all.stop()

p2.stop()

Samples.addPath('/home/diego/MusicProjects/algoclub-samples/export')
~s3 >> loop("guerreiros2", dur=[rest(8),rest(3.5), 4.5], beat_stretch=1, amp=0.3)

~s2 >> loop("voces-sacaram", dur=[4,3.4,rest(8.6)], amp=0.55)

s_all.stop()

~s3 >> loop("sacaram", dur=[rest(4),rest(4),1,2,1,1,2,rest(1), ], amp=0.4, rate=1)

~s2 >> loop("e-claro", dur=[2, rest(2),2, rest(2), rest(8)], amp=0.2, beat_stretch=1)

~s4 >> loop("venham-aqui", dur=[2, rest(2)], amp=0.2)


d5.stop()

p1 >> saw(var.r + P(0,2+7,4,6) - 7, dur=PDur(3,8,1)*2, amp=0.3, sus=1/2, pan=0, room=1)

p3 >> karp(var.r + P[0,2,4,6], dur=1/4, amp=0.8, drive=0.1, pan=linvar([-1,1])).shuffle().every(3, "offadd",-1)
p3.amplify = var([0,1], dur=PDur(5,8))

p2 >> soprano(var.r + P[0,2+7,4,6], dur=4, amp=0.4, pan=-0.5, room=1, mix=0.5).stop()

Group(d1,d2,d5,b1,p3,p1).solo(0)

s_all.stop()

p3.stop()

Group(s2,s3,p1,p2,p3,d1,b1).solo(0)

p_all.stop()

#Group(d2,d3,d4,b1,d1).stop()
#p3.stop()
p2 >> soprano(var.r + P[0,2+7,4,6], dur=4, amp=0.4, pan=-0.7, room=1, mix=0.5)

s_all.stop()

#########$#$#$#$#$#$#$#$#$$$$$$$$$$$$$$##################################
Scale.default = "dorian"
Root.default = "E"
Root.default -= 12
Clock.bpm = 100

##############3

Clock.bpm=80
~d2 >> play("..o.[ o].o( o)", amp=0.5)
~d1 >> play("x(x[xx]).x.[xx].( [ x])", amp=0.6)
~d3 >> play("------([- ][---])(-[- -])", amp=[1,0.6,0.8], pan=-8)
d4.stop()

p_all.stop()

Scale.default = "chromatic"

var.r = var([0,1,-3,-2], dur=2)

~b1 >> bass(var.r + P[0], dur=P[1, rest(3/4),1/4,1/2,1/2, rest(1)], amp=0.9, hpf=0)

~p2 >> piano(var.r + P(-12,0,4,7), oct=4,dur=1, amp=0.5, pan=-0.6)

~p3 >> quin(var.r + P[-12,0,7,4], dur=1/2, oct=6, crush=0.2, amp=0.6, drive=0.4, pan=0.6, sus=1/4, room=0.8, mix=0.5)

print(SynthDefs)

p2.stop()
Group(d1,d2,d3,p2).amplify = var([1,0], 1)

Group(d1,d2,d3,p2).amplify = var([1], 1)
p2 >> piano(var.r + P(-12,0,4,7), oct=4,dur=1, amp=0.5, pan=-0.6)

p2.stop()


Group(d1,d2,b1,p3).solo()




Clock.bpm = 80

var.metal = var([4])
~a1 >> play("X [XX]( [X])", dur=P[1/4]*var.metal, amp=0.5)
~a2 >> play(" O O", dur=P[1/4]*var.metal, amp=0.3)
~a3 >> play(" = =", dur=P[1/4]*var.metal, amp=1.4).stop()
a4 >> play("-")
b1 >> play("[XXXX].[XXXX].....", dur=[1/2], amp=[0.5])

var.r = var([2])
p1 >> pads(P[4, 2, 0, 6, 3, 1, 5], dur=PDur(7,16), amp=0.04, pan=0.4, dist=0.01, drive=0.6, chop=8, amplify=1).penta().every(8, "stutter", 3, pan=[-1,1], amp=0.02)

Scale.default = "phrygian"
c1 >> bass(var([0,var.r], dur=[8]), amp=0.5, drive=0.1)
