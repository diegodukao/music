d1 >> play("x-o-", sample=4, rate=[1.1,1,-1,0.9])

d1 >> play("{[xxx][xx ][x  ]}", dur=1/8)

d1 >> play("x  x  o=oo", sample=3, dur=1/4, spin=4)

d1 >> play("x-o-", sample=5, lpf=linvar([200,2000],16))

d1 >> play("x--x--x-", sample=2, hpf=linvar([200,2000],16))

Clock.bpm = 140

d1 >> play("-( [-[--]]-)  ", sample=2, dur=1/4, amp=1.5).every(4, "stutter", dur=2, cycle=8).stop()

d2 >> play("(ph)(-k )(-d )", sample=2, dur=1/4, amp=1)
