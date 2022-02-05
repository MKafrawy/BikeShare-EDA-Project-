import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago':'chicago.csv',
              'new york city':'new_york_city.csv',
              'washington':'washington.csv' }

MONTH_LIST = ['all', 'january', 'february', 'march',  'april', 'may',  'june']
              
DAYS_LIST = ['all','monday','tuesday','wednesday','thursday','friday',  'saturday','sunday']
            
             
             
           
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_na = ''
    while city_na.lower()  not in CITY_DATA:
          city_na = input('What city you want to analyze?...\n')
          if city_na.lower() in CITY_DATA:
            city = CITY_DATA[city_na.lower()]
           
          else:
               print("Sorry, Check your spelling!\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_na = ''
    while month_na.lower()  not in MONTH_LIST:
          month_na = input('What month you want to analyze?...\n')
          if month_na.lower() in MONTH_LIST:
             month = month_na.lower()
            
          else:
               print("Sorry, Check your spelling!\n")
  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_na = ''
    while day_na.lower()  not in DAYS_LIST:
          day_na = input('What day you want to analyze?...\n')
          if day_na.lower() in DAYS_LIST:
            day = day_na.lower()
            
          else:
               print("Sorry, Check your spelling!\n")

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

    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

   
    popular_month_number = df['Start Time'].dt.month.mode()[0]
    popular_month = MONTH_LIST[popular_month_number-1].title()
    print('The most commonly month is ', popular_month)
    
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most commonly day is ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most commonly hour is ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_Sstation = df['Start Station'].mode()[0]
    print('The most commonly start station is ', most_popular_Sstation)
    # TO DO: display most commonly used end station
    most_popular_Estation = df['End Station'].mode()[0]
    print('The most commonly end station is ', most_popular_Estation)

    # TO DO: display most frequent combination of start station and end station trip
    df["rout"] = df["Start Station"] + "-" + df["End Station"] 
    most_freq = df['rout'].mode()[0]
    print('The most frequent combination of start station and end station trip is ', most_freq)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()
    print('Total trip duration is ', total_trip_time)
    
    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts() 
    print("The count of user types: ", user_type_count)
    
    
    # TO DO: Display counts of gender
    if city == 'chicago.csv' or city == 'new_york_city.csv':
       gender_number = df['Gender'].value_counts()
       print("The count of gender: ", gender_number)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe\n')
        
    

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        e_year = df["Birth Year"].min()
        r_year = df["Birth Year"].max()
        c_year = df["Birth Year"].mode()[0]
        print("The earliest year is: ",e_year, "\n The most recent year is: ", r_year, "\n The most common year is: " ,c_year, "\n") 
    else:
        print('Birth Year stats cannot be calculated because Gender does not appear in the dataframe\n')
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data():
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    s_c = 0
    while (True):
        print(df.iloc[s_c:s_c])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
    
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
