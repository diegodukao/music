d1 >> play("x ")


Scale.default = "minor"
Root.default = "d"

def planet():
    d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4], pan=-0.6, amp=0.8)
    d2 >> play("X", sample=2, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.6)
    d3 >> play("O", sample=0,dur=[rest(1), 1], amp=0.35)
def cowbell():
    d4 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.3, pan=0.8)


planet()

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

Samples.addAPath('/home/diego/Music/samples')
~s2 >> loop('chegou-o-momento-da-verdade', dur=[1.7, rest(2.3), rest(4)], rate=1, amp=0.8)

planet()

solta()

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


~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(4),rest(1.8),2.2], rate=-0.8)

~s2 >> loop('esta-que-ta-aqui-atras', dur=[rest(2),1.1,rest(0.9),1.1,rest(0.8),2.1], amp=0.8, rate=-0.8)

~s4 >> loop('qual', dur=[1, rest(7)], rate=0.8, amp=0.4)

s3.stop()

s_all.stop()


s_all.stop()

~s4 >> loop('bom-pra-mim-e-esta-que-ta-aqui-atras', dur=[2,rest(2)], rate=[-0.8])

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
Root.default = "d"
Scale.default = "minor"

var.r= var(P[0,0.5,1,0.8],dur=[1.5,1,0.5,1])
def pancada():
    f3 >> play("V", sample=0,dur=8, room=1, mix=0.5)
    f4 >> play("x", sample=0,dur=8, room=1, mix=0.5)
    f5 >> play("X", sample=1,dur=8, room=1, mix=0.5)
    
pancada()

s_all.stop()

p1 >> pluck(var.r +P[0]-7, dur=[1/2,1/2, rest(1/2),1/2, 1/2,1/4,1/4, 1/2,1/2,
                      rest(1/2),1/2, 1/2,1/2, 1/2,1/4,1/4, 1/2,1/2,], pan=0, amp=0.7)
                      
b1 >> bass(var.r + P[0], dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),    3/4,rest(1/4), rest(1),1/2,1/2, 1/2,rest(1/2),], sus=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),    3/4,rest(1/4), rest(1),1/2,1/2, 1,rest(1/2),], amp=0.15, lpf=0)

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

