# lab3task2
The developed module parses an json object (file) obtained using the Twitter API.
The module contains a function get_multiple_fields_by(json_data: dict, detail=False) to provide access to various parts of the json object.
For example, get_user_choice_by(inner_data) asks the user to enter the dictionary key whose meaning he wants to view.
API returns a specific object the specific values of which a user want to view. We assume that the user knows what fields are in the object,
but the programme prompts with a set of fields from which the user can choose the desired data.
In response to the user-entered key, the programme shows the corresponding value.
There are cases in which the program behaves differently:
- if a value corresponding to the key is also an object - in this case the programme informs the user that it is also an object and display the available keys
- if a value is a list the programme reports that it is a list, asks what the number of the list item to display
