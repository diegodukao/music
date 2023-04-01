use_bpm 90

live_loop :met1 do
  sleep 1
end

bass = false
mel = false
mel_var = false

live_loop :loop, sync: :met1 do
  use_random_seed 700
  a=0.7
  8.times do
    sample :loop_amen, num_slices: 16, amp: a, slice: pick, rate: 0.5 if (spread 7,8).tick
    sleep 0.25
  end
  use_random_seed 660
  8.times do
    sample :loop_amen, num_slices: 16, amp: a, slice: pick, rate: 0.5 if (spread 5,8).tick
    sleep 0.25
  end
end

live_loop :db, sync: :met1 do
  a = 0.5
  sample :drum_bass_hard, amp: a if (spread 5,8, rotate: 1).tick
  sleep 0.5
end

live_loop :bass, sync: :met1 do
  use_synth :fm
  use_random_seed 65
  a = 0.3
  if not bass
    a = 0
  end
  with_fx :echo do
    play (scale :bb2, :minor).choose, amp: a if (spread 9, 16).tick
    sleep 0.5
  end
  7.times do
    play (scale :bb2, :minor).choose, amp: a if (spread 9, 16).tick
    sleep 0.5
  end
  use_random_seed 62664
  8.times do
    play (scale :bb2, :minor).choose, amp: a if (spread 7, 16).tick
    sleep 0.5
  end
end

live_loop :melody, sync: :met1 do
  use_random_seed 2222
  use_synth :dtri
  a= 0.15
  if not mel
    a = 0
  end
  p=-0.6
  r=0.5
  note = :bb2
  if mel_var
    note = :bb3
  end
  with_fx :bitcrusher, cutoff: 120 do
    7.times do
      play (scale note, :minor).choose, amp: a, pan: p, release: r if (spread 18,32).tick
      sleep 0.25
    end
    2.times do
      sleep 0.25
    end
    7.times do
      play (scale note, :minor).choose, amp: a, pan: p, release: r if (spread 18,32).tick
      sleep 0.25
    end
    2.times do
      sleep 0.25
    end
    14.times do
      play (scale note, :minor).choose, amp: a, pan: p, release: r if (spread 18,32).tick
      sleep 0.25
    end
  end
end


