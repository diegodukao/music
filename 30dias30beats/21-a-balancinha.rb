
use_bpm 130

live_loop :met do
  sleep 1
end

live_loop :snare, sync: :met do
  s1_amp = [1,0.3,0.3,1,  0.3,0.3,1,0.3,  0.3,1,0.3,0.3]
  s2_amp = [1,0.3,0.3,1]
  s6_amp = [1,0.3,0.4,0.3,0.4,1]
  12.times do
    sample :drum_snare_soft, amp: s1_amp.tick(:a)
    sleep 0.25
  end
  ##| 4.times do
  ##|   sample :drum_snare_soft, amp: s2_amp.tick(:b)
  ##|   sleep 0.25
  ##| end
  6.times do
    sample :drum_snare_soft, amp: s6_amp.tick(:c)
    sleep 1/6.0
  end
end

live_loop :hh, sync: :met do
  sleep 0.5
  sample :drum_cymbal_pedal, amp: 0.2, pan: -0.6
  sleep 0.5
  # sleep 1
end

live_loop :bd, sync: :met do
  ##| sleep 1
  sample :drum_bass_soft, amp: [0.7,1].tick
  sleep 1
end

mel = true

p1 = true
p2 = false
p3 = true
p4 = false
p5 = true
p6 = true
p7 = false

##| p1 = true
##| p2 = true
##| p3 = true
##| p4 = true
##| p5 = true
##| p6 = true
##| p7 = true

live_loop :melody, sync: :met do
  use_synth :dull_bell
  
  a = 1
  if not mel
    a = 0
  end
  
  with_fx :reverb do
    sc = (scale :c2, :major, num_octaves: 2)
    
    if p1
      play sc[7], amp: a
      sleep (1/3.0)*2
      play sc[7], amp: a
      sleep (1/3.0)*2
      play sc[7], amp: a
      sleep (1/3.0)*2
    end
    
    if p2
      play sc[7], amp: a
      sleep (1/3.0)*2
      play sc[8], amp: a
      sleep (1/3.0)*2
      play sc[9], amp: a
      sleep (1/3.0)*2
    end
    
    if p3
      play sc[6], amp: a, sustain: 1.5
      sleep 2
      
      play sc[4]+1, amp: a, sustain: 1.5
      sleep 2
    end
    
    if p4
      play sc[5], amp: a
      sleep (1/3.0)*2
      play sc[5], amp: a
      sleep (1/3.0)*2
      play sc[5], amp: a
      sleep (1/3.0)*2
    end
    
    if p5
      play sc[5], amp: a
      sleep (1/3.0)*2
      play sc[6], amp: a
      sleep (1/3.0)*2
      play sc[7], amp: a
      sleep (1/3.0)*2
    end
    
    if p6
      
      play sc[4], amp: a, sustain: 1.5
      sleep 2
      
      sleep 2
    end
    
    if p7
      play sc[5], amp: a
      sleep (1/3.0)*2
      play sc[8], amp: a
      sleep (1/3.0)*2
      play sc[7], amp: a
      sleep (1/3.0)*2
      
      play sc[4] +1, amp: a
      sleep (1/3.0)*2
      play sc[8], amp: a
      sleep (1/3.0)*2
      play sc[7], amp: a
      sleep (1/3.0)*2
      
      play sc[4], amp: a
      sleep (1/3.0)*2
      play sc[7], amp: a
      sleep (1/3.0)*2
      play sc[8], amp: a
      sleep (1/3.0)*2
      
      play sc[9], amp: a
      sleep 2
    end
    
    ##| play sc[9], amp: a
    ##| sleep 0.5
    ##| play sc[9], amp: a
    ##| sleep 0.5
    ##| play sc[9], amp: a
    ##| sleep 0.5
    ##| play sc[8], amp: a, sustain: 1
    ##| sleep 0.5
    
    ##| # play sc[8]
    ##| sleep 0.5
    ##| play sc[7], amp: a
    ##| sleep 0.5
    ##| play sc[8], amp: a
    ##| sleep 0.5
    ##| play sc[7], amp: a, sustain: 2.5
    ##| sleep 0.5
    
    ##| #play sc[7]
    ##| sleep 1
    ##| #play sc[7]
    ##| sleep 1
    
    ##| sleep 2
    
  end
end
