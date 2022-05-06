
use_bpm 100

live_loop :met do
  sleep 1
end

mel = true
bass = true
snare = true

mel_var = false


live_loop :snare, sync: :met do
  s1_amp = [0.3,1,0.3,1,  0.3,0.3,1,0.3,  1,0.3,0.3,1]
  s2_amp = [0.3,0.3,1,0.3]
  s6_amp = [1,0.3,0.4,0.3,0.4,1]
  
  if not snare
    s1_amp = [0]
    s2_amp = [0]
    s6_amp = [0]
  end
  12.times do
    sample :drum_snare_soft, amp: s1_amp.tick(:a)
    sleep 0.25
  end
  if [true].tick
    4.times do
      sample :drum_snare_soft, amp: s2_amp.tick(:b)
      sleep 0.25
    end
  else
    6.times do
      sample :drum_snare_soft, amp: s6_amp.tick(:c)
      sleep 1/6.0
    end
  end
end

live_loop :hh, sync: :met do
  sleep 0.5
  sample :drum_cymbal_pedal, amp: 0.2, pan: -0.6
  sleep 0.5
  # sleep 1
end

live_loop :bd, sync: :met do
  ##| sleep 1
  sample :drum_bass_soft, amp: [0.7,1].tick
  sleep 1
end

live_loop :bass, sync: :met do
  a = 0.4
  a_k = 1
  if not bass
    a =0
    a_k = 0
  end
  
  use_random_seed 807608
  use_synth :fm
  notes = (scale :e2, :harmonic_minor)
  8.times do
    use_synth :fm
    note = notes.choose
    play note, amp: a, release: [1, 0.7].tick
    
    use_synth :kalimba
    #play note + 12, pan: -0.8
    note_add = 12
    if mel_var
      note_add = 15
    end
    play note + note_add, amp: a_k, pan: 0.8
    sleep 1
  end
end

live_loop :melody, sync: :met do
  use_synth :beep
  
  a = 0.1
  if not mel
    a = 0
  end
  
  use_random_seed 605
  with_fx :reverb, room: 0.8, mix: 0.6 do
    with_fx :krush, cutoff: 120 do
      with_fx :normaliser, amp: a do
        8.times do
          sleep 0.25
        end
        8.times do
          play (scale :e3, :harmonic_minor).choose, release: 0.2 if (spread 23, 32).tick
          sleep 0.25
        end
        8.times do
          sleep 0.25
        end
        8.times do
          play (scale :e3, :harmonic_minor).choose, release: 0.2 if (spread 23, 32).tick
          sleep 0.25
        end
      end
    end
  end
end
