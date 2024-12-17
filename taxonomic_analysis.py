import os
import pandas as pd
import matplotlib.pyplot as plt

# Constants for input/output
INPUT_FILE = './taxonomic_data.csv'
OUTPUT_DIR = './output'

# Ensure the output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Created output directory at {OUTPUT_DIR}")

# Read the input CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        if data.isnull().values.any():
            raise ValueError("Input file contains missing values.")
        return data
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {e}")

# Analyze the data
def analyze_data(data):
    total_count = data.groupby('phylum')['count'].sum().reset_index()
    total_count.columns = ['phylum', 'total_count']

    avg_count = data.groupby('phylum')['count'].mean().reset_index()
    avg_count.columns = ['phylum', 'avg_count_per_species']

    summary = pd.merge(total_count, avg_count, on='phylum')
    return summary

# Save results
def save_results(summary):
    output_path = os.path.join(OUTPUT_DIR, 'summary_statistics.csv')
    summary.to_csv(output_path, index=False)
    print(f"Summary statistics saved to {output_path}")

# Generate a bar chart
def generate_bar_chart(summary):
    plt.figure(figsize=(10, 6))
    plt.bar(summary['phylum'], summary['total_count'], color='skyblue')
    plt.xlabel('Phylum')
    plt.ylabel('Total Species Count')
    plt.title('Total Species Count per Phylum')
    plt.xticks(rotation=45)
    plt.tight_layout()

    chart_path = os.path.join(OUTPUT_DIR, 'total_species_count_chart.png')
    plt.savefig(chart_path)
    print(f"Bar chart saved to {chart_path}")

# Main function
def main():
    print("Loading data...")
    data = load_data(INPUT_FILE)

    print("Analyzing data...")
    summary = analyze_data(data)

    print("Saving results...")
    save_results(summary)

    print("Generating visualizations...")
    generate_bar_chart(summary)

if __name__ == "__main__":
    main()

