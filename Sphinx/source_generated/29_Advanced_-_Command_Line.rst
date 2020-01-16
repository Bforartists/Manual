**************************
29 Advanced - Command Line
**************************

.. contents:: Contents




Command Line Arguments
======================

You can start Bforartists from the command line to perform a specific task. To render in Background for example, without the graphical interface.

The general useage is: Bforartists [arguments ...] [file] [arguments ...]

Example - rendering an animation in background mode, allowing drivers and other scripts to run:

Bforartists --background --enable-autoexec my_movie.blend --render-anim

Or running a script with it:

Bforartists --myscene.blend --background --python myscript.py

In the background case the user-preferences are still used but you may want to override them.

- Enable with -y or --enable-autoexec
- Disable with -Y or --disable-autoexec

.. Note:: These command line arguments can be used to start a regular ``Bforartists`` instance and will still override the user-preferences.



Render Options
--------------

-b, --background

Run in background (often used for UI-less rendering) 

-a, --render-anim

Render frames from start to end (inclusive) 

-S, --scene<name>

Set the active scene <name> for rendering 

-f, --render-frame<frame>

Render frame <frame> and save it. +<frame> start frame relative, -<frame> end frame relative. 

-s, --frame-start<frame>

Set start to frame <frame>, supports +/- for relative frames too. 

-e, --frame-end<frame>

Set end to frame <frame>, supports +/- for relative frames too. 

-j, --frame-jump<frames>

Set number of frames to step forward after each rendered frame 

-o, --render-output<path>

	Set the render path and file name. Use // at the start of the path to render relative to the blend file.

The # characters are replaced by the frame number, and used to define zero padding.

- ani_##_test.png becomes ani_01_test.png
- test-######.png becomes test-000001.png

When the filename does not contain #, The suffix #### is added to the filename.

The frame number will be added at the end of the filename, eg:

	Bforartists -b foobar.blend -o //render_ -F PNG -x 1 -a

	//render_ becomes //render_####, writing frames as //render_0001.png

-E, --engine<engine>

Specify the render engine use -E help to list available engines 

-t, --threads<threads>

Use amount of <threads> for rendering and other operations [1-64], 0 for systems processor count. 



Format Options
--------------

-F, --render-format<format>

	Set the render format, Valid options are... 

	TGA IRIS JPEG MOVIE IRIZ RAWTGA AVIRAW AVIJPEG PNG BMP FRAMESERVER 

	(formats that can be compiled into Bforartists, not available on all systems) 

	HDR TIFF EXR MULTILAYER MPEG AVICODEC QUICKTIME CINEON DPX DDS 

-x, --use-extension<bool>

Set option to add the file extension to the end of the file 



Animation Playback Options
--------------------------

-a<options><file(s)>

	Playback <file(s)>, only operates this way when not running in background. 

	-p <sx><sy> Open with lower left corner at <sx>, <sy> -m Read from disk (Don’t buffer) -f <fps><fps-base> Specify FPS to start with -j <frame> Set frame step to <frame> -s <frame> Play from <frame> -e <frame> Play until <frame>



Window Options
--------------

-w, --window-border

Force opening with borders (default) 

-W, --window-borderless

Force opening without borders 

-p, --window-geometry<sx><sy><w><h>

Open with lower left corner at <sx>, <sy> and width and height as <w>, <h>

-con, --start-console

Start with the console window open (ignored if -b is set), (Windows only) 

--no-native-pixels

Do not use native pixel size, for high resolution displays (MacBook Retina) 



Python Options
--------------

-y, --enable-autoexec

Enable automatic Python script execution 

-Y, --disable-autoexec

Disable automatic Python script execution (pydrivers & startup scripts), (default). 

-P, --python<filename>

Run the given Python script file 

--python-text<name>

Run the given Python script text block 

--python-expr<expression>

Run the given expression as a Python script 

--python-console

Run Bforartists with an interactive console 

--python-exit-code

Set the exit-code in [0..255] to exit if a Python exception is raised (only for scripts executed from the command line), zero disables. 

--addons

Comma separated list of addons (no spaces) 



Debug Options
-------------

-d, --debug

	Turn debugging on

