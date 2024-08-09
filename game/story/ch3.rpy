label ch3:
    scene sweets5 with Dissolve(1.0)
    play music "soundtracks/flaing-piano-loop-8782.mp3"
    "Fiera seems to be enjoying the ice cream, 
    and you feel your shoulders lighten a little."
    show fiera happy_1 with dissolve
    f "Thank you for the ice cream, Claude."
    show fiera smiling_1 at bounce_inf
    f "I love coming here!"
    c "That is exactly why we are here."
    c "(...And because, no matter what...)"
    c "(you always forgive me after you have some ice cream.)"

    scene black with Dissolve(1.0)
    $ persistent.ice_cream_ending = True
    "{b}Ice Cream Ending{/b}"
    stop music fadeout 2.0
    pause 2.0
    return