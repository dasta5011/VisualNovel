[_tb_system_call storage=system/_preview.ks ]

[tb_show_message_window] 
[bg  time="1000"  method="puff"  storage="cave.jpg"  ]
[chara_show  name="Derek"  time="1000"  left="141"  top="120"  ]
[tb_show_message_window  ]
#Derek
Welcome to my new Dotes lair.  [p]
If you keep hush about it, I'll let you in, got it?[p]


[glink  color="black"  storage="scene1.ks"  size="20"  target="*choice1_yes"  text="Yes,&nbsp;oh&nbsp;lord&nbsp;and&nbsp;master"  y="275"  x="360"  width="350"  ]
[glink  color="black"  storage="scene1.ks"  size="20"  target="*choice1_no"  text="I&nbsp;whip&nbsp;out&nbsp;my&nbsp;phone&nbsp;and&nbsp;tweet&nbsp;that&nbsp;shit"  y="360"  x="360"  width="350"  ]
[s  ]
*choice1_yes

Alright, I trust you...for now.[p]


[jump  storage="scene1.ks"  target="*choice1_end"  ]
*choice1_no

[chara_hide  name="Derek"  time="100"  ]
[chara_mod  name="Derek"  time="600"  storage="chara/1/lucy_mad.png"  ]
[chara_show  name="Derek"  time="100"  left="678"  top="120"  ]
[font  size="20"  color="0xff0000"  bold="true"  ]
What the shit?  I say keep quiet and you bust out your iPhone and start tweeting that shit?  What the fuck?!  #secretbases?  The fuck dude...?![p]


[resetfont  ]
[jump  storage="scene1.ks"  target="*choice1_end"  ]
*choice1_end

test[p]


[tb_start_tyrano_code]
[close]
[_tb_end_tyrano_code]

[s  ]
