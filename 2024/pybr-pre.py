#flavio
g1 >> cs80lead(PRand(0, 10) + b1.degree, amp=0.7).stop()

~g2 >> chipsy(
  var.r + P(0, 2, 2), 
  dur=[1, 0.5, 0.5, rest(1)], 
  amp=(0.3 + PRand(2, 5) * 0.1)
).stop()


~g3 >> chipsy(PRand(0, 8) + b1.degree, amp=1.1).every(3, "stutter")

~g4 >> sinepad(
  P[1, 1, 1] + var.r, 
  dur=16, 
  sus=16,
  amp=0.8,
  room=0.8,
  mix=0.2,
)

g5 >> fuzz(var.r + P[2, 4, 2, 7], amp=var([1, 0, dur=PDur(3, 8)]) * 0.3)


#########################################

# diego

Scale.default = "minor"

var.r = var([0])

d_all.stop()

d1 >> play("X ")

d2 >> play("-", amp=[1,0.8])

~b1 >> bass(var.r + P[0], dur=[0.5, 1], amp=0.3, sus=0.3)

p1 >> varsaw(P(0,2,4), dur=[8, rest(8)], amp=0.7, chop=60).stop()

d3 >> donk(var.r + P[0,0,4,6], dur=PDur(var([3,7], dur=[4,2]),8), amp=0.7)


Group(b1, d1).amplify = 0

d3 >> play("..o.")

Group(b1, d1).amplify = 1

~b1 >> sawbass(var.r + P[0,0,0,4,6], dur=P[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], sus=1/4, amp=0.7).every(4, "stutter", 2, dur=2, amp=0.35)

cowbell()

p1 >> pluck(var.r +P[0]-7, dur=[1/2,1/2, rest(1/2),1/2, 1/2,1/4,1/4, 1/2,1/2,
                      rest(1/2),1/2, 1/2,1/2, 1/2,1/4,1/4, 1/2,1/2,], pan=0, amp=0.7)

g3.amplify = var([1,0], dur=PDur(3,8))

print(SynthDefs)

d4.stop()

p1.stop()

d3.stop()

d_all.stop()

p_all.stop()

g_all.stop()

~b1 >> sawbass(var.r -7, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.8)

d2.stop()

d3 >> play("X", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], amp=0.9)
# volt mix 
d1 >> play("-", dur=1/2, pan=-0.8, amp=[0.7,0.5])
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.7)
d4 >> play("o", dur=[rest(1),1], amp=0.8)

d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=0.8, amp=1, drive=0.1)#.stop()


planet()

def planet():
    d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4], pan=-0.6, amp=0.8)
    d2 >> play("X", sample=2, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.6)
    d3 >> play("O", sample=0,dur=[rest(1), 1], amp=0.35)
def cowbell():
    d4 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.3, pan=0.8) 

p1 >> saw(var.r + P(0,2+7,4,6) - 7, dur=PDur(3,8,1)*2, amp=0.5, sus=1/2, pan=0, room=1)

p2 >> soprano(var.r + P[0,2+7,4,6], dur=4, amp=0.70, pan=-0.1, room=1, mix=0.5)

p2.stop()




##########################################

#hydra

s0.initScreen()

src(s0)
.modulate(
  src(s0).scale(() => 1 + a.fft[0])
)
.out()

a.show()




