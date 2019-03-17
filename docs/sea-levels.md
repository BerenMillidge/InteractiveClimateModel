# Projection of sea level rise for UK waters
## UKCP09: Climate scenarios projection data of sea level rise for UK waters

https://catalogue.ceda.ac.uk/uuid/de1e833f972248e69285424fbd9ceac2

Sea levels are represented as follows:

time: this is a list of items from 0-102. That is, time number of years since 1970. Nominally, the study is estimating 1990 until 2100, but in fact the times last from 1999-2099, which matches the data.

em_scen: this is an array with just three elements. That is, three different emissions scenarios. These are as follows: 0 - low scenario; 1 - medium scenario; 2 - high scenario.

abs_sea_level_rise: this is the absolute sea level rise, calculated from locations around the UK.

latitude: latitude referenced at different points. More on this later. It's just a list of items.

longitude: longitude refereced at different points.

bounds_latitude; bounds_longitude: provides bounds given that measurements of latitude and longitude have a degree of uncertainty.

rel_sea_level_rise: this is an array of relative sea level rises. Nominally, this is calculated subtracting the land movement rate from the absolute sea level rise.

--

abs_sea_level_rise is a four-dimensional array.
- The first element is time. That is, a given year.
- The second element is the emissions scenario. That is, a given scenario 0, 1, or 2.
- The third element is the latitude (northing). This references not an actual latitude, but an element in the latitude array. Likewise, this would reference an element in the latitude bounds array.
- The third element is the longitude (easting). This is the same reference as for northing.
- The fourth element is the actual sea level rise. This is represented in metres.

We found that the rel_sea_level_rise was mostly impossibly large values. The main reason for this is that most of the array is empty space, as it is a square grid, and areas that aren't empty sea (that actually have a land movement rate) are still unlikely to have a given relative sea level rise if they are land. This resulted in extremely sparse valid values.
