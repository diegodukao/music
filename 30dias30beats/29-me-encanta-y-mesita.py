Scale.default = "dorian"
Root.default = "E"
Root.default -= 12
Clock.bpm = 100

Clock.set_time(-1)
var.ch = var([0], dur=8)
b1 >> bass(var.ch + P[0, 2, 4], dur=PDur(3,8), amp=0.7, lpf=800)
n1 >> play("-[--]", dur=1/2)
~d2 >> play("[V ]V", dur=PDur(3, 8), amp=0.4)
~d4 >> play("[ K]", dur=var([2, 1, 1, 1/8], dur=P[14, 1, 3/4, 1/4]), delay=1/2, amp=0.9, sample=1, drive=0.03, hpf=2500, hpr=0.9)

var.ch = var([0], dur=8)

~p1 >> piano(var.ch + P(0,2+7,4,6,8-7) + var([0,2], dur=1), dur=PDur(5,8)*4, amp=0.6, pan=-0.2).every(8, "stutter", 3, pan=0.5, amp=0.6)

var.ch = var([0], dur=8)
~p2 >> space(var.ch + P[0,2+7,4,6,8-7] + var([0,2], dur=1), dur=1/4, amp=0.2, pan=-1, amplify=var([1,0], dur=PDur(7,8))).stop()
