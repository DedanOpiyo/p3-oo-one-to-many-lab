class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name 
        self.set_pet_type(pet_type) # or for setter and getter: # self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)

    def set_pet_type(self, pet_type):
        if pet_type not in self.__class__.PET_TYPES: # using self.__class__. instead of Pet. ...for inheritance/polymophism considerations
            raise ValueError("invalid pet type")
        
        self.pet_type = pet_type
    
    # # Alternativ with setter and getter...
    # @property
    # def pet_type(self):
    #     return self._pet_type

    # @pet_type.setter
    # def pet_type(self, pet_type):
    #     if pet_type not in self.PET_TYPES:
    #         raise Exception('Not a valid pet type.')
    #     self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner
        
    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner)or not owner):
            raise TypeError("owner must be an instance of Owner class")
        self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
       return sorted(self.pets(), key = lambda pet: pet.name)
