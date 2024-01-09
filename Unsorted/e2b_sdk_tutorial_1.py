####################################################################################################
# When you run this code, you'll see a list of files and directories from the root directory (/) printed to the console.
# If there are any errors during the process, those will be printed as well.
#After listing the files, the session is closed, and the program ends.
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
