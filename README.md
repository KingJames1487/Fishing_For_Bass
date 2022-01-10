# Fishing_For_Bass

Rules: 

3 - 6  Players

Each Player will start with one Warrior in a spot of their choosing.

On Turn 1, each placed warrior will automatically CLAIM that terrritory.

Each player goes once in a round

Each territory gives either 5, 3, 1, or 0 of a RESOURCE, with exception to Madagascar which gives 5 of each.

RESOURCES:  FOOD,  WOOD,  STEEL,  OIL

CLAIM: Claiming territories requires 5 consecutive turns of OWNERSHIP to begin receiving resources. A Claimed territory will produce the specified resources for the player.

OWNERSHIP : Ownership is defined as being the only player with a unit on any territory.

UNITS:

    WARRIOR: Unit
        COST: 10/0/0/0 - **(10 Food/ 0 Wood/ 0 Steel/ 0 Oil)**
        Equivalent to 1 Unit
        Mount : Any vehicle
        Speed : 1 Territory Per Turn
        Claim Speed : 5

    TANK: Unit
        COST: 50/0/150/0
        Equivalent to 10 Units
        Mount : None
        Speed : 1 Territory Per Turn
        Claim Speed : 5

    HORSE: Transporter
        COST: 20/0/0/0 
        Cannot Attack
        Speed : 2 Territories Per Turn
        Transport : 2
        Claim Speed : 3

    BUS: Transporter
        COST: 0/15/30/20
        Cannot Attack
        Speed : 3 Territories Per Turn
        Transport : 20
        Claim Speed : 3

    BOAT: Water Transport
        COST: 15/30/0/0
        Speed : 3 (Pathed Water Only or Coast Line)
        Transport : 5
        Claim Speed : 3

    INTERMEDIATE BOAT: Water Transport
        COST: 10/150/0/85
        Speed : 3
        Transport : 15
        Claim Speed : 3

    BIG BOAT: Water Transport
        COST: 0/150/150/200
        Speed : 3 (Can Travel to any Coast using 1 Speed)
        Transport : 30 (Can carry tanks)
        Claim Speed : 3
        MAY ATTACK WITH TRANSPORTED UNITS

    BARRIER: Defense
        COST: 0/25/50/0
        Placed on any border, if attacked from that border, kill
        attacking Units, then Destroy me at the end of the turn
        
    ANTI-AIRCRAFT : Defense
        COST : 10/0/100/50
        Place on any territory, if attacked by a PLANE, the PLANE dies, you do not lose units.
        
    PLANE: Arial
        COST: 0/0/250/200
        Attack : I attack a chosen territory, killing up to 5 Units. This can be done once per round
        
    NUKES: Arial
        COST:500/500/1000/1000 + 1000 OIL per territory moved (Max : 3)
        Must be fired from a freindly territory
        Destoys and unclaims all units in chosen destination as well as any surrounding territories
        Territory chosen cannot give resources for 10 rounds
