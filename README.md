## YouBike_Statistical_Analysis_and_Forecasting

## Preface
This is my side project for practicing statistical analysis, data analytics, and machine learning.
For a complete project introduction, please visit my **[personal website.](https://huberthuang2002.github.io/blog/post-6/)**

## Dataset Source
This dataset is provided by Professor **Ling-Chieh Kung** from the Department of Information Management at National Taiwan University. It was made available for the **Programming for Business Computing** course offered in the summer of 2024. 

The dataset comprises a total of 275,280 records related to YouBike data for July 2017 and includes 12 columns: `sno`, `sna`, `sarea`, `date`, `hour`, `lent`, `returned`, `temperature`, `relative_humidity`, `wind_speed`, `precipitation`, and `station_pres`. 

These columns represent the following:
| **sno** | **sna** | **sarea** | **date** | **hour** | **lent** | **returned** | **temperature** | **relative_humidity** | **wind_speed** | **precipitation** | **station_pres** |
|---------|---------|-----------|----------|----------|----------|--------------|-----------------|-----------------------|----------------|-------------------|---------------------|
- **sno**: Station number
- **sna**: Station name
- **sarea**: Administrative area where the station is located
- **date**: Date
- **hour**: Hour of the day (0 represents 0:00–1:00, 1 represents 1:00–2:00, and so on)
- **lent**: Number of rentals
- **returned**: Number of returns
- **temperature**: Average temperature at the station during that hour (°C)
- **relative_humidity**: Relative humidity at the station during that hour (%)
- **wind_speed**: Average wind speed at the station during that hour (knots)
- **precipitation**: Cumulative rainfall at the station during that hour (millimeters)
- **station_pres**: Average atmospheric pressure at the station during that hour (hectopascals)

## Research Objective
Through this project, I aim to combine my programming skills and statistical knowledge to analyze the impact of various factors on YouBike rental and return volumes.

## Research Tools
`Python`, mathematical computation libraries (e.g., `pandas`, `numpy`), data visualization libraries (e.g., `matplotlib`), and machine learning libraries.
