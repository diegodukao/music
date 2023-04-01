Clock.bpm = 65
Scale.default = "harmonicMinor"

Clock.set_time(-1)
d1 >> play("-", dur=P[rest(1/8), 1/8, 1/8, 1/8, rest(1/4), 1/4,   rest(1/4), 1/4, 1/4, rest(1/4),1/4, 1/4, rest(1/2),   1/6, 1/6, 1/6, 1/6, 1/6, 1/6 ], drive=0)
d2 >> play("x", dur=P[1/8, rest(3/8), 1/4, rest(1/4),    rest(3/4), 1/4, rest(1/2), 1/4, 1/4, rest(1)], amp=1)
d3 >> play(" H", sample=0, dur=1, amp=1, drive=0.2)#, dur=[rest(1), rest(1/4), 1/4, rest(1/2)])
var.b = var([0,2,-1], [2,1,1])
b1 >> bass(var.b, dur=P[1/2, rest(1/2),    rest(1/2), 1/2, rest(1/2), 1/4, rest(1/4), 1/2, 1/2], amp=0.7, lpf=200)

~p2 >> viola(P[3,4,1,2,0]-7,dur=PDur(5,8)*4, amp=0.4, drive=0.2, room=0.4, mix=0.4, amplify=0.5, pan=-0.6).every(4, "stutter", 4, sus=1/4, pan=1, amp=0.4)
~p3 >> viola(P[3,4,1,2,0]-7+2, dur=PDur(5,8)*4, amp=0.4, drive=0.2, room=0.4, mix=0.4, amplify=0.5, pan=0.6).every(4, "stutter", 4, sus=1/4, pan=-1, amp=0.4)

p_all.stop()
s1 >> karp(P[0:7][:10].shuffle(), dur=[4,2,1/2,rest(1/4),1/2,1/4,rest(1/4), 1/4,1,1], amp=0.2, drive=0.3, pan=0.2).penta()
s2 >> piano(var.b + P(0-7,2-7,2,4), dur=PDur(5,16), amp=0.2, pan=-0.6)

s1.stop()
~p2 >> viola(P[3,4,1,2,0]-7, dur=PDur(5,8)*4, amp=0.4, drive=0.2, room=0.4, mix=0.4, amplify=0.5, pan=-0.6).every(4, "stutter", 4, sus=1/4, pan=1, amp=0.4)
~p3 >> viola(P[3,4,1,2,0]-7+2, dur=PDur(5,8)*4, amp=0.4, drive=0.2, room=0.4, mix=0.4, amplify=0.5, pan=0.6).every(4, "stutter", 4, sus=1/4, pan=-1, amp=0.4)

s1.stop()

Group(d3, p2, p3).solo()


