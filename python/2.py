def find_matching_strings(string_list):


  for index, string in enumerate(string_list):
    if isinstance(string, str) and string[0] == string[-1]:
      print(f"String: {string}, Index: {index}")

if __name__ == "__main__":
  A = ['abc', 'xyz', 'aba', '1221']
  find_matching_strings(A)
