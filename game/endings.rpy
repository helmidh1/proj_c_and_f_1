define persistent.home_ending = False
define persistent.ice_cream_ending = False
define persistent.meanie_ending = False

# label reset_endings:
#     $ persistent.home_ending = False
#     $ persistent.ice_cream_ending = False
#     $ persistent.meanie_ending = False
init python:
    def reset_endings():
        persistent.home_ending = False
        persistent.ice_cream_ending = False
        persistent.meanie_ending = False