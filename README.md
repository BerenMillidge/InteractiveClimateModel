# InteractiveClimateModel
Project for Hack the Burgh 19.

See the effects of climate change on your area! This interactive map takes climate projections up to 2100 and displays them for you up to the year 2100. Choose the year and the level of projected emissions (low, medium or high) to see the projections rendered interactively on the map. Currently supports projected sea-levels and temperatures. Further climate variables might be forthcoming.

First run the backend server with "python server.py". If the server does not run on localhost you will need to change the paths in the frontend map2.html file.

Then just load the frontend html file map2.html. If all goes well it should load and the map should render.

The data is from the UK Climate Projet's Probabilistic Projections and Sea-levels datasets. All data is open access and can be found in the CEDA repository as part of the UKCP18 project. We found this data to be in .nc format - a binary format used in geosciences but not familiar to us or many computer-science/software engineering people. In the backend folder there is data relating to temperature and sea-level projections in the much more widely used JSON format, which we hope may be uesful for some in getting to grips with these climate datasets.
