require "/home/diego/Projects/sonic-pi/petal/petal.rb"

cps 0.9

d1 "bd ~ ~ ~", amp: 0.4
d2 "future(5,16)" , slow: 4, n: "irand 4", amp: 0.4 # rate: 'rand 1 2'
d3 "future(13,16)", slow: 4, n: "irand 3", amp: 0.15, pan: -1 # rate: 'rand 1 2'
d4 "sn(4,16,2)", slow: 4, n: 1, amp: 0.3

d5 "hh hh hh hh", amp: "0.1 0.08", pan: -0.6

d9 "kurt(5,16,2)" , slow: 2, n: "irand 6", rate: 'rand -0.8, -0.6', amp: 0.03, pan: 'rand -1, 1'

#d1 :silence
#d2 :silence

#d3 :silence
d4 :silence
d5 :silence
d9 :silence



##| d2 :silence
##| d3 :silence
##| d4 :silence
##| d5 :silence

# d5 "dork2(5,16,2)", n: "irand 4", rate: 4

# d7 "house(3,16,2)" , slow: 2, n: 1, rate: 'rand 1 0.8, 1.2, 0.6'

# d6 "jungbass(1,16,2)" , slow: 2, n: "irand 6" # , rate: 'rand 1 0.8, 1.2, 0.6'

#d9 "koy(1,16,2)" , slow: 4, rate: "1"


# d9 "less(5,16,2)" , slow: 1, n: "irand 0, 1, 1, 2, 1," # , rate: 'rand 1 0.8, 1.2, 0.6'

play_riff = false
play_melody = false
play_melody2 = true
cymbals = false

live_loop :cymbals, sync: :chord do
  if not cymbals then stop end
  use_bpm get_bpm
  sample :drum_splash_soft, amp: 0.4, pan: 0.3
  sleep 8
end

fim = false
live_loop :chord, sync: :d0 do
  use_bpm get_bpm
  use_synth :pluck
  with_fx :reverb, room: 1, mix: 0.4 do
    with_fx :tremolo do
      with_fx :distortion do
        if not fim then
          play (chord :c2, '5'), amp: 0.6
          sleep 4
          play (chord :c2, :minor), amp: 0.6
          sleep 4
        else
          play (chord :c2, '5'), amp: 0.6
          sleep 8
        end
      end
    end
  end
end

live_loop :melody2, sync: :chord do
  if not play_melody2 then stop end
  use_bpm get_bpm
  use_synth :pluck
  use_random_seed 3982989
  with_fx :tremolo do
    with_fx :distortion do
      sleep 2
      play (chord (scale :c2, :minor).choose, '5'), release: 3, amp: 0.1
      sleep 4
      play (chord (scale :c2, :minor).choose, '5'), release: 3, amp: 0.1
      sleep 4
      sleep 2
      4.times do
        #play (scale :c2, :minor).choose, amp: 0.1
        sleep 0.25
      end
    end
  end
end

mel_amp = 0.06
mel_pan = -0.9
live_loop :melody, sync: :chord do
  if not play_melody then stop end
  use_bpm get_bpm
  use_synth :pluck
  #with_fx :reverb, room: 1, mix: 0.4 do
  use_random_seed 3982989
  with_fx :tremolo do
    with_fx :distortion do
      sleep 2.5
      4.times do
        play (scale :c2, :minor).choose, amp: mel_amp, pan: mel_pan if (spread 2, 3, rotate: 1).tick
        sleep 0.125
      end
      #play (scale :c2, :minor).choose, amp: 0.1
      sleep 0.25
      4.times do
        play (scale :c2, :minor).choose, amp: mel_amp, pan: mel_pan if (spread 2, 3, rotate: 2).tick
        sleep 0.125
      end
      play (scale :c2, :minor)[6], amp: mel_amp, pan: mel_pan
      sleep 0.25
      
      sleep 2.5
      4.times do
        play (scale :c2, :minor).choose, amp: mel_amp, pan: mel_pan if (spread 2, 3, rotate: 2).tick
        sleep 0.125
      end
      #play (scale :c2, :minor).choose, amp: 0.1
      sleep 0.25
      4.times do
        play (scale :c2, :minor_pentatonic).choose, amp: mel_amp, pan: mel_pan if (spread 2, 3, rotate: 1).tick
        sleep 0.125
      end
      play (scale :c2, :minor)[6], amp: mel_amp, pan: mel_pan
      sleep 0.25
    end
  end
  #end
end

play_alter = true
live_loop :riff, sync: :chord do
  if not play_riff then stop end
  use_bpm get_bpm
  use_random_seed 412341
  if play_alter then
    32.times do
      #play :c3, amp: 0.6, release: 0.5 if (spread 7, 16, rotate: 14).tick
      play (scale :c3, :minor_pentatonic).choose, amp: 0.05, pan: 0.8 if (spread 5,16, rotate: 3).tick
      sleep 0.125
    end
  else
    play :c3, amp: 0.2, pan: 0.8, sustain: 2, release: 2
    sleep 4
  end
  
end

b_rel = 0.3
b_amp = 0.25
cscale = (scale :c3, :minor)
live_loop :baixo, sync: :chord do
  stop
  use_bpm get_bpm
  use_synth :fm
  play cscale[0], release: b_rel, amp: b_amp
  sleep 0.125
  play cscale[0], release: b_rel, amp: b_amp
  sleep 0.125
  sleep 0.25
  sleep 0.25
  play cscale[2], release: b_rel, amp: b_amp
  sleep 0.25
  sleep 1
  play cscale[4], release: b_rel, amp: b_amp
  sleep 0.125
  play cscale[4], release: b_rel, amp: b_amp
  sleep 0.125
  sleep 0.5
  play cscale[3], release: b_rel, amp: b_amp
  sleep 0.25
  sleep 1
end
