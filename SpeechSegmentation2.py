import os
directory="C:/Users/Sai Harshitha L/Project_Jio/TextChunks"
directory2="C:/Users/Sai Harshitha L/Project_Jio/TextChunks2"
# directory is the path for the folder which will be containing all the TextChunks of rttm files.
# directory2 is the path for the folder where we will be placing only text data of chunk file separated by @ symbol.
# The main aim of this function is to extract the text from the text chunks and separate the text using @ symbol whenever there's a speaker switching.
def SpeechSeparation(directory,directory2):
    l=[]
    # Creating the directory if it doesn't exist
    os.makedirs(directory2,exist_ok=True)
    # We are appending all the files in a directory to a list l.
    l= os.listdir(directory)
    # To sort the files in an order
    l.sort(key=lambda x: (x.split("_")[0], int(x.split("_")[1].split(".")[0])))
    # Iterating through all the files in the list.
    for file_name in l:
        file_path = os.path.join(directory, file_name)
        file_name=os.path.basename(file_path)
        file_name=file_name.split(".")[0]
        n=file_name.split(".")
        # Extracting the name of file .
        n=n[0]
        words=[]
        currentSpeaker=None
        # opening a file
        with open(file_path, "r") as f:
            for line in f:
                # Removing trailing and leading spaces.
                line=line.strip()
                # Splitting the line into parts and appending it to a list.
                parts=line.split()
                duration_index=-1
                # Iterating over the parts list and extracting duration index
                for i,part in enumerate(parts):
                    if part.startswith("Duration-"):
                        duration_index=i
                # If the duration index is not -1 then we will extract the duration otherwise we will set that to zero.
                if duration_index != -1:
                    duration=float(parts[duration_index].split('-')[1])
                else:
                    duration=0.00
                if(duration==0.00):
                    continue
                # If the duration is not zero then we will apply all thenecessary conditions Removing unecessary punctuation, Extra spaces and then converting the entire                  # text into lower case.
                else:
                    # Extracting speaker id to know who is the speaker.
                    sp=parts[0].split('-')[1]
                    spoken_text=' '.join(parts[duration_index+1:])
                    spoken_text=spoken_text.replace(".","").replace("_","")
                    spoken_text=spoken_text.replace("?","")
                    spoken_text=spoken_text.replace(",","")
                    spoken_text=spoken_text.strip().strip("'")
                    spoken_text=spoken_text.lower()
                    # If the currentSpeaker is none we will set it to sp.
                    if currentSpeaker is None:
                        currentSpeaker = sp
                    # If currentSpeaker is not sp then he is a new speaker so we need to separate the text by using @.
                    elif currentSpeaker != sp:
                        # To make switch between speakers we are appending @.
                        words.append(" @ ")
                        # Making the currentSpeaker as sp.
                        currentSpeaker = sp
                    else:
                    # If there is no speaker switch then we need to append a space.
                        words.append(" ")
                    # Appending the spoken text.
                    words.append(spoken_text)
        # To create a new file_name we are extracting first part of file_name
        new_name=file_name.split(".")
        new_file_name= f"{new_name[0]}.txt"
        print(new_file_name)
        # Joining the new file_name to the new directory.
        file_path2= os.path.join(directory2,new_file_name)
        # Opening the newly created file and writing the content.
        with open(file_path2, "w") as file:
            file.write(''.join(words))
# Calling the function SpeechSeparation.
SpeechSeparation(directory,directory2)     



    
