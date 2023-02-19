import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
          
                      
                   
         
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city= input('which city are you looking for?')
    while city not in (CITY_DATA.keys()):    
        print("sorry invalid city")
        city= input('which city are you looking for?').lower()
    check=input("would you like to filter data by month,day,both,or none ?")
    
    while check not in ["month","day","both","none"]:    
        print("sorry wrong information")
        check=input("would you like to filter data by month,day,both,or none ?").lower()
      
    months=["january","february","march","april","may","june"]
    if check=="month" or check=="both":    
         month= input('which month are you looking for?').lower()
         while month not in months:    
             print("sorry we have no information about this month")
             month= input('which month are you looking for?').lower()
    else:    
        month="all"
        
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    if check=="day" or check=="both":    
        day=input('which day are you looking for?').title()
        while day not in days:    
            print("sorry you enterd the wrong day")
            day=input('which day are you looking for?').title()
    else:    
        day="all"
        
   
    
    


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df =  pd.read_csv(CITY_DATA[city])
    df['Start Time'] =pd.to_datetime(df['Start Time']) 

    
    df['month'] =df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.day_name()


    
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =months.index(month)+1 
    
     
        df = df[df['month']==month]

    
    if day != 'all':
        
        df =df[df['day_of_week']==day.title()]

    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time() 
    df['Start Time'] =pd.to_datetime(df['Start Time']) 
    df['month'] =df['Start Time'].dt.month 
    print(f'popular_month is {df["month"].mode()[0]}')
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    print(f'popular_day_of_week is {df["day_of_week"].mode()[0]}')
    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    print(f'popular_hour is {df["hour"].mode()[0]}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f'popular_start_station is { df["Start Station"].mode()[0]}')

    # TO DO: display most commonly used end station
    print(f'popular_end_station is { df["End Station"].mode()[0]}')

    
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip=df['Start Station'] + 'to' + df['End Station']
    print(f'the popular_start_end_station is {popular_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f'the Total_travel_time is {df["Trip Duration"].sum()}')
    
    # TO DO: display mean travel time
    print(f' the average_travel_time is {df["Trip Duration"].mean()}')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
  

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print (f'User_Tybe_counts is {df["User Type"].value_counts()}')

    # TO DO: Display counts of gender
    if 'Gender' in(df.columns):
        print(f'Gender_counts is {df["Gender"].value_counts()}')
        

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        year=df['Birth Year']
    
        print(f'first_year is {year.min()}')
        
        print(f'the most_recent_year is {year.max()}') 
        
        print (f' the most_common_year is {year.mode()}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """Displays 5 rows as a sample of the DataFrame"""
    view_data=input('Would you like to view 5 rows of individual trip data ? Enter yes or no/')
    if view_data.lower()=='yes':                
        raws=0
        while True:    
            print(df.iloc[raws:raws+5])
            raws += 5
            another_question=input('do you wish to continue?: ').lower()
            if another_question.lower() != 'yes':    
                    break
                        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
