init python:
    current_face = ""
    
    def change_face(new_face:str):
        global current_face
        if new_face is not current_face:
            renpy.show(new_face)
            renpy.with_statement(Dissolve(0.1))
            if current_face == "":
                return
            renpy.hide(current_face)
            current_face = new_face
