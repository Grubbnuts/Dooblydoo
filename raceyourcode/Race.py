### Enable logging ###
#StartDetailedLoging()
#StartUserLog()

### Wait for the lights ###
WaitForGo()
### Racing until terminated ###
while Globals.running:
##	# Wait until we reach the first corner
##	WaitForWaypoint(2)
##	# Wait until we reach the start / finish line
##	WaitForWaypoint(1)
    # Full speed to the first corner
    Speed(100)
    AimForLane(0)
    WaitForWaypoint(2)
    # Slow down, move to the inside and wait for the apex
    Speed(0)
    AimForLane(-1)
    WaitForWaypoint(3)
    # Speed up and move to the center until the S curve starts
    Speed(100)
    AimForLane(0)
    WaitForWaypoint(4)
    # Move towards the outside until the S curve changes
    AimForLane(0)
    WaitForWaypoint(5)
    # Move towards the inside until the S curve ends
    AimForLane(+1)
    WaitForWaypoint(6)
    # Slow down and move to the inside around the corner
    Speed(60)
    AimForLane(-2)
    WaitForWaypoint(7)
    # Speed up for the back straight along the center
    Speed(100)
    AimForLane(-1)
    WaitForWaypoint(8)
    # High speed for the last corner on the inside
    Speed(50)
    AimForLane(+2)
    WaitForWaypoint(9)
    # Full speed until the start/finish line along the outside
    Speed(100)
    AimForLane(0)
    WaitForWaypoint(1)


### Wait for a few seconds ###
#WaitForSeconds(4)

### Disable logging ###
EndDetailedLog()
EndUserLog()

### End of the race ###
FinishRace()
