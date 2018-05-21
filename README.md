# Unpacker

Idea behind this tool is to take pack of models, which might consist of dozens of models and textures and different exchange formats put in the same place, and unpack them to separate folders depending on the naming of files and folder structure.

## Getting Started

example code:
test = Unpack()

for path in test.oneDeep():
    print(path, len(os.listdir(os.path.join(test.path, path))))
    test.twoDeep(path)
    test.exceptions(path)
    
    test.rename(path, "Test Pack Name - ")
    #test.rename2(path, "Test Pack Name - ")
    
    test.exceptionsList = {}
    test.objectsList = []
    
    test.archive(path)

test.deleteTemp()


### Prerequisites

Python 3+

## Authors

* **Vilius Juodziukynas** - *Initial work* - [viliusddd](https://github.com/viliusddd)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
