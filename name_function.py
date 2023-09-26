def get_formatted_name(first_name, last_name, middle=''): # keeping the middle name optional
    
    if middle:
        full_name = f"{first_name} {middle} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

