Scale.default = "minor"
Root.default = "A"
Root.default -= 12

#d1 >> piano(P[P(0,2+7,4+7,6,8), 4 + P(0-7,2,4-7,6), 5 + P(0-7,2-7,4,6,8-7), 2 + P(0,2-7,4-7,4,6,2+7), 3+ P(0,2-7,4-7,4,6,2+7)] -7, dur=[8,8,8,4,4])

#c1 = P[0,2+7,4+7,6,8].shuffle()[:4]
#c2 = 4 + P[0,2,4,6].shuffle()[:4]
#c3 = 5 + P[0,2,4,6,8-7].shuffle()[:4]
#c4 = 2 + P[0,2,4,4,6,2+7].shuffle()[:4]
#c5 = 3+ P[0,2,4,6,2+7].shuffle()[:4]

#d2 >> piano([c1, c1, c2,c2, c3,c3, c4,c5])


#d1 >> piano(P[P(0,2+7,4+7,6,8), 4 + P(0-7,2,4-7,6), 5 + P(0-7,2-7,4,6,8-7), 2 + P(0,2-7,4-7,4,6,2+7), 3+ P(0,2-7,4-7,4,6,2+7)] -7, dur=[8,8,8,4,4])


var.r = var([0,4], dur=4)

var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])

Clock.set_time(-1)
d1 >> play("x", dur=[1/2,rest(1),1/2], amp=0.5)
d2 >> play("t", sample=3, dur=PDur(7,16,2)*2, amp=1.2)
d3 >> play("-", amp=[0.8,0.3], pan=-0.8)
Clock.schedule(start, Clock.now() + 16)

def start():
    Clock.clear()
    Clock.set_time(-1)
    var.r = var([0,4], dur=4)
    var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
    p1 >> piano(var.r + var.f, dur=PDur(7,16,2)*2, amp=0.45, pan=-0.4)
    b1 >> bass(
        P[0,4,4,0,   4-7,8-7,13-7,11-7,8-7],
        dur=P[1.5, 0.5, 1, 1,    1, 0.5, 0.5, 1,1],
        sus=P[1.5, 0.5, 1, 1,    1, 0.4, 0.3, 0.9,1],
        lpf=800, amp=0.4)
    d1 >> play("x", dur=[1/2,rest(1),1/2], amp=0.5)
    d2 >> play("t", sample=3, dur=PDur(7,16,2)*2, amp=1.2)
    d3 >> play("-", amp=[0.8,0.3], pan=-0.8)
    

p2 >> quin(P[7, 9, 11, 6, 8,   -3+7, 6, 8, 10][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)


~p2 >> quin(P[7, 9, 11, 6, 8,   -3+7, 6, 8, 10][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)
var.r = var([0,4], dur=4)
var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
b1 >> bass(
    P[0,4,4,0,   4-7,8-7,13-7,11-7,8-7],
    dur=P[1.5, 0.5, 1, 1,    1, 0.5, 0.5, 1,1],
    sus=P[1.5, 0.5, 1, 1,    1, 0.4, 0.3, 0.9,1],
    lpf=800, amp=0.45)
~s1 >> play("#", dur=1, pan=0.6, amplify=var([1,0], dur=[1,2]), room=1, mix=0.5)

s1.stop()

p2.stop()



p2 >> quin(P[12, 14, 16-7, 11, 13,   0+7, 9, 11, 13][:11], dur=PDur(var([9,11,7], dur=[6,4,6]),16)*var([2,4], dur=[1.5,0.5]), amp=0.3, pan=0.5, room=1, mix=0.5, sus=p2.dur*0.5)
p2.amplify = var([0,1], dur=[1,1,0.5,1.5])
var.r = var([5,3], dur=[4])
var.f = var(P[P(0,2+7,4+7,6,8), P(0-7,2,4-7,6)] -7, dur=[2])
b1 >> bass(
    P[5-7,9-7,5-7,9-7,8-7,        3, 1, 2, 3, 2, 1],
    dur=P[1.5,0.5, 0.5, 0.5, 1,   0.75, 0.75, 0.5, 1, 0.5, 0.5],
    sus=P[1.5,0.5, 0.5, 0.5, 1,   0.7, 0.7, 0.4, 1, 0.4, 0.4],
    lpf=800, amp=0.45)
~s1 >> play("#", dur=1, pan=0.6, amplify=var([1,0], dur=[1,2]), room=1, mix=0.5)

s1.stop()

p2.stop()

########################3
a, b, c, d, e, f, g,
0, 1, 2, 3, 4, 5, 6

0, 4, 4, 0
a, e, e, a
1.5, 0.5, 1, 1

0, 4, 9,  7,  4
e, b, g8, e8, b
1, 0.5, 0.5, 1, 1
#



5-7, 9-7, 5-7, 9-7, 8-7
f, c, f, c, b
1.5, 0.5, 0.5, 0.5, 1

a, b, c, d, e, f, g,
0, 1, 2, 3, 4, 5, 6

2, 11, 13, 16, 3, 2, 1
c, e8, g8, c8, d, c, b
0.75, 0.25, 0.5, 0.5, 1, 0.5, 0.5
