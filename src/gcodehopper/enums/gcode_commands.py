from enum import Enum


class GCodeCommands(Enum):
    G0: str = "G0"  # Move
    G1: str = "G1"  # Move

    M82: str = "M82"  # Set extruder to absolute mode
    M83: str = "M83"  # Set extruder to relative mode

    G4: str = "G4"  # Dwell

    G10: str = "G10"  # Retract
    G11: str = "G11"  # Recover
    G28: str = "G28"  # Home
    G29: str = "G29"  # Auto bed leveling
    G30: str = "G30"  # Single probe
    G31: str = "G31"  # Set Z probe trigger value offset
    G32: str = "G32"  # Probe Z and calculate Z plane
    G90: str = "G90"  # Set to absolute positioning
    G91: str = "G91"  # Set to relative positioning
    G92: str = "G92"  # Set position

    M104: str = "M104"  # Set extruder temperature
    M106: str = "M106"  # Fan on
    M107: str = "M107"  # Fan off
    M109: str = "M109"  # Set extruder temperature and wait
    M140: str = "M140"  # Set bed temperature
    M190: str = "M190"  # Set bed temperature and wait
    M204: str = "M204"  # Set default acceleration
    M205: str = "M205"  # Set advanced settings
    M206: str = "M206"  # Set home offset
    M207: str = "M207"  # Set retract length
    M208: str = "M208"  # Set axis max travel
    M209: str = "M209"  # Enable automatic retract
    M220: str = "M220"  # Set speed factor override percentage
    M221: str = "M221"  # Set extrude factor override percentage
    M226: str = "M226"  # Gcode initiated pause
    M300: str = "M300"  # Beep
    M400: str = "M400"  # Finish all moves
    M600: str = "M600"  # Filament change pause
    M603: str = "M603"  # Filament change pause

    M0: str = "M0"  # Stop
    M1: str = "M1"  # Sleep
    M17: str = "M17"  # Enable steppers
    M18: str = "M18"  # Disable steppers
    M84: str = "M84"  # Stop idle hold
    M85: str = "M85"  # Set inactivity shutdown

    UNSUPPORTED: str = "UNSUPPORTED"  # Unsupported command
