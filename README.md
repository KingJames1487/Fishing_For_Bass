# Fishing_For_Bass

Rules: 

3 - 6  Players

Each player goes once in a round, going counterclockwise.

Each Player will start with one Warrior in a spot of their choosing, and automatically CLAIM that terrritory.

Each territory gives either 5, 3, 1, or 0 of a RESOURCE, with exception to Madagascar which gives 5 of each.

RESOURCES:  FOOD,  WOOD,  STEEL,  OIL

CLAIM: Claiming territories requires 5 consecutive turns of OWNERSHIP to begin receiving resources. 
A Claimed territory will produce the specified resources for the player. A territory is UNCLAIMED if you no 
longer have 0 power there.

OWNERSHIP : Ownership is defined as being the only player with a unit on any territory. A territory 
is UNOWNED is you have 0 power there.

TURN :

    START PHASE : At the Start of your turn, you first gain one point of OWNERSHIP towards any territories 
    not yet CLAIMED. Then, recieve any rescources you may acrue from your CLAIMED territories.
    
    BUY PHASE : Here, you may spend any resources you choose, any Units or Arial Units must be placed on a 
    territory, Water must be placed on a Coastline you own, and BARRIERS must be placed on a Border partially 
    owned by you.
    
    ACTION PHASE : Here, you may move or Attack Units. Once per round, you may choose to expend 1 of a 
    Units Speed to Attack. If the Attack leaves the Defending territory UNOWNED, the Attacking 
    unit(s) may move into the territory without expending Speed. Speed resets on your turn and if not used 
    to Attack, unless otherwise specified, can be used to move into adjacent allied or UNOWNED territories.


Attacking : When a Unit Attacks a territory with an enemy unit, the Attacking unit subtracts the defending 
territories power level from their current total. If this power level reaches 0 or less, the unit dies. The
defending territory then subtracts the Attacking units power level from its total. 

Water and Arial Units : Water and Arial Units cannot be Attacked and their total power does not factor into 
the power of the defending territory. If the territory an Arial unit is based in is no longer under OWNERSHIP 
by the player that purchased it, it is destroyed. Water and Arial units cannot be transported.

Transport Units : Transport Units are not full units, merely vessels to help move units quickly. They cannot 
Attack, and automatically die if the territory they are in is or becomes UNOWNED. Transport Units cannot carry
an amount of units such that their power level exceeds the transports capacity. Units may board or unboard a 
transport in their territory (or on a neighboring coast) at no cost.

UNITS:

    WARRIOR: Unit
        COST: 10/0/0/0 - **(10 Food/ 0 Wood/ 0 Steel/ 0 Oil)**
        Speed : 1
        Power : 1
        Attack : I Attack a neighboring territory
        Claim Speed : 5

    TANK: Unit
        COST: 50/0/150/0
        Speed : 1
        Power : 10
        Attack : I Attack a neighboring territory
        Claim Speed : 5
        Only Big Boats may carry Tanks

    HORSE: Transport
        COST: 20/0/0/0 
        Attack : None
        Speed : 2
        Capacity : 2
        Claim Speed : 3

    BUS: Transport
        COST: 0/15/30/20
        Attack : None
        Speed : 3
        Capacity : 20
        Claim Speed : 3

    BOAT: Water Transport
        COST: 15/30/0/0
        Attack : None
        Speed : 3 (Pathed Water Only or Coast Line)
        Capacity : 5
        Claim Speed : N/A

    INTERMEDIATE BOAT: Water Transport
        COST: 10/150/0/85
        Attack : None
        Speed : 3
        Capacity : 15
        Claim Speed : N/A

    BIG BOAT: Water Transport
        COST: 0/150/150/200
        Attack : Any and all Units being transported may Attack from this Transport
        Speed : 3 (Can Travel to any Coast using 1 Speed)
        Capacity : 30 (Can carry tanks)
        Claim Speed : N/A

    BARRIER: Defense
        COST: 0/25/50/0
        Defend : Kill any Unit Attacking through this border this turn. At the end of the turn, destroy me.
        Placed on any border of two territories.
        
    ANTI-AIRCRAFT : Defense
        COST : 10/0/100/50
        Defend : If the Attacker is a PLANE, kill it. You do not lose units.
        Place on any territory.
        
    PLANE: Arial
        COST: 0/0/250/200
        Speed : 1 Territory
        Power : 5
        Attack : I attack any chosen territory, I do not lose Power when I Attack.
        
    NUKES: Arial
        COST:500/500/1000/1500
        Attack : Destroys all units in chosen destination as well as any bordering territories. 
        The territory attacked cannot be CLAIMED for 10 rounds.
