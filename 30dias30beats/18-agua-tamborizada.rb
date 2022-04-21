require "~/Projects/livecoding/petal/petal.rb"

d1 "tabla:1(5,8)", slow: 2, rate: "1 0.8 0.6", pan: 0.5

d2 "bd", n: 1

with_fx :echo, phase: 0.25, max_phase: 4, decay: 2 do
  d4 "jazz/4", n: 2
end

d3 "tabla:3(3,8)", slow: 1, pan: -1

live_loop :bass, sync: :d0 do
  use_synth :fm
  if spread(3,8).tick
    play :eb2
    use_synth :tri
    with_fx :distortion do
      play :eb2, amp: 0.9, release: 0.8
    end
  end
  
  sleep 0.5
end

live_loop :riff, sync: :d0 do
  with_fx :reverb do
    use_synth :piano
    notes = (ring :eb2)
    a = 0
    p = -0.4
    use_random_seed 5870
    notes = (scale :eb2, :phrygian)
    play notes.choose, amp: a, pan: p
    sleep 1.5
    play notes.choose, amp: a, pan: p, sustain: 0
    sleep 0.125
    play notes.choose, amp: a, pan: p, sustain: 0
    sleep 0.125
    play notes.choose, amp: a, pan: p
    sleep 0.25
    play notes.choose, amp: a, pan: p
    sleep 0.5
    play notes.choose, amp: a, pan: p
    sleep 0.5
    play notes.choose, amp: a, pan: p, sustain: 0
    sleep 0.125
    play notes.choose, amp: a, pan: p, sustain: 0
    sleep 0.125
    play notes.choose, amp: a, pan: p
    sleep 0.25
    play notes.choose, amp: a, pan: p
    sleep 0.5
  end
end