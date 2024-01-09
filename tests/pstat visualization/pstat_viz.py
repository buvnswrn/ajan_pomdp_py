import pstats
import matplotlib.pyplot as plt

stats = pstats.Stats('../results/system_test_with_all_ajan_model_not_optimized.pstat')

# Extract the data you're interested in
# For example, let's extract the total time spent in each function
rdflib_functions = {'evalQuery', 'evalPart', 'evalConstructQuery', 'evalLeftJoin', 'evalLazyJoin', 'evalBGP',
                    'forget', 'triples', 'operators', 'eval', 'preParse', 'value'}
custom_functions = {'distance', 'near'}
function_times = {k[2]: v[2] for k, v in stats.stats.items() if k[0].__contains__("rdflib")}

# Sort the functions by time spent
function_times = dict(sorted(function_times.items(), key=lambda item: item[1], reverse=True))
# Plot the data
plt.bar(function_times.keys(), function_times.values())
plt.xlabel('Function')
plt.ylabel('Time spent (seconds)')
plt.title('Time spent in each function')
plt.xticks(rotation=90)  # Rotate the x-axis labels for readability
plt.show()