import time

import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Lower() function used to handle all the ways a user may use to type the city name

    city = input("Please Choose which city you want to explore- Chicago, new york city or washington?: ").lower()
    # while loop to handle invalid inputs
    while city not in (CITY_DATA):
        print("Please Pick one of the city names in front of you")
        city = input("Chicago, new york city or washington?: ").lower()

    # get user input for month (all, january, february, ... , june)
    # while loop running till getting a good form of choosing
    while True:
        month = input(
            "Please Choose which month you want to explore- (january,february,march,april,may,june or 'all' for the six months): ").lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']

        # If statement to handle any error happens while choosing month name
        if month not in months and month != 'all':
            print("Please Pick one of the month names in front of you or type 'all'")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:

        day = input("Please Type which day you want to explore or 'all' for the whole week: ").lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

        # If statement to handle any error happens while choosing day name
        if day not in days and day != 'all':
            print("Please type one of the day names Or type 'all'")
        else:
            break

    print('-' * 40)
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
    # load the choosen city data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # getting month and day of week from Start Time column to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # checking the choice made by user regarding the month
    if month != 'all':
        # index of the months list used to get the int value of chcoosen month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # checking the choice made by user regarding the day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(months[most_common_month - 1]))

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: {}'.format(most_common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: {}'.format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: {}'.format(common_end_station))

    # display most frequent combination of start station and end station trip
    common_start_end_station = (df['Start Station'] + '--' + 'to' + '--' + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is: {}".format(common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time done is: {} seconds, which is equal to {} hours".format(total_travel_time,
                                                                                         total_travel_time / 3600))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time done is: {} seconds, which is equal to {} hours".format(mean_travel_time,
                                                                                        mean_travel_time / 3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Brith Year' in df:
        theEarliest = int(df['Brith Year'].min())
        print("The earliest year of brith is: {}".format(theEarliest))
        theRecent = int(df['Brith Year'].max())
        print("The Recent year of brith is: {}".format(theRecent))
        most_common_year = int(df['Brith Year'].mode()[0])
        print("The most common year is: {}".format(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at time"""
    answer = input("Do you want to display the first 5 raws of data? yes/no: ").lower()
    i = 0
    while True:
        if answer == 'no':
            break
        print(df[i:i + 5])
        answer = input("Do you want to display the next 5 raws of data? yes/no: ").lower()
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
