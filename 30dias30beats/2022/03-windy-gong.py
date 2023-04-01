Scale.default = "minor"
Clock.bpm = 80

Clock.set_time(-1)
~p1 >> gong(P[0,3,1,2,6][:8],oct=4,dur=PDur(5,8), pan=-1, amp=0.8)
~p2 >> gong(P[0,3,1,2,6][:8],oct=4,dur=PDur(5,8), pan=1, amp=0.8)#.every(2,"reverse").every(4, "offadd", -2)

p3 >> space(P[0, -1], dur=4, sus=2, pan=[0.8,-0.8])

Group(p1,p2).amplify = var([1,0], dur=PDur(3,8))

d1 >> donk(P[0,0,4,2], dur=PDur(3,8)/2, amp=0.2, pan=-0.8)
d2 >> play("X", dur=1/2, amp=0.15, pan=0, sus=0.8)
d3 >> play(".((o[oo])).[o o]", amp=0.2, pan=0.2)

p_all.solo()
