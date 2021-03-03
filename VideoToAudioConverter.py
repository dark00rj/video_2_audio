imimport moviepy.editor as mp 
  
# Insert Local Video File Path  
clip = mp.VideoFileClip(r"D:/VideoSongs/alan walker/Alan Walker - The Spectre.mp4") 
  
# Insert Local Audio File Path 
clip.audio.write_audiofile(r"D:/VideoSongs/alan walker/Alan Walker - The Spectre.mp3")
