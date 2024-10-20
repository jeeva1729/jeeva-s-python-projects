class todolist:
    def __init__(self):
        self.task_list=[]
    def add_task(self, task):
        self.task_list.append(task)
        print(f'{task} is added to the list')
    def view_task(self):
        if not self.task_list:
            print('Empty List')
        else:
            for i, task in enumerate(self.task_list, start=1):
                print(f'{i}.{task}')
    def remove_task(self, task_no):
        if 0<task_no<=len(self.task_list):
            removed_task=self.task_list.pop(task_no-1)
            print(f'{removed_task} is removed from the list')
        else:
            print('Invalid Task Number')
def main():
    obj=todolist()
    while True:
        print('Menu:')
        print('1. Add List')
        print('2. View List')
        print('3. Remove List')
        print('4. Exit')
        choice=input('Enter a value between 1 to 4:')
        if choice=='1':
            task=input('Enter a task:')
            obj.add_task(task)
        elif choice=='2':
            obj.view_task()
        elif choice=='3':
            task_no=int(input('Enter a task number that you want to remove:'))
            obj.remove_task(task_no)
        elif choice=='4':
            print('Exiting the Application')
            break
        else:
            print('Invalid input. Please try again')
if __name__=='__main__':
    main()
    
