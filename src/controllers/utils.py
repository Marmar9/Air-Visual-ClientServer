from datetime import datetime 

def compute_hour_difference(date1_str, date2_str) -> float:
    # Parse the date strings into datetime objects
    date1 = datetime.fromisoformat(date1_str)
    date2 = datetime.fromisoformat(date2_str)
    
    # Compute the difference in hours between the two dates
    hour_difference = (date2 - date1).total_seconds() / 3600
    
    return abs(hour_difference)
