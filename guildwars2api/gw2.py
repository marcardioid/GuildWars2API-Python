import requests

class GW2(object):
    """Python 3.x wrapper for the second version of the Guild Wars 2 API."""
    def __init__(self, language="EN", timeout=5):
        self.API_SERVER = "https://api.guildwars2.com"
        self.API_LANGUAGE = language
        self.API_TIMEOUT = timeout
        self.API_ENDPOINTS_V2 = [
            "account",
            "account/bank",
            "account/dyes",
            "account/materials",
            "account/skins",
            "account/wallet",
            "build",
            "characters",
            "colors",
            "commerce",
            "commerce/exchange",
            "commerce/exchange/coins",
            "commerce/exchange/gems",
            "commerce/listings",
            "commerce/prices",
            "commerce/transactions",
            "continents",
            "currencies",
            "files",
            "items",
            "maps",
            "materials",
            "pvp/games",
            "pvp/stats",
            "quaggans",
            "recipes",
            "recipes/search",
            "skins",
            "specializations",
            "tokeninfo",
            "traits",
            "worlds"
        ]
        self.API_KEY = None
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "GUILD WARS 2 API WRAPPER FOR PYTHON 3.X", "Accept": "application/json"})

    def get_commerce_transactions_current_buys(self, token=None):
        """Returns the current buying commerce transactions for the current session token or the given token."""
        return self._request("commerce/transactions/current/buys", access_token=token) if token else self._request("commerce/transactions/current/buys")

    def get_commerce_transactions_current_sells(self, token=None):
        """Returns the current selling commerce transactions for the current session token or the given token.
        The API endpoint only supplies the commerce transaction history of the past 90 days.
        """
        return self._request("commerce/transactions/current/sells", access_token=token) if token else self._request("commerce/transactions/current/sells")

    def get_commerce_transactions_history_buys(self, token=None):
        """Returns the buying commerce transaction history for the current session token or the given token.
        The API endpoint only supplies the commerce transaction history of the past 90 days.
        """
        return self._request("commerce/transactions/history/buys", access_token=token) if token else self._request("commerce/transactions/history/buys")

    def get_commerce_transactions_history_sells(self, token=None):
        """Returns the selling commerce transaction history for the current session token or the given token."""
        return self._request("commerce/transactions/history/sells", access_token=token) if token else self._request("commerce/transactions/history/sells")

    def get_continents(self, *ids):
        """Returns the continent data for the continent(s) with the given id(s) as a list."""
        return self._request("continents", ids=','.join(str(id) for id in ids))

    def get_continents_ids(self):
        """Returns just all the continent ids as a list."""
        return self._request("continents")

    def get_continent_floors(self, continent_id, *ids):
        """Returns the floor data for the floor(s) with the given id(s) for the given continent as a list."""
        return self._request("continents/{}/floors".format(continent_id), ids=','.join(str(id) for id in ids))

    def get_continent_floors_ids(self, continent_id):
        """Returns just all the floor ids for the given continent as a list."""
        return self._request("continents/{}/floors".format(continent_id))

    def get_continent_floor_regions(self, continent_id, floor_id, *ids):
        """Returns the region data for the region(s) with the given id(s) for the given continent and floor as a list."""
        return self._request("continents/{}/floors/{}/regions".format(continent_id, floor_id), ids=','.join(str(id) for id in ids))

    def get_continent_floor_regions_ids(self, continent_id, floor_id):
        """Returns just all the region ids for the given continent and floor as a list."""
        return self._request("continents/{}/floors/{}/regions".format(continent_id, floor_id))

    def get_continent_floor_region_maps(self, continent_id, floor_id, region_id, *ids):
        """Returns the map data for the map(s) with the given id(s) for the given continent, floor and region a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps".format(continent_id, floor_id, region_id), ids=','.join(str(id) for id in ids))

    def get_continent_floor_region_maps_ids(self, continent_id, floor_id, region_id):
        """Returns just all the map ids for the given continent, floor and region as a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps".format(continent_id, floor_id, region_id))

    def get_continent_floor_region_map_sectors(self, continent_id, floor_id, region_id, map_id, *ids):
        """Returns the sector data for the sectors(s) with the given id(s) for the given continent, floor, region and map a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps/{}/sectors".format(continent_id, floor_id, region_id, map_id), ids=','.join(str(id) for id in ids))

    def get_continent_floor_region_map_sectors_ids(self, continent_id, floor_id, region_id, map_id):
        """Returns just all the sector ids for the given continent, floor, region and map as a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps/{}/sectors".format(continent_id, floor_id, region_id, map_id))

    def get_continent_floor_region_map_pois(self, continent_id, floor_id, region_id, map_id, *ids):
        """Returns the point of interest data for the point(s) of interest with the given id(s) for the given continent, floor, region and map a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps/{}/pois".format(continent_id, floor_id, region_id, map_id), ids=','.join(str(id) for id in ids))

    def get_continent_floor_region_map_pois_ids(self, continent_id, floor_id, region_id, map_id):
        """Returns just all the point of interest ids for the given continent, floor, region and map as a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps/{}/pois".format(continent_id, floor_id, region_id, map_id))

    def get_continent_floor_region_map_tasks(self, continent_id, floor_id, region_id, map_id, *ids):
        """Returns the task data for the task(s) with the given id(s) for the given continent, floor, region and map a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps/{}/tasks".format(continent_id, floor_id, region_id, map_id), ids=','.join(str(id) for id in ids))

    def get_continent_floor_region_map_tasks_ids(self, continent_id, floor_id, region_id, map_id):
        """Returns just all the task ids for the given continent, floor, region and map as a list."""
        return self._request("continents/{}/floors/{}/regions/{}/maps/{}/tasks".format(continent_id, floor_id, region_id, map_id))

    def get_currencies(self, *ids):
        """Returns the currency data for the currency/currencies with the given id(s) as a list."""
        return self._request("currencies", ids=','.join(str(id) for id in ids))

    def get_currencies_ids(self):
        """Returns just all the currency ids as a list."""
        return self._request("currencies")

    def get_files(self, *ids):
        """Returns the file data for the file(s) with the given id(s) as a list."""
        return self._request("files", ids=','.join(str(id) for id in ids))

    def get_files_ids(self):
        """Returns just all the file ids as a list."""
        return self._request("files")

    def get_items(self, *ids):
        """Returns the item data for the item(s) with the given id(s) as a list."""
        return self._request("items", ids=','.join(str(id) for id in ids))

    def get_items_ids(self):
        """Returns just all the item ids as a list."""
        return self._request("items")

    def get_maps(self, *ids):
        """Returns the map data for the map(s) with the given id(s) as a list."""
        return self._request("maps", ids=','.join(str(id) for id in ids))

    def get_maps_ids(self):
        """Returns just all the maps ids as a list."""
        return self._request("maps")

    def get_materials(self, *ids):
        """Returns the material data for the material(s) with the given id(s) as a list."""
        return self._request("materials", ids=','.join(str(id) for id in ids))

    def get_materials_ids(self):
        """Returns just all the material ids as a list."""
        return self._request("materials")

    def get_pvp_games(self, *ids, token=None):
        """Returns the pvp game data for the pvp game(s) with the given id(s) as a list.
        The API endpoint only supplies the 10 latest games at most.
        """
        matches = ','.join(str(id) for id in ids)
        return self._request("pvp/games", access_token=token, ids=matches) if token else self._request("pvp/games", ids=matches)

    def get_pvp_games_ids(self, token=None):
        """Returns just all the pvp game ids as a list.
        The API endpoint only supplies the 10 latest games at most.
        """
        return self._request("pvp/games", access_token=token) if token else self._request("pvp/games")

    def get_pvp_stats(self, token=None):
        """Returns the pvp stats for the current session token or the given token."""
        return self._request("pvp/stats", access_token=token) if token else self._request("pvp/stats")

    def get_quaggans(self, *ids):
        """Returns the quaggan data for the quaggan(s) with the given id(s) as a list."""
        return self._request("quaggans", ids=','.join(str(id) for id in ids))

    def get_quaggans_ids(self):
        """Returns just all the quaggan ids as a list."""
        return self._request("quaggans")

    def get_recipes(self, *ids):
        """Returns the recipe data for the recipe(s) with the given id(s) as a list."""
        return self._request("recipes", ids=','.join(str(id) for id in ids))

    def get_recipes_ids(self):
        """Returns just all the recipe ids as a list."""
        return self._request("recipes")

    def get_recipes_ids_by_ingredient(self, lookup, id): # TODO: Split to two functions?
        """Returns a list of recipes using the given ingredient. Searchable by input and output ingredient."""
        if lookup == "input":
            return self._request("recipes/search", input=id)
        elif lookup == "output":
            return self._request("recipes/search", output=id)
        else:
            return [] # TODO: Raise API exception!

    def get_skins(self, *ids):
        """Returns the skin data for the skin(s) with the given id(s) as a list."""
        return self._request("skins", ids=','.join(str(id) for id in ids))

    def get_skins_ids(self):
        """Returns just all the skin ids as a list."""
        return self._request("skins")

    def get_specializations(self, *ids):
        """Returns the specialization data for the specialization(s) with the given id(s) as a list."""
        return self._request("specializations", ids=','.join(str(id) for id in ids))

    def get_specializations_ids(self):
        """Returns just all the specialization ids as a list."""
        return self._request("specializations")

    def get_tokeninfo(self, token=None):
        """Returns the tokeninfo for the current session token or the given token."""
        return self._request("tokeninfo", access_token=token) if token else self._request("tokeninfo")

    def get_traits(self, *ids):
        """Returns the trait data for the trait(s) with the given id(s) as a list."""
        return self._request("traits", ids=','.join(str(id) for id in ids))

    def get_traits_ids(self):
        """Returns just all the trait ids as a list."""
        return self._request("traits")

    def get_worlds(self, *ids):
        """Returns the world data for the world(s) with the given id(s) as a list."""
        return self._request("worlds", ids=','.join(str(id) for id in ids))

    def get_worlds_ids(self):
        """Returns just all the world ids as a list."""
        return self._request("worlds")

    def get_endpoints(self):
        """Returns the available API endpoints for version 2 of the Guild Wars 2 API as a list."""
        return self.API_ENDPOINTS_V2

    def get_connection_details(self):
        """Returns the API connection details as a string."""
        return "Connected to '{}' ({}).{}".format(self.API_SERVER,
                                                  self.API_LANGUAGE.upper(),
                                                  " (With token: {})".format(self.API_KEY) if self.API_KEY else '')

    def authenticate(self, key):
        """Authenticate to the GuildWars2 API using the given API key."""
        self.API_KEY = key
        self.session.headers.update({"Authorization": "Bearer {}".format(key)})

    def _request(self, location, **kwargs):
        """Send a request to the Guild Wars 2 API."""
        kwargs["lang"] = self.API_LANGUAGE
        version = "v2" if location in self.API_ENDPOINTS_V2 or location.split('/')[0] in self.API_ENDPOINTS_V2 else "v1"
        try:
            r = self.session.get("{}/{}/{}".format(self.API_SERVER, version, location),
                                 params=kwargs.items(),
                                 timeout=self.API_TIMEOUT)
            r.raise_for_status()
            try:
                return r.json()
            except ValueError as e:
                print(e)
                return []
        except (requests.exceptions.HTTPError, requests.exceptions.Timeout, ConnectionError) as e:
            print(e)
            return []