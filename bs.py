import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv'}
    
months = ['January', 'February', 'March',
         'April', 'May','June','All']
    
day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday','Saturday','All']

from collections import Counter

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        else:
           prompt == 'no'
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # get user input for city (chicago, new york city, washington)
    
    print("Would you like to see data for Chicago, New York, or Washington?")
    while True:
        city = input("Enter city: ")
        print('\n')
        if city in CITY_DATA:
            break
        else:
            print("We're only exploring bikeshare data in Chicago, New York, or Washington")
            continue

# get user input for month (january, february, ... , june)
    print('Which month? January, February, March, April, May, June, or All?')
    while True:
        month = input('Enter month: ')
        print('\n')
        if month in months:
            break
        if month == 'All':
            break
        else:
            print('Please select January, February, March, April, May, June, or All')
            continue

    # get user input for day of week (monday, tuesday, ... sunday)
    
    print('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All?')
    while True:
        day = input('Enter day: ')
        print('\n')
        if day in day_of_week:
            break
        if day == 'All':
            break
        else:
            print('Please select Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All.')
            continue
            
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
    
    df = pd.read_csv(CITY_DATA[city])
        
    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'All':
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    
    # display the most common month    
    df['month_name'] = df['Start Time'].dt.month
    month = df['month_name'].tolist()
    if len(set(month)) == 1:
        pass
    else:
        c = Counter(month)
        k = c.most_common()
        kc = k[0][0]
        
        if kc == 1:
            print('Most common month...')
            print('Common month: January\n')
        elif kc == 2:
            print('Most common month...')
            print('Common month: February\n')
        elif kc == 3:
            print('Most common month...')
            print('Common month: March\n')
        elif kc == 4:
            print('Most common month...')
            print('Common month: April\n')
        elif kc == 5:
            print('Most common month...')
            print('Common month:: May\n')
        elif kc == 6:
            print('Most common month...')
            print('Common month: June\n')
    
    # display the most common day of week
    df['weekday_name'] = df['Start Time'].dt.weekday_name
    day = df['weekday_name'].tolist()
    if len(set(day)) == 1:
           pass
    else:
        c = Counter(day)
        k = c.most_common()
        print('Most common day...')
        print('Common day:',k[0][0],'\n')
        
        
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    
    print('Most common hour...')
    print('Common hour:',common_hour)
    
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].tolist()
    c = Counter(start_station)
    k = c.most_common()
    
    print('Most common start station and count...')
    print('Start Station:',k[0][0],'|', 'Count:',k[0][1],'\n')
    
    
    # display most commonly used end station
    end_station = df['End Station'].tolist()
    c = Counter(end_station)
    k = c.most_common()
    
    print('Most common end station and count...')
    print('End Station:',k[0][0],'|', 'Count:',k[0][1],'\n')
    

    # display most frequent combination of start station and end station trip
    s_station = df['Start Station']
    e_station = df['End Station']
    czip = zip(s_station,e_station)
    c = Counter(czip)
    z = c.most_common()
    
    print('Most common trip and count...')
    print("('start station', 'end station'):",z[0][0],'|', "Count:",z[0][1])
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total duration of trip...')
    print('Total Duration:',sum(df['Trip Duration']),'\n')
    
    # display mean travel time
    avg_trip = df['Trip Duration'].mean()
    print('Average duration of trip...')
    print('Average Duration:',int(avg_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].tolist()
    print('Counts of each user type...')
    print('Subsciber:',user_types.count('Subscriber'),'|','Customer:',user_types.count('Customer'),'\n')
    
    # Display counts of gender
    try:
        gender = df['Gender'].tolist()
        print('Counts of each gender...')
        print('Male:',gender.count('Male'),'|','Female:',gender.count('Female'),'\n')
    except:
        print('Counts of each gender...')
        print('No info for Washington\n')
    
    # Display earliest, most recent, and most common year of birth
    try:
        birth_year = df['Birth Year']
        b = pd.Series(birth_year).value_counts().index.tolist()
        max_year = max(birth_year)
        min_year = min(birth_year)
    
        print('Earliest, most recent, and most common year of birth...')
        print('Earliest:',int(min_year),'|','Most Recent:',int(max_year),'|','Most Common:',int(b[0]))
    except:
        print('Earliest, most recent, and most common year of birth...')
        print('No info for Washington\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    
    df = df.drop('month_name', axis=1)
    df = df.drop('weekday_name',axis=1)
    df = df.drop('hour', axis=1)    
    df = df.drop('month', axis=1)
    df = df.drop('day', axis=1)
        
   
    pd.set_option('display.width', 1000)
    c = df
        
    for index in c:
        prompt = input("\nWould you like to see raw data? Enter yes or no.\n")
        try:
            if prompt == 'yes':
                d = input("\nPlease enter integer for number of rows you want to view.\n") 
                print(c[:int(d)])
            else:
                prompt == 'no'
                break
        except:
            print("\nPlease enter a interger for the number of rows you want to view.\n")
            
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()










    