# FoxDot - Do Zero à Algorave
# @diegodukao

Pietro Bapthysthe

Clock.bpm = 120

p1 >> play("X O ", sample=3, dur=1)

p2 >> play("-")

Root.default = "C"
Scale.default = "minor"

p3 >> bass(P[0,2,4], dur=[4])

p4 >> keys(p3.pitch + P(0,2,4), dur=2, amp=1.5)

p5 >> sitar(p3.pitch + P[0:6], amp=0.7).every(4, "stutter", 2, oct=3).every(4, "offadd", 2).shuffle()

~p5 >> sitar(P[0:6], dur=[1,1/2,2], amp=0.7)

print(SynthDefs)


