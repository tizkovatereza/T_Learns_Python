####################################################################################################
# UGLY CODE
####################################################################################################

####################################################################################################
# Imports and Setup:
####################################################################################################

#Statements: import
#Libraries: asyncio
#Modules: logging, Session
#Packages: e2b
#Variables: id

# Importing a library to write concurrent code using the async/await syntax. Asyncio works for asynchromous programming
import asyncio

# With the logging module imported, you can use something called a “logger” to log messages that you want to see. 
# Logging is a way to store information about your script and track events that occur

import logging 

# Importing a module or class named 'Session' from the 'e2b' package
from e2b import Session

# Setting a variable 'id' with a string value
id = "5udkAFHBVrGz"

# Configuring the logging module to display only ERROR level messages and above
logging.basicConfig(level=logging.ERROR)


####################################################################################################
#Setting up the necessary libraries and configurations
####################################################################################################

# This is the main function where most of the action happens.
# It's defined as async, meaning it can perform tasks concurrently without blocking the main thread.
async def main():
    # Creates session with the given id
    session = await Session.create(id)
 

    #Here, a new session is created using the previously defined id.
    #This section starts a process (ls command, which lists files in a directory) and prints its output. 
    proc = await session.process.start(
        #ls = command, which lists files in a directory
        "ls",
        rootdir="/",
        #The on_stderr and on_stdout are callback functions that print errors and standard outputs, respectively.
        on_stderr=lambda data: print("ERR", data),
        on_stdout=lambda data: print("OUT", data),
    )
    output = await proc

    # output.lines
    print(output.messages)
    
    #Closing the Session:
    await session.close()
    #The return statement right after it means that the function will exit here, and none of the code below this point will be executed.
    return

    await session.filesystem.write("test.txt", "Hello World")

    f = await session.filesystem.read("test.txt")
    print("RESULT read2", f)

    await session.filesystem.make_dir("test")
    ls = await session.filesystem.list("/")
    print("RESULT ls", [ls for ls in ls if ls.is_dir and ls.name == "test"])

    await session.filesystem.remove("test")
    ls = await session.filesystem.list("/")
    print("RESULT ls", [ls for ls in ls if ls.is_dir and ls.name == "test"])

    w = await session.filesystem.watch_dir("/")

    w.add_event_listener(lambda e: print("EVENT", e))
    await w.start()

    print("PATH", w.path)

    await session.filesystem.make_dir("testx")

    await w.stop()

    def on_stdout(data):
        print("STDOUT", data)

    def on_stderr(data):
        print("STDERR", data)

    url = session.get_hostname(80)
    print("URL", url)

    proc = await session.process.start(
        "pwd",
        on_stdout=on_stdout,
        on_stderr=on_stderr,
        on_exit=lambda: print("EXIT"),
        rootdir="/code",
    )
    # await proc.send_stdin("lore olympus")
    # await proc.send_stdin("\nnew line too")

    # await proc.kill()

    print("end")

    await session.process.start(cmd="python3 -m http.server 8022")

    term = await session.terminal.start(
        on_data=lambda data: print("DATA", data),
        cols=80,
        rows=24,
        rootdir="/code",
    )

    await term.send_data("echo 1\n")

    # await term
    print("end")

    # await term.resize(80, 30)

    await term.kill()

    await session.close()

    # await asyncio.Future()


asyncio.new_event_loop().run_until_complete(main())







####################################################################################################
# NICE CODE
####################################################################################################



# Import the asyncio library for asynchronous programming
import asyncio

# Import the Session class from the e2b package
from e2b import Session

# Assign the string "Python3" to the variable named 'id'
id = "Python3"

# Define an asynchronous function named 'main'
async def main():
    # Create a new session using the 'id' and assign it to the 'session' variable
    session = await Session.create(id)
    
    # Start a process to run the 'ls' command, set the root directory to '/',
    # and define callback functions for standard error and standard output
    proc = await session.process.start(
        "ls",
        rootdir="/",
        on_stderr=lambda data: print(data.line),
        on_stdout=lambda data: print(data.line),
    )
    
    # Wait for the process to complete and assign its output to the 'output' variable
    output = await proc

    # Close the session
    await session.close()

# Create a new event loop and run the 'main' asynchronous function until it completes
asyncio.new_event_loop().run_until_complete(main())


#########
#When you run this code, you'll see a list of files and directories from the root directory (/) printed to the console. If there are any errors during the process, those will be printed as well. After listing the files, the session is closed, and the program ends.
