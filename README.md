# Guild Wars 2 API (Python)
A Python 3.x wrapper for the second version of the <a href="https://wiki.guildwars2.com/wiki/API:Main" target="_blank">Guild Wars 2 API</a>.

## Usage

    import guildwars2api
    gw = guildwars2api.GW2()
    
    # You can specify a preferred localization and a connection timeout (in seconds).
    gw = guildwars2api.GW2(language="EN", timeout=5)
    
    # Print details about your connection to the Guild Wars 2 API, e.g. the current API key.
    print(gw.get_connection_details())
    
    # Print the currently available endpoints of the second version of the Guild Wars 2 API.
    print('\n'.join(gw.get_endpoints()))
    
    # Get a list of details of respectively a world, a few worlds and all worlds.
    world = gw.get_world(1001)
    worlds = gw.get_world(1001, 1002, 1003)
    worlds = gw.get_worlds()
    
    # You can also grab just all the world ids.
    world_ids = gw.get_worlds_ids()
    
    # Print out all the world names of the worlds with a very high population of players.
    worlds = gw.get_worlds()
    for world in worlds:
        if world["population"] == "VeryHigh":
            print("{}".format(world["name"]))

## List of currently supported endpoints

- /v2/traits
- /v2/worlds

## License

Code in this repository is licensed under the [MIT License](LICENSE).