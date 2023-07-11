
from os import listdir

def get_pet_labels(image_dir):

    in_files = listdir(image_dir)
    
    results_dic = dict()
   
    for idx in range(0, len(in_files), 1):
       
       if in_files[idx][0] != ".":
           
           pet_label = ""

           # Processes each filename in the in_files list to extract the dog breed name
           filename_parts = in_files[idx].lower().split('_')
           for word in filename_parts:
               if word.isalpha():
                   pet_label += word + " "
           pet_label = pet_label.strip()

           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    # Replace None with the results_dic dictionary that you created with this function
    return results_dic