Clock.bpm = 120
Scale.default = "minor"         

Clock.set_time(-1)

var.chords = var([P(-7,0,2,4,6), P(-7,0,2,4,7)-2, P(6-7,0,2,4)+3-7, P(2-7,0+7,2,4)-2], dur=[3,5])
d1 >> play("-", dur=1/2, pan=-0.8, amp=[0.7,0.5])
d2 >> play("s", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.5, sample=3)
d4 >> play("s", dur=[rest(1),1], amp=0.8)
p2 >> vinsine(P[0,var.chords[0],2,6,var.chords[1],6,4,var.chords[2]], dur=[rest(1/2),1/2,1/2,1/2,1/2,1/2,1/2,1/2], amp=0.9, pan=-0.4)

p1 >> epiano(var.chords, dur=[3,5], amp=0.6, formant=0, drive=0.2, room=0.8, mix=0.5, pan=0.4)

p2.solo()

d3 >> play("X", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], amp=0.85)
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.5, sample=3)
d6 >> play("o", dur=[rest(1),1], amp=0.8)
d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=0.8, amp=1, drive=0.1)
var.chordsb = var([P(-7,0,2,4,6), P(-7,0,2,4,7)-2, P(6-7,0,2,4)+3-7, P(2-7,0+7,2,4)-2], dur=[4])
b1 >> bassguitar(P[var.chordsb[0], var.chordsb[0], var.chordsb[1]] + 7, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], drive=0.4)
Group(p1, p2).stop()

Group(p1,p2,d5).solo()





