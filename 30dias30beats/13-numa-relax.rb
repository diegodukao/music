use_bpm 70

live_loop :met1 do
  sleep 1
end

define :pattern do |pattern|
  return pattern.ring.tick == "x"
end

play_ = false

live_loop :kick, sync: :met1 do
  if not play_
    stop
  end
  a = 1.1
  sample :bd_fat, amp: a if pattern "x-----x---x---x-x-----x---x--x--"
  sleep 0.25
end

live_loop :snare, sync: :met1 do
  if not play_
    stop
  end
  sleep 1
  sample :drum_snare_hard, amp: 0.7
  sleep 1
end


live_loop :hh, sync: :met1 do
  #sleep 0.5
  sample :drum_cymbal_closed, amp: 0.4, pan: -0.5 if pattern "x-x-x-x-xxx-x-x-"
  sleep 0.25
end

chords = (ring :a3, :e3, :f3, :c3, :d3)

live_loop :chords, sync: :met1 do
  use_synth :pretty_bell
  a=0.8
  play (chord chords.tick, :m9), amp: a, sustain: 2
  sleep 4
  play (chord chords.tick, :m7), amp: a, sustain: 2
  sleep 4
  play (chord chords.tick, :major7), amp: a, sustain: 2
  sleep 4
  play (chord chords.tick, :major7, invert: 1, num_octaves: 2), amp: a, sustain: 1
  sleep 2
  play (chord chords.tick, :m7, invert: 1, num_octaves: 2), amp: a, sustain: 1
  sleep 2
end

live_loop :bass, sync: :chords do
  i = 0
  
  64.times do
    if i == 16
      i = 0
    end
    use_synth :fm
    a = 0.4
    notes = (ring :a3, :e3, :a3, :d3, :e3, :f3, :e3, :d3, :f3, :c3, :f3, :e3, :c3, :d3, :c3, :e3)
    if pattern "x-----x---x---x-x-----x---x--x--"
      play notes[i], amp: a
      i = i+ 1
    end
    sleep 0.25
  end
  
end

