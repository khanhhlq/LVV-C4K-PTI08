# Lớp đối tượng có sẵn 

class Homework: 
    def __init__(self, name, priority, completed=False): 

        self.name = name 

        self.priority = priority 

        self.completed = completed 

# Lớp quản lý 

class HomeworkList: 
    def __init__(self): 
        self.items = [] 

    def add_item(self, item): 
        self.items.append(item) 

    def all_completed(self): 
        completed = True 
        for item in self.items: 
            if item.completed == False: 
                completed = False 
                print(item.name) 
            if completed: 
                print("All finished!") 
                
hw_list = HomeworkList() 

hw_list.add_item(Homework("Lập trình App Producer", 3)) 

hw_list.add_item(Homework("Làm văn", 2, True)) 

hw_list.add_item(Homework("Lập trình GameMaker", 3)) 

hw_list.all_completed() 