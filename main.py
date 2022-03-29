from pytube import*
#يسأل عن رابط المقطع
link = input("Enter the video link:  ")
ytdata = YouTube(link)
Path = r'C:\Users\person\Videos' #download path , edit this to ur folder path

#يظهر التفاصيل
print("Title: ",ytdata.title)
print("Number of views: ",ytdata.views)
print("Length of video: ",ytdata.length)
print("Rating of video: ",ytdata.rating)
#ياخذ المقطع بأعلى جودة ممكنة
ys = ytdata.streams.get_highest_resolution()
#يحمل
print("Downloading...")
ys.download(Path)
print("Done!")

