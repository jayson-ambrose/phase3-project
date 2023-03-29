import click
from lib.db.models import (Sighting, Truther, Base)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///encounter_counter.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu_text():
    print('''
            [report  (r)]  : Report a UFO or UAP sighting. (requires login)
            [profile (p)]  : Create a profile/login. 
            [search  (s)]  : Search the Encounter Counter database.
            [quit    (q)]  : Exit Encounter Counter.
        ''')

def main_menu ():

    choice = ""
    main_menu_text()
    while choice != 'quit' and choice != 'q':        

        if (choice == 'r') or (choice == 'report'):
            report_sighting()
        if (choice == 'p') or (choice == 'profile'):
            profile()
        if (choice == 's') or (choice == 'search'):
            search()

        choice = click.prompt("Enter selection")

def check_location_valid(string):
    #these functions will be used to verify form input so that it matches the rest of the DB to avoid errors.
    pass

def check_time_valid(string):
    pass

def check_date_valid(string):
    pass

def check_encounter_type_valid(string):
    pass

def check_summary_valid(string):
    pass

def check_ufo_shape_valid(string):
    pass

def current_user_check(username):
    current_user = session.query(Truther).filter(Truther.username == username)
    for row in current_user:
        print(row.id)
    return isinstance(current_user, Truther)
    #return session.query(Truther).filter(Truther.username == username) 

def report_sighting():

    click.echo("UFO OR UAP ENCOUNTER REPORT")

    choice = ""
    while (choice != "N") and (choice !="n"):

        if (choice == 'Y') or (choice == 'y'):

            click.echo("Please fill out the following form... \n")

            input_location = None
            input_time = None
            input_date = None
            input_duration = None
            input_encounter_type = None
            input_summary = None
            input_ufo_shape = None

            #while(check_location_valid(input_location) == False):
            input_location = click.prompt("Where did the event occur? (City, ST)", type=str)

            input_time = click.prompt("What time did the event occur? (24-hr clock time)", type=str)
            input_date = click.prompt("What was the date? (YYYY-MM-DD)", type=str)
            input_duration = click.prompt("For how long did the event continue? (sec)", type=int)
            input_encounter_type = click.prompt("What type of encounter did you experience? (sighting, greeting, abduction)", type=str)
            input_summary = click.prompt("Please enter a brief description of the event", type=str)
            input_ufo_shape = click.prompt("What shape was the object?", type=str)

            print(f'''
            ENTERED VALUES:
            ----------------------------------------------
                Location:          ->  {input_location}
                Time (HH:MM):      ->  {input_time}
                Date (YYYY-MM-DD:  ->  {input_date}
                Duration (MM:SS):  ->  {input_duration}
                Encounter Type:    ->  {input_encounter_type}
                Summary:           ->  {input_summary}
                Object Shape:      ->  {input_ufo_shape}
            ----------------------------------------------
            ''')
            
            # commented out db persistence to work on error handling
            event = Sighting(location=input_location,
                             time=input_time,
                             date= input_date,
                             duration=input_duration,
                             encounter_type=input_encounter_type,
                             summary=input_summary,
                             ufo_shape=input_ufo_shape)
            
            session.add(event)
            session.commit()

        choice = click.prompt("Report Encounter? (Y/N)")
        print('Returning to main menu.')
        main_menu_text()

def profile():
    click.echo("....................................")
    choice = ""
    while (choice != 'Q') or (choice != 'q'):
        if (choice == 'Y') or (choice == 'y'):
            click.echo("A new Truther! Initiating a profile...")

            input_username = click.prompt("Select your username", type=str)
            input_base_location = click.prompt("Please enter your base location", type=str)

            print(f'''
                PROFILE SAVED:
                ----------------------------------------------
                    Username:          ->  {input_username}
                    Base Location:     ->  {input_base_location}
                ----------------------------------------------
                ''')
            # new_truther = Truther(username = input_username, 
            #                     base_location = input_base_location)
            # session.add(new_truther)
            # session.commit()

        elif choice.upper() == "N":
            input_username = click.prompt("Please enter your username to login", type=str)
            current_user_check(input_username)
            click.prompt(f"Welcome back, {input_username}, would you like to report an encounter? (Y/N)", type=str)
            report_sighting() if choice.upper() == Y else main_menu_text()
            

        
        elif choice.upper() == "Q":
            click.echo('Returning to main menu...')
            main_menu_text()
        
        choice = click.prompt("Welcome! Are you new here? (Y/N)")
           


def search():
    # last_encounter = session.query(Sighting).first()
    # locations = session.query(Sighting.location)
    # by_date = session.query(Sighting).order_by(Sighting.date)
    # query = session.query(Sighting).filter(Sighting.id == "1").all()

    click.echo('What records are you looking for?')
    # click.echo(last_encounter)
    click.prompt('''
            [Date     (1)]  : View by date
            [Location (2)]  : View by location
            [UFO      (3)]  : View by UFO type
            [Encounter(4)]  : View by encounter type
            [Recent   (5)]  : Find most recently reported sighting
            [Common   (6)]  : Find most commonly reported UFO
            [Truthiest(7)]  : Find Truther with most encounters
    ''')
    
   

    
    