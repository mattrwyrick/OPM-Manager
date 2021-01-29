# Availability
Availability of the network after exercising the weeks worth of supplier shipments and demand. Availability is the 
weighted % demand based on product frequency (e.g. high moving product success affects availability more than less 
frequent items)

The availability results show results based off pure forecasting, and do not ship product between DCs or order more from 
suppliers. There are plans to introduce an improvement algorithm to redistribute excess in the network and order more 
materials for under estimated forecasts.

## Material Frequency and Availability
* <b>5</b> <i>(Highest Moving)</i>
  * 38% influence on availability
* <b>4</b> <i>(High Moving)</i>
  * 27% influence on availability
* <b>3</b> <i>(Moderate Moving)</i>
  * 20% influence on availability
* <b>2</b> <i>(Slow Moving)</i>
  * 10% influence on availability
* <b>1</b> <i>(Slowest Moving)</i>
  * 5% influence on availability
  
## Improvements 
* Relative scoring (e.g. DC score is also dependent on the health of neighboring DCs)
* Incorporate more weighted material scoring (e.g. cost of item, not just high/low moving)

## Simulation Results

[How forecasts were created in this simulated environment](/docs/forecast.md)

### Tight Forecast Availability (No Adjustments)
<b>Week 1</b> 100.0%  
<b>Week 2</b> 100.0%  
<b>Week 3</b> 99.872%  
<b>Week 4</b> 98.861%  
<b>Week 5</b> 97.54%  
<b>Week 6</b> 90.14%  
<b>Week 7</b> 61.995%  
<b>Week 8</b> 33.489%  
<b>Week 9</b> 16.568%  
<b>Week 10</b> 7.939%   

### Moderate Forecast Availability (No Adjustments)
<b>Week 1</b> 99.289%  
<b>Week 2</b> 93.981%  
<b>Week 3</b> 88.534%  
<b>Week 4</b> 62.255%  
<b>Week 5</b> 29.646%  
<b>Week 6</b> 11.43%  
<b>Week 7</b> 4.971%  
<b>Week 8</b> 2.004%  
<b>Week 9</b> 0.955%  
<b>Week 10</b> 0.632% 

### Volatile Forecast Availability (No Adjustments)
<b>Week 1</b> 90.022%  
<b>Week 2</b> 83.328%  
<b>Week 3</b> 68.517%  
<b>Week 4</b> 44.899%  
<b>Week 5</b> 22.738%  
<b>Week 6</b> 11.047%  
<b>Week 7</b> 5.728%  
<b>Week 8</b> 2.764%  
<b>Week 9</b> 1.628%  
<b>Week 10</b> 0.933% 

## Why do the Seasons end with Low Availability?
Right now the system orders the forecast and makes no adjustments based on actual demand. The demand is also set to be between 
70% to 115% of the networks capacity even if perfectly forecasted. With a product dense supply chain network, and no management 
of ordering/redistributing mid-season, over ordered products begin taking up space in the DCs and no effort to reduce these materials -
in favor of ones that would help reduce failures - is made. 

Hill climbing methods testing optimal STOs and POs to maximise availability would be the next phase of this project, and would 
prevent the inevitable decline of availability given the parameters in this simulation.