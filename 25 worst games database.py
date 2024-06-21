'''Dylan wiliiams game database application'''

import sqlite3


DATABASE = "database.db"

#to use go back on studio related things this needs to be defined (go to 160 if you want to see)
second_qestion_b = ""

#making it cohen proof
while True:

    #getting user input first qestion
    print("These are the 25 worst games acording to meta critic")
    print("what would you like to view?")
    print("1 for games and other things")
    print("2 for just studio related things")
    print("end to leave")
    first_qestion = input()




    #user want game and other things
    while True:
        if first_qestion == "1":

            # asking more qestions for second qestion a
            print("What would you like to see?")
            print("1 games best to worst")
            print("2 games worst to best")
            print("3 game and genre only")
            print("4 game and rating asc only")
            print("5 game and rating desc only")
            print("6 game and release date ascending only")
            print("7 game and release date descending only")
            print("8 game and studio only")
            print("back to go back")
            second_qestion_a = input("")

            #cheking if user picked relevent number
            if second_qestion_a == "1":
                def print_all_games_best_to_worst():
                    '''print all the games nicely best to worst'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT  game_name, studio_name, game_rating, game_creation, game_genre FROM Game ORDER BY game_id asc;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Game name                                     Studio name                                                                                    Rating  Release date   Genre")
                        for game in results:
                            print(f"{game[0]:<46}{game[1]:<95}{game[2]:<8}{game[3]:<15}{game[4]:<6}")

                print_all_games_best_to_worst()

            #cheking if user picked relevent number
            if second_qestion_a == "2":
                def print_all_games_worst_to_best():
                    '''print all the games nicely worst to best'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT  game_name, studio_name, game_rating, game_creation, game_genre FROM Game ORDER BY game_id desc;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Game name                                     Studio name                                                                                    Rating  Release date   Genre")
                        for game in results:
                            print(f"{game[0]:<46}{game[1]:<95}{game[2]:<8}{game[3]:<15}{game[4]:<6}")

                print_all_games_worst_to_best()

            #cheking if user picked relevent number
            if second_qestion_a == "3":
                def print_all_games_and_genre():
                    '''print all the games and genra only and nicely'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT game_name, game_genre FROM Game;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Game name                                     Genre")
                        for game in results:
                            print(f"{game[0]:<46}{game[1]:<}")

                print_all_games_and_genre()

            #cheking if user picked relevent number
            if second_qestion_a == "4":
                def print_all_games_and_rating_asc():
                    '''print all the games and rating only ascending and nicely'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT game_name, game_rating FROM Game ORDER BY game_id asc;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Game name                                     rating")
                        for game in results:
                            print(f"{game[0]:<46}{game[1]:<}")

                print_all_games_and_rating_asc()
                
            #cheking if user picked relevent number
            if second_qestion_a == "5":
                def print_all_games_and_rating_desc():
                    '''print all the games and rating only descending and nicely'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT game_name, game_rating FROM Game ORDER BY game_id desc;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Game name                                     rating")
                        for game in results:
                            print(f"{game[0]:<46}{game[1]:<}")

                print_all_games_and_rating_desc()

            #cheking if user picked relevent number
            if second_qestion_a == "6":
                def print_all_games_and_release_date_asc():
                    '''print all the games and release date only ascending and nicely'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT game_name, game_creation FROM Game ORDER BY game_creation asc;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Game name                                     release date")
                        for game in results:
                            print(f"{game[0]:<46}{game[1]:<}")

                print_all_games_and_release_date_asc()

            #cheking if user picked relevent number
            if second_qestion_a == "7":
                def print_all_games_and_release_date_desc():
                    '''print all the games and release date only descending and nicely'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT game_name, game_creation FROM Game ORDER BY game_creation desc;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Game name                                     release date")
                        for game in results:
                            print(f"{game[0]:<46}{game[1]:<}")

                print_all_games_and_release_date_desc()

            #cheking if user picked relevent number
            if second_qestion_a == "8":
                def print_all_games_and_studio():
                    '''print all the studio and game only and nicely'''
                    with sqlite3.connect(DATABASE) as db:
                        cursor = db.cursor()
                        sql = "SELECT studio_name, game_name FROM Game;"
                        cursor.execute(sql)
                        results = cursor.fetchall()
                        print(f"Studio name                                                                                    Game name")
                        for game in results:
                            print(f"{game[0]:<95}{game[1]:<}")

                print_all_games_and_studio()

            #to go back
            if second_qestion_a == "back":
                    break

        #When back is used it still in a while true loop so I need to break both loops
        #If break when it sees back then it can never be used again so I set it to "" so it skips over this
        if second_qestion_b == "back":
             second_qestion_b = ""
             break

        # user wants studio related things
        while True:
            if first_qestion == "2":

                # asking more qestions for second qestion b
                print("What would you like to see?")
                print("1 studio names only")
                print("2 studio names and rating from game asc only")
                print("3 studio names and rating from game desc only")
                print("4 studio and game only")
                print("back to go back")
                second_qestion_b = input("")

                #cheking if user picked relevent number
                if second_qestion_b == "1":
                    def print_all_Studios_names():
                        '''print all the studio names nicely'''
                        with sqlite3.connect(DATABASE) as db:
                            cursor = db.cursor()
                            sql = "SELECT studio_name FROM Game;"
                            cursor.execute(sql)
                            results = cursor.fetchall()
                            print(f"Studio name")
                            for game in results:
                                print(f"{game[0]:<}")
                            


                    print_all_Studios_names()

                #cheking if user picked relevent number
                if second_qestion_b == "2":
                    def print_all_Studios_and_rating_asc():
                            '''print all the studio names and rating ascending nicely'''
                            with sqlite3.connect(DATABASE) as db:
                                cursor = db.cursor()
                                sql = "SELECT studio_name, game_rating FROM Game Order by game_id asc;"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                print(f"Studio name                                                                                    Game rating")
                                for game in results:
                                    print(f"{game[0]:<95}{game[1]:<}")
                                


                    print_all_Studios_and_rating_asc()
                    
                #cheking if user picked relevent number
                if second_qestion_b == "3":
                    def print_all_Studios_and_rating_desc():
                            '''print all the studio names and rating descending nicely'''
                            with sqlite3.connect(DATABASE) as db:
                                cursor = db.cursor()
                                sql = "SELECT studio_name, game_rating FROM Game Order by game_id desc;"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                print(f"Studio name                                                                                    Game rating")
                                for game in results:
                                    print(f"{game[0]:<95}{game[1]:<}")
                                


                    print_all_Studios_and_rating_desc()

                #cheking if user picked relevent number
                if second_qestion_b == "4":
                    def print_all_studio_and_game():
                                '''print all the studio and games only and nicely'''
                                with sqlite3.connect(DATABASE) as db:
                                    cursor = db.cursor()
                                    sql = "SELECT studio_name, game_name FROM Game;"
                                    cursor.execute(sql)
                                    results = cursor.fetchall()
                                    print(f"Studio name                                                                                    Game name")
                                    for game in results:
                                        print(f"{game[0]:<95}{game[1]:<}")

                    print_all_studio_and_game()

                #to go back2
                if second_qestion_b == "back":
                    break
            
            #If invalide button was presed
            else:
                print("That was not an option")
    
    #To end the code or programe
    if first_qestion == "end":
                    break

