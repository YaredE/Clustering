import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from fuzzywuzzy import fuzz

def fuzzy_cluster_csv(filename, column_name, num_clusters):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(filename)
    
    # Clean and preprocess the data
    data[column_name] = data[column_name].astype(str)
    
    # Calculate fuzzy matching scores between each pair of strings
    def fuzzy_similarity(str1, str2):
        return fuzz.token_set_ratio(str1, str2)
    
    # Create a similarity matrix
    similarity_matrix = pd.DataFrame([[fuzzy_similarity(row1[column_name], row2[column_name]) 
                                      for _, row2 in data.iterrows()] 
                                     for _, row1 in data.iterrows()])
    
    # Perform clustering using KMeans
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data[column_name])
    
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(vectors)
    
    # Add cluster labels to the DataFrame
    data['cluster'] = kmeans.labels_
    
    return data

# Example usage
filename = 'your_file.csv'
column_name = 'your_column'
num_clusters = 3
clustered_data = fuzzy_cluster_csv(filename, column_name, num_clusters)
print(clustered_data)
