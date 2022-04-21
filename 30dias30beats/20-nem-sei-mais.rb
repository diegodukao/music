require "~/Projects/livecoding/petal/petal.rb"

cps 0.5
use_bpm get_bpm

d1 "bd ~", slow: 1

d3 "tabla:3(5,8)", slow: 1, rate: "1 0.8 0.6", pan: 0.5

d2 "hh(13,16)", slow: 2,  amp: "0.6 0.4 0.3 0.5", pan: -0.5

d4 "perc(9,16,2)", amp: 0.3

#d2 :silence
#d4 :silence
bass = true

live_loop :chords, sync: :d0 do
  puts get_bpm
  use_synth :blade
  s = 3
  a= 0.7
  with_fx :reverb, room: 0.8 do
    with_fx :slicer, wave: 1, phase: 0.25 do
      play (chord :e3, 'm7'), sustain: s, amp: a
      sleep 4
      play (chord :d3, 'm7+9'), sustain: s, amp: a
      sleep 4
      play (chord :g3, '13'), sustain: s, amp: a
      sleep 4
      play (chord :c3, :major7), sustain: s*2, amp: a
      sleep 4
    end
  end
end

live_loop :bass, sync: :d0 do
  use_random_seed 5326
  use_synth :fm
  a = 0.2
  if not bass
    a =0
  end
  r = 0.25
  32.times do
    play (chord :e2, 'm7').choose, amp: a, release: r if (spread 7, 16).tick
    sleep 0.125
  end
  16.times do
    play (chord :d2, 'm7+9').choose, amp: a, release: r if (spread 7, 16).tick
    sleep 0.125
  end
  16.times do
    play (chord :d2, 'm7+9').choose, amp: a, release: r if (spread 11, 16).tick
    sleep 0.125
  end
  32.times do
    play (chord :g2, '13').choose, amp: a, release: r if (spread 5, 16).tick
    sleep 0.125
  end
  16.times do
    play (chord :c3, :major7).choose, amp: a, release: r if (spread 5, 16).tick
    sleep 0.125
  end
  16.times do
    play (chord :c2, :major7).choose, amp: a, release: r if (spread 5, 16).tick
    sleep 0.125
  end
end