def convert_to_dict(color_names, color_codes):
 

  if len(color_names) != len(color_codes):
    raise ValueError("Lists must have the same length")

  return [{"colorName": name, "colorCode": code} for name, code in zip(color_names, color_codes)]


ListColour = ["Black", "Red", "Maroon", "Yellow"]
ListCode = ["000000", "FF0000", "800000", "FFFF00"]

result = convert_to_dict(ListColour, ListCode)
print(result)
