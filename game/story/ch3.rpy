label ch3:
    scene sweets5 with pixellate
    "Fiera seems to be enjoying the ice cream, 
    and you feel your shoulders lighten a little."
    show fiera happy_1 with dissolve
    f "Thank you for ice cream, Claude.
    \nI love coming here!"
    c "That is exactly why we are here."
    c "(...And because, no matter what...)"
    c "(you always forgive me after you have some ice cream.)"

    scene black with Dissolve(1.0)
    $ persistent.ice_cream_ending = True
    "{b}Ice Cream Ending{/b}"
    return