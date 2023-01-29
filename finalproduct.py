from machine import ADC, Pin
import time

# Logic to read from SMS
soil = ADC(Pin(26))
min_moisture=19000 
max_moisture=38500

# Logic for Logging to File
file = open("logs.txt", "a")

# Function and Variables for Starting/Stopping Relay and Water Pump
SECONDS_TO_WATER = 20
RELAY = Pin(18, Pin.OUT)
RELAY.high()
def water_plant(relay, seconds):
    relay.toggle()
    print("Plant is being watered!")
    time.sleep(seconds)
    print("Watering is finished!")
    relay.toggle()

# Boolean Logic
while True:
    moisture = (max_moisture-soil.read_u16())*100/(max_moisture-min_moisture)
    if moisture < 5: # If Moisture is lower than that of Somewhat Wet Plant used in Calibration (37525 in ADC units)
        print(moisture)
        water_plant(RELAY, SECONDS_TO_WATER)
        file.write("Watered plant, moisture was at " + str(moisture) + "\n")
        file.flush()
        time.sleep(5400) # Sleep for 1 and a half hours

        
    else: 
        file.write("Plant is sufficiently watered at a value of " + str(moisture) + "\n")
        file.flush()
        time.sleep(900) # Sleep for 15 minutes



