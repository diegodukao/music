Clock.bpm = 80

var.metal = var([4])
~a1 >> play("X [XX]( [X])", dur=P[1/4]*var.metal, amp=0.5)
~a2 >> play(" O O", dur=P[1/4]*var.metal, amp=0.3)
~a3 >> play(" = =", dur=P[1/4]*var.metal, amp=1.4).stop()
a4 >> play("-")
b1 >> play("[XXXX].[XXXX].....", dur=[1/2], amp=[0.5])

var.r = var([2])
p1 >> pads(P[4, 2, 0, 6, 3, 1, 5], dur=PDur(7,16), amp=0.02, pan=0.4, dist=0.01, drive=0.6, chop=8, amplify=1).penta().every(8, "stutter", 3, pan=[-1,1], amp=0.02)

p1.amplify = var([1,0], dur=1)
p2 >> saw(P[c1.pitch,2,4] - 7, dur=[5,2,1], pan=-0.9, amp=0.051, dist=0.02, drive=0.4)

p2.stop()

Scale.default = "phrygian"
var.r = var([0])
Clock.set_time(-1)
c1 >> bass(var([0,var.r], dur=[8]), amp=0.5, drive=0.1)
~d2 >> dirt(
  (c1.pitch, c1.pitch+4), 
  oct=4, 
  sus=0.5, 
  dur=0.5, 
  amp=0.35, 
  dist=0.2,
  #drive=0.09, 
  chop=10,
  amplify=var([1,0], dur=PDur(9,16,3))
)
