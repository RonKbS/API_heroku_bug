from datetime import datetime


'''Note that user model has not been included
which will enable more distinguishing between
several users'''



class Diary:
    entry_id = 1
    entries = []

    @staticmethod
    def add_entry(enter_content):
        '''create empty entry if entry has been used before'''
        entry = {}
        date = datetime.now()
        content = enter_content
        new_entry = {
            "date": date.strftime('%A.%B.%Y'),
            "content": content,
            "ID": Diary.entry_id
        }
        for entry in Diary.entries:
            if Diary.entries == []:
                Diary.entries.append(new_entry)
                return entry
            elif new_entry["content"] == entry["content"]:
                return "New entry is similar to older entry"
            else:
                entry["ID"] = entry["ID"] + 1
        Diary.entries.append(new_entry)
        return new_entry

    @staticmethod
    def find_entry_by_id(entry_id):
        for entry in Diary.entries:
            if entry_id == entry["ID"]:
                return entry
        return 'No such entry'

    
    
    @staticmethod
    def modify_entry(entry_id, content):
        for entry in Diary.entries:
            if entry_id == entry["ID"]:
                entry["content"] = content
                return entry
        return 'No such entry'

    @staticmethod
    def delete_entry(entry_id):
        for entry in Diary.entries:
            if entry_id == entry['ID']:
                Diary.entries.remove(entry)
                return "Entry deleted"
        return 'No such entry'

    @staticmethod
    def list_all_entries():
        if Diary.entries != []:
            return Diary.entries
        return 'No entries'
