from menu import *

if __name__ == "__main__":
    try:
        choix = int(input('\n\t Voulez vous voir une demo du module (y/n) ? '))
    except Exception as e:
        print(" Choix incorrect :( ")
        exit(e.with_traceback)
    else: 
        if choix in ['y','Y','oui','yes']:
            def HelloWord():
                print(" Bonjour tout le monde :) !... ")
    
            def GoodBye():
                print(" Aurevoir tout le monde :) !... ")

            def Moonlight():
                print(" Au clair de la lune :) !... ")
    
            option1 = Option("Hello",HelloWord)
            option2 = Option('Bye',GoodBye)
            option3 = Option(exe=Moonlight)

            sub_menu1 = Menu(
                    titre='sub_sub 1',
                    options=[option1,option2]
                )

            menu1 = Menu(
                    titre='sub menu 1',
                    options=[option1,option2,option3,sub_menu1]
                )

            menu2 = Menu(
                    titre='sub menu 2',
                    options=[option1,option2,option3,sub_menu1]
                )

            menu3 = Menu(
                        titre='sub menu 3',
                        options=[option1,option2,option3]
                    )

            main_menu = Menu(
                            titre='Menu principale',
                            options=[
                                    menu1,menu2,menu3
                                    ]
                            )

            super_menu = Menu(
                options=[
                        Menu(
                            titre="Envoie d'argent",
                            options=[
                                    Menu(
                                        titre="Abonné",
                                        options=[option1,option2]
                                        ),
                                    Menu(
                                        titre="Non abonné",
                                        options=[option1,option2]
                                        )   
                                    ]
                            ),
                    
                        Menu(
                            titre='Payement des facture',
                            options=[
                                    Menu(
                                        titre='Facture E2C',
                                        options=[option1]
                                        ),
                                    Menu(
                                        titre="Facture LCDE",
                                        options=[option1,option2]
                                        )
                                    ]
                            ),
                        
                        Menu(
                            titre="Achat credit et forfait",
                            options=[
                                    Menu(
                                        titre="Pour soi meme",
                                        options=[
                                                Menu(
                                                    titre="Forfait voix",
                                                    options=[
                                                            Menu(
                                                                titre='Forfait 1 jour',
                                                                options=[
                                                                        Option(libelle="4 min",exe=HelloWord),
                                                                        Option(libelle="14 min",exe=Moonlight),
                                                                        Option(libelle="17 min",exe=GoodBye)
                                                                        ]
                                                                ),
                                                            Menu(
                                                                titre='Forfait 7 jours',
                                                                options=[
                                                                        Option(libelle="27 mi",exe=Moonlight),
                                                                        Option(libelle="45 min",exe=GoodBye),
                                                                        Option(libelle="95 min",exe=GoodBye)
                                                                        ]
                                                                ),
                                                            Menu(
                                                                titre='Forfait 30 jours',
                                                                options=[
                                                                        Option(libelle="105 min",exe=HelloWord)
                                                                        ]
                                                                )
                                                            ]
                                                    ),
                                                
                                                Menu(
                                                    titre='Forfait sms',
                                                    options=[
                                                            Option(libelle="100 sms",exe=Moonlight)
                                                            ]
                                                    ),
                                                
                                                Menu(
                                                    titre="Forfait internet",
                                                    options=[
                                                            option1,
                                                            option2
                                                            ]
                                                    )
                                                ]
                                        ),    
                                    ]
                            ),
                        Menu(
                            titre="Epargne et credit",
                            options=[option1]
                            ),
                        Menu(
                            titre="Mon compte",
                            options=[option2]
                            ),
                        Menu(
                            titre="Momopay",
                            options=[option3]
                            ),
                        Menu(
                            titre="Banque",
                            options=[option3]
                            ),
                        Menu(
                            titre="GIMAC-PAY",
                            options=[option1]
                            )
                        ]
                )

            super_menu.run()

        else:
            print("Bye")
            



