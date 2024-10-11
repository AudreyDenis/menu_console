class Option: #-------------------------------------------------------------Chaque element du menu est une option, une option peut etre un menu ou une fonction 
    
    num_opt = 0 
    def __init__(self,libelle='Option',exe=object):
        Option.num_opt += 1
        self.num = Option.num_opt
        if libelle == 'Option' :
            self.libelle = f"{libelle} {self.num}"
        else:
            self.libelle = libelle
        self.__exe = exe
        self.pagination = f'> {self.libelle} '
        
    def format_option(self,num=0):
        print(f"\t|  {num} - )  {self.libelle}")
    
    def run(self,page=''):
        system('cls')
        print('\n',page,self.pagination,'\n','_-'*int((len(self.pagination+page)/2)),'\n')
        self.__exe()
        sleep(1)
        print('')
