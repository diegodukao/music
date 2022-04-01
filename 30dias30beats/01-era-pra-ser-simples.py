d1 >> play("Xs", amp=0.5)

b1 >> bass(P[0], dur=PDur(2,5,3), sus=0.25, amp=0.4)

p2 >> swell(var.r + P[0,2,4-7] -7,dur=[1/4, 1/4,1/2, 1/4,1/4], amp=0.2, pan=-0.7)
p2.amplify = var([1,0], dur=PDur(6,8))
p2.amp = var([0.3,0], dur=[6,2])

p3 >> swell(var.r + P[0,2,4-7] -7 +4,dur=[1/4, 1/4,1/2, 1/4,1/4], amp=0.2, pan=0.8)
p3.amplify = var([1,0], dur=PDur(6,8))
p3.amp = var([0.3,0], dur=[6,2])

p4 >> swell(var.r + P[0,2,4-7] -7 +2,dur=[1/4, 1/4,1/2, 1/4,1/4], amp=0.2)
p4.amplify = var([1,0], dur=PDur(6,8))
p4.amp = var([0.3,0], dur=[6,2])
Group(b1,p2,p3,p4).solo()

Group(p2,p3,p4).solo(0)
d2 >> play("-", amp=0.5, pan=-0.8)
d3 >> play("  o ", amp=0.5)

var.r = var([3])

p1 >> keys(var.r + P[0:7].shuffle(), dur=[6,1/2,1/4,1/2,1/4,rest(1/4), 1/4,1,1], amp=0.02, drive=0.6, pan=0.3).penta()


