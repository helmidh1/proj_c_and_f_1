label ch2:
    scene classroom9 with dissolve
    "You arrive at the school's infirmary room."
    "You tell Fiera to put the roses to the side and wash her wounds."
    "When she is done, you pick her up and sit her on the stool."

    if ch1_choice == "scold":
        jump scolded
    elif ch1_choice == "praise":
        jump praised
    elif ch1_choice == "focus":
        jump focused

label scolded:
    show fiera sad_1 with dissolve
    f "Claude?
    \nAre you mad at me?"
    menu:
        "Yes":
            jump scolded_yes
        "No":
            jump scolded_no

    label scolded_yes:
        c "I sure am!"
        c "And I hope this serves as a lesson to never do this again."
        f crying_1 "Wahh!!!"
        c "Oh, stop your whining."
        c "If you want to cry, I'll give you something to cry about."
        "You apply the disinfectant."
        f "WWWAAAAHHHHHH!!!!!"
        c "I bet you will think twice before acting so recklessly now."
        f "It stings!"
        c "Hush, child!"
        "You apply the ointment and bandage.
        \nFiera continues crying."
        c "There, all better."
        "She is still crying."
        c "(Maybe I am being a tad harsh.)"
        c "(But this is the same way I was taught whenever I made mistakes.)"
        menu:
            c "(Should I comfort her or let her be?)"
            "Comfort":
                jump comfort
            "Let her be":
                jump let_her_be

        label comfort:
            c "Oh, I am sorry, Miss Fiera."
            c "I know I am being quite rough, 
            but that is only because it pains me to see you injure yourself."
            c "How about we stop by the ice cream parlor on the way home?"
            f "(sniffle) ... Okay..."
            c "And, Miss Fiera..."
            f "Yeah?"
            c "I really do appreciate your gift, ever so much."
            jump ch3

        label let_her_be:
            c "(No. I was left to cry when I was her age, and that taught me well.)"
            c "(She may be upset with me now...)"
            c "(... but she will no doubt remember this lesson.)"
            "Fiera continues whailing."
            c "(...)"
            c "(... Even if it hurts to see her like this.)"
            scene black with dissolve
            $ persistent.meanie_ending = True
            "{b}Meanie Ending{/b}"
            return

    label scolded_no:
        c "No, Miss Fiera. I am not mad at you."
        c "I am just concerned, is all."
        c "Your cuts could very well get infected, and then you may get sick."
        c "And none of us want that again."
        c "Do you?"
        "Fiera shakes her head."
        c "That is what I thought."
        c "Now, hold still. I am going to apply the disinfectant. This may sting a little."
        f crying_1 "(screams) Ahh!!!"
        c "I know it hurts, but this is so you do not get an infection."
        c "Please, bear it for me."
        f sad_1 "(wincing) Okay."
        "You apply the ointment and bandage."
        c "There. How does that feel?"
        f "(sniffle) Better..."
        c "(She behaved herself well. I am proud of her.)"
        c "Oh, and thank you for the flowers, Miss Fiera.
        \nThey are beautiful. I will make sure to find a proper vase for them at home."
        c "Really?"
        f "Yes."
        c "Hooray!!!"
        c "(I am glad to see her feeling better.)"
        menu:
            c "Should we go out for a treat or head straight home?"
            "Go for ice cream":
                jump ice_cream
            "Head home":
                jump head_home
        
        label ice_cream:
            c "How about we go for some ice cream, Miss Fiera?
            \nWould you like that?"
            f happy_1 "Yes! Ice cream! Let's go!"
            c "Okay, okay."
            jump ch3

        label head_home:
            c "Let us go home."
            c "Your father is probably wondering what is taking us so long."
            f neutral_1 "Okay!"
            scene black with dissolve
            $ persistent.home_ending = True
            "{b}Home Ending{/b}"
            return

