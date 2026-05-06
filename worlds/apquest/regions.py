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

    smb3_game_region = create_region(multiworld, player, active_locations, 'smb3_game', None)
    
    smb3_w1_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_region, None)

    smb3_w1_1_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
    smb3_w1_1_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
    smb3_w1_1_exit_1 = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_exit,
                                           [LocationName.smb3_w1_1_exit])
    smb3_w1_2_tile = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_tile, None)
    smb3_w1_2_region = create_region(multiworld, player, active_locations, LocationName.smb3_w1_1_region, None)
    smb3_w1_2_exit_1 = create_region(multiworld, player, active_locations, LocationName.smb3_w1_2_exit,
                                           [LocationName.smb3_w1_2_exit])
    
    # Let's put all these regions in a list.
    multiworld.regions += [
        menu_region,
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

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    if world.options.hammer:
        top_middle_room = Region("Top Middle Room", world.player, world.multiworld)
        regions.append(top_middle_room)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: APQuestWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    menu = world.get_region("Menu")
    smb3_game = world.get_region("Super Mario Bros. 3")
    smb3_w1 = world.get_region("SMB3 Grass Land")
    smb3_w1_1 = world.get_region("SMB3 Grass Land 1")
    smb3_w1_2 = world.get_region("SMB3 Grass Land 2")
    smb3_w1_3 = world.get_region("SMB3 Grass Land 3")
    smb3_w1_4 = world.get_region("SMB3 Grass Land 4")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    def connect_regions(world: World, level_to_tile_dict):
    multiworld: MultiWorld = world.multiworld
    player: int = world.player

    names: typing.Dict[str, int] = {}

    connect(world, "Menu", LocationName.smb3_game)
    connect(world, LocationName.smb3_game, LocationName.smb3_w1)
    connect(world, LocationName.smb3_w1_region, LocationName.smb3_w1_1_tile)

    # Connect regions within levels using rules
    connect(world, LocationName.smb3_w1_1_region, LocationName.smb3_w1_1_exit)
    connect(world, LocationName.smb3_w1_2_region, LocationName.smb3_w1_2_exit)
    connect(world, LocationName.smb3_w1_3_region, LocationName.smb3_w1_3_exit)
    connect(world, LocationName.smb3_w1_4_region, LocationName.smb3_w1_4_exit)
    connect(world, LocationName.yoshis_island_castle_region, LocationName.yoshis_island_castle,
            lambda state: (state.has(ItemName.mario_climb, player)))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        overworld.connect(top_middle_room, "Overworld to Top Middle Room")
