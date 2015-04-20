# The game starts here.
label start:
    #variables for game tracking   
    
    $ikida = 0    #family reputation
    $jagura = 0
    $kenshido = 0
    $maclynn = 0
    $akosnov = 0
    
    $gameover = False
    
    #keep this beginning section clean ## used as a master jump sequences to control flow of the game
    window show #keeps text window from hiding during transitions
    
    call prologue
    call opening
    call day1_meetup
    call day1_cafe
    call day1_gunshop
    #returns to main menu if gameover condition variable is set
    if gameover:
        return
    call day1_home
    call day1_nightdream
    call day1_mayuhome
    call day2_open
    call test
    return