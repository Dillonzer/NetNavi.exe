import json

class ProgramAdvance:
    def __init__(self, locale):
        self.Refresh(locale)
    
    def GetAutocompleteNames(self):
        uniqueNames = []
        for val in self.pa:
            if(val["Name"] not in uniqueNames):
                uniqueNames.append(val["Name"]) 
        
        return uniqueNames

    def Refresh(self, locale):
        self.pa = []
        self.uniqueNames = []
        self.autocompleteNames = []
        try:
            print(f"Getting Chips for {locale}...")
            f = open(f'./chips/{locale}.json', encoding='utf-8-sig')
            jsonCards = json.load(f) 

            for data in jsonCards:
                if(data['Category'] == 'Program Advance'):
                    self.pa.append(data)

            self.autocompleteNames = self.GetAutocompleteNames()
            print(f"Gathered PA for {locale}!")
            f.close()
        except Exception as e:
            self.pa = []
            print(f"Failed to get PA for {locale}! Exception: {e}")