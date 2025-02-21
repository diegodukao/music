Scale.default = "minor"

var.r = var(P[0], dur=8)

~p1 >> rlead(dur=4, spin=4)

p2 >> pianovel(var.r + [P(0,2,4,0), P(0,2,4,6)], shape=0.5, dur=8, formant=4, amp=0.5)

b1 >> bass(var.r, dur=1/2, sus=1/2, amp=0.3, chop=2)

b1 >> bass(var.r, dur=PDur(5,8), sus=1/2, amp=0.3, chop=2).every([6,2],"offadd", 3)

~d4 >> donk(var.r + P[0,2,4], dur=PDur(3,8), room=0.4, echo=0.75, echotime=6).shuffle().often("offadd", 3)

Group(b1, d4, p1).solo(0)

d4.stop()
Group(b1, d4, p1).solo(0)
~d1 >> play("xs")
d2 >> play("  o ")
d3 >> play("[--]-[---]-", amp=[0.2,0.8])

+++++++++++++++++++++++++++++++++
  
p3 >> pluck(fmod=linvar([-10,10],8), dur=1/4, sus=1, amp=0.1)


p2 >> dirt(P[0] + P(0,4), shape=0.5, dur=8, amp=1, amplify=0.5)


p2 >> dirt([0,5], shape=0.5, dur=8, amp=1, amplify=0.5) + (0,4)


print(SynthDefs)

p1 >> pluck(formant=7)


# Shift a synth's pitch
p1 >> rhodes(pshift=[0,1,2,3])

	
# Glide to and from the 5th note in the scale (7th semitone)
p1 >> pluck([0, 4], dur=4, glide=[7,-7])
 
# Shift a sample's pitch
p2 >> play("C", dur=2, pshift=[0,1,2,3])
 
# Can be used to make chords
p2 >> play("C", dur=2, pshift=[0, (0,4,7)], sample=3)

b1 >> bass(P[0,3,5], dur=PDur(3,8), sus=0.5)


p1 >> pluck(dur=4, vib=4)

p1 >> pluck(dur=4, slide=-1)

# Delay the slide effect to start half way through the note
p1 >> pluck(dur=4, slidefrom=0.5, slidedelay=0.5)

# Bend to 0 and back again
p1 >> pluck(dur=4, bend=-1)

p1 >> pluck(dur=4, slide=0.5, bend=0.5)


b1 >> bass(var([0,-2], dur=8),dur=2, chop=4, coarse=0)

d1 >> play("x-o-", hpf=linvar([0,2000],32))

d1 >> play("x-o-", hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28))

# Apply the bit-crusher effect
d1 >> play("X O ", crush=4)
  
# Reduce the number of bits for more distortion
d1 >> play("X O ", crush=4, bits=4)
  
# Or reduce the sample rate for a different style of distortion!
d1 >> play("X O ", crush=32, bits=8)


d1 >> play("x * ", shape=0.5)
  


# We can use echo to make drum loops more interesting too
d1 >> play("(x )( x)o ", room=0.1, echo=0.75/2, echotime=4)


print(SynthDefs)

# Move the pan left to right 4 times across 1 beat
p1 >> rlead(dur=4, sus=1, spin=4)
