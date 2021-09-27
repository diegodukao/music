# FoxDot: Fazendo a pista dançar com Python
# @diegodukao

# linktr.ee/diegodukao

### brega funk ####

Scale.default = "minor"
Clock.bpm = 80
var.r = var([0])

# base
Clock.set_time(-1)
b1 >> bass(var.r+ P[0,4, 0,1,2], sus=1/4,
    dur=[1,1,1,1/2,1/2], amp=0.5, pan=-0, oct=4)
p1 >> keys(P(0,2,4), dur=[rest(1/2), rest(1/4), 1/4, rest(1/2), 1/2],
       oct=6, sus=1/4, amp=0.05, pan=0, drive=0.2)

p1 >> keys(P(0,2,4), dur=[1/4, 3/4],
       oct=6, sus=1/4, amp=0.05, drive=0.2)
d1 >> play("oooo", dur=[1/4, 3/4], amp=0.5)

p1 >> keys(P(0,2,4), dur=[rest(1/2), rest(1/4), 1/4, rest(1/2), 1/2],
       oct=6, sus=1/4, amp=0.05, pan=0, drive=0.2)
d1 >> play("..o.o", dur=[1/2, 1/4, 1/4, 1/2, 1/2], amp=0.4, sample=0)
d2 >> play("x", dur=[1,1,1,1/2,1/2], amp=0.6, sample=3, room=0.3, mix=0.3)       
d3 >> donk(var.r+ P[0,4, 0,1,2], sus=1/4,
    dur=[1,1,1,1/2,1/2], amp=0.5, oct=4)
   
p1 >> keys(P(0,2,4), dur=[1,1,1,1/2,1/2],
       oct=6, sus=1/4, amp=0.05, drive=0.2)
d1 >> play("oooo", dur=[1,1,1,1/2,1/2], amp=0.5)
Group(p1, d2,b1,p2,d1).solo()
    
p1 >> keys(P(0,2,4), dur=[1/4, 3/4],
       oct=6, sus=1/4, amp=0.05, drive=0.2)
d1 >> play("oooo", dur=[1/4, 3/4], amp=0.5)
p4 >> pluck(P[0,0,0,1,2]+ P(0,2,4), sus=1/4,
    dur=[rest(1),rest(1),rest(1),1/2,1/2], amp=0.4, pan=-0.8, oct=4)

p1 >> keys(P(0,2,4), dur=[rest(1/2), rest(1/4), 1/4, rest(1/2), 1/2],oct=6, sus=1/4,  amp=0.05, drive=0.2)
#p1.stop()
b1 >> bass(var.r+ [0,1, 0,1,2], sus=1/4,
    dur=[1,1,1,1/2,1/2], amp=0.6, oct=4)
d1 >> play("..o.o", dur=[1/2, 1/4, 1/4, 1/2, 1/2], amp=0.5, sample=0)
d2 >> play("x", dur=[1,1,1,1/2,1/2], amp=0.6, sample=3, room=0.3, mix=0.3)

p1 >> keys(P(0,2,4), dur=[1/4, 3/4],
       oct=6, sus=1/4, amp=0.05, drive=0.2)
d1 >> play("oooo", dur=[1/4, 3/4], amp=0.5)

p1.stop()
                                         
p2 >> piano(var.r + P[0,2,4,6,8].shuffle(), sus=1/4, dur=PDur(7,8), amp=0.3, pan=linvar(-0.8,0.8))

var.r = var([0])


d_all.stop()



p1 >> keys(P(0,2,4), dur=[1,1,1,1/2,1/2],
       oct=6, sus=1/4, amp=0.05, drive=0.2)
d1 >> play("oooo", dur=[1,1,1,1/2,1/2], amp=0.5)
Group(p1, d2,b1,p2,d1).solo()
    
p1 >> keys(P(0,2,4), dur=[1/4, 3/4],
       oct=6, sus=1/4, amp=0.05, drive=0.2)
d1 >> play("oooo", dur=[1/4, 3/4], amp=0.5)

p_all.stop()
d_all.stop()
b_all.stop()
d2 >> play("x", dur=[8], amp=0.6, sample=3, room=0.3, mix=0.3)
b1 >> bass(var.r+ P[0], sus=1/4,
    dur=[8], amp=0.5, pan=-0, oct=4)
d3 >> donk(var.r+ P[0], sus=1/4,
    dur=[8], amp=0.5, oct=4)



d1 >> play("oooo", dur=[1/4, 3/4], amp=0.5)

d2 >> play("xxxx", dur=[1/4, 3/4])



# variacao
d1 >> play("oooo", dur=[1/4, 3/4])
d2 >> play("xxxx", dur=[1/4, 3/4])
p1 >> keys(P(0,2,4), dur=[1/4, 3/4], oct=6, sus=1/4)
b1 >> bass(0, dur=[1/4, 3/4], sus=1/4)
