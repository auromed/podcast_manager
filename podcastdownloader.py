#Podcast Downloader 
#Ver 0.0.1

import urllib2

def download_podcast(url, filename):
	call_download = urllib2.urlopen(url)
	output = open(filename, 'wb')
	output.write(call_download.read())
	output.close
	
current_url = "http://media.blubrry.com/packetpushers/p/content.blubrry.com/packetpushers/Show-186-The_Silicon_Inside_Your_Network_Device-Part_2.mp3"
current_filename = "packetpushers187.mp3"
	
download_podcast(current_url, current_filename)

