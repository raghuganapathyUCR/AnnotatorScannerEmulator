import wget
import os
class AnnotatorScannerEmulator:
    def __init__(self, pathToTargetProject):
        self.pathToTargetProject = pathToTargetProject
    def getJarFileFromNet(self, url, path):
        # download the jar file
        try:
            # Check if the temp folder doesn't exist
            if(not os.path.exists("./temp")):
                # Create the temp folder
                print("Creating temp folder")
                os.mkdir("./temp")
            else:
                path = "./temp/"+path
                # Add the path to object
                self.pathToJar = path   
                # Folder exists, Check if the file already exists
                if(os.path.exists(path)):
                    print("File already exists")
                    return True 
                print("Temp folder already exists")
            # Update the path
            path = "./temp/"+path
            # Add the path to object
            self.pathToJar = path
            # Download the file
            wget.download(url,path)
        except IOError:
            # Error downloading the file - raise IOError
            raise IOError("Error downloading jar file from " + url)
        
        # check if the file was downloaded
        try:
            # Try to open the file to validate it was downloaded
            f = open(path, "r")
            # Close the file
            f.close()
        except IOError:
            # If we couldn't open the file, raise FileNotFoundError
            raise FileNotFoundError("Error downloading jar file from " + url)
        # If we got here, the file was downloaded successfully
        return True

    def runAnnotator(self):
        buildCommand = "java -jar " + self.pathToJar + " --build-command " + "cd {} && ./gradlew build -x test".format(self.pathToTargetProject)
        print("\n")
        print(buildCommand)
    
if __name__ == "__main__":

    pathToTargetProject = "/Users/raghuganapathy/Desktop/JavaProjects/exttemp"

    a = AnnotatorScannerEmulator(pathToTargetProject=pathToTargetProject)
    # Jar Metadata
    jarUrl = "https://repo.maven.apache.org/maven2/edu/ucr/cs/riple/annotator/annotator-core/1.3.6/annotator-core-1.3.6.jar"
    jarName = "annotator-core-1.3.6.jar"
    # Download the jar file and store it in the temp folder
    a.getJarFileFromNet(jarUrl, jarName)

    # Run the annotator
    a.runAnnotator()