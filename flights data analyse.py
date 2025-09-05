import pandas as pd
import plotly.express as px

flights = pd.read_csv("flights.csv")
airlines = pd.read_csv("airlines.csv")
airports = pd.read_csv("airports.csv")

delay_columns = ['AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']
flights[delay_columns] = flights[delay_columns].fillna(0)

flights['CANCELLATION_REASON'] = flights['CANCELLATION_REASON'].fillna('Not Cancelled')

def convert_to_time(row):
    try:
        time = str(int(float(row))).zfill(4)
        hour = int(time[:2])
        minute = int(time[2:])
        return pd.to_datetime(f"{hour}:{minute}", format='%H:%M').time()
    except:
        return None

flights['SCHEDULED_DEPARTURE_TIME'] = flights['SCHEDULED_DEPARTURE'].apply(convert_to_time)
flights['SCHEDULED_ARRIVAL_TIME'] = flights['SCHEDULED_ARRIVAL'].apply(convert_to_time)

flights['FLIGHT_DATE'] = pd.to_datetime(flights[['YEAR', 'MONTH', 'DAY']])

reason_map = {
    'A': 'Airline/Carrier',
    'B': 'Weather',
    'C': 'National Air System',
    'D': 'Security',
    'Not Cancelled': 'Not Cancelled'
}
flights['CANCELLATION_REASON_DESC'] = flights['CANCELLATION_REASON'].map(reason_map)

airlines.columns = airlines.columns.str.upper()
if 'AIRLINE' in airlines.columns:
    flights = pd.merge(flights, airlines, how='left', left_on='AIRLINE', right_on='IATA_CODE')
    flights.rename(columns={'AIRLINE_y': 'AIRLINE_NAME'}, inplace=True)

total_flights = len(flights)
avg_dep_delay = flights['DEPARTURE_DELAY'].mean()
avg_arr_delay = flights['ARRIVAL_DELAY'].mean()
on_time_pct = (flights['ARRIVAL_DELAY'] <= 0).sum() * 100 / total_flights
cancel_rate = (flights['CANCELLED'] == 1).sum() * 100 / total_flights

route_counts = flights.groupby(['ORIGIN_AIRPORT', 'DESTINATION_AIRPORT']).size().reset_index(name='count')
most_common_route = route_counts.sort_values(by='count', ascending=False).iloc[0]

airline_perf = flights.groupby('AIRLINE').apply(lambda x: (x['ARRIVAL_DELAY'] <= 0).sum() * 100 / len(x)).reset_index(name='on_time_pct')
best_airline = airline_perf.sort_values(by='on_time_pct', ascending=False).iloc[0]

print("\n Flights KPI Report\n")
print(f" Total Flights: {total_flights:,}")
print(f" Average Departure Delay: {avg_dep_delay:.2f} mins")
print(f" Average Arrival Delay: {avg_arr_delay:.2f} mins")
print(f" On-Time Arrival Rate: {on_time_pct:.2f}%")
print(f" Cancellation Rate: {cancel_rate:.2f}%")
print(f" Most Frequent Route: {most_common_route['ORIGIN_AIRPORT']} → {most_common_route['DESTINATION_AIRPORT']} ({most_common_route['count']:,} flights)")
print(f" Best On-Time Airline: {best_airline['AIRLINE']} ({best_airline['on_time_pct']:.2f}%)")

# ========== 8) Visualizations ==========
fig1 = px.histogram(flights, x='DEPARTURE_DELAY', nbins=50, title='Departure Delay Distribution')
fig1.show()

avg_delay = flights.groupby('AIRLINE')['DEPARTURE_DELAY'].mean().reset_index()
fig2 = px.bar(avg_delay, x='AIRLINE', y='DEPARTURE_DELAY', title='Average Departure Delay by Airline')
fig2.show()

origin_count = flights['ORIGIN_AIRPORT'].value_counts().reset_index()
origin_count.columns = ['Airport', 'Flight Count']
fig3 = px.bar(origin_count.head(10), x='Airport', y='Flight Count', title='Top 10 Origin Airports')
fig3.show()

fig4 = px.scatter(flights, x='DISTANCE', y='ARRIVAL_DELAY', title='Distance vs Arrival Delay', opacity=0.5)
fig4.show()

flights.to_csv("cleaned_flights.csv", index=False)
print("\nCleaned data saved as cleaned_flights.csv")
