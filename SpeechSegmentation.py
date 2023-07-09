import os
directorySpeech="C:/Users/Sai Harshitha L/Project_Jio/stt_sv_rttmfiles"
directorytwo="C:/Users/Sai Harshitha L/Project_Jio/TextChunks"
# The directorySpeech folder is the path to the folder containing speech files in rttm format.
# directorytwo is the location to the folder where our textchunks will be placed after segmentation.
# The above folder paths will be passed to the speechSegmentation function to divide the given file into chunks.
def speechSegmentation(directorySpeech,directorytwo):
    # Travesrsing through all the files in the given folder
    for file_name in os.listdir(directorySpeech):
        file_path = os.path.join(directorySpeech, file_name)
        file_name=os.path.basename(file_path)
        print(file_name)
        os.makedirs(directorytwo,exist_ok=True)
        datalist=[]
        # Opening a single file from the directory
        with open(file_path, "r") as f:
            for line in f:
           # We're removing spaces and splitting words before appending them to a list called parts.
                line=line.strip()
                parts=line.split()
                #If the line starts with speaker then we are trying to fetch the indexes of Start_time, End_time, duration_index, SpeakerID
                if line.startswith('SPEAKER'):
                    start_time_index=-1
                    end_time_index=-1
                    duration_index=-1
                    spidindex=-1
                    s=('A','B','C','D','E')
                    #Iterating over the parts list and storing their corresponding indexes.
                    for i,part in enumerate(parts):
                        if part.startswith(s):
                            spidindex=i
                        if part.startswith("Start_time-"):
                            start_time_index=i
                        if part.startswith("End_time-"):
                            end_time_index=i
                        if part.startswith("Duration-"):
                            duration_index=i
                    # If the indexes values which we have fetched is not -1 then we will be extracting the values otherwise we will continue the same process.
                    if spidindex!=-1:
                        spiId=parts[1]
                    if start_time_index!=-1:
                        start_time=float(parts[start_time_index].split('-')[1])
                    else:
                        continue
                    if end_time_index!=-1:
                        end_time=float(parts[end_time_index].split('-')[1])
                    else:
                        continue
                    if duration_index != -1:
                        duration=float(parts[duration_index].split('-')[1])
                    else:
                        duration=0.00
                    # If the duration is 0.00 then we will not process the text.
                    if duration==0.00:
                        continue
                    # If the duration is not 0.00 then we will extract the speech part and then we will be removing unecessary punctuation and removing trailing                               # and leading spaces and then we are converting the text into lower case.
                    else:
                        spoken_text=' '.join(parts[duration_index+1:])
                        spoken_text=spoken_text.replace(".","").replace("_","")
                        spoken_text=spoken_text.replace("?","")
                        spoken_text=spoken_text.replace(",","")
                        spoken_text=spoken_text.strip().strip("'")
                        spoken_text=spoken_text.lower()
                        strings={}
                        # Taking a empty dictionary called String and then we are appending Start_time, End_time, Duration, Speech_Spoken to it. And then we are appending                         # it to a dalist which is of the type list.
                        strings={"Speaker":spiId,"Start_time":start_time,"End_time":end_time,"duration":duration,"Speech_Spoken":spoken_text}
                        datalist.append(strings)
        # As we need to divide the chunk into 20 sec duration we need to initialize it into 20.00
        Seg_duration=20.0
        # For the segmentation of given file into chunk we are using the function divsionOfChunksSpeech and to that function we are passing datalist, Seg_duration,                # file_name
        divsionOfChunksSpeech(datalist,Seg_duration,file_name)
# Every time to create a new chunk we will use the function create_chunk which will get the inputs from divsionOfChunksSpeech.
def create_chunk(sp,start_time, end_time, duration,spoken_text):
    return f"Speaker-{sp} Start_time-{start_time:.2f}  End_time-{end_time:.2f}  Duration-{duration:.2f}  {spoken_text}\n"
def divsionOfChunksSpeech(datalist,Seg_duration,file_name):
    c=1
    # Let pres_chunk, pres_duration be 0.00 or null
    pres_chunk=""
    pres_duration=0.00
    # Now we are iterating over the datalist and storing the required values speakerid, start_time, end_time, duaration, Speech_Spoken.
    for item in datalist:
        sp=item["Speaker"]
        st=item["Start_time"]
        et=item["End_time"]
        d=item["duration"]
        ss=item["Speech_Spoken"]
        # If the duration of the single speaker is greater than 20 secs then it will be created as a single chunk.
        if d>Seg_duration:
            # createchunk function retuen a new chunk with the specified input parameters.
            pres_chunk+= create_chunk(sp,st,et,d,ss)
            pres_duration+= d
        # Checking if the duration are summing upto 20 secs and then creating a chunk.
        elif pres_duration+d<=Seg_duration:
            # createchunk function retuen a new chunk with the specified input parameters.
            pres_chunk+= create_chunk(sp,st,et,d,ss)
            pres_duration+= d
        # After the segmentation we are creating a new txt file and writing the current chunk to the new file. We are having a count varibale which gets incremented After         # the division of eacha nd every new chunk.
        else:
            new_name=file_name.split(".")
            new_file_name= f"{new_name[0]}_{c}.txt"
            file_path = os.path.join(directorytwo,new_file_name)
            with open(file_path, "a") as file:
                file.write(pres_chunk)
            # createchunk function retuen a new chunk with the specified input parameters.
            pres_chunk =create_chunk(sp,st,et,d,ss)
            pres_duration =d
            c+= 1
    # Finally If we are left with any chunk then we are writing that chunk to the txt file.
    if pres_chunk:
        new_name=file_name.split(".")
        new_file_name= f"{new_name[0]}_{c}.txt"
        file_path = os.path.join(directorytwo,new_file_name)
        with open(file_path, "w") as file:
            file.write(pres_chunk)
speechSegmentation(directorySpeech,directorytwo)
