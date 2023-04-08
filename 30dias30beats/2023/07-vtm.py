from foxdot_chord import Chord
Scale.default = "chromatic"

Clock.bpm = 65

Clock.set_time(-1)
c1 = P(-1,0,4,7,11,14,18)  # CMaj9(#11)
c2 = P(-3,3,7,11,14)  # B7alt
c3 = P(-8,-5,2,6,11)  # Em9
c4 = P(-10,-7,0,4,9)  # Dm9
var.chords = var(P[c1,c2,c3,c4], dur=[1,1,4,2])
p1 >> rhodes(var.chords, dur=[1,1,2,2,2], amp=0.3, pan=-0.6)
~b1 >> bass(var.chords[0], dur=[1/4,3/4,1/4,3/4,1/4,7/4,2,2], drive=0)
var.p_b = var(P[1,1,0,0, 0,0,0,1, 1,1,0,0, 0,0,0,0], dur=1/4)
d1 >> play("x", dur=1/4, amplify=1*var.p_b, amp=0.8)
d2 >> play("-", dur=1/4, amp=[1,0.3,0.3,0.3], pan=-0.8)
d3 >> play(".o", dur=1, amp=0.7)

p2 >> pianovel(P[var.chords[0],0,var.chords[-1]-12,2,var.chords[1],2], dur=PDur(var([6,4,3,4,3], dur=[2,1,3,1,1]),8), scale=Scale.major, drive=0.04, room=1, pan=0.5)


Group(b1,p2,d2).solo()
