from record import *

class Artist:
    
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
    def get_records(self):
        return [record for record in Record.get_all() if record.get_artist()==self]
    
    def get_first_record(self):
        records=self.get_records()
        min_record=records[0]
        for i in range(1,len(records)):
            if(records[i].get_year()<min_record.get_year()):
                min_record=records[i]
        return min_record