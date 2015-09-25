# Guild Wars 2 API (Python)
A Python 3.x wrapper for the second version of the <a href="https://wiki.guildwars2.com/wiki/API:Main" target="_blank">Guild Wars 2 API</a>.

## Installation

- Clone or download the repository
- Run `python setup.py install`

## Usage

    import guildwars2api
    gw = guildwars2api.GW2()
    
    # You can specify a preferred localization and a connection timeout (in seconds).
    gw = guildwars2api.GW2(language="EN", timeout=5)
    
    # Print details about your connection to the Guild Wars 2 API, e.g. the current API key.
    print(gw.get_connection_details())
    
    # Print the currently available endpoints of the second version of the Guild Wars 2 API.
    print('\n'.join(gw.get_endpoints()))
    
    # Some player account endpoints, e.g. /v2/pvp/stats, require an authenticated connection.
    # You can authenticate an entire session directly...
    gw.authenticate("REDACTED_API_KEY")
    print(gw.get_pvp_stats())
    # ...or if need be.
    print(gw.get_pvp_stats("REDACTED_API_KEY"))
    # Likewise, you can securely retrieve access token information for the session token...
    print(gw.get_tokeninfo())
    # ...or a given API key.
    print(gw.get_tokeninfo("REDACTED_API_KEY"))
    
    # Get a list of details of respectively a world, a few worlds and all worlds.
    world = gw.get_worlds(1001)
    worlds = gw.get_worlds(1001, 1002, 1003)
    worlds = gw.get_worlds("all")
    
    # You can also grab just all the world ids.
    world_ids = gw.get_worlds_ids()
    
    # Print out all the world names of the worlds with a very high population of players.
    worlds = gw.get_worlds("all")
    for world in worlds:
        if world["population"] == "VeryHigh":
            print("{}\t{}".format(world["id"], world["name"]))

## List of currently supported endpoints

- /v2/currencies
- /v2/files
- /v2/items
- /v2/maps
- /v2/materials
- /v2/pvp/games
- /v2/pvp/stats
- /v2/quaggans
- /v2/recipes
- /v2/recipes/search
- /v2/skins
- /v2/specializations
- /v2/tokeninfo
- /v2/traits
- /v2/worlds

## License

Code in this repository is licensed under the [MIT License](LICENSE).