live_loop :met do
  sleep 1
end

use_bpm 120

bass = false
mel = true

live_loop :bd, sync: :met do
  with_fx :reverb, room: 0.9, mix: 0.5 do
    with_fx :normaliser, amp: 0.6 do
      sample :tabla_ghe2, amp: 0.6
    end
  end
  4.times do
    sample :tabla_tas3, rate: 0.5
    sleep 3/4.0
    sleep 1/4.0
    sleep 1
    sample :tabla_tas3
    sleep 1/2.0
    sample :tabla_tas3
    sleep 1/2.0
    sleep 3/4.0
    sample :tabla_tas3
    sleep 1/4.0
  end
  with_fx :reverb, room: 0.9, mix: 0.5 do
    with_fx :normaliser, amp: 0.6 do
      sample :tabla_ghe2, amp: 0.6
    end
  end
  4.times do
    sample :tabla_tas3, rate: 0.6
    sleep 3/4.0
    sleep 1/4.0
    sleep 1
    sample :tabla_tas3
    sleep 1/2.0
    sample :tabla_tas3
    sleep 1/2.0
    sleep 3/4.0
    sample :tabla_tas3
    sleep 1/4.0
  end
end

live_loop :sn, sync: :met do
  sleep 3/4.0
  sample :drum_snare_soft
  sleep 1/4.0
  sleep 1/2.0
  sample :drum_snare_soft
  sleep 1/2.0
  sleep 1
  sample :drum_snare_soft
  sleep 1
end

live_loop :mel, sync: :met do
  use_random_seed 7765
  use_synth :pluck
  a = 0.4
  if not mel
    a = 0
  end
  
  with_fx :reverb, room: 0.9, mix: 0.5 do
    with_fx :normaliser, amp: 0.2 do
      5.times do
        play (scale :bb3, :harmonic_minor).choose, amp: a
        sleep 1/2.0
        play (scale :bb3, :harmonic_minor).choose, amp: a
        sleep 1/4.0
        play (scale :bb3, :harmonic_minor).choose, amp: a
        sleep 1/4.0
      end
      play (scale :bb3, :harmonic_minor).choose, amp: a
      sleep 1/2.0
      play (scale :bb3, :harmonic_minor).choose, amp: a
      sleep 1/2.0
      play (scale :bb3, :harmonic_minor).choose, amp: a
      sleep 1/2.0
      play (scale :bb3, :harmonic_minor).choose, amp: a
      sleep 1/2.0
      
      play (scale :bb3, :harmonic_minor).choose, amp: a
      sleep 1
    end
  end
  
end

live_loop :bass, sync: :met do
  use_synth :fm
  
  a = 0.2
  if not bass
    a = 0
  end
  with_fx :distortion do
    play :bb2, sustain: 2, amp: a
    sleep 3
    play :bb2, sustain: 0.2, amp: a
    sleep 1
    play :b2, sustain: 3, amp: a
    sleep 4
    
    
    play :bb2, sustain: 2, amp: a
    sleep 3
    play :bb2, sustain: 0.2, amp: a
    sleep 1
    play :b2, sustain: 0.2, amp: a
    sleep 1
    play :d3, sustain: 0.2, amp: a
    sleep 1
    play :b2, sustain: 0.2, amp: a
    sleep 1
    play :bb2, sustain: 0.2, amp: a
    sleep 1
  end
end