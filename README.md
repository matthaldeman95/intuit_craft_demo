# intuit_craft_demo
Craft demo for Intuit interview - Applications Operations Engineer

A Django web application that continuously monitors the availability and load time of the websites:

      https://turbotax.intuit.com/?cid=seq_intuit_tt_click_hd
      https://en.wikipedia.org/wiki/Intuit
      
Features:
- Collects site availability and load time every minute
- Tables and plots display site load times over user configurable time ranges
- If a site is unavailable, an email is sent to myself with the HTTP error code
