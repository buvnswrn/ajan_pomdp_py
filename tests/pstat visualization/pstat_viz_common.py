import pstats
import matplotlib.pyplot as plt

# Load the first pstat file
stats1 = pstats.Stats('../results/system_test_with_all_ajan_model_not_optimized.pstat')

# Extract the "rdflib" function names and time spent for functions
function_times1 = {k[2]: v[2] for k, v in stats1.stats.items() if "rdflib" in k[0]}

# Sort the functions by time spent and get the top 10
function_times1_sorted = dict(sorted(function_times1.items(), key=lambda item: item[1], reverse=True))
function_times1_top_10 = dict(sorted(function_times1.items(), key=lambda item: item[1], reverse=True)[:10])

# Repeat the process for the second pstat file
stats2 = pstats.Stats('../results/system_test_with_all_ajan_model_optimized.pstat')
function_times2 = {k[2]: v[2] for k, v in stats2.stats.items() if "rdflib" in k[0]}
function_times2_sorted = dict(sorted(function_times2.items(), key=lambda item: item[1], reverse=True))
function_times2_top_10 = dict(sorted(function_times2.items(), key=lambda item: item[1], reverse=True)[:10])

# Get the function names that are in the top 10 for both files
common_functions = set(function_times1_top_10.keys()).intersection(set(function_times2_top_10.keys()))
all_functions = set(function_times1_top_10.keys()).union(set(function_times2_top_10.keys()))

# For each function, get the time spent from both files
times1 = [function_times1_sorted.get(func, 0) for func in all_functions]
times2 = [function_times2_sorted.get(func, 0) for func in all_functions]


# For each common function, get the time spent from both files
common_times1 = [function_times1[func] for func in common_functions]
common_times2 = [function_times2[func] for func in common_functions]

# Plot the time spent for each function in both files
x = range(len(common_functions))
plt.bar(x, common_times1, width=0.4, label='Not Optimized', color='b', align='center')
plt.bar(x, common_times2, width=0.4, label='Optimized', color='r', align='edge')
plt.xlabel('Function')
plt.ylabel('Time spent (seconds)')
plt.title('Time spent in common functions for both queries')
plt.xticks(x, common_functions, rotation=90)  # Rotate the x-axis labels for readability
plt.legend()
plt.show()
