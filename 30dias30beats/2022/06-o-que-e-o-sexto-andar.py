Scale.default = "harmonicMinor"
Clock.bpm = 88

Clock.set_time(-1)
d1 >> play("-----(-[---])--")
var.r = var([0, 3, 2, 4,1,-1], dur=[16,4,4,4,2,2])
p1 >> piano(var.r+P(0-7,2+7,4-7,6,8), dur=[8,8,4,4,4,2,2], amp=1, sus=4)
d2 >> play("x(.x[.x]).([.x].x)")
d3 >> play("..o.")

var.r = var([0, 3, 2, 4,1,-1], dur=[16,4,4,4,2,2])
d4 >> play("#", dur=32, pan=0.8)
p2_dur = P[3,1/2,1/2, 1/2, rest(1/2),2, rest(1),
           3,1/2,1/2, 1/2, rest(1/2),2, rest(1),
           3,1,   2, 1/2, rest(1/2),1,
           3,1/2,1/2, 1/2, 1/2,1, 1/2, 1/2,1]
p2_notes = P[0, 4,2,1,0,6,0,
             0, 4,2,1,0,6,0,
             0, 4,2,1,0,6,
             0, 3,4,6,5,4,3,2,2]
~p2 >> nylon(var.r+p2_notes -14,  dur=p2_dur, amp=0.7, lpf=0, drive=0)

Group(p1,p2,d1,d2).solo()
