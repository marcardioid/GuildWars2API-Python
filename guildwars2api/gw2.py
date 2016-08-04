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
            "achievements",
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
            "minis",
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

    def get_account(self, token=None):
        """Returns the account data as a dictionary for the current session token or the given token."""
        return self._request("account", access_token=token) if token else self._request("account")

    def get_account_bank(self, token=None):
        """Returns the bank data as a list for the current session token or the given token."""
        return self._request("account/bank", access_token=token) if token else self._request("account/bank")

    def get_account_dyes(self, token=None):
        """Returns the unlocked dye data as a list for the current session token or the given token."""
        return self._request("account/dyes", access_token=token) if token else self._request("account/dyes")

    def get_account_materials(self, token=None):
        """Returns the material storage data as a list for the current session token or the given token."""
        return self._request("account/materials", access_token=token) if token else self._request("account/materials")

    def get_account_skins(self, token=None):
        """Returns the unlocked skin data as a list for the current session token or the given token."""
        return self._request("account/skins", access_token=token) if token else self._request("account/skins")

    def get_account_wallet(self, token=None):
        """Returns the wallet data as a list for the current session token or the given token."""
        return self._request("account/wallet", access_token=token) if token else self._request("account/wallet")

    def get_achievements(self, *ids):
        """Returns the achievement data for the achievement(s) with the given id(s) as a list."""
        return self._request("achievements", ids=','.join(str(id) for id in ids))

    def get_achievements_ids(self):
        """Returns just all the achievement ids as a list."""
        return self._request("achievements")

    def get_build(self):
        """Returns the current build id of the Guild Wars 2 game as an integer."""
        return int(self._request("build")["id"])

    def get_characters(self, *ids, token=None):
        """Returns the character data for the character(s) with the given name(s) as a list."""
        names = ','.join(str(id) for id in ids)
        return self._request("characters", access_token=token, ids=names) if token else self._request("characters", ids=names)

    def get_characters_names(self, token=None):
        """Returns just all the character names as a list for the current session token or the given token as a list."""
        return self._request("characters", access_token=token) if token else self._request("characters")

    def get_character_equipment(self, name, token=None):
        """Returns the equipment data for the character with the given name as a list for the current session token or the given token."""
        name =  requests.utils.quote(name)
        location = "characters/{}/equipment".format(name)
        return self._request(location, access_token=token) if token else self._request(location)

    def get_character_inventory(self, name, token=None):
        """Returns the inventory data for the character with the given name as a list for the current session token or the given token."""
        name =  requests.utils.quote(name)
        location = "characters/{}/inventory".format(name)
        return self._request(location, access_token=token) if token else self._request(location)

    def get_colors(self, *ids):
        """Returns the color data for the color(s) with the given id(s) as a list."""
        return self._request("colors", ids=','.join(str(id) for id in ids))

    def get_colors_ids(self):
        """Returns just all the color ids as a list."""
        return self._request("colors")

    def coins_to_gold(self, copper):
        """Returns the amount of gold, silver and copper in the given (positive) amount of coins as a dictionary."""
        gold = silver = 0
        copper = abs(copper)
        while copper >= 10000:
            gold += 1
            copper -= 10000
        while copper >= 100:
            silver += 1
            copper -= 100
        return {"gold": gold, "silver": silver, "copper": copper}

    def gold_to_coins(self, gold=0, silver=0, copper=0):
        """Returns the total amount of coins in the given dictionary of gold, silver and copper coins as an integer."""
        return sum([gold*10000, silver*100, copper])

    def get_commerce_profit(self, sell_price, buy_price=0):
        """Returns the profit of the item with the given sell price and optional cost if sold on the trading post
        as a dictionary including the profit, the transaction fee and the exchange fee.
        """
        listing_fee = max(round((sell_price / 100) * 5), 1)
        exchange_fee = max(round((sell_price / 100) * 10), 1)
        profit = sell_price - listing_fee - exchange_fee - buy_price
        return {"fee": listing_fee, "tax": exchange_fee, "profit": profit}

    def get_commerce_exchange(self):
        """Returns all accepted resources for the gem exchange as a list."""
        return self._request("commerce/exchange")

    def get_commerce_exchange_coins(self, amount):
        """Returns the current coins to gems exchange rate for the given amount of coins as a dictionary."""
        return self._request("commerce/exchange/coins", quantity=amount)

    def get_commerce_exchange_gems(self, amount):
        """Returns the current gems to coins exchange rate for the given amount of gems as a dictionary."""
        return self._request("commerce/exchange/gems", quantity=amount)

    def get_commerce_listings(self, *ids):
        """Returns the item trading post listing data for the item(s) with the given id(s) as a list.
           If a list if ids is not supplied, all listings will be returned.
        """
        if not ids:
            ids = self.get_commerce_listings_ids()
        else:
            ids = ids[0]
        
        if isinstance(ids, int):
            return self._request("commerce/listings", ids=str(ids))
        elif len(ids) <= 200:
            return self._request("commerce/listings", ids=','.join(str(id) for id in ids))
        else:
            return self._get_many("commerce/listings", ids)

    def get_commerce_listings_ids(self):
        """Returns just all the item ids of all the items on the trading post as a list."""
        return self._request("commerce/listings")

    def get_commerce_prices(self, *ids):
        """Returns the item trading post price data for the item(s) with the given id(s) as a list.
        Because of trading post regulations, you are unable to use the 'all' keyword for this endpoint.
        """
        if not ids:
            ids = self.get_commerce_prices_ids()
        else:
            ids = ids[0]
        
        if isinstance(ids, int):
            return self._request("commerce/prices", ids=str(ids))
        elif len(ids) <= 200:
            return self._request("commerce/prices", ids=','.join(str(id) for id in ids))
        else:
            return self._get_many("commerce/prices", ids)

    def get_commerce_prices_ids(self):
        """Returns just all the item ids of all the items on the trading post as a list."""
        return self._request("commerce/prices")

    def get_commerce_transactions_current_buys(self, token=None): # TODO: Add paging support!
        """Returns the current buying commerce transactions for the current session token or the given token."""
        return self._request("commerce/transactions/current/buys", access_token=token) if token else self._request("commerce/transactions/current/buys")

    def get_commerce_transactions_current_sells(self, token=None): # TODO: Add paging support!
        """Returns the current selling commerce transactions for the current session token or the given token.
        The API endpoint only supplies the commerce transaction history of the past 90 days.
        """
        return self._request("commerce/transactions/current/sells", access_token=token) if token else self._request("commerce/transactions/current/sells")

    def get_commerce_transactions_history_buys(self, token=None): # TODO: Add paging support!
        """Returns the buying commerce transaction history for the current session token or the given token.
        The API endpoint only supplies the commerce transaction history of the past 90 days.
        """
        return self._request("commerce/transactions/history/buys", access_token=token) if token else self._request("commerce/transactions/history/buys")

    def get_commerce_transactions_history_sells(self, token=None): # TODO: Add paging support!
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
        if not ids:
            ids = self.get_items_ids()
        else:
            ids = ids[0]
        
        if isinstance(ids,int):
            return self._request("items", ids=str(ids))
        elif len(ids) <= 200:
            return self._request("items", ids=','.join(str(id) for id in ids))
        else:
            return self._get_many("items", ids)

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

    def get_minis(self, *ids):
        """Returns the mini data for the mini(s) with the given id(s) as a list."""
        return self._request("minis", ids=','.join(str(id) for id in ids))

    def get_minis_ids(self):
        """Returns just all the mini ids as a list."""
        return self._request("minis")

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
        if not ids:
            ids = self.get_recipes_ids()
        else:
            ids = ids[0]
        
        if isinstance(ids, int):
            return self._request("recipes", ids=str(ids))
        elif len(ids) <= 200:
            return self._request("recipes", ids=','.join(str(id) for id in ids))
        else:
            return self._get_many("recipes", ids)

    def get_recipes_ids(self):
        """Returns just all the recipe ids as a list."""
        return self._request("recipes")

    def get_recipes_ids_by_input_ingredient(self, id):
        """Returns a list of recipes using the given input ingredient id."""
        return self._request("recipes/search", input=id)

    def get_recipes_ids_by_output_ingredient(self, id):
        """Returns a list of recipes using the given output ingredient id."""
        return self._request("recipes/search", output=id)

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
        return self.get_tokeninfo(key)

    def _get_many(self, endpoint, ids):
        """Send many requests to the Guild Wars 2 API and compile them into one result.
            Assumes that there are no duplicates in the ids list."""
        x = 0
        all_objects = []
        while x < len(ids)-200:
            batch_objects = self._request(endpoint, ids=','.join(str(id) for id in ids[x:x+200]))
            all_objects.extend(batch_objects)
            x = x+200
        
        batch_objects = self._request(endpoint, ids=','.join(str(id) for id in ids[x:len(ids)+1]))
        all_objects.extend(batch_objects)
        
        return all_objects


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
            except ValueError as e: # TODO: Throw exception if not authenticated instead of returning the endpoint error array.
                print(e)
                return [] # TODO: Throw custom API exception?
        except (requests.exceptions.HTTPError, requests.exceptions.Timeout, ConnectionError) as e:
            print(e)
            return [] # TODO: Throw custom API exception?