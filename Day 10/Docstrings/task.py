def format_name(f_name, l_name):
    """This function takes your name as an input and gives title case version of it, As an output."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



