# FloodChecker

### Test mode

To activate test mode:
1. Run the docker file to manage all dependencies
2. Run the seed script.
  * In the command line './scripts/'
  ```
  > python seed.py
  ```
3. Run the MQTT script
  * In the command line './scripts/'
```
> python mqtt.py
```
4. In your browser go to: [http://localhost:8888/frontendWebsite/test.html](http://localhost:8888/frontendWebsite/test.html)
5. Enter the the severity level of your manual test Flood Warning
6. Enter the description of your manual test Flood Warning
7. Enter the message for your manual test Flood Warning
8. Enter the latitude and longditude of your manual test Flood Warning
9. Click 'Add Flood Warning' to add this test data to the list of test inputs
10. Repeat steps 5-9 for as many test inputs as you desire
11. Click 'Test' to be redirected back to the index page, which should show all your test inputs as Flood Warnings on the map, with on-click pop-up descriptions and colour-coding based on severity level.


#Database
Despite large amounts of attempts to install mysql using docker we eventually concluded that it was too much of a constraint, so instead we decided to use the Dragon database service the university uses. We obviously understand that due to this, the website will only be completely functional when on the university campus or using a VPN to connect to the university campus. Since a server will not be created each time all data will be deleted from the server when the seed.py script is used. Hence re entereing the data from the last 7 days to avoid duplicate data.

#Docker
We had a large amount of issues running docker and getting it to work. In the case that it did not work, we used MAMP for it to run and used pyhthon 2.7 for the python scripts.