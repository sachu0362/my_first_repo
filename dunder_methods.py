class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name':'Sarchin',
            'has_pets' : True
        }
    # def __str__(self):
    #     return f'{self.color}'
    def __len__(self):
        return 1000
    def __call__(self):
        return('Yessss')
    def __getitem__(self, item):
        return self.my_dict[item]


action_figure = Toy('Red',2)
print(action_figure.__getitem__('name'))
