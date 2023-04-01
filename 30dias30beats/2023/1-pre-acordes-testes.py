Scale.default = "chromatic"

#Cmin79

p1 >> tworgan4(P(0,2-7,3,7,var([10,9], dur=16)), dur=2, hpf=600, lpf=0, amp=0.4, sus=1.7)
b1 >> sawbass(P[0,2-7,3,7,var([10,9], dur=16)][:8], dur=[2/3], sus=0.8, amp=0.8).reverse()

d1 >> play("- ", dur=1/3)

d2 >> play("x ( o)", dur=1/3)

~p2 >> vinsine(P[0,2-7,3,7,var([10,9], dur=16)], dur=1/3, sus=1/3, amplify=var([1,0], PDur(7,9)/3)).shuffle()

d3 >> donk(P[0,2-7,3,7,var([10,9], dur=16)], dur=2/3).every(4, "stutter", var([2,3], dur=[1]))

Group(p1, d3, b1).solo(0)

print(SynthDefs)
