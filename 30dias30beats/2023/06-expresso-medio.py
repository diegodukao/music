from foxdot_chord import Chord

Scale.default = "chromatic"

Clock.set_time(-1)

var.chords = var([P(Chord('Amin7')) - 12, P(Chord('G7')) -12, Chord('Cm9'), P(5, 9, 12-12, 14-12) ], 4) 
p1 >> risseto(var.chords, dur=4, amp=0.4)
d1 >> play("X.")
d4 >> play(".s")
p3 >> pluck(P[0,var.chords[2],0,0,var.chords[0],0,0,0,0,0], dur=[1/2,1/2,rest(1/2),1/2,1/4,1/4,1/4,1/4,1/2,1/2], amp=0.8)

var.p_bass = var([1,0,1,0,0,0,1,0,  0,0,1,1,0,1,0,1], dur=1/4)
b1 >> abass(P[var.chords[0], var.chords[1], var.chords[0], var.chords[2]], dur=1/4, amplify=1*var.p_bass, sus=1/4, amp=0.8, oct=4)

Group(p3,d4).solo()

Group(p3,d4).solo(0)
p2 >> soprano(var.chords[0], dur=4, pan=0.8, amp=0.6)
b1 >> abass(P[var.chords[0], var.chords[1], var.chords[0], var.chords[2]], dur=1/4, amplify=1*var.p_bass, sus=1/4, amp=0.8, oct=4)
d2 >> play(".o", dur=1)
var.p_hh = var([1,0,1,0,1,1,0,1,  1,0,1,0,1,1,1,1], dur=1/4)
d3 >> play("-", dur=1/4, pan=-0.8, amplify=1*var.p_hh)

p1.stop()

print(SynthDefs)
