
'''
   This module attempts to create a common location to set up the list of needed
   / expected generic MRI scanner events, and their corresponding items on the
   various vendors' platforms.

   This will be set as a Pandas data frame, which each vendor as a column label,
   and with each 'event' forming a row.
'''



import pandas



vendors = ['Generic', 'GEHC', 'Siemens']
events  = [['00_Generic', '00_GEHC', '00_Siemens'],
           ['01_Generic', '01_GEHC', '01_Siemens'],
           ['02_Generic', '02_GEHC', '02_Siemens']]

scanner_events_df = pandas.DataFrame.from_records(events, index=None, columns=vendors)
print(scanner_events_df)

