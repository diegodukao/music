Clock.bpm = 160
Scale.default = "mixolydian"

Clock.set_time(-1)
d1 >> play("x", dur=[1/2,rest(1),1/2], amp=0.5)
d2 >> play("t", sample=3, dur=PDur(7,16,2)*2, amp=1.5)
d3 >> play("-", amp=[0.8,0.3], pan=-0.8)
Clock.schedule(start2, Clock.now() + 16)

def start2():
    Clock.clear()
    Clock.set_time(-1)
    d1 >> play("x", dur=[1/2,rest(1),1/2], amp=0.5)
    d2 >> play("t", sample=3, dur=PDur(7,16,2)*2, amp=1.5)
    d3 >> play("-", amp=[0.8,0.3], pan=-0.8)
    var.r = var([0,4], dur=4)
    var.n = var([0])
    ~b1 >> bass(
        var.n +var.r + P[0,0,0, 2,2,2],
        dur=[1/2,rest(1),1/2,1/2,rest(1),1/2,  1/2,rest(1),1/2, 1,1/2,rest(1/2)],
        sus=[1,1/2,1/2,1,1/2,1/2,   1,1/2,1/2, 1,1,0],
        #sus=P[1.5, 0.5, 1, 1,    1, 0.4, 0.3, 0.9,1],
        lpf=800, amp=0.3)
    var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
    p1 >> piano(var.n+var.r + var.f, dur=PDur(7,16,2)*2, amp=0.4, pan=0.4)


var.n = var([0])

p2.stop()

~p2 >> razz(var.n + P[2,3,4,3,0,0], dur=[14, 1/2,1/2,1,8, rest(8)], amp=0.5, pan=-0.4, room=1)

