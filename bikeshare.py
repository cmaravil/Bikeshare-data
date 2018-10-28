
import csv
import pprint
import datetime
import time
import pandas as pd


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'



def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')

    city= city.lower()
    if city == 'chicago':
        print('Ok, Let\'s explore the data for Chicago!')
        return chicago

    elif city == 'new york':
        print('Ok, Let\'s explore the data for New York!')
        return new_york_city

    elif city== 'washington':
        print('Ok, Let\'s explore the data for Washington')
        return washington
    else:
        print ('Sorry that is not a valid input, please make sure you are using lowercase letters.')
        return get_city()


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Time period for a city's bikeshare data.
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')


    if time_period == 'month':
        print('Great, let\'s filter the data by month.')
        return get_month()

    elif time_period == 'day':
        print('Great, let\'s filter the data by day.')
        return get_day()

    elif time_period == 'none':
        print('Great, we will not filter the time period.')
        return time_period
    else:
        print('Sorry, that is not a valid input, please try again.')
        return get_time_period()


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str): Returns the month the user chooses.
    '''

    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    month= month.lower()
    if month not in ['january', 'february', 'march', 'april','may', 'june']:
        print('This input is not valid.')
        return get_month()
    return month



def get_day():
    '''Asks the user for as an integer day and returns the specified day.

    Args:
        none.
    Returns:
        (int): Returns the day of the weeek that the user chooses.
    '''

    day = input('\nWhich day? Please type your response as an integer. For example Mon=0, Tues=1, etc.\n')
    if int(day) not in [0,1,2,3,4,5,6]:
        print('This input is not valid.')
        return get_day()
    day = int(day)
    return day


def load_df(city):
    '''Loads data frame.
    Args:
        City
    Returns:
        Loads city CSV using pandas.
    '''

    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # df['End Time'] = pd.to_datetime(df['End Time'])
    return df



def popular_month(city_file, time_period):
    ''' Question: What is the most popular month?
    Args:
        city_file and time_period
    Returns:
        (int) Mode of popular month for a city's bikeshare data.
    '''
    df = load_df(city_file)
    df['month'] = df['Start Time'].dt.month
    popular_month_num = int(df['month'].mode())
    return popular_month_num


def popular_day(city_file, time_period):
    '''
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    Args:
        city_file, time_period
    Returns:
        (int) Most popular startime for a city's bikeshare data.

    '''

    popular_day=('\n The most popular day of the week for start time is :\n')
    df = load_df(city_file)
    if time_period is 'none'or 'month':
        days_strings = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday','Friday','Saturday']
        df['weekday'] = df['Start Time'].dt.weekday_name.mode().index[0]
        return int(df['weekday'].mode()[0])


    #print('Most Popular Day:', popular_day) in statistics

def popular_hour(city_file, time_period):
    '''
    Question: What is the most popular hour of day for start time?
    Args:
        city_file, time_period
    Returns:
        (int) Most popular hour of the day for starting time.
    '''
    #setting a new column for the results using df[]
    popular_hour= ('\nThe most popular hour of the day for start time is :\n')
    df = load_df(city_file)
    df['hour'] = df['Start Time'].dt.hour
    return int(df['hour'].mode())





def trip_duration(city_file, time_period):
    '''
    Question: What is the total trip duration and average trip duration?
    Args:
        city_file, time_period
    Returns:
        (int,int) Returns the total sum of the drip durations and the average.
    '''
    trip_duration=('\nThe total and average durations of trips are:\n')
    df=load_df(city_file)

    tot_duration=df['Trip Duration'].sum()
    avg_duration=df['Trip Duration'].mean()
    return tot_duration,avg_duration



def popular_stations(city_file, time_period):
    '''
    Question: What is the most popular start station and most popular end station?
    Args:
        city_file, time_period
    Returns:
        (str,str) Returns most common start and end station.
    '''
    #popular_stations(city,time_period)
    #query to data frame
    df = load_df(city_file)
    st= df.groupby('Start Station')['Start Station'].count().sort_values(ascending=False).index[0]
    ed= df.groupby('End Station')['End Station'].count().sort_values(ascending=False).index[0]
    return st,ed


def popular_trip(city_file, time_period):
    '''Question: What is the most popular trip?
    Args:
        city_file, time_period
    Returns:
        (str,str) Returns most popular trip.
    '''
    df = load_df(city_file)
    return df.groupby(['Start Station','End Station'])['Start Station'].count().sort_values(ascending=False).index[0]



def users(city_file, time_period):
    '''Question: What are the counts of each user type?
    Args:
        city_file, time_period
    Returns:
        (str,int) Returns counts for each user type.
    '''
    df = load_df(city_file)
    user_results = pd.value_counts(df['User Type'])
    return user_results

def gender(city_file, time_period):
    '''Question: What are the counts of gender?
    Args:
        city_file, time_period
    Returns:
        (str,int) Returns counts for gender types.
    '''
    df = load_df(city_file)
    if 'Gender' in df:
        gender_results = pd.value_counts(df['Gender'])
        return gender_results
    else:
        return "Sorry, this data is not available for Washington."


def birth_years(city_file, time_period):
    '''Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    Args:
        city_file, time_period
    Returns:
        (int) Returns youngest, oldest and most popular birth years.
    '''
    df = load_df(city_file)
    if 'Birth Year' in df:
        return (int(df['Birth Year'].max()),int(df['Birth Year'].min()),int(df['Birth Year'].mode()[0]))
    else:
        return "Sorry, this data is not available for Washington."
        
def display_data(city_files, current_idx=0):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        city_file, index
    Returns:
        5 rows at a time from csv converted to data frame.
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    if display == 'yes':
        df=load_df(city_files)
        print(df.iloc[current_idx:current_idx+5])
        display_data(city_files, current_idx+5)

    if display == 'no':
        print('Thank you have a nice day!')


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time() #this is for the running timer

        #TODO: call popular_month function and print the results
        pop_month = popular_month(city, time_period)
        print('Most Popular Month:', pop_month)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")


    # What is the most popular day of week (Monday, Tuesday, etc.) for start time
    if time_period == 'none' or 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        popular_day_results = popular_day(city, time_period)
        print('The most popular day for start time is:',popular_day(city, time_period))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")


    start_time = time.time()
    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    print('Most Popular Hour is:',popular_hour(city, time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")



    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results

    print('The total and average trip duration is:',trip_duration(city, time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")



    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results

    print('The most popular start station and end stations are:',popular_stations(city, time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")


    start_time = time.time()
    print("The most popular trip is:",popular_trip(city, time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")


    start_time = time.time()
    print ('The counts for each user type are:',users (city, time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    print('The counts for gender are:',gender(city, time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    print('The youngest user, oldest user and most popular birth years:',birth_years(city, time_period))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")

    start_time = time.time()
    display_data(city)
    print("That took %s seconds." % (time.time() - start_time))








if __name__ == "__main__":
	statistics()
