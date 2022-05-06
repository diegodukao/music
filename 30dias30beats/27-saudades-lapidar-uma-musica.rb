use_bpm 60

live_loop :met1 do
  sleep 1
end

define :pattern do |pattern|
  return pattern.ring.tick == "x"
end

kick = true
snare = true
melody = false
melody2 = true
mel2_var = false

live_loop :kick, sync: :met1 do
  a = 1
  if not kick
    a= 0
  end
  sample :bd_fat, amp: a if pattern "x--x-x-x--x-x-x-x-----x----x--x-"
  sleep 0.25
end

live_loop :hh, sync: :met1 do
  a = 0.15
  sample :drum_cymbal_closed, amp: a, pan: -0.6 if pattern "xxxx--x-x-x-x-x-x--x--x-xx-xx-x-"
  sleep 0.125
end

live_loop :snare, sync: :met1 do
  a = 0.8
  if not snare
    a = 0
  end
  sample :drum_snare_soft, amp: a if pattern "--x-"
  sleep 0.5
end

bass = true
live_loop :bass, sync: :met1 do
  use_synth :fm
  a = 0.2
  if not bass
    a =0
  end
  p = 0
  use_random_seed 2362
  16.times do
    play (scale :b2, :harmonic_minor).choose, amp: a, pan: p if spread(7, 16).tick(:a)
    sleep 0.25
  end
  play :b2, amp: a, pan: p
  sleep 0.25
  7.times do
    #play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(3, 16).tick
    sleep 0.25
  end
  16.times do
    #play (scale :b2, :harmonic_minor).choose, amp: a, pan: p if spread(3, 8, rotate: 1).tick(:b)
    sleep 0.125
  end
end

live_loop :melody, sync: :met1 do
  use_synth :hoover
  a = 0.1
  if not melody
    a =0
  end
  p = 0.5
  use_random_seed 2362
  with_fx :flanger do
    16.times do
      play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(7, 16).tick
      sleep 0.25
    end
    8.times do
      #play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(3, 16).tick
      sleep 0.25
    end
    with_fx :echo, phase: 0.25, max_phase: 4, decay: 4, pan: p do
      8.times do
        #play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(4, 16).tick
        sleep 0.25
      end
    end
  end
end

live_loop :melody2, sync: :met1 do
  use_synth :pretty_bell
  a = 0.1
  if not melody2
    a =0
  end
  p = -0.5
  sleep 4
  
  if mel2_var
    use_random_seed 369
    16.times do
      play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(21, 32).tick
      sleep 0.125
    end
    sleep 0.25
    14.times do
      play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(15, 16).tick
      sleep 0.25
    end
    sleep 0.25
    14.times do
      play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(18, 32).tick
      sleep 0.125
    end
    sleep 0.25
    16.times do
      #play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(13, 16).tick
      sleep 0.25
    end
  else
    use_random_seed 7606078
    16.times do
      play (scale :b3, :harmonic_minor).choose, amp: a, pan: p if spread(13, 16).tick
      sleep 0.25
    end
    sleep 8
  end
end
