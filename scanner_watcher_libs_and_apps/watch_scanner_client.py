
# inspired by examples at:
#
#   https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import asyncio
import requests
import datetime



state_poll_interval = 1.0   # in seconds
state_src_url       = 'http://localhost:5000/scanner_state'
current_state_dict  = {}



async def poll_state(state_url, polling_interval):

   while True:

      await asyncio.sleep(polling_interval)

      try:

         # get date and time at which scanner state is polled
         current_state_check_date_time = datetime.datetime.now().strftime("%Y_%m_%d_%H:%M:%S")

         # poll URL where state is published to
         state = requests.get(state_url)

         # Convert published JSON struct to Python dictionary
         data = state.json()
         # print(type(data))
         # print(data)
         # Extract desired information from packet
         current_state_dict = data['all_events']
         print (str(current_state_dict))
         print('   \n' + data['scanner AE Title'] + " is in state " + data['scanner_state'] + " and occurred at time: " + data['scanner_last_event_time']
               + ' detected at ' + current_state_check_date_time + '\n')

      except:

          print("Couldn't reach URL: %s to determine scanner state." % state_url)



if __name__ == "__main__":

   loop = asyncio.get_event_loop()

   try:
      asyncio.ensure_future(poll_state(state_src_url, state_poll_interval))
      loop.run_forever()
   except KeyboardInterrupt:
      pass
   finally:
      print("Stopping task.")
      loop.close()

