2025 Vex code; python only
  latest commit/pull :
        12/11/2025 : 2:25 PM
            *Added fix for swivel_dir waiting until the turn_to_position is finished, which would cause an indefinite buffer when motor was stuck on anything.
            *Current config for controls is :
                    # L2-swivel arm
                    # L1-Switch intake direction
                    # R1-Start/stop intake
                    # R2-
                    # ^-
                    # <-
                    # >-
                    # \/-
                    # A-
                    # B-
                    # X-
                    # Y-
                    # LStick_X_axis-Middle wheel control
                    # LStick_Y_axis-Four main wheels FWD/REV
                    # RStick_X_axis-Rotate bot in place
                    # RStick_Y_axis-
