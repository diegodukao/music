rimshot = "/home/diego/.virtualenvs/foxdot/lib/python3.10/site-packages/FoxDot/snd/t/lower/alt_rimshot_3.wav"
use_bpm 115

live_loop :met do
  sleep 1
end

bass = true
bd = true
rim = true
mel = true
chords = false

live_loop :bd, sync: :met do
  a = [0.7,1]
  if not bd
    a = [0]
  end
  sample :drum_bass_soft, amp: a.tick
  sleep 0.25
  sleep 0.25
  sleep 0.25
  sample :drum_bass_soft, amp: a.tick
  sleep 0.25
  
  sample :drum_bass_soft, amp: a.tick
  sleep 0.25
  sleep 0.25
  sleep 0.25
  sample :drum_bass_soft, amp: a.tick
  sleep 0.25
end

live_loop :rimshot, sync: :met do
  a = 1
  if not rim
    a = 0
  end
  sample rimshot, amp: a if spread(7, 16, rotate: 2).tick
  sleep 0.25
end

live_loop :hh, sync: :met do
  sleep 0.5
  sample :drum_cymbal_pedal, amp: 0.2, pan: -0.6
  sleep 0.5
  # sleep 1
end

live_loop :bass, sync: :met do
  use_synth :fm
  
  a = 0.4
  if not bass
    a = 0
  end
  
  use_random_seed 239
  with_fx :reverb, room: 0.9, mix: 0.5 do
    32.times do
      play (scale :f2, :dorian).choose, release: 0.2, amp: a, pan: 0 if spread(7, 16, rotate: 2).tick
      sleep 0.25
    end
  end
  
end

live_loop :chords, sync: :met do
  use_synth :piano
  a = 0.4
  if not chords
    a = 0
  end
  p = -0.5
  64.times do
    play (chord_degree :i, :f3, :dorian), amp: a, pan: p if spread(7, 16).tick
    sleep 0.25
  end
  64.times do
    play (chord_degree :ii, :f3, :dorian), amp: a, pan: p if spread(7, 16).tick
    sleep 0.25
  end
end

live_loop :melody, sync: :met do
  use_synth :chiplead
  
  a = 0.2
  if not mel
    a = 0
  end
  
  use_random_seed 239
  with_fx :reverb, room: 0.9, mix: 0.5 do
    32.times do
      play (scale :f3, :dorian).choose, release: 0.2, amp: a, pan: 0.4 if spread(7, 16, rotate: 2).tick
      sleep 0.25
    end
  end
end