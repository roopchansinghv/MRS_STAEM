
# inspired by examples at:
#
#   https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/

import asyncio
import requests



scanner_poll_interval = 1.0   # in seconds
scanner_state_src_url = 'http://localhost:5000/scanner_state'



async def poll_scanner_state():

   while True:

      await asyncio.sleep(scanner_poll_interval)

      try:

         state = requests.get(scanner_state_src_url)

         data = state.json()
         print(data['scanner AE Title'] + " is in state " + data['scanner_state'] + " and occurred at time: " + data['scanner_last_event_time'])
         print(data)

      except:

          print("Couldn't reach URL: %s to determine scanner state." % scanner_state_src_url)



if __name__ == "__main__":

   loop = asyncio.get_event_loop()

   try:
      asyncio.ensure_future(poll_scanner_state())
      loop.run_forever()
   except KeyboardInterrupt:
      pass
   finally:
      print("Stopping task.")
      loop.close()

