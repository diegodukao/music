rimshot = "/home/diego/.virtualenvs/foxdot/lib/python3.10/site-packages/FoxDot/snd/t/lower/alt_rimshot_3.wav"

use_bpm 130

live_loop :met1 do
  sleep 1
end

define :pattern do |pattern|
  return pattern.ring.tick == "x"
end

kick = true
hh = true
keys = true
guit = false
bass = false
riff = false

guit = true
bass = true
riff = false

live_loop :kick, sync: :met1 do
  a = 0.4
  if not kick
    a= 0
  end
  sample :drum_bass_soft, amp: a if pattern "x-"
  sleep 0.5
end

live_loop :hh, sync: :met1 do
  sample :drum_cymbal_closed, amp: [0.2,0.1].tick, pan: -0.6
  sleep 0.5
end

live_loop :sn, sync: :met1 do
  a = 0.5
  with_fx :reverb, room: 0.8 do
    with_fx :distortion do
      32.times do
        sample rimshot, amp: a if pattern "--------x-----x---------x-----x-"
        sleep 0.25
      end
      32.times do
        sample rimshot, amp: a if pattern "--------x-----x---x-x---x--x--x-"
        sleep 0.25
      end
    end
  end
end

live_loop :riff, sync: :met1 do
  use_synth :saw
  a = 0.07
  if not riff
    a = 0
  end
  r = 0.5
  
  with_fx :reverb, room: 0.9, mix: 0.5 do
    with_fx :distortion do
      sleep 3
      play :a3, amp: a, release: r
      sleep 0.5
      play :b3, amp: a, release: r
      sleep 0.5
      play :c4, amp: a, release: r
      sleep 3
      play :c4, amp: a, release: r
      sleep 0.5
      play :b3, amp: a, release: r
      sleep 0.5
      play :a3, amp: a, release: r
      
      sleep 3
      play :a3, amp: a, release: r
      sleep 0.5
      play :b3, amp: a, release: r
      sleep 0.5
      play :c4, amp: a, release: r
      sleep 1
      play :c4, amp: a, release: r
      sleep 1
      play :c4, amp: a, release: r
      sleep 0.5
      play :b3, amp: a, release: r
      sleep 0.5
      play :a3, amp: a, release: r
      sleep 1
    end
  end
end

live_loop :guit, sync: :met1 do
  use_synth :pluck
  a = 0.3
  p = 1
  if not guit
    a = 0
  end
  
  2.times do
    sleep 1
    play (chord :a3, :minor), amp: a, pan: p
    sleep 1
  end
  2.times do
    sleep 1
    play (chord :g3, :major), amp: a, pan: p
    sleep 1
  end
end

live_loop :keys, sync: :met1 do
  use_synth :blade
  a = 0.4
  r = 0.4
  p = -1
  if not keys
    a = 0
  end
  2.times do
    sleep 0.5
    play (chord :a2, :minor), amp: a, release: r, pan: p
    sleep 0.5
    play (chord :a3, :minor), amp: a, release: r, pan: p
    sleep 0.5
    play (chord :a2, :minor), amp: a, release: r, pan: p
    sleep 0.5
  end
  2.times do
    sleep 0.5
    play (chord :g2, :major), amp: a, release: r, pan: p
    sleep 0.5
    play (chord :g3, :major), amp: a, release: r, pan: p
    sleep 0.5
    play (chord :g2, :major), amp: a, release: r, pan: p
    sleep 0.5
  end
end

live_loop :bass, sync: :met1 do
  use_synth :fm
  a = 0.2
  if not bass
    a = 0
  end
  play (chord :a2, :minor)[0], amp: a
  sleep 1
  play (chord :a2, :minor)[0], amp: a
  sleep 1
  play (chord :a2, :minor)[2], amp: a, release: 1.5
  sleep 2
  
  play (chord :g2, :major)[0], amp: a
  sleep 1
  play (chord :g2, :major)[0], amp: a
  sleep 1
  play (chord :g2, :major)[2], amp: a, release: 1.5
  sleep 2
  
  
  play (chord :a2, :minor)[0], amp: a
  sleep 1
  play (chord :a2, :minor)[0], amp: a
  sleep 1
  play (chord :a2, :minor)[2], amp: a
  sleep 1
  play (chord :a2, :minor)[0], amp: a
  sleep 1
  
  play (chord :g2, :major)[0], amp: a
  sleep 1
  play (chord :g2, :major)[0], amp: a
  sleep 1
  play (chord :g2, :major)[2], amp: a, release: 1.5
  sleep 2
end