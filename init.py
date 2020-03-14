import sys
import pandas

def main(csv_path, json_path):
    results = pandas.read_csv('test.csv')
    print(results)

if __name__== "__main__":
  if(len(sys.argv) < 3):
    raise Exception("This code takes two argument i.e. csv and json \
        file path for ingredients and recipes respectively")
  main(int(sys.argv[1], sys.argv[2]))