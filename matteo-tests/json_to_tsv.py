import json
import csv

def json_to_tsv(json_file, tsv_file):
    # Read the JSON file
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Open the TSV file for writing
    with open(tsv_file, 'w', encoding='utf-16', newline='', errors='ignore') as f:
        tsv_writer = csv.writer(f, delimiter='\t')

        # Write the header
        tsv_writer.writerow(['document ID', 'title', 'text'])

        # Write the rows
        for doc_id, content in data.items():
            title = content['title']#.encode('utf-8')
            text = content['text']#.encode('utf-8')
            tsv_writer.writerow([doc_id, title, text])


if __name__ == "__main__":
    json_file = 'wiki_musique_corpus_full.json'
    tsv_file = '../data/doc/dataset/wiki_musique_corpus_full.tsv'
    json_to_tsv(json_file, tsv_file)
