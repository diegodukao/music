use_sample_bpm :loop_amen_full, num_beats: 16

live_loop :met1 do
  sleep 1
end

live_loop :loop, sync: :met1 do
  sample :loop_amen_full, num_slices: 16, slice: (ring 10, 3, 2,4, 1,6,2,3).tick, rate: 0.8
  sleep 1
end

live_loop :loop3, sync: :loop do
  use_synth :fm
  use_random_seed 20
  a = 1
  8.times do
    play (chord :e2, :m9).choose, amp: a if spread(5,8).tick
    sleep 0.5
  end
  8.times do
    play (chord :e2, :m9).choose, amp: a if spread(5,8).tick
    sleep 1
  end
  8.times do
    play (chord :e2, :m9).choose, amp: a if spread(5,8).tick
    sleep 0.5
  end
end

live_loop :loop4, sync: :loop do
  use_synth :rodeo
  use_random_seed 20
  a = 1
  8.times do
    play (chord :e2, :m9).choose, amp: 0 if spread(5,8).tick
    sleep 0.5
  end
  2.times do
    play (chord :e3, :m9), amp: a if spread(5,8).tick
    sleep 1
    play (chord :e3, :m9), amp: a if spread(5,8).tick
    sleep 1
    play (chord :g3, :m9), amp: a if spread(5,8).tick
    sleep 1
    play (chord :b2, :m9), amp: a if spread(5,8).tick
    sleep 1
  end
  8.times do
    play (chord :e2, :m9).choose, amp: 0 if spread(5,8).tick
    sleep 0.5
  end
end



