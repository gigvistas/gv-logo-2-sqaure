from square_img_using_PIL import squareify
import os

def run_all_tests(): # checks for transparency in an image
    directory = os.fsencode(os.path.join(os.path.dirname(__file__), 'assets'))
    out_path = os.path.join(os.path.dirname(__file__), 'test_output')
    print(directory)
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if not filename.startswith('.') and (os.path.isdir(filename) is False):
            print("Testing ",filename)
            squareify("assets/"+filename,200, out_path, os.path.splitext(filename)[0])

def main():
    print("Running all tests")
    run_all_tests()

if __name__ == "__main__":
    main()