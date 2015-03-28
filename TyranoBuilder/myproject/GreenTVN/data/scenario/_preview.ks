[_tb_system_call storage=system/_preview.ks ]

[bg  time="10"  method="puff"  storage="cave.jpg"  ]
[playbgm  loop="true"  storage="iron_man_01.mp3"  ]
[tb_show_message_window] 
[chara_show  name="Derek"  time="10"  left="141"  top="120"  ]
[chara_hide  name="Derek"  time="100"  ]
[chara_mod  name="Derek"  time="600"  storage="chara/1/lucy_mad.png"  ]
[chara_show  name="Derek"  time="100"  left="516"  top="730"  ]
[tb_start_tyrano_code]
[anim name="Derek" top="100" time="500"]
[wait time=100]
[wa]
[_tb_end_tyrano_code]

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
