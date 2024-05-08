# Usage

The `download_prism` function allows you to download PRISM climate data for a specified time range and frequency.

## Function Signature

```python
def download_prism(start: str = None, end: Optional[str] = None, variable: str = None,
                   freq: Optional[str] = "daily", download_dir: Optional[str] = None,
                   unzip: Optional[bool] = True, remove_zip: Optional[bool] = True) -> None:
```

## Parameters

- `start`: The start date of the time range to download. Must be in the format `YYYYMMDD`. Defaults to `None`.
- `end`: The end date of the time range to download. Must be in the format `YYYYMMDD`. If `None`, defaults to the latest available date for the specified variable.
- `variable`: The PRISM variable to download. Must be one of `["ppt", "tmin", "tmax", "tmean", "tdmean", "vpdmin", "vpdmax"]`.
- `freq`: The frequency of the data to download. Must be one of `["daily", "monthly", "annual"]`. If `None`, defaults to `"daily"`.
- `download_dir`: The directory to download the data to. If `None`, defaults to `data` under current working directory. If the directory does not exist, it will be created.
- `unzip`: Whether to unzip the downloaded data. If `True`, the data will be unzipped. If `False`, the data will not be unzipped. Defaults to `True`. 
- `remove_zip`: Whether to remove the downloaded zip file after unzipping. If `True`, the zip file will be removed. If `False`, the zip file will not be removed. Defaults to `True`. 

## Example Usage

### Example 1: Download daily data for a single date

```python
from prism import download_prism
download_prism(start="20100101", variable="ppt")
```

### Example 2: Download daily data for a time range

```python
download_prism(start="20100101", end="2010-01-31", variable="ppt")
```

### Example 3: Download monthly data for a single date

```python
download_prism(start="202305", variable="tmean", freq="monthly")
```

### Example 4: Download annual data for a single year

```python
download_prism(start="2023", variable="tmean", freq="annual")
```

### Example 5: Download daily data for a time range and save to a specific directory

```python
download_prism(start="20230501", variable="vpdmax", download_dir="path/to/download/directory")
```

## Note

- The function will only download data if it doesn't already exist in the specified download directory.
- The downloaded data will be saved in a subdirectory named after the variable within the specified download directory.
- The function will raise a `ValueError` if an invalid variable, frequency, or date range is provided.

## Valid Variable Options

The following are the valid options for the `variable` parameter:

1. `ppt`: Precipitation
2. `tmin`: Minimum temperature
3. `tmax`: Maximum temperature
4. `tmean`: Mean temperature
5. `tdmean`: Mean dew point temperature
6. `vpdmin`: Minimum vapor pressure deficit
7. `vpdmax`: Maximum vapor pressure deficit

## Valid Frequency Options

The following are the valid options for the `freq` parameter:

1. `daily`: Daily data
2. `monthly`: Monthly data
3. `annual`: Annual data

## Date Range Considerations

- For daily data, the start date must be provided in the `YYYYMMDD` format and must be on or after January 1, 1981. The end date, if provided, must also be in the `YYYYMMDD` format and cannot be after yesterday's date.
- For monthly data, the start date must be provided in the `YYYYMM` format and must be on or after January 1981. The end date, if provided, must also be in the `YYYYMM` format and cannot be after the previous month.
- For annual data, the start date must be provided in the `YYYY` format and must be on or after 1981. The end date, if provided, must also be in the `YYYY` format and cannot be after the previous year.
- If the end date is not provided, the function will download data for a single date specified by the start date.
- The start date cannot be after the end date.

## Output Format

The downloaded data will be saved in NetCDF format with the following naming convention:

- Daily data: `daily_YYYYMMDD.nc`
- Monthly data: `monthly_YYYYMM.nc`
- Annual data: `annual_YYYY.nc`

The NetCDF files will contain the climate variable data reprojected to the EPSG:4326 coordinate reference system.