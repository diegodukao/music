Scale.default = "chromatic"

#Cmin79
Clock.set_time(-1)

p1 >> tworgan4(P(0,2-7,3,7,var([10,9], dur=16)), dur=2, hpf=600, lpf=0, amp=0.35, sus=1.7, chop=0)

p1 >> tworgan4(P(0,2-7,3,7,var([10], dur=16)), dur=3, hpf=600, lpf=0, amp=0.35, sus=3, chop=0).solo()

# p1 >> tworgan4(P(0,2-7,3,7,var([10,9], dur=16)), dur=2, hpf=600, lpf=0, amp=0.7, sus=1.7, chop=3)

d3 >> donk(P[0,2-7,3,7,var([10,9], dur=16)], dur=2/3).every(4, "stutter", var([2,3], dur=[1]), pan=-1)

b1 >> sawbass(P[0,2-7,3,7,var([10,9], dur=16)][:8], dur=[2/3], sus=0.8, amp=0.6).reverse()
d1 >> play("- ", dur=1/3)
d2 >> play("x ( o)", dur=1/3)

~p2 >> pianovel(P[0,2-7,3,7,var([10,9], dur=16)] +12, dur=1/3, sus=1/3, amplify=var([1,0], PDur(7,9)/6), amp=0.55, pan=1).shuffle()


print(SynthDefs)



Group(b1, d3, p2).solo(0)
















Scale.default = "minor"

var.p_kick = var([1,0,0,0,0,0,1,0,  0,0,1,0,0,1,0,1], dur=1/3)
d1 >> play("x", dur=1/4, amplify=1*var.p_kick, amp=0.7)

d2 >> play("....o...", dur=1/3)

d3 >> play("-")

var.p_mel = var([1,0,0,1,1,1,1,0,  0,0,1,0,0,1,0,0], dur=1/4)
p1 >> quin(PRand(P[0:7][:4],seed=400), dur=1/4, amplify=1*var.p_mel)

print(list(PRand([8])))

print(SynthDefs)

print(SynthDefs)
