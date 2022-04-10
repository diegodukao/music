p1 >> karp(P[0,0.5]-7, dur=1/4, amplify=var([1,0], 1), amp=0.4, drive=0.3)
Clock.bpm = 40
var.metal = var([4])
~a1 >> play("X [XX]( [ ])", dur=P[1/4]*var.metal)
~a2 >> play(" O O", dur=P[1/4]*var.metal, amp=0.7)
~a3 >> play(" = =", dur=P[1/4]*var.metal, amp=1.4)
a4 >> play("-")


~d1 >> play('[VV]', dur=1/4, amplify=var([0, .3], dur=1/2 * P[1, 1/2, 1/2, 1, 1/4, 3/4]), lpf=1400, sample=1, pan=PWhite(-.3, .3))


~d2 >> dirt(
  (c1.pitch - 7, c1.pitch, c1.pitch + var([0, -5], 1/2)), 
  oct=4, 
  sus=4, 
  dur=2, 
  amp=0.25, 
  dist=0.1, 
  chop=2
)

b_all.stop()

a_all.stop()
~b1 >> play("X", dur=1/8, amp=[0.8, 0.7, 0.6])
~b2 >> play("O  O  O  O  O   ", dur=1/8, amp=0.7)
~b3 >> play("=...=...=...=...", dur=1/8, amp=1.4)
