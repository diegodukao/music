rimshot = "/home/diego/.virtualenvs/foxdot/lib/python3.10/site-packages/FoxDot/snd/t/lower/alt_rimshot_3.wav"

use_bpm 70

live_loop :met do
  sleep 1
end

mel = false
rim = false
bd = false
hh = true
pchords = false
bass = false

rim = true
bd = true
hh = true
pchords = true
bass = true

live_loop :rimshot, sync: :met do
  a = 1
  if not rim
    a = 0
  end
  sample rimshot, amp: a if spread(7, 16, rotate: 2).tick
  sleep 0.25
end

live_loop :bd, sync: :met do
  a = 0.7
  if not bd
    a = 0
  end
  
  sample :drum_bass_soft, amp: a
  sleep 0.25
  sleep 0.5
  sample :drum_bass_soft, amp: a
  sleep 0.25
end

live_loop :hh, sync: :met do
  a = [0.2,0.13]
  if not hh
    a = [0]
  end
  
  sample :drum_cymbal_closed, pan: -0.8, amp: a.tick
  sleep 0.25
end

#(chord :b2, '7', invert: 2, num_octaves: 2)

chords = [(chord :e3, :major7), (chord :e3, :major7), (chord :e3, :major7), (chord :f3, :m7), false,(chord :f3, :m7), false]
live_loop :chords, sync: :met do
  use_synth :piano
  a = 0.4
  if not pchords
    a = 0
  end
  
  if spread(7, 16, rotate: 2).tick(:a)
    cchord = chords.tick(:b)
    play cchord, amp: a if cchord
  end
  sleep 0.25
end

live_loop :bass, sync: :met do
  use_synth :fm
  a=0.35
  if not bass
    a = 0
  end
  
  play :e2, amp: a
  sleep 0.25
  sleep 0.5
  
  sample :e2, amp: a
  sleep 0.25
  play :e2, amp: a
  sleep 0.25
  sleep 0.5
  
  sample :e2, amp: a
  sleep 0.25
  play :f2, amp: a
  sleep 0.25
  sleep 0.5
  
  sample :f2, amp: a
  sleep 0.25
  play :f2, amp: a
  sleep 0.25
  sleep 0.5
  
  sample :f2, amp: a
  sleep 0.25
end

live_loop :melody, sync: :met do
  use_synth :blade
  use_random_seed 66
  a = 0.1
  if not mel
    a = 0
  end
  
  with_fx :reverb, mix: 0.5, room: 1 do
    with_fx :ixi_techno, phase: 3, res: 0.6 do
      64.times do
        play (chord :f3, 'm7').choose, amp: a, pan: 0.4 if spread(5, 16).tick(:c)
        sleep 0.25
      end
    end
  end
end