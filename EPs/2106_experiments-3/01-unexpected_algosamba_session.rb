require "/home/diego/Projects/sonic-pi/petal/petal.rb"

cps 0.5

d1 "hh(6,16)", slow: 1, amp: "0.3 0.4", pan: -0.5
d2 "bd [~ bd] bd [~ bd] bd [~ bd] [~ bd] [~ bd]", amp: 0.3
#d2 "bd [~ bd] bd [~ bd] bd [~ bd] bd [~ bd]", amp: 0.2
d3 "tabla(7,16,2)", slow: 1, n: "4", amp: 0.3, pan: 0.5

#d1 :silence
d2 :silence
#d3 :silence

melody = false
bass = false
chords = true
solo = false

# E, Em
# C, C#m
# Ddim, Baug (nao)
# A, Am, A#dim

single_amp = 0
isStart = true
if isStart then
  curr_chord = (chord :e3, :minor7)
end
live_loop :chords, sync: :d0 do
  if not chords then stop end
  use_bpm get_bpm
  use_synth :piano
  
  play 55 - 12, amp: single_amp
  curr_chord = (chord :e3, :minor7)
  play curr_chord
  sleep 1
  
  play 56 - 12, amp: single_amp
  curr_chord = (chord :cs3, :minor7, invert: 1)
  play curr_chord
  sleep 0.5
  
  play 55 - 12, amp: single_amp
  curr_chord = (chord :c3, '7', invert: 1)
  play curr_chord
  sleep 0.5
  
  play 53 - 12, amp: single_amp
  curr_chord = (chord :f2, 'major7', invert: 3)
  play curr_chord
  sleep 1
  
  #curr_chord = (chord :as1, 'm7b5', invert: 2)
  play 58 - 12, amp: single_amp
  curr_chord = (chord :as2, :diminished7, invert: 2)
  play curr_chord
  sleep 0.5
  
  play 57 - 12, amp: single_amp
  curr_chord = (chord :a2, :minor7, invert: 2)
  play curr_chord
  sleep 0.5
end

solo_amp = 0.06
solo_pan = 0.3
live_loop :solo, sync: :chords do
  if not solo then stop end
  use_bpm get_bpm
  use_synth :prophet
  #use_random_seed 3256
  use_random_seed 626961
  
  16.times do
    play (scale :c3, :minor_pentatonic).choose, amp: solo_amp, release: 0.1, pan: solo_pan if (spread 5, 8, rotate: 3).tick
    sleep 0.0625
  end
  use_random_seed 4636
  16.times do
    play (scale :c3, :minor_pentatonic).choose, amp: solo_amp, release: 0.1, pan: solo_pan if (spread 5, 9, rotate: 3).tick
    sleep 0.0625
  end
  use_random_seed 2365236
  16.times do
    play (scale :c3, :minor_pentatonic).choose, amp: solo_amp, release: 0.1, pan: solo_pan if (spread 7, 16, rotate: 3).tick
    sleep 0.0625
  end
  use_random_seed 4636
  16.times do
    play (scale :c3, :minor_pentatonic).choose, amp: solo_amp, release: 0.1, pan: solo_pan if (spread 5, 9, rotate: 3).tick
    sleep 0.0625
  end
  
end

amp_b = 0.2
live_loop :bass, sync: :chords do
  if not bass then stop end
  use_bpm get_bpm
  use_synth :fm
  3.times do
    2.times do
      play :e2, amp: amp_b, release: 0.1
      sleep 0.25/2
      sleep 0.125/2
      play :e2, amp: amp_b, release: 0.1
      sleep 0.125/2
    end
    sleep 0.125/2
    play :f3, amp: amp_b, release: 0.1
    sleep 0.25/2
    play :f3, amp: amp_b, release: 0.1
    sleep 0.125/2
    
    play :a2, amp: amp_b, release: 0.1
    sleep 0.25/2
    sleep 0.125/2
    play :a2, amp: amp_b, release: 0.1
    sleep 0.125/2
  end
  4.times do
    sleep 0.125/2
    play :f3, amp: amp_b, release: 0.1
    sleep 0.25/2
    play :f3, amp: amp_b, release: 0.1
    sleep 0.125/2
  end
  ##| use_random_seed 626961
  ##| 16.times do
  ##|   play (chord :e2, :minor7, num_octaves: 2).choose, amp: amp_b, release: 0.1 if (spread 9, 16, rotate: 2).tick
  ##|   sleep 0.0625
  ##| end
end

arp_amp = 0.12
mel_pan = -0.7
live_loop :arpeggio, sync: :chords do
  if not melody then stop end
  use_bpm get_bpm
  use_synth :blade
  with_fx :reverb, mix: 0.6, room: 0.9 do
    #with_fx :ping_pong do
    play 55, amp: arp_amp, pan: mel_pan
    sleep 1
    
    play 56, amp: arp_amp, pan: mel_pan
    sleep 0.5
    
    play 55, amp: arp_amp, pan: mel_pan
    sleep 0.5
    
    play 53, amp: arp_amp, pan: mel_pan
    sleep 1
    
    play 58, amp: arp_amp, pan: mel_pan
    sleep 0.5
    
    play 57, amp: arp_amp, pan: mel_pan
    sleep 0.5
    #end
  end
end




