use_bpm 130

live_loop :met1 do
  sleep 1
end

define :pattern do |pattern|
  return pattern.ring.tick == "x"
end

kick = false
snare = false
melody = true
melody2 = false
mel2_var = true

live_loop :kick, sync: :met1 do
  a = 1
  if not kick
    a= 0
  end
  sample :bd_fat, amp: a if pattern "x-----x---x---x-x-----x----x--x-"
  sleep 0.25
end

live_loop :hh, sync: :met1 do
  a = 0.2
  sample :drum_cymbal_closed, amp: a, pan: -0.6 if pattern "xxxx--x-x-x---x-x--x--x-xx-x--x-"
  sleep 0.25
end

live_loop :snare, sync: :met1 do
  a = 0.8
  if not snare
    a = 0
  end
  sample :drum_snare_soft, amp: a if pattern "--x-"
  sleep 0.5
end

live_loop :chords, sync: :met1 do
  use_synth :blade
  with_fx :echo, phase: 0.5, max_phase: 4, decay: 4 do
    play (chord_degree :i, :a3, :harmonic_minor, 4, invert: 0)
    sleep 4
    play (chord_degree :iv, :a2, :harmonic_minor, 5, invert: 1)
    sleep 2
    play (chord_degree :v, :a2, :harmonic_minor, 4, invert: 2)
    sleep 2
  end
end

live_loop :bass, sync: :met1 do
  use_synth :fm
  a = 0.2
  3.times do
    play :a2, amp: a
    sleep 0.5
  end
  sleep 0.5
  sleep 2
  3.times do
    play :f2, amp: a
    sleep 0.5
  end
  sleep 0.5
  3.times do
    play :b2, amp: a
    sleep 0.5
  end
  sleep 0.5
end

live_loop :melody2, sync: :met1 do
  use_synth :pulse
  a = 0.15
  p = -0.5
  if not melody2
    a = 0
  end
  3.times do
    play :a2, amp: a, pan: p
    sleep 0.5
  end
  sleep 0.5
  sleep 2
  3.times do
    play :f2, amp: a, pan: p
    sleep 0.5
  end
  sleep 0.5
  3.times do
    play :b2, amp: a, pan: p
    sleep 0.5
  end
  sleep 0.5
  
  note = :a2
  if mel2_var
    note = :c3
  end
  3.times do
    play note, amp: a, pan: p
    sleep 0.5
  end
  sleep 0.5
  sleep 2
  3.times do
    play :f2, amp: a, pan: p
    sleep 0.5
  end
  sleep 0.5
  3.times do
    play :b2, amp: a, pan: p
    sleep 0.5
  end
  sleep 0.5
end

live_loop :melody, sync: :met1 do
  use_synth :pluck
  a = 0.3
  if not melody
    a =0
  end
  p = 0.5
  use_random_seed 789
  with_fx :flanger do
    16.times do
      play (scale :a3, :harmonic_minor).choose, amp: a, pan: p if spread(4, 16).tick
      sleep 0.25
    end
    8.times do
      play (scale :a3, :harmonic_minor).choose, amp: a, pan: p if spread(5, 16).tick
      sleep 0.25
    end
    with_fx :echo, phase: 0.25, max_phase: 4, decay: 4, pan: p do
      8.times do
        play (scale :a3, :harmonic_minor).choose, amp: a, pan: p if spread(3, 16).tick
        sleep 0.25
      end
    end
  end
end
