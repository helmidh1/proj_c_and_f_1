transform bounce_1:
    easein 0.1 yoffset -20
    easein 0.15 yoffset 0
    repeat 2

transform bounce_2:
    easein 0.1 yoffset -120
    easein 0.15 yoffset 0
    pause 0.1
    repeat 2

transform bounce_inf:
    easein 0.1 yoffset -120
    easein 0.1 yoffset 0
    pause 0.1
    easein 0.1 yoffset -120
    easein 0.1 yoffset 0
    pause 2.0
    repeat

transform zoomin:
    linear 1 zoom 1.2
    
transform zoomout:
    linear 1 zoom 0.8

transform flash:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    # linear 0.5 matrixcolor ContrastMatrix(1.0)
    linear 0.5 matrixcolor ContrastMatrix(5.0)
    linear 0.5 matrixcolor ContrastMatrix(1.0)

transform hover:
    easein 2.0 yoffset -15
    easein 2.0 yoffset 0
    repeat

transform hop_1:
    easein 0.1 yoffset -5
    easein 0.1 yoffset 0

transform hop_2:
    easein 0.1 yoffset -10
    easein 0.1 yoffset 0

transform hop_3:
    easein 0.1 yoffset -120
    easein 0.1 yoffset 0

transform hop_4:
    easein 0.2 yoffset -120
    easein 0.15 yoffset 0

transform hop_5:
    easein 0.2 yoffset -180
    easein 0.15 yoffset 0

transform shake_1:
    easein 0.1 xoffset -20
    easein 0.1 xoffset 20
    easein 0.1 xoffset -20
    easein 0.1 xoffset 20
    easein 0.1 xoffset 0