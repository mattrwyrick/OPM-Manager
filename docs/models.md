# Data Models


## BinLocation
[view src](/src/opm_manager/tools.py)   
3 types of bin locations: STANDARD, HAZMAT, and REFRIGERATION

## Distribution Center
[view src](/src/opm_manager/models/sku.py)  
Class representation of a DC

## Location
[view src](/src/opm_manager/tools.py)  
Abastract Class to represent physical supplier and DC locations

## Material
[view src](/src/opm_manager/models/sku.py)  
Class to represent a material

## Network
[view src](/src/opm_manager/models/network.py)  
Class to connect entities in the supply chain and score relative availability  

## Node
[view src](/src/opm_manager/models/network.py)  
Class to hold a supplier or DC in the network

## Storage
[view src](/src/opm_manager/models/sku.py)  
Class to manage the storage and bin locations in a DC

## Supplier
[view src](/src/opm_manager/models/supplier.py)  
Class to represent a supplier

## Transaction
[view src](/src/opm_manager/models/transaction.py)
Class to record transactions in the network. This would be used to capture and export the optimal decisions of an improvement algorithm. 
The transactions could be then copied in real life, or compared against other simulation recommendations / transactions 



