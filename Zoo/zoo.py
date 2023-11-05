def function():
    # A program for obtaining ASCII images and the possibility of continuous operation without rebooting.

    camel = r"""
    The camel habitat...
     ___.-''''-.
    /___ @     |
    ',,,,.     |         _.'''''''._
         '     |        /           \
         |     \    _.-'             \
         |      '.-'                  '-.
         |                               ',
         |                                '',
          ',,-,                           ':;
               ',,| ;,,                 ,' ;;
                  ! ; !'',,,',',,,,'!  ;   ;:
                 : ;  ! !       ! ! ;  ;   :;
                 ; ;   ! !      ! !  ; ;   ;,
                ; ;    ! !     ! !   ; ;
                ; ;    ! !    ! !     ; ;
               ;,,      !,!   !,!     ;,;
               /_I      L_I   L_I     /_I
    Look at that!"""

    rabbit = r"""
    The rabbit habitat...
             ,
            /|      __
           / |   ,-~ /
          Y :|  // /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \
    \//\/      .- \
     Y        /    Y
     l       I     !
     ]\      _\    /"\
    (" ~----( ~   Y.  )
    It looks fine!"""

    lion = r"""
    The lion habitat...
                                                   ,w.
                                                 ,YWMMw  ,M  ,
                            _.---.._   __..---._.'MMMMMw,wMWmW,
                       _.-""        '''           YP"WMMMMMMMMMb,
                    .-' __.'                   .'     MMMMW^WMMMM;
        _,        .'.-'"; `,.       /`     .--""     :MMM[==MWMW^;
     ,mM^"     ,-'.'   /    ;      ;      /  ,       MMMMb_wMW"  @\
    ,MM:.   .'.-'   .'       ;     `\    ;    `,     MMMMMMMW `"=./`-,
    WMMm__,-'.'     /       _.\      F'''-+,,  ;_,_.dMMMMMMMM[,_ / `=_}
    "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
               /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
              /  .'             /  (       .'  /     Ww._     `.  `"
             /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
            (--, )                `,_ /  `) \/"")     ^"      `-, -;"\:
    The lion is roaring!"""

    deer = r"""
    The deer habitat...
       /|       |\
    `__\\        //__'
        ||      ||
      \__`\     |'__/
        `_\\   //_'
       _.,:---;,._
       \_:     :_/
         |@. .@|
         |     |
         ,\.-./ \
         ;;`-'   `---__________-----.-.
         ;;;                         \_\
         ';;;                         |
          ;   |                       ;
           \   \     \        |      / 
            \_, \    /        \      |\
              |';|  |,,,,,,,,/ \     \ \_
              |  |  |           \    /   |
              \  \  |           |   /  \ |
               | || |           | |    | |
               | || |           | |    | |
               | || |           | |    | |
               |_||_|           |_|    |_|
               /_//_/           /_/    /_/
    Pretty good!"""

    goose = r"""
    The goose habitat...
                                       _               
                                   ,-"" "".            
                                 ,' ____   `.          
                               ,' ,'     `.  `._       
      (`.         _..--.._   ,' ,'          \    \     
     (`-.\    .-""        ""'  /            (  d _b    
    (`._  `-"" ,._            (              `-(   \   
    <_  `     (  <`<           \                `-._\  
     <`-       (__< <          :                        
      (__        (_<_<         ;                       
       `------------------------------------------        
    Beautiful!"""

    bat = r"""
    The bat habitat...
    _________________             _________________
     ~-.             \  |\___/|  /             .-~
         ~-.          \ / o o \ /          .-~
             >         \\  W  //          <
            /           /~---~\            \
           /_          |       |           _\
              ~-.      |       |       .-~
                ;       \     /        i
               /___     /\   /\     ___\
                   ~-. /  \_/  \ .-~
                      V         V
    It's doing fine."""

    animals = [camel, lion, deer, goose, bat, rabbit]

    # Create a loop to repeat the program
    while True:
        # Ask for the number of the animal
        number = input("Please enter the number of the habitat you would like to view: ")

        # Check if the user wants to log out
        if number == "exit":
            break

        # Check if a number is an integer
        try:
            number = int(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Check if the number is between 0 and the number of elements in the list
        if number < 0 or number >= len(animals):
            print("Invalid input. Please enter a number between 0 and " + str(len(animals) - 1) + ".")
            continue

        # Print the animal
        print(animals[number])


function()

# End the program
print("See you later!")