label praised:
    f happy_1 "I'm so glad you liked the flowers!"
    c "I have never seen such beautiful roses in my life!"
    menu:
        c "Now, hold still while I apply the disinfectant."
        "Warn her that it may sting":
            jump warn_her
        "Do not warn her":
            jump no_warning

    label warn_her:
        c "This may sting a little."
        "You apply the disinfectant carefully."
        "Fiera winces from the stinging."
        c "Is everything alright?"
        f "Yes. Thank you for warning me. I probably would have screamed if you didn't tell me."
        jump praised_cont

    label no_warning:
        "You apply the disinfectant carefully."
        show fiera crying_1 with Dissolve(0.1)
        "Fiera screams from the shock."
        c "Miss Fiera, are you alright?"
        f "It stings!"
        c "I am sorry! Forgive me for not warning you."
        f sad_1 "(sniffles) It's okay. I'm a big girl. I can handle it."
        jump praised_cont

    label praised_cont:
        c "(Look at how far Miss Fiera has come.)"
        c "(I still remember how selfish and demanding she once was.)"
        c "(Now, she loves gifting to others and bears her pain as best she can.)"
        c "(It is about time to head home, 
        but I also want to reward her for how far she has come.)"
        menu:
            c "(What should I do?)"
            "Go straight home":
                jump go_home
            "Go for ice cream":
                jump go_for_ice_cream

    label go_for_ice_cream:
        c "Miss Fiera, thank you so much for the roses."
        c "Now I feel like getting you a gift as well."
        c "Would you care for ice cream?"
        f happy_1 "Ice cream!"
        c "Okay, let us stop by an ice cream parlor on the way home."
        f "Yaaaayyy!!!"
        jump ch3

    label go_home:
        c "Miss Fiera, I am so proud of you for bearing through that."
        c "And the roses are a very thoughtful gift."
        c "Let us go home so I may get these in a vase."
        c "Also, so we can tell your father about how brave you were today. Okay?"
        f "Okay!"
        scene black with dissolve
        $ persistent.home_ending = True
        "{b}Home Ending{/b}"
        return

label focused:
    show fiera sad_1 with Dissolve(0.1)
    pause 1.0
    f speaking_1 "Claude, am I in trouble?"
    menu:
        "Is she in trouble?"
        "Yes":
            jump trouble_yes
        "No":
            jump trouble_no

    label trouble_yes:
        c "{i}Immense trouble{/i}, I am afraid."
        f worried_1 "What?!"
        c "Just joking, my dear."
        f speaking_2 "That's not funny!
        \nI thought I was actually in trouble!"
        jump focused_cont_1
        
    label trouble_no:
        c "No, of course not, my dear."
        jump focused_cont_1

    label focused_cont_1:
        "You prepare the disinfectant."
        c "However, though you are not in trouble, this will sting a bit."
        "You apply the disinfectant."
        f speaking_2 "(wincing) Ah!"
        c "I told you."
        show fiera sad_1 with Dissolve(0.1)
        "You apply the ointment and bandage."
        "You notice Fiera still has a worried look on her face."
        c "Miss Fiera, are you alright?"
        f speaking_1 "Yeah, the cut doesn't hurt anymore."
        c "I am glad, but I was referring to that troubled look on your face."
        f "..."
        c "Miss Fiera, you can tell me. I will not be upset with you."
        f "..."
        f "Do you really like the roses, Claude?"
        c "Of course I do!"
        f "But you yelled at me for getting hurt."
        c "That I did."
        f speaking_2 "But I'm okay! The cuts don't even hurt! So everything should be fine, right?"
        c "Having multiple cuts on your hands are not {i}\"fine\"{/i}."
        f "..."
        c "I do appreciate you gift..."
        c "... but I do not appreciate you getting hurt when you did not need to."
        f "There were so many thorns, though! 
        It was impossible to get roses without touching the thorns!"
        f "I wanted to do something nice for you! 
        Doesn't that count for something?"
        c "..."
        "You embrace Fiera."
        c "Of course that counts."
        c "However, if your really want to do something nice for me..."
        c "{i}Tell me{/i} you appreciate me."
        f "(muffled) But you already know I do."
        c "Yes, but I could hear it a thousand times and cherish it more with each iterration."
        "You let go of Fiera."
        f "..."
        f "You just want me want me to say I appreciate you?"
        c "Yes."
        f "But you don't want flowers?"
        menu:
            "Depends how you get them.":
                jump depends
            "No. Never again.":
                jump never_again

    label depends:
        c "That depends on how you get them."
        c "Preferably without injuring yourself."
        jump focused_cont_2

    label never_again:
        c "After today's incident, never again."
        jump focused_cont_2

    label focused_cont_2:
        c "But, I will accept these for today."
        menu:
            "Go for ice cream":
                jump ice_cream
            "Go Home":
                jump head_home
            
    return