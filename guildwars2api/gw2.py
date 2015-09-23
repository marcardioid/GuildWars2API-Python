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
        self.session.headers.update({"User-Agent": "TEST GW2API WRAPPER FOR PYTHON 3.5", "Accept": "application/json"})

    def get_material(self, *ids):
        """Returns the material data for the material(s) with the given id(s) as a list."""
        return self._request("materials", ids=','.join(str(id) for id in ids))

    def get_materials_ids(self):
        """Returns just all the material ids as a list."""
        return self._request("materials")

    def get_pvp_game(self, *ids, token=None):
        """Returns the pvp game data for the pvp game(s) with the given id(s) as a list.
        The API endpoint only supplies the 10 lates games at most.
        """
        matches = ','.join(str(id) for id in ids)
        return self._request("pvp/games", access_token=token, ids=matches) if token else self._request("pvp/games", ids=matches)

    def get_pvp_games_ids(self, token=None):
        """Returns just all the pvp game ids as a list.
        The API endpoint only supplies the 10 lates games at most.
        """
        return self._request("pvp/games", access_token=token) if token else self._request("pvp/games")

    def get_pvp_stats(self, token=None):
        """Returns the pvp stats for the current session token or the given token."""
        return self._request("pvp/stats", access_token=token) if token else self._request("pvp/stats")

    def get_quaggan(self, *ids):
        """Returns the quaggan data for the quaggan(s) with the given id(s) as a list."""
        return self._request("quaggans", ids=','.join(str(id) for id in ids))

    def get_quaggans_ids(self):
        """Returns just all the quaggan ids as a list."""
        return self._request("quaggans")

    def get_recipe(self, *ids):
        """Returns the recipe data for the recipe(s) with the given id(s) as a list."""
        return self._request("recipes", ids=','.join(str(id) for id in ids))

    def get_recipes_ids(self):
        """Returns just all the recipe ids as a list."""
        return self._request("recipes")

    def get_recipes_ids_by_ingredient(self, lookup, id):
        """Returns a list of recipes using the given ingredient. Searchable by input and output ingredient."""
        if lookup == "input":
            return self._request("recipes/search", input=id)
        elif lookup == "output":
            return self._request("recipes/search", output=id)
        else:
            return [] # TODO: Raise API exception!

    def get_skin(self, *ids):
        """Returns the skin data for the skin(s) with the given id(s) as a list."""
        return self._request("skins", ids=','.join(str(id) for id in ids))

    def get_skins_ids(self):
        """Returns just all the skin ids as a list."""
        return self._request("skins")

    def get_specialization(self, *ids):
        """Returns the specialization data for the specialization(s) with the given id(s) as a list."""
        return self._request("specializations", ids=','.join(str(id) for id in ids))

    def get_specialization_ids(self):
        """Returns just all the specialization ids as a list."""
        return self._request("specializations")

    def get_tokeninfo(self, token=None):
        """Returns the tokeninfo for the current session token or the given token."""
        return self._request("tokeninfo", access_token=token) if token else self._request("tokeninfo")

    def get_trait(self, *ids):
        """Returns the trait data for the trait(s) with the given id(s) as a list."""
        return self._request("traits", ids=','.join(str(id) for id in ids))

    def get_traits_ids(self):
        """Returns just all the trait ids as a list."""
        return self._request("traits")

    def get_world(self, *ids):
        """Returns the world data for the world(s) with the given id(s) as a list."""
        return self._request("worlds", ids=','.join(str(id) for id in ids))

    def get_worlds(self):
        """Returns all the world data as a list."""
        return self._request("worlds", ids="all") # TODO: This also works by calling get_world("all"). Merge functions?

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
        version = "v2" if location in self.API_ENDPOINTS_V2 else "v1"
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