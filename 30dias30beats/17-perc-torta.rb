require "~/Projects/livecoding/petal/petal.rb"


with_fx :pitch_shift, pitch: 0, window_size: [0.001, 0.005, 0.01].choose do
  with_fx :distortion do
    d1 "peri(9,16)", slow: 2, rate: 1, amp: 0.3, n: "2", pan: "0.5"
    d2 "ifdrums(5,16)", slow: 1, rate: 1, amp: 0.5, n: "1", pan: "-0.5"
    
    d3 "peri(3,8)", amp: 0.4, amp: 0.2, n: 1
    
    d4 "jazz(7,16,14)", amp: 0.05, n: 1
    
    d6 "[peri peri peri ~] [perc perc perc ~] [sn ~ ~ ~] ~ [perc perc] [~ perc] [sn peri] peri", slow: 2, amp: 0.2, n: 2
    
    d5 "tech(3,4)", slow: 2, amp: 1, n: "irand 1", rate: "0.2 0.3 0.4 0.3"
    
    d5 :silence
    
  end
end
