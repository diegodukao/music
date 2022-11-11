##| d1 >> play("-", dur=[1/2,1/4,1/4,1/2,1/4,1/4,1/2,1/4,1/4,1/4,1/4,1/4,1/4])
##| d2 >> play("T", dur=[1/2,1/2,1/4,1/2,1/4,rest(1/4),1/2,1/4,1/2,1/2], amp=0.2, pan=-0.8).stop()
##| d3 >> play("o", dur=[rest(1), 1])
##| d4 >> play("x", dur=[1,rest(1/2),1/2,rest(2),1,rest(1/2),1/2,rest(1/2),1/2,rest(1/4),3/4])
##| f1 >> play("X", dur=[3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),1/4,    3/4,rest(1/4), rest(1),1/2,1/2, rest(3/4),rest(1/4),], amp=0.8)
##| f2 >> play("k", sample=0, dur=[rest(3/4),1/4, rest(1/2),1/2, rest(1),1], drive=0.04)
use_bpm 120

live_loop :met do
  sleep 1
end

def is_list_like?(o)
  o.is_a?(Array) || o.is_a?(SonicPi::Core::SPVector)
end

def sample_timed(sampl, times, *args)
  times.each do |duration|
    kwargs = if args.last.is_a?(Hash) then args.last else {} end
    if duration.is_a? String  # rest. sample is not played
      duration = eval(duration)
    else
      sample(sampl, *[kwargs])
    end
    kwargs[:duration] = duration
    sleep(duration)
  end
end



# planet rock
live_loop :hh do
  stop
  sample_timed :drum_cymbal_closed, [1/2.0,1/4.0,1/4.0,1/2.0,1/4.0,1/4.0,1/2.0,1/4.0,1/4.0,1/4.0,1/4.0,1/4.0,1/4.0]
end
live_loop :bd do
  stop
  sample_timed :drum_bass_soft, [1.0,'1/2.0',1/2.0,'2.0',1.0,'1/2.0',1/2.0,'1/2.0',1/2.0,'1/4.0',3/4.0]
end
live_loop :sn do
  stop
  sample_timed :drum_snare_hard, ['1.0', 1.0]
end
live_loop :cb do
  stop
  sample_timed :drum_cowbell, [1/2.0,1/2.0,1/4.0,1/2.0,1/4.0,'1/4.0',1/2.0,1/4.0,1/2.0,1/2.0]
end


# beatbox do catra
live_loop :bd2 do
  stop
  sample_timed :drum_bass_soft, [3/4.0,'1/4.0','1',1/2.0,1/2.0,'3/4.0',1/4.0,3/4.0,'1/4.0','1',1/2.0,1/2.0,'3/4.0','1/4.0']
end
live_loop :rim do
  stop
  sample_timed :drum_cowbell, ['3/4.0',1/4.0,'1/2.0',1/2.0,'1',1]
end


# volt mix
##| d1 >> play("-", dur=1/2, pan=-0.8)
##| d2 >> play("m", dur=[1/4,1/4,1/2,rest(1),rest(1/2),1/4,1/4], amp=0.2)
##| d3 >> play("x", dur=[3/4,1/4,rest(1/2),1/2,rest(1/2),1/2,rest(1)], amp=0.7)
##| d4 >> play("o", dur=[rest(1),1], amp=0.4)
##| d5 >> play("t", dur=[rest(3/4),1/4,rest(1/4),3/4,3/4,1/4,rest(1/2),1/2], pan=0.8, amp=0.6)

chegou = "/home/diego/MusicProjects/algoclub-samples/export/chegou-o-momento-da-verdade.wav"
esta = "/home/diego/MusicProjects/algoclub-samples/export/esta-que-ta-aqui-atras.wav"


qual_vc = "/home/diego/MusicProjects/algoclub-samples/export/qual-voce-acha-que-e.wav"
bom_esta = "/home/diego/MusicProjects/algoclub-samples/export/bom-pra-mim-e-esta-que-ta-aqui-atras.wav"

bom = "/home/diego/MusicProjects/algoclub-samples/export/bom-pra-mim.wav"


define :liberta do
  esta = "/home/diego/MusicProjects/algoclub-samples/export/esta-que-ta-aqui-atras.wav"
  live_loop :sampler, sync: :bd3 do
    stop
    sample esta, beat_stretch: 2
    sleep 8
  end
end

sample bom, beat_stretch: 2
sleep 1.1
liberta()

live_loop :hh3, sync: :met do
  sample_timed :drum_cymbal_closed, [1/2.0]
end
live_loop :bd3, sync: :met do
  sample_timed :drum_bass_soft, [3/4.0,1/4.0,'1/2.0',1/2.0,'1/2.0',1/2.0,'1/2.0','1/2.0']
end
live_loop :sn3, sync: :met do
  sample_timed :drum_snare_hard, ['1',1]
end
live_loop :rim3, sync: :met do
  sample_timed :tabla_tas3, ['3/4.0',1/4.0,'1/4.0',3/4.0,3/4.0,1/4.0,'1/2.0',1/2.0]
end
live_loop :tom, sync: :met do
  sample_timed :elec_soft_kick, [1/4.0,1/4.0,1/2.0,'1','1/2.0',1/4.0,1/4.0]
end
