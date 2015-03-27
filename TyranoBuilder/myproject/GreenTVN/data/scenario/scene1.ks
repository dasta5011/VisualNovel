[_tb_system_call storage=system/_scene1.ks]

[cm  ]
*start

[bg  time="1000"  method="puff"  storage="cave.jpg"  ]
[chara_show  name="Derek"  time="1000"  left="125"  top="120"  ]
[tb_show_message_window  ]
Welcome to my new Dotes lair.  [p]
If you keep hush about it, I'll let you in, got it?[p]


[glink  color="black"  storage="scene1.ks"  size="40"  target="*choice1_yes"  text="Yes,&nbsp;oh&nbsp;lord&nbsp;and&nbsp;master"  y="30"  ]
[glink  color="black"  storage="scene1.ks"  size="40"  target="*choice1_no"  text="I&nbsp;whipe&nbsp;out&nbsp;my&nbsp;phone&nbsp;and&nbsp;tweet&nbsp;that&nbsp;shit"  y="100"  ]
[s  ]
*choice1_yes

Alright, I trust you...for now.[p]


[jump  storage="scene1.ks"  target="*choice1_end"  ]
*choice1_no

[font  size="20"  color="0xff0000"  bold="true"  ]
What the shit?  I say keep quiet and you bust out your iPhone and start tweeting that shit?  What the fuck?!  #secretbases?  The fuck dude...?![p]


[resetfont  ]
[jump  storage="scene1.ks"  target="*choice1_end"  ]
*choice1_end

test[p]


[s  ]
