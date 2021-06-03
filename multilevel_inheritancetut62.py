class dad:
    basketball=1
class son(dad):
    dance=1
    basketball = 5
    def isdance(self):
        return f'yes i dance {self.dance} no. of times'
class grandson(son):
    dance=6
    def isdance(self):
        return f'yes i dance very well {self.dance} no. of times'

bapu=dad()
munda=son()
pota=grandson()
print(pota.isdance())  # it will not display the isdance in son class
#it will display it if it is not present in the grandson class
print(pota.basketball)  # this will display the basket ball number of son class
# because it doesn't need to go on top because the grandson class find basketball in
#son class if it is not present there than it will look for it in father class


#### exercise make a multilevel inheritance on
#electronic gadget
#pocket gadget
#phone

class electronic_gadget:
    development=5
    def type_of_gadget(self):
        print(f'radio,television')
class pocket_gadget(electronic_gadget):
    development = 7
    def type_of_gadget(self):
        print(f'the ipod,calculator')
class phone(electronic_gadget):
    development = 9
    def type_of_gadget(self):
        print('the mobile phones')

gadget=phone()
gadget.type_of_gadget()
print(gadget.development)