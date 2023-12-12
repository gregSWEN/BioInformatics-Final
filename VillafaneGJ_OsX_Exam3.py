import os
import matplotlib.pyplot as plt


# Directory where gene files are located
directory = 'YeastGenes'

# Motif I'm searching for
motif = 'AGT'

# Initialize lists to store data for plotting
file_names = []
motif_counts = []

"""
Count the occurrences of a motif within a given DNA sequence.

Parameters:
sequence (str): The DNA sequence to be searched.
motif (str): The motif to search for within the sequence.

Returns:
int: The count of the motif's occurrences in the DNA sequence.
"""


def count_motif_in_sequence(sequence, motif):
    return sequence.count(motif)


# Get a sorted list of all .txt files in the directory
all_files = [f for f in os.listdir(directory) if f.endswith(".txt")]
all_files = sorted(all_files)


# Process only the first 50 files, doing all is too much
for filename in all_files[:51]:
    filepath = os.path.join(directory, filename)

    # Open and read the contents of the file
    with open(filepath, 'r') as file:
        lines = file.readlines()

        # Assuming the first line is a header and skipping it
        # Join the lines to get the sequence and remove newline characters
        sequence = ''.join(lines[1:]).replace('\n', '')

        # Count the occurrences of the motif
        motif_count = count_motif_in_sequence(sequence, motif)
        # Remove the .txt extension for display
        file_names.append(filename.replace('.txt', ''))
        motif_counts.append(motif_count)

# Plotting the data using a bar chart
plt.figure(figsize=(15, 5))  # Set the figure size to be larger
bars = plt.bar(file_names, motif_counts, color='skyblue')  # Create a bar chart

# Add the text label above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval +
             0.5, yval, ha='center', va='bottom')


plt.xlabel('Gene File')  # Set the x-label
plt.ylabel('Count of Motif AGT')  # Set the y-label
plt.title('Motif AGT Count in Gene Sequences for the first 50 files')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
