import urllib.request
urls = open("C://Users//Kamio//.git//pyTasks//htmlDownloading//url.txt", "r")
for url in urls.readlines():
    if url.strip() != '':
        htmlCodeOfPage = urllib.request.urlopen(url)
        print(url)
        fileToWrite = open("C://Users//Kamio//.git//pyTasks//htmlDownloading///htmls/" + str(url).strip()[8:] + '.html', "w")
        for line in htmlCodeOfPage.readlines():
            fileToWrite.write(str(line))
        fileToWrite.close()

            
        
