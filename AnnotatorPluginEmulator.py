import wget
import os
class AnnotatorPluginEmulator:
    def getJarFileFromNet(self, url, path):
        # download the jar file
        try:
            if(not os.path.exists("./temp")):
                print("Creating temp folder")
                os.mkdir("./temp")
            else:
                path = "./temp/"+path

                # Check if the file already exists
                if(os.path.exists(path)):
                    print("File already exists")
                    return True 
                print("Temp folder already exists")
            path = "./temp/"+path
            self.pathToJar = path
            wget.download(url,path)
        except IOError:
            raise IOError("Error downloading jar file from " + url)
        
        # check if the file was downloaded
        try:
            f = open(path, "r")
            f.close()
        except IOError:
            raise FileNotFoundError("Error downloading jar file from " + url)
        
        return True

    def buildAnnotatorFlags(self, jarFile, classPath, classToRun, args):
        flags = ["java", "-cp", classPath, classToRun]
        flags.extend(args)
        return flags
if __name__ == "__main__":
    a = AnnotatorPluginEmulator()
    a.getJarFileFromNet("https://repo.maven.apache.org/maven2/edu/ucr/cs/riple/annotator/annotator-core/1.3.6/annotator-core-1.3.6.jar", "1.jar")
