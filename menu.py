from option import *
from utils import *

class Menu(Option):
    
    def __init__(self,titre='Menu principale',options=list):
        Option.__init__(self,libelle=titre,exe=object())
        self.pagination = f'/  {self.libelle} '
        self.options = {k+1:v for k,v in enumerate(options)}
        
    def affiche_menu(self,page=''):
        system('cls')
        print("\n\n\n")
        print("=".center(120,'='))
        print("[ Ecrit par >++> Designer_#@rt_242 (~_~) ]".center(100,"$"))
        print('\n\t\t ',page,self.pagination,
              '\n\t\t','_-'*int((len(self.pagination+page)/2)),
              '\n'
              )
        for num,opt in self.options.items():
            opt.format_option(num)
        if len(page) == 0:
            print("\t|  0 - )  Quitter \n")
        else:
            print("\t|  0 - )  Retour  \n")
        
    
    def __choisit_option(self,page=''):
        try :
            choix = input("\t Entrer votre choix > ").strip()
            if len(choix) == 0:
                print('\n\t Aucune option selectionnée :( ...' )
                sleep(1.20)
                chargement(message='Redirection vers le menu ...',tour=1)
                system('cls')
                return
            choix = int(choix)
        except KeyboardInterrupt:
            confirme_sortit = input(" Tentative d'interruption d'urgence, veuillez confirmer [yes/no] > ").lower()
            if confirme_sortit in ['yes','y','oui']:
                system('cls')
                chargement(message="Sortit d'urgence en cours ...")
                system('cls')
                return 0
            else:
                print("\n Tentative de sortit annuler ! ")
                sleep(1)
                chargement(message='Redirection vers le menu ')
                system('cls')
                return  
        except ValueError:
            print('\n Choix incorrect !')
            sleep(1.20)
            chargement(message='Redirection vers le menu ...')
            system('cls')
            return
        except Exception :
            print('\n Une erreur inconnue est survenue :( !!!!!!')
            sleep(1.20)
            chargement(message='Redirection vers le menu ...')
            sleep(0.30)
            system('cls')
            return
        else: #--------------------------------------------------------------------------------Si aucun platage ne survient dans la saisit du choix ! Alors 
            if choix == 0:
                chargement(message='Sortit du menu :) !...') #-------------------------------------Si l'utilisateur quitte le menu ! 
                system('cls')
                return 0 
            elif choix not in self.options.keys(): #---------------------------------------------Si le numero d'option n'est pas present dans la liste ! 
                print('\n Option inexisitante ! veuillez selectioner une option presente dans le menu !')
                sleep(1.20)
                chargement(message='Redirection vers le menu ...')
                sleep(0.30)
                system('cls')
            else :
                for num,opt in self.options.items():#------------------------------------------l'utilisateur entre un numero d'option valide alors on execute l'option correspondante 
                    if choix == num :
                        opt.run(page+" "+self.pagination)
    
    def run(self,page='',choix=0):
        chargement(tour=3)
        while 1 : 
            self.affiche_menu(page)
            if self.__choisit_option(page) == 0:
                break           
  