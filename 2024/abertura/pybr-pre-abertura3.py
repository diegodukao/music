# @diegodukao
# ALGORAVE AMANHA - Galpao Ladeira das Artes - 18hs

~s1 >> loop("/home/diego/Projects/music/samples/python-sample.wav", dur=[1,1/2,1, rest(2.5)], rate=0.9, amp=0.3)

planet()




~b1 >> sawbass(var.r, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.9)

p2 >> pluck(var.r + P[0:6], amp=0.8, dur=PDur(3,8), pan=-0.8).every(4,"offadd",2).penta()



p1.stop()

p_all.stop()

d_all.stop()













var.r = var(P[2])


p1 >> saw(var.r + P(0,2+7,4,6) - 7, dur=PDur(3,8,1)*2, amp=0.5, sus=1/2, pan=0, room=1)

~b1 >> sawbass(var.r, dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),1/2,rest(1/4)], sus=[1/4,1/4,1/4,1,1/4,1/4,1/4], amp=0.5)

p2 >> pluck(var.r + P[0:6], amp=0.8, dur=PDur(3,8), pan=-0.8).every(4,"offadd",2).penta()

planet()

b1.stop()

cowbell()

d_all.stop()

p2.stop()




def planet():
    d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4], pan=-0.6, amp=0.8)
    d2 >> play("X", sample=2, dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4], amp=0.6)
    d3 >> play("O", sample=0,dur=[rest(1), 1], amp=0.35)
def cowbell():
    d4 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.3, pan=0.8)
