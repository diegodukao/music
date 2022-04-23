
use_bpm 80

live_loop :met do
  sleep 1
end

mel = true
bass = false
chords = false
snare = false

bass = true
chords = true

live_loop :snare, sync: :met do
  s1_amp = [1,0.3,0.3,1,  0.3,0.3,1,0.3,  0.3,1,0.3,0.3]
  s2_amp = [1,0.3,0.3,1]
  s6_amp = [1,0.3,0.4,0.3,0.4,1]
  
  if not snare
    s1_amp = [0]
    s2_amp = [0]
    s6_amp = [0]
  end
  12.times do
    sample :drum_snare_soft, amp: s1_amp.tick(:a)
    sleep 0.25
  end
  if [true, false].tick
    4.times do
      sample :drum_snare_soft, amp: s2_amp.tick(:b)
      sleep 0.25
    end
  else
    6.times do
      sample :drum_snare_soft, amp: s6_amp.tick(:c)
      sleep 1/6.0
    end
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

live_loop :bass, sync: :met do
  a = 0.8
  if not bass
    a =0
  end
  
  use_random_seed 80706808
  use_synth :fm
  16.times do
    play (scale :e2, :harmonic_minor).choose, amp: a, release: 0.7 if (spread 5, 16).tick
    sleep 0.25
  end
end

live_loop :chords, sync: :met do
  a = 0.3
  if not chords
    a = 0
  end
  
  use_synth :piano
  with_fx :pan, pan: 0.5 do
    with_fx :normaliser, amp: a do
      play (chord_degree :i, :e3, :harmonic_minor, 4)
      sleep 1
      sleep 2
      play (chord_invert (chord_degree :iv, :e3, :harmonic_minor, 4), 1)
      sleep 1
    end
  end
end

live_loop :melody, sync: :met do
  use_synth :hollow
  
  a = 0.4
  if not mel
    a = 0
  end
  
  use_random_seed 95623065
  with_fx :reverb do
    with_fx :normaliser, amp: a do
      32.times do
        play (scale :e3, :harmonic_minor).choose, release: 0.2 if (spread 15, 32).tick
        sleep 0.25
      end
      
    end
  end
  
end
