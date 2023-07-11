import argparse

def get_input_args():
    parser = argparse.ArgumentParser()

    #3 command line arguments using add_argument() from ArguementParser method
    parser.add_argument('--dir', type=str, default='home/pet_images', help='path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='chosen model')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='text file that has dognames')
    
    # parser.parse_args() parsed argument collection that I created with this function 
    return parser.parse_args()