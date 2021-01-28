# Distribution Center
Grainger DCs and Store Fronts map to the Distribution Center class for sake of simplifying the network. 
Distribution Centers (Grainger DCs and Store Fronts) have 3 types of storage space - STANDARD, HAZMAT, 
REFRIGERATION. STANDARD makes up ~80% of the total storage while the other 2 split the remaining 20%. Once the 
improvement algorithm is made, DCs can only ship to neighboring DCs within ~700 miles.

## Grainger DCs
The 10 Grainger DCs were pulled off of GoogleMaps and added to the sample data. Weights (1 to 5) were given to the DCs 
to represent likely size / significance to the network.  
* <b>5</b>:  <i>701 Grainger Way, Minooka, IL 60447</i>
* <b>5</b>: <i>400 Bordentown Hedding Rd, Fieldsboro, NJ 08505</i>
* <b>5</b>: <i>parkway, 2710 Keystone Pacific Pkwy, Patterson, CA 95363</i>
* <b>4</b>: <i>101 Southchase Blvd, Fountain Inn, SC 29644</i>
* <b>4</b>: <i>11200 MO-210, Kansas City, MO 64161</i>
* <b>4</b>: <i>Industrial equipment supplier in Roanoke, Texas</i>
* <b>3</b>: <i>8001 Forshee Dr, Jacksonville, FL 32219</i>
* <b>3</b>: <i>8211 Bavaria Dr E, Macedonia, OH 44056</i>
* <b>3</b>: <i>4300 Old Airways Boulevard, Southaven, MS 38671</i>
* <b>3</b>: <i>4700 Hamner Ave, Mira Loma, CA 91752</i>

## Store Fronts
62 Store Fronts were simulated from a random sample of the most populated cities in America (simplemaps).  Weights were 
randomly selected between 1 and 2.  
