# Imports necessary modules:
# os: Provides functions for interacting with the operating system.
# pydub.AudioSegment: Allows manipulation of audio files.
import os
from pydub import AudioSegment
directory="C:/Users/Sai Harshitha L/Project_Jio/headset" # Path to the directory containing audio files
directory1="C:/Users/Sai Harshitha L/Project_Jio/TextChunks"  # Path to the directory containing text chunk files
directoryone="C:/Users/Sai Harshitha L/Project_Jio/AudioChunk1"  # Path to the output directory
def seconds_to_ms(time):
    return int(time*1000)
def generate_silence(duration_ms):
    silence_segment = AudioSegment.silent(duration=duration_ms)
    return silence_segment
def ComAudio(directory,directory1,directoryone):
    os.makedirs(directoryone,exist_ok=True)  # Create the output directory if it doesn't exist
    k= os.listdir(directory1)
    k.sort(key=lambda x: (x.split("_")[0], int(x.split("_")[1].split(".")[0])))
    # Sort the text chunk files based on a custom sorting key:
    # The key extracts the information before the first underscore (_) and sorts numerically based on the second part
    for filename in k:
        l=[] # Initialize a list to store audio files matching the current text chunk
        file_path = os.path.join(directory1,filename)  # Get the path of the current text chunk file
        name=os.path.basename(file_path)
        name1=name.split(".")[0] # Extract the filename without extension
        name=name.split("_")  # Split the filename by underscores
        h=name[0] # Extract the first part of the filename
        audio_path = os.path.join(directory,h)  # Construct the path to the audio directory based on the first part
        audio_path1=os.path.join(audio_path,"audio") # Construct the path to the specific audio subdirectory
        for file_name in os.listdir(audio_path1):
            f= os.path.join(audio_path1, file_name)
            n=os.path.basename(f)
            new=n.split(".")[0]
            if(h==new):
                l.append(n)
                # Append the audio file name to the list if it matches the current text chunk
        output_audio = AudioSegment.empty() # Initialize an empty audio segment to store the combined audio
        with open(file_path, "r") as f1:
            lines = f1.readlines()
            firstline=""
            firstline=lines[0]
            firstline=firstline.split(" ")
            start_time0=firstline[1]
            start_time0= float(start_time0.split("-")[1])
            et=seconds_to_ms(start_time0)-1
            # Extract the start time from the first line of the text chunk file
            # Convert the start time to milliseconds and set it as the initial end time
            for i in lines:
                h1=i.split()
                k1=h1[0].split("-")[1]
                # Extract the relevant information from each line of the text chunk
                if(k1=='A'):
                    while(True):
                        start_time = float(h1[1].split("Start_time-")[1].split()[0])
                        end_time = float(h1[2].split("End_time-")[1].split()[0])
                        audio_path2=l[0]
                        f2= os.path.join(audio_path1,audio_path2)
                        audio=AudioSegment.from_file(f2)
                        start_ms = seconds_to_ms(start_time)
                        end_ms = seconds_to_ms(end_time)
                        extracted_audio = audio[start_ms:end_ms]
                         # Extract the specified portion of the audio segment
                        if(start_ms==et+1):
                            output_audio += extracted_audio
                            et=end_ms
                            break
                            # If the extracted audio segment starts immediately after the previous segment,
                            # append it to the output audio and update the end time
                        else:
                            et1=et+1
                            start_ms1=start_ms-1
                            d=start_ms1-et1
                            empty_audio = generate_silence(d)
                            output_audio=output_audio+empty_audio
                            et=start_ms1
                            continue
                            # If there is a gap between the previous segment and the current segment,
                            # fill the gap with silence and update the end time
                elif(k1=='B'):
                    while(True):
                        start_time = float(h1[1].split("Start_time-")[1].split()[0])
                        end_time = float(h1[2].split("End_time-")[1].split()[0])
                        audio_path2=l[1]
                        f2= os.path.join(audio_path1,audio_path2)
                        audio=AudioSegment.from_file(f2)
                        start_ms = seconds_to_ms(start_time)
                        end_ms = seconds_to_ms(end_time)
                        extracted_audio = audio[start_ms:end_ms]
                        # Extract the specified portion of the audio segment
                        if(start_ms==et+1):
                            output_audio += extracted_audio
                            et=end_ms
                            break
                            # If the extracted audio segment starts immediately after the previous segment,
                            # append it to the output audio and update the end time
                        else:
                            et1=et+1
                            start_ms1=start_ms-1
                            d=start_ms1-et1
                            empty_audio = generate_silence(d)
                            output_audio=output_audio+empty_audio
                            et=start_ms1
                            continue
                            # If there is a gap between the previous segment and the current segment,
                            # fill the gap with silence and update the end time
                            
                elif(k1=='C'):
                    while(True):
                        start_time = float(h1[1].split("Start_time-")[1].split()[0])
                        end_time = float(h1[2].split("End_time-")[1].split()[0])
                        audio_path2=l[2]
                        f2= os.path.join(audio_path1,audio_path2)
                        audio=AudioSegment.from_file(f2)
                        start_ms = seconds_to_ms(start_time)
                        end_ms = seconds_to_ms(end_time)
                        extracted_audio = audio[start_ms:end_ms]
                        # Extract the specified portion of the audio segment
                        if(start_ms==et+1):
                            output_audio += extracted_audio
                            et=end_ms
                            break
                            # If the extracted audio segment starts immediately after the previous segment,
                            # append it to the output audio and update the end time
                        else:
                            et1=et+1
                            start_ms1=start_ms-1
                            d=start_ms1-et1
                            empty_audio = generate_silence(d)
                            output_audio=output_audio+empty_audio
                            et=start_ms1
                            continue
                            # If there is a gap between the previous segment and the current segment,
                            # fill the gap with silence and update the end time
                elif(k1=='D'):
                    while(True):
                        start_time = float(h1[1].split("Start_time-")[1].split()[0])
                        end_time = float(h1[2].split("End_time-")[1].split()[0])
                        audio_path2=l[3]
                        f2= os.path.join(audio_path1,audio_path2)
                        audio=AudioSegment.from_file(f2)
                        start_ms = seconds_to_ms(start_time)
                        end_ms = seconds_to_ms(end_time)
                        extracted_audio = audio[start_ms:end_ms]
                        # Extract the specified portion of the audio segment
                        if(start_ms==et+1):
                            output_audio += extracted_audio
                            et=end_ms
                            break
                            # If the extracted audio segment starts immediately after the previous segment,
                            # append it to the output audio and update the end time
                        else:
                            et1=et+1
                            start_ms1=start_ms-1
                            d=start_ms1-et1
                            empty_audio = generate_silence(d)
                            output_audio=output_audio+empty_audio
                            et=start_ms1
                            continue
                            # If there is a gap between the previous segment and the current segment,
                            # fill the gap with silence and update the end time
                elif(k1=='E'):
                    while(True):
                        start_time = float(h1[1].split("Start_time-")[1].split()[0])
                        end_time = float(h1[2].split("End_time-")[1].split()[0])
                        audio_path2=l[4]
                        f2= os.path.join(audio_path1,audio_path2)
                        audio=AudioSegment.from_file(f2)
                        start_ms = seconds_to_ms(start_time)
                        end_ms = seconds_to_ms(end_time)
                        extracted_audio = audio[start_ms:end_ms]
                        # Extract the specified portion of the audio segment
                        if(start_ms==et+1):
                            output_audio += extracted_audio
                            et=end_ms
                            break
                            # If the extracted audio segment starts immediately after the previous segment,
                            # append it to the output audio and update the end time
                        else:
                            et1=et+1
                            start_ms1=start_ms-1
                            d=start_ms1-et1
                            empty_audio = generate_silence(d)
                            output_audio=output_audio+empty_audio
                            et=start_ms1
                            continue
                            # If there is a gap between the previous segment and the current segment,
                            # fill the gap with silence and update the end time
                else:
                    while(True):
                        start_time = float(h1[1].split("Start_time-")[1].split()[0])
                        end_time = float(h1[2].split("End_time-")[1].split()[0])
                        audio_path2=l[5]
                        f2= os.path.join(audio_path1,audio_path2)
                        audio=AudioSegment.from_file(f2)
                        start_ms = seconds_to_ms(start_time)
                        end_ms = seconds_to_ms(end_time)
                        extracted_audio = audio[start_ms:end_ms]
                        # Extract the specified portion of the audio segment
                        if(start_ms==et+1):
                            output_audio += extracted_audio
                            et=end_ms
                            break
                            # If the extracted audio segment starts immediately after the previous segment,
                            # append it to the output audio and update the end time
                        else:
                            et1=et+1
                            start_ms1=start_ms-1
                            d=start_ms1-et1
                            empty_audio = generate_silence(d)
                            output_audio=output_audio+empty_audio
                            et=start_ms1
                            continue
                            # If there is a gap between the previous segment and the current segment,
                            # fill the gap with silence and update the end time
        new_file_name=name1+".wav" # Construct the output file name
        output_path = os.path.join(directoryone,new_file_name)  # Construct the output file path
        output_audio.export(output_path,format="wav") # Export the combined audio as a WAV file
        print(new_file_name," exported successfully") # Print success message for exported file
    print("ALL ARE DONE") # Print completion message                    
ComAudio(directory,directory1,directoryone)  # Call the main function