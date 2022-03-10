
#!/usr/bin/env python

# Basic infrastruture to parse Siemens scanner logs

import      re





class event_catcher():

   """
      Parser of scanner log files to catch events,
      and determine the date and time of those events.
   """



   def __init__(self, scanner_vendor='siemens', platform_version='ve11c'):

      """
         Right now, this is entry point to general object to parse data from the
         scanners.  However, not sure if this will be a general entry point that
         will 'hand-off' to objects to deal with the different scanner vendors,
         and vendor-specific implementations, or if this object itself will be
         particular to a vendor, and the create corresponding objects for other
         vendors.

         Start with the former case (general object, hand off to vendor specific
         within here).  If it stays this way, change name of module to reflect
         this.
      """

      # Since we are looking for order of events to determine what the scanner
      # is doing, and what state it is in, set up regular expression parsers to
      # get the date and time, and set up list of events to search for.
      if (scanner_vendor == 'siemens'):
         if (platform_version == 've11c'):
            self.event_date_00   = re.compile(r'\d{4}-\d{2}-\d{2}')
            self.event_time_00   = re.compile(r'\d{2}:\d{2}:\d{2}.\d{3}')

            self.scanner_events  = ['MSR_OK', 'MSR_STARTED', 'MSR_SCANNER_FINISHED',
                                    'MSR_ACQ_FINISHED', 'MSR_MEAS_FINISHED',
                                    'EVENT_PATIENT_DEREGISTERED']



   def find_event (self, event_to_find, log_to_search):

      """
         Parse through logs passed to this routine
         (usually an array containing lines of text,
         read in from scanner's log files).
      """

      for current_line in log_to_search:

         # # If any event is in current_line - capture and print.
         # if any(this_event in current_line for this_event in self.scanner_events):

            # # get the event itself, by finding intersection of set of events
            # # possible, and the text in the line.
            # # have to remove parentheses to match to array of events.
            # current_line_elements   = current_line.replace("(","").replace(")","").split()
            # current_event           = set(current_line_elements) & set(self.scanner_events)

         # Make sure we are dealing with event we can handle
         if (event_to_find in self.scanner_events):
            # Then determine if the line contains the event of interest.
            if (event_to_find in current_line):

               # If it does, then get the event's date and time.
               this_event_date         = self.event_date_00.search(current_line)
               this_event_time         = self.event_time_00.search(current_line)

               print ("Event %s happened at date: %s, time: %s" % (event_to_find, this_event_date.group(), this_event_time.group()))

               # return (event_to_find, this_event_date.group(), this_event_time.group())

         else:

            # Have to handle error for event being searched for not in list
            # of events.

            print ("Event %s not in list of possible events!" % event_to_find)
            break

