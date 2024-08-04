python:
    ch1_choice = ""

label ch1:
    scene stairs2 with dissolve

    "You sit on the stairs, waiting patiently."
    "You scan the area looking for someone."
    c "(I am curious to see what reason she has for being late this time.)"
    "Suddenly, footsteps can be heard. It sounds like someone is quickly approaching."
    f "Claude!"
    c "Hmm!"
    c "(sigh)"
    c "Ahh, there you are..."
    show fiera happy_1 with dissolve
    c "Miss Fiera."
    f "Sorry for being late!"
    f "I was busy getting you a gift!"
    "She extends a set of freshly picked roses to you."
    c "Well, that is most appreciated. Thank you, very much, Miss-"
    "As you reach for the roses, you notice the numerous cuts on Fiera's hands."
    c "Miss Fiera! What happened here?"
    c "Why are your hands covered with cuts?"
    show fiera smiling_1
    f "Whoops! Hehe..."
    f "Well, I had to go through a lot of bushes and thorns to find your gift."
    f "But it's okay, because I got them for you!"
    menu:
        "Scold Fiera":
            jump scold
        "Praise Fiera":
            jump praise
        "Focus on bandaging cuts":
            jump focus

label scold:
    python:
        ch1_choice = "scold"
    c "Miss Fiera!!!"
    f shocked_1 "Ah!"
    c "You should not act so recklessly!"
    c "What would your father say if I were to hand you back in that condition?!"
    f sad_1 "..."
    f "I'm sorry..."
    f "I'll be more careful next time."
    f worried_1 "{i}Please, don't be mad at me...{/i}"
    c "Let us hurry and get you bandaged up."
    f "(sniffle) Okay..."
    "You grab her hand and hurry to the infirmary."
    jump ch2

label praise:
    python:
        ch1_choice = "praise"
    c "Miss Fiera, that is quite selfless of you."
    c "And this gift means so much more because of the effort you put in for it."
    f "Thank you, Claude!"
    c "Now, let us get you bandaged up, okay?"
    f "Okay!"
    "She grabs your hand and you head to the infirmary together."
    jump ch2

label focus:
    python:
        ch1_choice = "focus"
    c "Miss Fiera, though I appreciate the gesture, we must get you bandaged at once."
    c "Come with me."
    "You grab her hand and start walking to the infirmary room."
    f "But, Claude!"
    f "Don't you like my gift?"
    c "Of course. But right now, we must focus on your injuries."
    f "Okay..."
    "She takes your hand and you go off to the infirmary together."
    jump ch2