- Enables memory error detection 
- Disables mouse grab (to interact with a debugger in some cases) 
- Keeps Python’s sys.stdin rather than setting it to None 

--debug-value<value>

Set debug value of <value> on startup 

--debug-events

Enable debug messages for the event system 

--debug-ffmpeg

Enable debug messages from FFmpeg library 

--debug-handlers

Enable debug messages for event handling 

--debug-libmv

Enable debug messages from libmv library 

--debug-cycles

Enable debug messages from Cycles 

--debug-memory

Enable fully guarded memory allocation and debugging 

--debug-jobs

Enable time profiling for background jobs. 

--debug-python

Enable debug messages for Python 

--debug-depsgraph

Enable debug messages from dependency graph 

--debug-depsgraph-no-threads

Switch dependency graph to a single threaded evaluation 

--debug-gpumem

Enable GPU memory stats in status bar 

--debug-wm

Enable debug messages for the window manager, also prints every operator call 

--debug-all

Enable all debug messages (excludes libmv) 

--debug-fpe

Enable floating point exceptions 

--disable-crash-handler

Disable the crash handler 



Misc Options
------------

--factory-startup

Skip reading the startup.blend in the users home directory 

--env-system-datafiles

Set the Bforartists_SYSTEM_DATAFILES environment variable 

--env-system-scripts

Set the Bforartists_SYSTEM_SCRIPTS environment variable 

--env-system-python

Set the Bforartists_SYSTEM_PYTHON environment variable 

-nojoystick

Disable joystick support 

-noglsl

Disable GLSL shading 

-noaudio

Force sound system to None 

-setaudio

Force sound system to a specific device NULL SDL OPENAL JACK 

-h, --help

Print this help text and exit 

-R

Register .blend extension, then exit (Windows only) 

-r

Silently register .blend extension, then exit (Windows only) 

-v, --version

Print Bforartists version and exit 

--

Ends option processing, following arguments passed unchanged. Access via Python’s sys.argv



Other Options
-------------

/?

Print this help text and exit (windows only) 

--debug-freestyle

Enable debug/profiling messages from Freestyle rendering 

--debug-gpu

Enable gpu debug context and information for OpenGL 4.3+. 

--disable-abort-handler

Disable the abort handler 

--enable-new-depsgraph

Use new dependency graph 

--verbose<verbose>

Set logging verbosity level. 



Experimental features
---------------------

--enable-new-depsgraph

Use new dependency graph 



Argument Parsing
----------------

Arguments must be separated by white space, eg:

	Bforartists -ba test.blend

...will ignore the a

	Bforartists -b test.blend -f8

...will ignore 8 because there is no space between the -f and the frame value



Argument Order
--------------

Arguments are executed in the order they are given. eg:

	Bforartists --background test.blend --render-frame 1 --render-output '/tmp'

...will not render to /tmp because --render-frame 1 renders before the output path is set

	Bforartists --background --render-output /tmp test.blend --render-frame 1

...will not render to /tmp because loading the blend file overwrites the render output that was set

	Bforartists --background test.blend --render-output /tmp --render-frame 1

...works as expected.



Environment Variables
---------------------

.. list-table::

	* - Bforartists_USER_CONFIG:

	* -  
	  - Directory for user configuration files.

	* - Bforartists_USER_SCRIPTS:

	* -  
	  - Directory for user scripts.

	* - Bforartists_SYSTEM_SCRIPTS:

	* -  
	  - Directory for system wide scripts.

	* - Bforartists_USER_DATAFILES:

	* -  
	  - Directory for user data files (icons, translations, ..).

	* - Bforartists_SYSTEM_DATAFILES:

	* -  
	  - Directory for system wide data files.

	* - Bforartists_SYSTEM_PYTHON:

	* -  
	  - Directory for system python libraries.

	* - TEMP:
	  - Store temporary files here.

	* - TMP:
	  - or $TMPDIR Store temporary files here.

	* - SDL_AUDIODRIVER:

	* -  
	  - LibSDL audio driver - alsa, esd, dma.

	* - PYTHONHOME:
	  - Path to the python directory, eg. /usr/lib/python.

