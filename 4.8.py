# Define the time_string function
def time_string(hours, minutes, time_format):
    if time_format == '24':
        # Format time in 24-hour format
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        # Convert to 12-hour format
        period = 'am' if hours < 12 else 'pm'
        hours_12 = hours % 12
        hours_12 = 12 if hours_12 == 0 else hours_12  # Handle 12:xxam and 12:xxpm
        return f"{hours_12}:{minutes:02}{period}"
    else:
        return "Invalid time format"
# Run test
print(time_string(0,7,'12'))
