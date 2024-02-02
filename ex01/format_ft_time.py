import datetime
import time

# Get the current time in seconds since the epoch
seconds_since_epoch = time.time()

# Print the time in seconds since the epoch
print(f"Seconds since January 1, 1970: {seconds_since_epoch} or {seconds_since_epoch:.2e} in scientific notation")

# Get the current time
current_time = datetime.datetime.now()

# Print the current time in the specified format
print(current_time.strftime("%b %d %Y"))