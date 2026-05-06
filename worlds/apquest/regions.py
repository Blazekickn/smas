from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SMASWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: SMASWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: SMASWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    menu_region = create_region(multiworld, player, active_locations, 'Menu', None)

    if world.options.smb3_game:
        smb3_game_region = create_region(multiworld, player, active_locations, 'smb3_game', None)

        smb3_w1_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_region, None)

        smb3_w1_1_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_1_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_1_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_exit,
                                           [LocationName.smb3_w1_1_exit])
        smb3_w1_2_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_2_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_2_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_2_exit])
        smb3_w1_3_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_3_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_3_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_3_exit])                                           
        smb3_w1_4_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_4_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_4_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_4_exit]) 
        smb3_w1_fortress_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_fortress_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_fortress_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_fortress_exit])   
        smb3_w1_5_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_5_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_5_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_5_exit])
        smb3_w1_6_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_6_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_6_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_6_exit])                                         
        smb3_w1_airship_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
        smb3_w1_airship_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
        smb3_w1_airship_exit = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_airship_exit]) 
 
        if world.options.smb3_chests:
            smb3_w1_house1_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_house1_tile, None)
            smb3_w1_house1_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_house1_region, None)
            smb3_w1_house1_chest = create_region(multiworld, player, active_locations, LocationName.smb3_w1_house1_chest, 
                                           [LocationName.smb3_w1_house1_chest_1])
                                        
            smb3_w1_house2_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_house2_tile, None)
            smb3_w1_house2_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_house2_region, None)
            smb3_w1_house2_chest = create_region(multiworld, player, active_locations, LocationName.smb3_w1_house2_chest, 
                                           [LocationName.smb3_w1_house2_chest_1]) 

            smb3_w1_4_whitehouse_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_4_whitehouse_region, None)
            smb3_w1_4_whitehouse_chest = create_region(multiworld, player, active_locations, LocationName.smb3_w1_4_whitehouse_chest, 
                                           [LocationName.smb3_w1_4_whitehouse_chest]) 
            smb3_w1_3_chestroom_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_3_chest_region, None)
            smb3_w1_3_chestroom_chest = create_region(multiworld, player, active_locations, LocationName.smb3_w1_3_chestroom_chest, 
                                           [LocationName.smb3_w1_3_chestroom_chest]) 
            smb3_w1_fortress_chestroom_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_fortress_chestroom_region, None)
            smb3_w1_fortress_chestroom_chest = create_region(multiworld, player, active_locations, LocationName.smb3_w1_fortress_chestroom_chest, 
                                           [LocationName.smb3_w1_fortress_chestroom_chest]) 
 
 
 
    # Let's put all these regions in a list.
    multiworld.regions += [
        menu_region,

        if world.options.smb3_game:
            smb3_game,
            smb3_w1_region,
            smb3_w1_1_tile,
            smb3_w1_1_region,
            smb3_w1_1_exit,
            smb3_w1_2_tile,
            smb3_w1_2_region,
            smb3_w1_2_exit,
            smb3_w1_3_tile,
            smb3_w1_3_region,
            smb3_w1_3_exit,
            smb3_w1_4_tile,
            smb3_w1_4_region,
            smb3_w1_4_exit,
            smb3_w1_fortress_tile,
            smb3_w1_fortress_region,
            smb3_w1_fortress_exit,
            smb3_w1_5_tile,
            smb3_w1_5_region,
            smb3_w1_5_exit,
            smb3_w1_6_tile,
            smb3_w1_6_region,
            smb3_w1_6_exit,
            smb3_w1_airship_tile,
            smb3_w1_airship_region,
            smb3_w1_airship_exit,

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
        if world.options.smb3_chests:
            smb3_w1_house1_tile,
            smb3_w1_house1_region,
            smb3_w1_house1_chest,
            smb3_w1_house2_tile,
            smb3_w1_house2_region,
            smb3_w1_house2_chest,
            smb3_w1_4_whitehouse_region,
            smb3_w1_4_whitehouse_chest,
            smb3_w1_3_chestroom_region,
            smb3_w1_3_chestroom_chest,
            smb3_w1_fortress_chestroom_region,
            smb3_w1_fortress_chestroom_chest,



    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions

    names: typing.Dict[str, int] = {}
    if world.options.smb3_game:
        connect(world, "Menu", LocationName.smb3_game)
        connect(world, LocationName.smb3_game, LocationName.smb3_w1)
        connect(world, LocationName.smb3_w1_region, LocationName.smb3_w1_1_tile)

        # Connect regions within levels using rules
        connect(world, LocationName.smb3_w1_1_region, LocationName.smb3_w1_1_exit)
        connect(world, LocationName.smb3_w1_2_region, LocationName.smb3_w1_2_exit)
        connect(world, LocationName.smb3_w1_3_region, LocationName.smb3_w1_3_exit)
        connect(world, LocationName.smb3_w1_4_region, LocationName.smb3_w1_4_exit)
        connect(world, LocationName.smb3_w1_fortress_region, LocationName.smb3_w1_fortress_exit)
        connect(world, LocationName.smb3_w1_5_region, LocationName.smb3_w1_5_exit)
        connect(world, LocationName.smb3_w1_6_region, LocationName.smb3_w1_6_exit)
        connect(world, LocationName.smb3_w1_airship_region, LocationName.smb3_w1_airship_exit)

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
        if world.options.chests:
            add_location_to_region(multiworld, player, active_locations, LocationName.smb3_w1_house1_region, LocationName.smb3_w1_house1_chest)
            add_location_to_region(multiworld, player, active_locations, LocationName.smb3_w1_house2_region, LocationName.smb3_w1_house2_chest)
            add_location_to_region(multiworld, player, active_locations, LocationName.smb3_w1_4_whitehouse_region, LocationName.smb3_w1_4_whitehouse_chest)
            add_location_to_region(multiworld, player, active_locations, LocationName.smb3_w1_3_chestroom_region, LocationName.smb3_w1_3_chestroom_chest)
            add_location_to_region(multiworld, player, active_locations, LocationName.smb3_w1_fortress_chestroom_region, LocationName.smb3_w1_fortress_chestroom_chest)