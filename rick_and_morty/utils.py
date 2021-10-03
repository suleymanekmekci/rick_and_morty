import requests



class APIAccess():

    def __init__(self,episode):
        self.episode = episode
        super().__init__()

    
    def get_current_episode(self):
        r = requests.get("https://rickandmortyapi.com/api/episode/{}".format(self.episode))
        if r.status_code == 404:
            return None
        location_list = []
        r = r.json()
        
        characters = r['characters']

        character_list = self.__get_character(characters)

        r['characters'] = character_list
        del r['url']
        
        return r

    
    def __get_character(self,character_url_list):
        output = []
        for character_url in character_url_list:
            r = requests.get(character_url)
            r = r.json()
            del r['episode']
            del r['url']
            del r['id']
            

            origin_location_url = r['origin']['url']
            last_known_location_url = r['location']['url']

    

            if r['origin']['name'] != 'unknown':
                origin_location = self.__get_location(origin_location_url)
                del origin_location['residents']
                del origin_location['id']
            else:
                origin_location = r['origin']
            
            if r['location']['name'] != 'unknown':
                last_known_location = self.__get_location(last_known_location_url)
                del last_known_location['residents']
                del last_known_location['id']


            else:
                last_known_location = r['location']

            del origin_location['url']
            del last_known_location['url']
            r['origin'] = origin_location
            r['location'] = last_known_location

            output.append(r)
        return output



    def __get_location(self,location_url):
        r = requests.get(location_url)

        return r.json()