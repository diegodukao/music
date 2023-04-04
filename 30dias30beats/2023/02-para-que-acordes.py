from foxdot_chord import Chord

Scale.default = "chromatic"

Clock.set_time(-1)
var.chords = var(P[Chord('Gmin7'), P(Chord('C7(b9)')) +12 , Chord('Amin7'), Chord('Dmin7')], 4)
var.p_bass = var([1,0,1,0,0,0,1,0,  0,0,1,1,0,1,0,1], dur=1/4)
b1 >> sawbass(P[var.chords[0], var.chords[1], var.chords[0], var.chords[2]], dur=1/4, amplify=1*var.p_bass, sus=1/4, amp=0.8, oct=4)
p1 >> risseto(var.chords, dur=PDur(3,8)*2, scale=Scale.chromatic, oct=4, amp=0.3, chop=0)

~p2 >> klank(P[var.chords[1]], dur=PDur(5,8,1)*2, pan=0.8, scale=Scale.chromatic, amp=0.8, amplify=var([1,0], dur=PDur(3,8,2)))

var.p_kick = var([1,0,0,0,0,0,1,0,  0,0,1,0,0,0,0,1], dur=1/4)
d1 >> play("X", dur=1/4, amplify=1*var.p_kick, amp=0.6, sample=0)
d2 >> play("....O...", dur=1/4, amp=0.5, sample=0)
d3 >> play("-------[--]", amp=0.7, pan=-1)

Group(b1, p2).solo()

Group(b1, p2).solo(0)
~p2 >> klank(P[var.chords[1]], dur=PDur(5,8,1)*2, pan=0.8, scale=Scale.chromatic, amp=1, amplify=var([1,0], dur=PDur(3,8,2)), chop=2).shuffle()
p1 >> risseto(var.chords, dur=PDur(3,8)*2, scale=Scale.chromatic, oct=4, amp=0.3, chop=2)
d4 >> play('[ss]', amplify=var([1,0], dur=[2,2,2,2,2,2,1,1/2,1,1/2,1/2,1/2]), pan=0.6)

p1.chop = 0
p2.chop = 0
Group(p1, p2).solo()


