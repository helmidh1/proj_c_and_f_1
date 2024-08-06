transform bounce:
    yoffset 0
    easein 0.175 yoffset -60
    easein 0.175 yoffset 0
    easeout 0.175 yoffset -30
    easeout 0.175 yoffset 0
    yoffset 0
    repeat 1

transform zoomin:
    linear 1 zoom 1.2
    
transform zoomout:
    linear 1 zoom 0.8

transform flash:
    matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    # linear 0.5 matrixcolor ContrastMatrix(1.0)
    linear 0.5 matrixcolor ContrastMatrix(5.0)
    linear 0.5 matrixcolor ContrastMatrix(1.0)