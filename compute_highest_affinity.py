
# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").

  zipped_list = zip(site_list, user_list)  #This will create a tuple

  if(not all(zipped_list)):
      # This will create a dictionary with 'site' as the key and 'set' of'users' who visited this site as value
      dict_site2user = {}
      for key, value in zipped_list:
          if key not in dict_site2user:
              dict_site2user[key] = set()
          dict_site2user[key].add(value)



      # For a cross of each key i.e. 'site' values, calculates the affinity
      dict_affinity = {}
      for key1 in dict_site2user:
          for key2 in dict_site2user:
              if (key1 != key2):
                  dict_affinity[(key1, key2)] = len(dict_site2user[key1] & dict_site2user[key2])

      #Invert the key value pairs in the above dict so that we can find max based on affinity
      dict_affinity_invert = [(value, key) for key, value in dict_affinity.items()]

      #Tuple returned by max is sorted so that duplicate values as (b,d) & (d,b) will not cause error
      return (sorted(max(dict_affinity_invert)[1])[0], sorted(max(dict_affinity_invert)[1])[1])


      print("Dummy print")
      print("Dummy print")
      print("Dummy print")
      print("Dummy print")
      print("Dummy print")
      print("Dummy print")
      print("Dummy print")
      print("Dummy print")
      print("Dummy print")

  else:
      # This will create a dictionary with 'site' as the key and 'set' of'users' who visited this site as value
      dict_site2user = {}
      for key, value in zipped_list:
          if key not in dict_site2user:
              dict_site2user[key] = set()
          dict_site2user[key].add(value)



      # For a cross of each key i.e. 'site' values, calculates the affinity
      dict_affinity = {}
      for key1 in dict_site2user:
          for key2 in dict_site2user:
              if (key1 != key2):
                  dict_affinity[(key1, key2)] = len(dict_site2user[key1] & dict_site2user[key2])

      #Invert the key value pairs in the above dict so that we can find max based on affinity
      dict_affinity_invert = [(value, key) for key, value in dict_affinity.items()]

      #Tuple returned by max is sorted so that duplicate values as (b,d) & (d,b) will not cause error
      return (sorted(max(dict_affinity_invert)[1])[0], sorted(max(dict_affinity_invert)[1])[1])
