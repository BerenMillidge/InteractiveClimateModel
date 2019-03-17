# UK climate projection data information
## UK climate projection data API

CEDA (The Centre for Environmental Data Science) produce and host a large number of data sets, most of which are open access.
Especially interesting among these are their enviromental prediction datasets, covering many factors from sea levels
to regional weather.

Interestingly, they also have an API. As well as a web interface (found in the 'Products' section in the web dashboard
at https://ukclimateprojections-ui.metoffice.gov.uk/), there is a Python API: 
https://github.com/ukcp-data/ukcp-api-client/blob/master/examples/run_12_requests.py. Documentation for the API is to 
be found here: https://ukclimateprojections-ui.metoffice.gov.uk/ui/api_docs.

Unfortunately, the API and web UI only have access to the 'Probabilistic Projections for the UK' data source. The only variables available are as follows:
  - Total cloud anomaly (%)
  - Specific humidity anomaly at 1.5m (%)
  - Precipitation rate anomaly (%)
  - Sea level pressure anomaly (hPa)
  - Net Surface long wave flux anomaly (W m-2)
  - Total downward shortwave flux anomaly (W m-2)
  - Net Surface short wace flux anomaly (W m-2)
  - Mean air temperature anomaly at 1.5m (°C)
  - Maximum air temperature anomaly at 1.5m (°C)
  - Minimum air temperature anomaly at 1.5m (°C)

The API is actually pretty good. It can export the data in either comma-separated values (CSV), or in NetCDF (more on this later). 
Yet, there are in fact a number of other datasets available on the CEDA website, which are equally interesting, such as 
predicted sea levels.

## NetCDF

All of the datasets available on the CEDA website, open access or otherwise, appear to be in just NetCDF format (or as seemingly-corrupted CSV files). They appear to mostly be in NetCDF classic format.

NetCDF is the de-facto standard in the environmental and earth sciences areas. It is a binary format and the data structure is described here: https://www.unidata.ucar.edu/software/netcdf/docs/file_structure_and_performance.html

There are various libraries available which can process NetCDF files. Most of these communicate with the C NetCDF libary. These include:
  - C: https://github.com/Unidata/netcdf-c
  - R: netcdf4 or RNetCDF
  - Python: netcdf4-python

NetCDF has two types of variables: ones with defined length and others with unlimited length. The format represents them as arrays of arbitrary dimensions (within reason, e.g. there may be a limit of 2GiB depending on certain conditions).

It is remarkably difficult to visualise NetCDF files - unlike CSV, they are in a binary format. Therefore, programs exist that can represent the data in other formats such as CDL, as well as
XML or simply just text data. The two main OSS programs are:
  - nco
  - ncdump from NetCDF-bin (e.g. in Debian)

Matlab and Octave can also visualise the files, and can export these as CSV or another format.

## Resources

- https://www.metoffice.gov.uk/research/collaboration/ukcp/download-data
- https://unidata.github.io/netcdf4-python/
- http://geog.uoregon.edu/bartlein/courses/geog607/Rmd/netCDF_01.htm
