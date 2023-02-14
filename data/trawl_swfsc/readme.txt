Data obtained from:
https://coastwatch.pfeg.noaa.gov/erddap/tabledap/FRDCPSTrawlLHSpecimen.html

Data URL:
https://coastwatch.pfeg.noaa.gov/erddap/tabledap/FRDCPSTrawlLHSpecimen.nc?cruise%2Cship%2Chaul%2Ccollection%2Clatitude%2Clongitude%2Ctime%2Citis_tsn%2Cscientific_name%2Cspecimen_number%2Csex%2Cis_random_sample%2Cweight%2Cstandard_length%2Cfork_length%2Ctotal_length%2Cmantle_length&time%3E=2003-07-09T05%3A04%3A00Z&time%3C=2019-09-08T09%3A25%3A00Z

The Dataset Attribute Structure (.das) for this Dataset:

Attributes {
 s {
  cruise {
    Int32 actual_range 200307, 201907;
    String description "Six-digit cruise number fixed by year and predominant month of cruise, often with overlapping information in the CalCOFI Database.";
    String ioos_category "Identifier";
    String long_name "Cruise";
  }
  ship {
    String description "CalCOFI type two-character ship code.";
    String ioos_category "Identifier";
    String long_name "Ship";
  }
  haul {
    Int32 actual_range 1, 175;
    String description "Haul number, consecutively from 1 within a ship of a cruise.";
    String ioos_category "Identifier";
    String long_name "Haul Number";
  }
  collection {
    Int32 actual_range 2004, 4267;
    String description "Four-digit number used with specimen number for labeling gonads and during subsequent lab-histo processing.";
    String ioos_category "Identifier";
    String long_name "Collection";
  }
  latitude {
    String _CoordinateAxisType "Lat";
    Float32 actual_range 31.3443, 54.3102;
    String axis "Y";
    String description "Latitude   position at Equilibrium Time, when fishing starts.";
    String ioos_category "Location";
    String long_name "Latitude";
    String standard_name "latitude";
    String units "degrees_north";
  }
  longitude {
    String _CoordinateAxisType "Lon";
    Float32 actual_range -132.7302, -117.2888;
    String axis "X";
    String description "Longitude  position at Equilibrium Time, when fishing starts.";
    String ioos_category "Location";
    String long_name "Longitude";
    String standard_name "longitude";
    String units "degrees_east";
  }
  time {
    String _CoordinateAxisType "Time";
    Float64 actual_range 1.05772704e+9, 1.5679347e+9;
    String axis "T";
    String description "Date-Time when net and wire are fully deployed and fishing has begun.";
    String ioos_category "Time";
    String long_name "Time";
    String standard_name "time";
    String time_origin "01-JAN-1970 00:00:00";
    String units "seconds since 1970-01-01T00:00:00Z";
  }
  itis_tsn {
    String description "Intergrated Taxomomic Information System Taxonomic Serial Number.";
    String ioos_category "Identifier";
    String long_name "ItisTSN";
  }
  scientific_name {
    String description "Scientific name of species.";
    String ioos_category "Identifier";
    String long_name "Scientific Name";
  }
  specimen_number {
    String description "Number identifying a specimen  of a species within a cruise, ship and haul.";
    String ioos_category "Other";
    String long_name "Specimen Number";
  }
  sex {
    String description "Sex of the specimen: male, female, notDetermined.";
    String ioos_category "Other";
    String long_name "Sex";
  }
  is_random_sample {
    String description "Is sample randomly selected?  Y/N.";
    String ioos_category "Other";
    String long_name "Is Random Sample";
  }
  weight {
    String description "Fresh body weight in g.";
    String ioos_category "Other";
    String long_name "Weight";
    String units "g";
  }
  standard_length {
    String description "Standard length in mm.";
    String ioos_category "Other";
    String long_name "Standard Length";
    String units "mm";
  }
  fork_length {
    String description "Fork length in mm.";
    String ioos_category "Other";
    String long_name "Fork Length";
    String units "mm";
  }
  total_length {
    String description "Total length in mm.";
    String ioos_category "Other";
    String long_name "Total Length";
    String units "mm";
  }
  mantle_length {
    String description "Mantle length in mm.";
    String ioos_category "Other";
    String long_name "Mantle Length";
    String units "mm";
  }
 }
  NC_GLOBAL {
    String acknowledgment "National Oceanic and Atmospheric Administration, Southwest Fisheries Science Center";
    String cdm_data_type "Other";
    String contributor_name "Fisheries Research Division";
    String Conventions "COARDS, CF-1.0, Unidata Dataset Discovery v1.0, NCCSV-1.0";
    String creator_email "swfsc.cps-lht@noaa.gov";
    String creator_name "Coastal Pelagic Species Life History Program";
    String creator_url "https://swfsc.noaa.gov/FRD/";
    String date_created "2014-12-12";
    String date_issued "2014-12-12";
    String date_modified "2014-12-12";
    String defaultGraphQuery "longitude,latitude,time&scientific_name=\"Sardinops sagax\"&.draw=markers&.marker=5|5&.color=0x000000&.colorBar=|||||";
    Float64 Easternmost_Easting -117.2888;
    Float64 geospatial_lat_max 54.3102;
    Float64 geospatial_lat_min 31.3443;
    String geospatial_lat_units "degrees_north";
    Float64 geospatial_lon_max -117.2888;
    Float64 geospatial_lon_min -132.7302;
    String geospatial_lon_units "degrees_east";
    String history
"2020-02-10T19:59:30Z (source database)
2020-02-10T19:59:30Z http://coastwatch.pfeg.noaa.gov/erddap/tabledap/FRDCPSTrawlLHSpecimen.html";
    String infoUrl "https://swfsc.noaa.gov/FRD/";
    String institution "NOAA-Fisheries/Southwest Fisheries Science Center";
    String keywords "life history, Oceans >Coastal pelagic species, trawl";
    String license
"The data may be used and redistributed for free but is not intended
for legal use, since it may contain inaccuracies. Neither the data
Contributor, ERD, NOAA, nor the United States Government, nor any
of their employees or contractors, makes any warranty, express or
implied, including warranties of merchantability and fitness for a
particular purpose, or assumes any legal liability for the accuracy,
completeness, or usefulness, of this information.";
    Float64 Northernmost_Northing 54.3102;
    String project "Costal Pelagic Species Surveys";
    String publisher_email "swfsc.cps-lht@noaa.gov";
    String publisher_name "Coastal Pelagic Species Life History Program";
    String sourceUrl "(source database)";
    Float64 Southernmost_Northing 31.3443;
    String standard_name_vocabulary "CF-11";
    String subsetVariables "cruise, ship, haul, collection,scientific_name, time, latitude, longitude";
    String summary "Individual specimens measured (weight in grams and length in mm) and sexed from mainly targeted species caught during SWFSC-FRD fishery independent trawl surveys of coastal pelagic species. Individuals are categorized as random or non-random samples. Does not include species with length bins recorded in the CPS Trawl Life History Length Frequency dataset.";
    String time_coverage_end "2019-09-08T09:25:00Z";
    String time_coverage_start "2003-07-09T05:04:00Z";
    String title "CPS Trawl Life History Specimen Data";
    Float64 Westernmost_Easting -132.7302;
  }
}
