import json

class Chips:
    def __init__(self, locale):
        self.Refresh(locale)
    
    def GetAutocompleteNames(self):
        uniqueNames = []
        for val in self.chips:
            if(val["Name"] not in uniqueNames):
                uniqueNames.append(val["Name"]) 
        
        return uniqueNames

    def Refresh(self, locale):
        self.chips = []
        self.uniqueNames = []
        self.autocompleteNames = []
        try:
            print(f"Getting Chips for {locale}...")
            f = open(f'./chips/{locale}.json', encoding='utf-8-sig')
            jsonCards = json.load(f)
            
            self.chips = jsonCards
            self.autocompleteNames = self.GetAutocompleteNames()
            print(f"Gathered Chips for {locale}!")
            f.close()
        except Exception as e:
            self.chips = []
            print(f"Failed to get Chips for {locale}! Exception: {e}")