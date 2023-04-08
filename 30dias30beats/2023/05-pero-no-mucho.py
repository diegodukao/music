Scale.default = "minor"
Clock.bpm=100

Clock.set_time(-1)
var.r = var([0,-1], dur=16)
~p2 >> spacesaw(var.r+ P(0,2+7,4,8-7) + var([0,2], dur=1), dur=PDur(5,8)*4, amp=0.5, oct=4, pan=-0.5)
var.p_hh = var([1,0,1,0,1,1,0,0,  1,1,1,0,1,1,0,1], dur=1/4)
var.p_b  = var([0,0,0,1,0,0,1,0,   0,0,0,1,0,0,1,0], dur=1/4)
var.p_s  = var([0,0,0,0,0,0,0,1,   0,0,0,0,0,0,0,0], dur=1/4)
d1 >> play("-", dur=1/4, amplify=1*var.p_hh, pan=-0.8, amp=P[1,0,1,0,0.8,0.8,0,0,  1,0.8,0.8,0,0.8,0.8,0,0.8]-P[0.2])
d2 >> play("[V ]V", dur=PDur(3,8), amp=0.3)
d3 >> play(".KK", dur=PDur(3,8), amp=0.5)
d5 >> play("X..", dur=PDur(3,8), amp=0.5)

~d4 >> play("[ K]", dur=var([2,1,1,1/8], dur=P[14,1,3/4,1/4]), delay=1/2, amp=0.5, drive=0.03)

#var.p_mel1 = var([1,0,0,1,1,1,1,0,  0,0,1,0,0,0,0,1], dur=1/4)
var.p_mel1 = var([1,1,0,1,0,1,1,1,  1,0,1,0,0,1,0,1], dur=1/4)
~p1 >> tworgan3(PRand(P[0:7], seed=100)[:8] + var.r, dur=1/4, amplify=1*var.p_mel1, amp=0.2, sus=0.4, pan=0.5)#.every(3,"offadd",-1)
b1 >> bass(var.r + P[0,2,4], dur=PDur(3,8), amp=0.6, sus=[0.7,0.4,0.4], oct=5)

Group(p2,d3,d4).solo()

