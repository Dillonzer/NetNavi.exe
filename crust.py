import json

class Crust:
    def __init__(self, locale):
        self.Refresh(locale)
    
    def GetAutocompleteNames(self):
        uniqueNames = []
        for val in self.crust:
            if(val["Part"] not in uniqueNames):
                uniqueNames.append(val["Part"]) 
        
        return uniqueNames

    def Refresh(self, locale):
        self.crust = []
        self.uniqueNames = []
        self.autocompleteNames = []
        try:
            print(f"Getting Crust for {locale}...")
            f = open(f'./cust/{locale}-crust.json', encoding='utf-8')
            jsonCards = json.load(f)
            
            self.crust = jsonCards
            self.autocompleteNames = self.GetAutocompleteNames()
            print(f"Gathered Crust for {locale}!")
            f.close()
        except Exception as e:
            self.crust = []
            print(f"Failed to get Crust for {locale}! Exception: {e}")