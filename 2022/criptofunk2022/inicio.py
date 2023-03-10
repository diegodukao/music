# Fazendo Funk com Programação - Criptofunk 2022
# @diegodukao e @thaisnviana

d1 >> play("-", dur=1/2)
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4])
d3 >> play("x", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)])
d4 >> play("o", dur=[rest(1),1])

d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2])


var.r = var([0], dur=8)
p1 >> piano(var.r + P[0,1,2,3,4,5,6,7], dur=1, amp=0.6).shuffle().every(3, "stutter", 3).penta().stop()
p2 >> bass(var.r, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)], sus=1/2, amp=0.6)


d1 >> play("x", dur=[3/4,rest(1/4),rest(1),1/2,1/2,rest(3/4),1/4])
d2 >> play("o", dur=[rest(3/4), 1/4, rest(1/2), 1/2, rest(1),1])



# volt mix 
d1 >> play("-", dur=1/2)
d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4])
d3 >> play("x", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)])
d4 >> play("o", dur=[rest(1),1])
d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2])

# planet rock
d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])
d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.5)
d3 >> play("o", dur=[rest(1), 1])
d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])
d5.stop()
