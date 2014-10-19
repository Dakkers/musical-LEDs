Musical LEDs
------------

A goofy hackathon project created by Dakota St. Laurent and Jacky Ngai at BoilerMake II (Fall 2014). Given a song (WAV format only right now), the sound is analyzed via FFTs to see what notes are being played and then lights up the BoilerMake Arduino badge. The badge has 16 LEDs, so 12 of them are used - one for each note on a piano. The lights are played according to the song! Does that make sense? No? We're sleep deprived.

### TODO
- currently, arbitrary frequencies have been picked (0 to 10 Hz, 10 to 20 Hz, etc.) - we're working on this right meow
- add in real delay between notes, instead of the standard sampling frequency (god help us)

### Acknowledgements
Thanks to Imtiaz Hussian, Joey Nicholl, Victor Reyes, and Pieter Stam for putting up with the copious amounts of swearing and frustration.