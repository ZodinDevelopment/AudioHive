# py_intercom


This is a small application intended to demonstrate and explore the pyaudio library's audio streaming capabilities and implement it in a simple client-server intercom to PA utility. It achieves this with two seperate scripts; the serverside send_audio.py tha records a snippet of audio data on command and sends it to the clientside get_audio.py, which respectively plays back the audio data. 


[Server Side]
Breaking down the concept and design of the project begins with the server side script. 

The functional requirements of the server side design are:
  + Open a TCP network socket on a specified hostname and port and wait for a connection.
  + Upon accepting a connection from a client, await for some command (in this case "press enter") 
  + Once the trigger or command is given, initialize an audio input stream 
  + If there is a functioning audio input device available, the stream capture audio from it
  + Read 'n' amount of frames at specified chunk size, where n is an integer given by the formula "framerate / chunksize * duration(in seconds)"
  + Close the audio stream after all the data is captured
  + Open a wav file and configure the channel amount, sample width, and framerate of our captured audio data, then write all our captured frames of audio as one bytes object to the wav file. 
  + Read the wav file as bytes, and send the entirety of the audio data to the client that connected to our open network socket.
  + Upon sending all of the binary data, close the connection and await the next client connection where it will repeat this process as desired.
  
 [Client Side]
 Most of the client's design is dependent on how we go about approaching our server design, and is by comparison a simpler method to grasp than the server code. 
 
 Despite this notable difference, the client side's script was the source of most of the headaches experienced in the debugging and testing of the project. However, this was more a consequence of my approach to receiving the binary data and our client knowing when to stop listening and to START PLAYING back the audio data it received. 
 
 Nonetheless, the client should:
 
  + Open a network socket over TCP and attempt to connect via the specified hostname and port.
  + If our server's socket is already open and listening, it should begin the recursive process of waiting for and receiving any data from the server.
  + receive data via the socket connection 16 bytes at a time, and if it receives a chunk of data that appears to be empty, stop listening and proceed to write the binary data to the complete wav file.
  + After receiving all of the data (or getting an empty chunk of data signalling no more data to be received) and writing to wav file, open the wav file and read all of it's contents as binary wave audio data.
  + Open a pyaudio stream, detecting the format from the sample width, the number of channels, and the framerate based on the structure of the binary data. The stream will be an output stream.
  
  + read the audio frames from the wav data chunk by chunk, writing the data to the stream which is outputting directly to our client's current audio playback source .
  + Once it runs out of audio data to stream, close the stream, and recursively call the main function where it will attempt to connect to our server once again and wait for the next data send.
  
  
 
Microsoft Windows
Install using pip:

python -m pip install pyaudio
Notes:

If pip is not already bundled with your installation of Python, get it here.
pip will fetch and install PyAudio wheels (prepackaged binaries). Currently, there are wheels compatible with the official distributions of Python 2.7, 3.4, 3.5, and 3.6. For those versions, both 32-bit and 64-bit wheels are available.
These binaries include PortAudio v19 v190600_20161030, built with MinGW. They support only the Windows MME API and do not include support for DirectX, ASIO, etc. If you require support for APIs not included, you will need to compile PortAudio and PyAudio.

Apple Mac OS X
Use Homebrew to install the prerequisite portaudio library, then install PyAudio using pip:

brew install portaudio
pip install pyaudio
Notes:

If not already installed, download Homebrew.
pip will download the PyAudio source and build it for your version of Python.
Homebrew and building PyAudio also require installing the Command Line Tools for Xcode (more information).

Debian/Ubuntu
Use the package manager to install PyAudio:

sudo apt-get install python-pyaudio python3-pyaudio
If the latest version of PyAudio is not available, install it using pip:

pip install pyaudio
Notes:

pip will download the PyAudio source and build it for your system. Be sure to install the portaudio library development package (portaudio19-dev) and the python development package (python-all-dev) beforehand.
For better isolation from system packages, consider installing PyAudio in a virtualenv.

PyAudio Source
Source is available for download at the Python Package Index (PyPI): pypi.python.org/pypi/PyAudio.

Or clone the git repository:

git clone https://people.csail.mit.edu/hubert/git/pyaudio.git
To build PyAudio from source, you will also need to build PortAudio v19. See compilation hints for some instructions on building PyAudio for various platforms. To build PyAudio using Microsoft Visual Studio, check out Sebastian Audet's instructions.
