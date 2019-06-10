# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

# MAPPING 
print("--------------")

mapped_list = [n * 100 for n in my_numbers]
print("MAPPED: ", mapped_list)

# FILTERING
print("--------------")
filtered_list = [n for n in my_numbers if n > 3]
print("FILTERED LIST W/ MATCHES ", filtered_list)

print("--------------")
no_matches = [n for n in my_numbers if n > 8]
print("FILTERED LIST W/O MATCHES ", no_matches)

# MAPPING AND FILTERING

print("--------------")
map_filter = [n * 100 for n in my_numbers if n > 3]
print ("MAPPED AND FILTERED LIST: ", map_filter)