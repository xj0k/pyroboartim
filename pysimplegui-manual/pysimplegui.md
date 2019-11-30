PySimpleGUI User's Manual
=========================

### 

------------------------------------------------------------------------

Jump-Start
==========

Install
-------

    pip install pysimplegui
    or
    pip3 install pysimplegui

### This Code

    import PySimpleGUI as sg
    
    sg.change_look_and_feel('DarkAmber')    # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    
    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):   # if user closes window or clicks cancel
            break
        print('You entered ', values[0])
    
    window.close()



A Complete PySimpleGUI Program (Getting The Gist)
-------------------------------------------------

Before diving into details, here's a description of what PySimpleGUI is/does and why that is so powerful.

You keep hearing "custom window" in this document because that's what you're making and using... your own custom windows.

**ELEMENTS** is a word you'll see everywhere... in the code, documentation, ... Elements == PySimpleGUI's Widgets. As to not confuse a tkinter Button Widget with a PySimpleGUI Button Element, it was decided that PySimpleGUI's Widgets will be called Elements to avoid confusion.

Wouldn't it be nice if a GUI with 3 "rows" of Elements was defined in 3 lines of code? That's exactly how it's done. Each row of Elements is a list. Put all those lists together and you've got a window.

What about handling button clicks and stuff. That's 4 lines of the code below beginning with the while loop.

Now look at the `layout` variable and then look at the window graphic below. Defining a window is taking a design you can see visually and then visually creating it in code. One row of Elements = 1 line of code (can span more if your window is crowded). The window is exactly what we see in the code. A line of text, a line of text and an input area, and finally ok and cancel buttons.

This makes the coding process extremely quick and the amount of code very small

    import PySimpleGUI as sg
    sg.change_look_and_feel('DarkAmber')   # Add a little color to your windows
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  [sg.Text('Some text on Row 1')],
                [sg.Text('Enter something on Row 2'), sg.InputText()],
                [sg.OK(), sg.Cancel()]]
    
    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (None, 'Cancel'):
            break
    
    window.close()



------------------------------------------------------------------------

The Quick Tour
==============

Let's take a super-brief tour around PySimpleGUI before digging into the details. There are 2 levels of windowing support in PySimpleGUI - High Level and Customized.

The high-level calls are those that perform a lot of work for you. These are not custom made windows (those are the other way of interacting with PySimpleGUI).

Let's use one of these high level calls, the `Popup` and use it to create our first window, the obligatory "Hello World". It's a single line of code. You can use these calls like print statements, adding as many parameters and types as you desire.

    import PySimpleGUI as sg
    
    sg.Popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')

<span class="image">hello world</span>

Or how about a ***custom GUI*** in 1 line of code? No kidding this is a valid program and it uses Elements and produce the same Widgets like you normally would in a tkinter program. It's just been compacted together is all, strictly for demonstration purposes as there's no need to go that extreme in compactness, unless you have a reason to and then you can be thankful it's possible to do.

    import PySimpleGUI as sg
    
    event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()

Getting Started with PySimpleGUI
================================

There is a "Troubleshooting" section towards the end of this document should you run into real trouble. It goes into more detail about what you can do to help yourself.

Installing PySimpleGUI
----------------------

Of course if you're installing for Qt, WxPython, Web, you'll use PySimpleGUIQt, PySimpleGUIWx, and PySimpleGUIWeb instead of straight PySimpleGUI in the instructions below. You should already have the underlying GUI Framework installed and perhaps tested. This includes tkinter, PySide2, WxPython, Remi

### Installing on Python 3

`pip install --upgrade PySimpleGUI`

On some systems you need to run pip3. (Linux and Mac)

`pip3 install --upgrade PySimpleGUI`

On a Raspberry Pi, this is should work:

`sudo pip3 install --upgrade pysimplegui`

Some users have found that upgrading required using an extra flag on the pip `--no-cache-dir`.

`pip install --upgrade --no-cache-dir PySimpleGUI`

On some versions of Linux you will need to first install pip. Need the Chicken before you can get the Egg (get it... Egg?)

`sudo apt install python3-pip`

`tkinter` is a requirement for PySimpleGUI (the only requirement). Some OS variants, such as Ubuntu, do not some with `tkinter` already installed. If you get an error similar to:

`ImportError: No module named tkinter`

then you need to install `tkinter`.

For python 2.7

`sudo apt-get install python-tk`

For python 3 `sudo apt-get install python3-tk`

More information about installing tkinter can be found here: https://www.techinfected.net/2015/09/how-to-install-and-use-tkinter-in-ubuntu-debian-linux-mint.html

Using - Python 3
----------------

To use in your code, simply import.... `import PySimpleGUI as sg`

Then use either "high level" API calls or build your own windows.

`sg.Popup('This is my first Popup')`

<span class="image">first popup</span>

Yes, it's just that easy to have a window appear on the screen using Python. With PySimpleGUI, making a custom window appear isn't much more difficult. The goal is to get you running on your GUI within ***minutes***, not hours nor days.

***WARNING*** Do NOT use PySimpleGUI with Python 3.7.3 and 3.7.4. tkiter is having issues with that release. Things like Table colors stopped working entirely. None of us want to debug tkinter code. It's difficult enough debugging your code and PySimpleGUI code. A lot of time has already been spent debugging this one so no need for you to suffer too.



Progress Meters!
================

We all have loops in our code. 'Isn't it joyful waiting, watching a counter scrolling past in a text window? How about one line of code to get a progress meter, that contains statistics about your code?

    OneLineProgressMeter(title,
                current_value,
                max_value,
                key,
                *args,
                orientation=None,
                bar_color=DEFAULT_PROGRESS_BAR_COLOR,
                button_color=None,
                size=DEFAULT_PROGRESS_BAR_SIZE,
                border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH):

Here's the one-line Progress Meter in action!

    for i in range(1,10000):
        sg.OneLineProgressMeter('My Meter', i+1, 10000, 'key','Optional message')

That line of code resulted in this window popping up and updating.

<span class="image">preogress meter</span>

A meter AND fun statistics to watch while your machine grinds away, all for the price of 1 line of code. With a little trickery you can provide a way to break out of your loop using the Progress Meter window. The cancel button results in a `False` return value from `OneLineProgressMeter`. It normally returns `True`.

***Be sure and add one to your loop counter*** so that your counter goes from 1 to the max value. If you do not add one, your counter will never hit the max value. Instead it will go from 0 to max-1.

Debug Output (EasyPrint = Print = eprint)
=========================================

Another call in the 'Easy' families of APIs is `EasyPrint`. As is with other commonly used PySimpleGUI calls, there are other names for the same call. You can use `Print` or `eprint` in addition to `EasyPrint`. They all do the same thing, output to a debug window. If the debug window isn't open, then the first call will open it. No need to do anything but stick an 'sg.Print' call in your code. You can even replace your 'print' calls with calls to EasyPrint by simply sticking the statement

    print = sg.EasyPrint

at the top of your code.

`Print` is one of the better ones to use as it's easy to remember. It is simply `print` with a capital P. `sg.Print('this will go to the debug window')`

    import PySimpleGUI as sg
    
    for i in range(100):
        sg.Print(i)



Or if you didn't want to change your code:

    import PySimpleGUI as sg
    
    print=sg.Print
    for i in range(100):
    print(i)

Just like the standard print call, `EasyPrint` supports the `sep` and `end` keyword arguments. Other names that can be used to call `EasyPrint` include `Print`, `eprint`, If you want to close the window, call the function `EasyPrintClose`.

You can change the size of the debug window using the `SetOptions` call with the `debug_win_size` parameter.

There is an option to tell PySimpleGUI to reroute all of your stdout and stderr output to this window. To do so call EasyPrint with the parameter `do_not_reroute_stdout` set to `False`. After calling it once with this parameter set to True, all future calls to a normal`print` will go to the debug window.

If you close the debug window it will re-open the next time you Print to it. If you wish to close the window using your code, then you can call either `EasyPrintClose()` or `PrintClose()`

------------------------------------------------------------------------

Custom window API Calls (Your First window)
===========================================

This is the FUN part of the programming of this GUI. In order to really get the most out of the API, you should be using an IDE that supports auto complete or will show you the definition of the function. This will make customizing go smoother.

This first section on custom windows is for your typical, blocking, non-persistent window. By this I mean, when you "show" the window, the function will not return until the user has clicked a button or closed the window with an X.

Two other types of windows exist. 1. Persistent window - the `Window.read()` method returns and the window continues to be visible. This is good for applications like a chat window or a timer or anything that stays active on the screen for a while. 2. Asynchronous window - the trickiest of the lot. Great care must be exercised. Examples are an MP3 player or status dashboard. Async windows are updated (refreshed) on a periodic basis. You can spot them easily as they will have a `timeout` parameter on the call to read. `event, values = window.Read(timeout=100)`

It's both not enjoyable nor helpful to immediately jump into tweaking each and every little thing available to you. Make some simple windows. Use the Cookbook and the Demo Programs as a way to learn and as a "starting point".



Copy these design patterns!
===========================

All of your PySimpleGUI programs will utilize one of these 2 design patterns depending on the type of window you're implementing.

Pattern 1 - "One-shot Window" - Read a window one time then close it
--------------------------------------------------------------------

This will be the most common pattern you'll follow if you are not using an "event loop" (not reading the window multiple times). The window is read and closed.

The input fields in your window will be returned to you as a dictionary (syntactically it looks just like a list lookup)

    import PySimpleGUI as sg
    
    layout = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                     [sg.InputText(), sg.FileBrowse()],
                     [sg.Submit(), sg.Cancel()]]
    
    window = sg.Window('SHA-1 & 256 Hash', layout)
    
    event, values = window.read()
    window.close()
    
    source_filename = values[0]     # the first input element is values[0]

Pattern 2 A - Persistent window (multiple reads using an event loop)
--------------------------------------------------------------------

Some of the more advanced programs operate with the window remaining visible on the screen. Input values are collected, but rather than closing the window, it is kept visible acting as a way to both output information to the user and gather input data.

This code will present a window and will print values until the user clicks the exit button or closes window using an X.

    import PySimpleGUI as sg
    
    layout = [[sg.Text('Persistent window')],
              [sg.Input()],
              [sg.Button('Read'), sg.Exit()]]
    
    window = sg.Window('Window that stays open', layout)
    
    while True:
        event, values = window.read()
        if event is None or event == 'Exit':
            break
        print(event, values)
    
    window.close()

Pattern 2 B - Persistent window (multiple reads using an event loop + updates data in window)
---------------------------------------------------------------------------------------------

This is a slightly more complex, but maybe more realistic version that reads input from the user and displays that input as text in the window. Your program is likely to be doing both of those activities (input and output) so this will give you a big jump-start.

Do not worry yet what all of these statements mean. Just copy it so you can begin to play with it, make some changes. Experiment to see how thing work.

A final note... the parameter `do_not_clear` in the input call determines the action of the input field after a button event. If this value is True, the input value remains visible following button clicks. If False, then the input field is CLEARED of whatever was input. If you are building a "Form" type of window with data entry, you likely want False. The default is to NOT clear the input element (`do_not_clear=True`).

This example introduces the concept of "keys". Keys are super important in PySimpleGUI as they enable you to identify and work with Elements using names you want to use. Keys can be ANYTHING, except `None`. To access an input element's data that is read in the example below, you will use `values['_IN_']` instead of `values[0]` like before.

    import PySimpleGUI as sg
    
    layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', size=(12,1), key='_OUTPUT_')],
              [sg.Input(key='_IN_')],
              [sg.Button('Show'), sg.Button('Exit')]]
    
    window = sg.Window('Window Title', layout)
    
    while True:  # Event Loop
        event, values = window.read()       # can also be written as event, values = window()
        print(event, values)
        if event is None or event == 'Exit':
            break
        if event == 'Show':
            # change the "output" element to be the value of "input" element
            window['_OUTPUT_'].update(values['_IN_'])
            # above line can also be written without the update specified
            window['_OUTPUT_'](values['_IN_'])
    
    window.close()



How GUI Programming in Python Should Look? At least for beginners ?
-------------------------------------------------------------------

While one goal was making it simple to create a GUI another just as important goal was to do it in a Pythonic manner. Whether it achieved these goals is debatable, but it was an attempt just the same.

The key to custom windows in PySimpleGUI is to view windows as ROWS of GUI Elements. Each row is specified as a list of these Elements. Put the rows together and you've got a window. This means the GUI is defined as a series of Lists, a Pythonic way of looking at things.

Let's dissect this little program

    import PySimpleGUI as sg
    
    layout = [[sg.Text('Rename files or folders')],
                [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
                [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
                [sg.Submit(), sg.Cancel()]]
    
    window = sg.Window('Rename Files or Folders', layout)
    
    event, values = window.read()
    window.close()
    folder_path, file_path = values[0], values[1]       # get the data from the values dictionary
    print(folder_path, file_path)

<span class="image">snap0131</span>

Let's agree the window has 4 rows.

The first row only has **text** that reads `Rename files or folders`

The second row has 3 elements in it. First the **text** `Source for Folders`, then an **input** field, then a **browse** button.

Now let's look at how those 2 rows and the other two row from Python code:

    layout = [[sg.Text('Rename files or folders')],
              [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
              [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
              [sg.Submit(), sg.Cancel()]]

See how the source code mirrors the layout? You simply make lists for each row, then submit that table to PySimpleGUI to show and get values from.

And what about those return values? Most people simply want to show a window, get the input values and do something with them. So why break up the code into button callbacks, etc, when I simply want my window's input values to be given to me.

For return values the window is scanned from top to bottom, left to right. Each field that's an input field will occupy a spot in the return values.

In our example window, there are 2 fields, so the return values from this window will be a dictionary with 2 values in it. Remember, if you do not specify a `key` when creating an element, one will be created for you. They are ints starting with 0. In this example, we have 2 input elements. They will be addressable as values\[0\] and values\[1\]

    event, values = window.read()
    folder_path, file_path = values[0], values[1]

In one statement we both show the window and read the user's inputs. In the next line of code the *dictionary* of return values is split into individual variables `folder_path` and `file_path`.

Isn't this what a Python programmer looking for a GUI wants? Something easy to work with to get the values and move on to the rest of the program, where the real action is taking place. Why write pages of GUI code when the same layout can be achieved with PySimpleGUI in 3 or 4 lines of code. 4 lines or 40? Most would choose 4.

Return values
-------------

There are 2 return values from a call to `Window.read()`, an `event` that caused the `Read` to return and `values` a list or dictionary of values. If there are no elements with keys in the layout, then it will be a list. However, some elements, like some buttons, have a key automatically added to them. **It's best to use keys on all of your input type elements.**

### Two Return Values

All Window Read calls return 2 values. By convention a read statement is written:

    event, values = window.read()

You don't HAVE to write your reads in this way. You can name your variables however you want. But if you want to code them in a way that other programmers using PySimpleGUI are used to, then use this statement.

Events
------

The first parameter `event` describes **why** the read completed. Events are one of these:

For all Windows:

-   Button click
-   Window closed using X

For Windows that have specifically enabled these. Please see the appropriate section in this document to learn about how to enable these and what the event return values are.

-   Keyboard key press
-   Mouse wheel up/down
-   Menu item selected
-   An Element Changed (slider, spinner, etc)
-   A list item was clicked
-   Return key was pressed in input element
-   Timeout waiting for event
-   Text was clicked
-   Combobox item chosen
-   Table row selected
-   etc

***Most*** of the time the event will be a button click or the window was closed. The other Element-specific kinds of events happen when you set `enable_events=True` when you create the Element.

### Window closed event

Another convention to follow is the check for windows being closed with an X. *This is an critically important event to catch*. If you don't check for this and you attempt to use the window, your program will crash. Please check for closed window and exit your program gracefully. Your users will like you for it.

Close your windows when you're done with them even though exiting the program will also close them. tkinter can generate an error/warning sometimes if you don't close the window. For other ports, such as PySimpleGUIWeb, not closing the Window will potentially cause your program to continue to run in the background.

To check for a closed window use this line of code:

    if event is None:

Putting it all together we end up with an "event loop" that looks something like this:

    while True:
        event, values = window.read()
        if event is None:
            break
    window.Close()

You will very often see the examples and demo programs write this check as:

        event, values = window.read()
        if event in (None, 'Exit'):
            break

This if statement is the same as:

        if event is None or event == 'Exit':
            break

Instead of `'Exit'` use the name/key of the button you want to exit the window (Cancel, Quit, etc)

### Button Click Events

By default buttons will always return a click event, or in the case of realtime buttons, a button down event. You don't have to do anything to enable button clicks. To disable the events, disable the button using its Update method.

You can enable an additional "Button Modified" event by setting `enable_events=True` in the Button call. These events are triggered when something 'writes' to a button, ***usually*** it's because the button is listed as a "target" in another button.

The button value from a Read call will be one of 2 values: 1. The Button's text - Default 2. The Button's key - If a key is specified

If a button has a key set when it was created, then that key will be returned, regardless of what text is shown on the button. If no key is set, then the button text is returned. If no button was clicked, but the window returned anyway, the event value is the key that caused the event to be generated. For example, if `enable_events` is set on an `Input` Element and someone types a character into that `Input` box, then the event will be the key of the input box.

### **None is returned when the user clicks the X to close a window.**

If your window has an event loop where it is read over and over, remember to give your user an "out". You should ***always check for a None value*** and it's a good practice to provide an Exit button of some kind. Thus design patterns often resemble this Event Loop:

    while True:
        event, values = window.read()
        if event is None or event == 'Quit':
            break

Actually, the more "Pythonic version" is used in most Demo Programs and examples. They do **exactly** the same thing.

    while True:
        event, values = window.read()
        if event in (None, 'Quit'):
            break

### Element Events

Some elements are capable of generating events when something happens to them. For example, when a slider is moved, or list item clicked on or table row clicked on. These events are not enabled by default. To enable events for an Element, set the parameter `enable_events=True`. This is the same as the older `click_submits` parameter. You will find the `click_submits` parameter still in the function definition. You can continue to use it. They are the same setting. An 'or' of the two values is used. In the future, click\_submits will be removed so please migrate your code to using `enable_events`.

| Name             | events                |
|------------------|-----------------------|
| InputText        | any change            |
| Combo            | item chosen           |
| Listbox          | selection changed     |
| Radio            | selection changed     |
| Checkbox         | selection changed     |
| Spinner          | new item selected     |
| Multiline        | any change            |
| Text             | clicked               |
| Status Bar       | clicked               |
| Graph            | clicked               |
| Graph            | dragged               |
| Graph            | drag ended (mouse up) |
| TabGroup         | tab clicked           |
| Slider           | slider moved          |
| Table            | row selected          |
| Tree             | node selected         |
| ButtonMenu       | menu item chosen      |
| Right click menu | menu item chosen      |

### Other Events

#### Menubar menu item chosen for MenuBar menus and ButtonMenu menus

You will receive the key for the MenuBar and ButtonMenu. Use that key to read the value in the return values dictionary. The value shown will be the full text plus key for the menu item chosen. Remember that you can put keys onto menu items. You will get the text and the key together as you defined it in the menu definition.

#### Right Click menu item chosen

Unlike menu bar and button menus, you will directly receive the menu item text and its key value. You will not do a dictionary lookup to get the value. It is the event code returned from WindowRead().

#### Windows - keyboard, mouse scroll wheel

Windows are capable of returning keyboard events. These are returned as either a single character or a string if it's a special key. Experiment is all I can say. The mouse scroll wheel events are also strings. Put a print in your code to see what's returned.

#### Timeouts

If you set a timeout parameter in your read, then the system TIMEOUT\_KEY will be returned. If you specified your own timeout key in the Read call then that value will be what's returned instead.

### The `values` Variable - Return values as a list

The second parameter from a Read call is either a list or a dictionary of the input fields on the Window.

By default return values are a list of values, one entry for each input field, but for all but the simplest of windows the return values will be a dictionary. This is because you are likely to use a 'key' in your layout. When you do, it forces the return values to be a dictionary.

Each of the Elements that are Input Elements will have a value in the list of return values. If you know for sure that the values will be returned as a list, then you could get clever and unpack directly into variables.

event, (filename, folder1, folder2, should\_overwrite) = sg.Window('My title', window\_rows).Read()

Or, more commonly, you can unpack the return results separately. This is the preferred method because it works for **both** list and dictionary return values.

    event, values = sg.Window('My title', window_rows).Read()
    event, value_list = window.read()
    value1 = value_list[0]
    value2 = value_list[1]
         ...

However, this method isn't good when you have a lot of input fields. If you insert a new element into your window then you will have to shuffle your unpacks down, modifying each of the statements to reference `value_list[x]`.

The more common method is to request your values be returned as a dictionary by placing keys on the "important" elements (those that you wish to get values from and want to interact with)

### `values` Variable - Return values as a dictionary

For those of you that have not encountered a Python dictionary, don't freak out! Just copy and paste the sample code and modify it. Follow this design pattern and you'll be fine. And you might learn something along the way.

For windows longer than 3 or 4 fields you will want to use a dictionary to help you organize your return values. In almost all (if not all) of the demo programs you'll find the return values being passed as a dictionary. It is not a difficult concept to grasp, the syntax is easy to understand, and it makes for very readable code.

The most common window read statement you'll encounter looks something like this:

`window = sg.Window("My title", layout).Read()`

To use a dictionary, you will need to: \* Mark each input element you wish to be in the dictionary with the keyword `key`.

If **any** element in the window has a `key`, then **all** of the return values are returned via a dictionary. If some elements do not have a key, then they are numbered starting at zero.

Let's take a look at your first dictionary-based window.

    import PySimpleGUI as sg
    
    layout = [
                [sg.Text('Please enter your Name, Address, Phone')],
                [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='_NAME_')],
                [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='_ADDRESS_')],
                [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='_PHONE_')],
                [sg.Submit(), sg.Cancel()]
                ]
    
    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    window.Close()
    
    sg.Popup(event, values, values['_NAME_'], values['_ADDRESS_'], values['_PHONE_'])

To get the value of an input field, you use whatever value used as the `key` value as the index value. Thus to get the value of the name field, it is written as

    values['_NAME_']

Think of the variable values in the same way as you would a list, however, instead of using 0,1,2, to reference each item in the list, use the values of the key. The Name field in the window above is referenced by `values['_NAME_']`.

You will find the key field used quite heavily in most PySimpleGUI windows unless the window is very simple.

One convention you'll see in many of the demo programs is keys being named in all caps with an underscores at the beginning and the end. You don't HAVE to do this... your key value may look like this: `key = '_NAME__'`

The reason for this naming convention is that when you are scanning the code, these key values jump out at you. You instantly know it's a key. Try scanning the code above and see if those keys pop out. `key = '_NAME__'`

The Event Loop / Callback Functions
-----------------------------------

All GUIs have one thing in common, an "event loop". Usually the GUI framework runs the event loop for you, but sometimes you want greater control and will run your own event loop. You often hear the term event loop when discussing embedded systems or on a Raspberry Pi.

With PySimpleGUI if your window will remain open following button clicks, then your code will have an event loop. If your program shows a single "one-shot" window, collects the data and then has no other GUI interaction, then you don't need an event loop.

There's nothing mysterious about event loops... they are loops where you take care of.... wait for it..... *events*. Events are things like button clicks, key strokes, mouse scroll-wheel up/down.

This little program has a typical PySimpleGUI Event Loop.

The anatomy of a PySimpleGUI event loop is as follows, *generally speaking*. \* The actual "loop" part is a `while True` loop \* "Read" the event and any input values the window has \* Check to see if window was closed or user wishes to exit \* A series of `if event ....` statements

Here is a complete, short program to demonstrate each of these concepts.

    import PySimpleGUI as sg
    
    sg.ChangeLookAndFeel('GreenTan')
    
    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
                ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Help', '&About...'], ]
    
    # ------ Column Definition ------ #
    column1 = [[sg.Text('Column 1', background_color='lightblue', justification='center', size=(10, 1))],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
    
    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Text('(Almost) All widgets in one Window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        [sg.Frame(layout=[
        [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.Multiline(default_text='A second multi-line', size=(35, 3))],
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sg.Frame('Labelled Group',[[
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
         sg.Column(column1, background_color='lightblue')]])],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]
    
    window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)
    event, values = window.read()
    
    sg.Popup('Title',
             'The results of the window.',
             'The button clicked was "{}"'.format(event),
             'The values are', values)

This is a complex window with quite a bit of custom sizing to make things line up well. This is code you only have to write once. When looking at the code, remember that what you're seeing is a list of lists. Each row contains a list of Graphical Elements that are used to create the window. If you see a pair of square brackets \[ \] then you know you're reading one of the rows. Each row of your GUI will be one of these lists.

This window may look "ugly" to you which is because no effort has been made to make it look nice. It's purely functional. There are 30 Elements in the window. THIRTY Elements. Considering what it does, it's miraculous or in the least incredibly impressive. Why? Because in less than 50 lines of code that window was created, shown, collected the results and showed the results in another window.

50 lines. It'll take you 50 lines of tkinter or Qt code to get the first 3 elements of the window written, if you can even do that.

No, let's be clear here... this window will take a massive amount of code using the conventional Python GUI packages. It's a fact and if you care to prove me wrong, then by ALL means PLEASE do it. Please write this window using tkinter, Qt, or WxPython and send the code!

Note this window even has a menubar across the top, something easy to miss.

<span class="image">image</span>

Clicking the Submit button caused the window call to return. The call to Popup resulted in this window.

<span class="image">image</span>

**`Note, event values can be None`**. The value for `event` will be the text that is displayed on the button element when it was created or the key for the button. If the user closed the window using the "X" in the upper right corner of the window, then `event` will be `None`. It is ***vitally*** ***important*** that your code contain the proper checks for None.

For "persistent windows", **always give your users a way out of the window**. Otherwise you'll end up with windows that never properly close. It's literally 2 lines of code that you'll find in every Demo Program. While you're at it, make sure a `window.Close()` call is after your event loop so that your window closes for sure.

You can see in the results Popup window that the values returned are a dictionary. Each input field in the window generates one item in the return values list. Input fields often return a `string`. Check Boxes and Radio Buttons return `bool`. Sliders return float or perhaps int depending on how you configured it or which port you're using.

If your window has no keys and it has no buttons that are "browse" type of buttons, then it will return values to you as a list instead of a dictionary. If possible PySimpleGUI tries to return the values as a list to keep things simple.

Note in the list of return values in this example, many of the keys are numbers. That's because no keys were specified on any of the elements (although one was automatically made for you). If you don't specify a key for your element, then a number will be sequentially assigned. For elements that you don't plan on modifying or reading values from, like a Text Element, you can skip adding keys. For other elements, you'll likely want to add keys so that you can easily access the values and perform operations on them.

### Operations That Take a "Long Time"

If you're a Windows user you've seen windows show in their title bar "Not Responding" which is soon followed by a Windows popop stating that "Your program has stopped responding". Well, you too can make that message and popup appear if you so wish! All you need to do is execute an operation that takes "too long" (i.e. a few seconds) inside your event loop.

You have a couple of options for dealing this with. If your operation can be broken up into smaller parts, then you can call `Window.Refresh()` occassionally to avoid this message. If you're running a loop for example, drop that call in with your other work. This will keep the GUI happy and Window's won't complain.

If, on the other hand, your operation is not under your control or you are unable to add `Refresh` calls, then the next option available to you is to move your long operations into a thread.

There are a couple of demo programs available for you to see how to do this. You basically put your work into a thread. When the thread is completed, it tells the GUI by sending a message through a queue. The event loop will run with a timer set to a value that represents how "responsive" you want your GUI to be to the work completing.

These 2 demo programs are called

    Demo_Threaded_Work.py - Best documented.  Single thread used for long task
    Demo_Multithreaded_Long_Tasks.py - Similar to above, but with less fancy GUI. Allows you to set amount of time

These 2 particular demos have a LOT of comments showing you where to add your code, etc. The amount of code to do this is actually quite small and you don't need to understand the mechanisms used if you simply follow the demo that's been prepared for you.

### Multitheaded Programs

While on the topic of multiple threads, another demo was prepared that shows how you can run multiple threads in your program that all communicate with the event loop in order to display something in the GUI window. Recall that for PySimpleGUI (at least the tkinter port) you cannot make PySimpleGUI calls in threads other than the main program thread.

The key to these threaded programs is communication from the threads to your event loop. The mechanism chosen for these demonstrations uses the Python built-in `queue` module. The event loop polls these queues to see if something has been sent over from one of the threads to be displayed.

You'll find the demo that shows multiple threads communicating with a single GUI is called:

    Demo_Multithreaded_Queued.py

Once again a **warning** is in order for plain PySimpleGUI (tkinter based) - your GUI must never run as anything but the main program thread and no threads can directly call PySimpleGUI calls.

------------------------------------------------------------------------



Window Object - Beginning a window
==================================

The first step is to create the window object using the desired window customizations.

Note - There is no direct support for "**modal windows**" in PySimpleGUI. All windows are accessable at all times unless you manually change the windows' settings.

**IMPORTANT** - Many of the `Window` methods require you to either call `Window.Read` or `Window.Finalize` (or set `finalize=True` in your `Window` call) before you call the method. This is because these 2 calls are what actually creates the window using the underlying GUI Framework. Prior to one of those calls, the methods are likely to crash as they will not yet have their underlying widgets created.

### Window Location

PySimpleGUI computes the exact center of your window and centers the window on the screen. If you want to locate your window elsewhere, such as the system default of (0,0), if you have 2 ways of doing this. The first is when the window is created. Use the `location` parameter to set where the window. The second way of doing this is to use the `SetOptions` call which will set the default window location for all windows in the future.

#### Multiple Monitors and Linux

The auto-centering (default) location for your PySimpleGUI window may not be correct if you have multiple monitors on a Linux system. On Windows multiple monitors appear to work ok as the primary monitor the tkinter utilizes and reports on.

Linux users with multiple monitors that have a problem when running with the default location will need to specify the location the window should be placed when creating the window by setting the `location` parameter.

### Window Size

You can get your window's size by access the `Size` property. The window has to be Read once or Finalized in order for the value to be correct. Note that it's a property, not a call.

`my_windows_size = window.Size`

To finalize your window:

    window = Window('My Title', layout).Finalize()

If using PySimpleGUI 4.2 and later:

    window = Window('My Title', layout, finalize=True)

### Element Sizes

There are multiple ways to set the size of Elements. They are:

1.  The global default size - change using `SetOptions` function
2.  At the Window level - change using the parameter `default_element_size` in your call to `Window`
3.  At the Element level - each element has a `size` parameter

Element sizes are measured in characters (there are exceptions). A Text Element with `size = (20,1)` has a size of 20 characters wide by 1 character tall.

The default Element size for PySimpleGUI is `(45,1)`.

There are a couple of widgets where one of the size values is in pixels rather than characters. This is true for Progress Meters and Sliders. The second parameter is the 'height' in pixels.

### No Titlebar

Should you wish to create cool looking windows that are clean with no windows titlebar, use the no\_titlebar option when creating the window.

Be sure an provide your user an "exit" button or they will not be able to close the window! When no titlebar is enabled, there will be no icon on your taskbar for the window. Without an exit button you will need to kill via taskmanager... not fun.

Windows with no titlebar rely on the grab anywhere option to be enabled or else you will be unable to move the window.

Windows without a titlebar can be used to easily create a floating launcher.

Linux users! Note that this setting has side effects for some of the other Elements. Multi-line input doesn't work at all, for example So, use with caution.

<span class="image">floating launcher</span>

### Grab Anywhere

This is a feature unique to PySimpleGUI.

Note - there is a warning message printed out if the user closes a non-blocking window using a button with grab\_anywhere enabled. There is no harm in these messages, but it may be distressing to the user. Should you wish to enable for a non-blocking window, simply get grab\_anywhere = True when you create the window.

### Always on top

To keep a window on top of all other windows on the screen, set keep\_on\_top = True when the window is created. This feature makes for floating toolbars that are very helpful and always visible on your desktop.

### Focus

PySimpleGUI will set a default focus location for you. This generally means the first input field. You can set the focus to a particular element. If you are going to set the focus yourself, then you should turn off the automatic focus by setting `use_default_focus=False` in your Window call.

Closing Windows
---------------

When you are completely done with a window, you should close it and then delete it so that the resources, in particular the tkinter resources, are properly cleaned up.

If you wish to do this in 1 line of code, here's your line:

    window.close(); del window

The delete helps with a problem multi-threaded application encounter where tkinter complains that it is being called from the wrong thread (not the program's main thread)

Window Methods That Complete Formation of Window
------------------------------------------------

After you have completed making your layout, stored in a variable called `layout` in these examples, you will create your window.

The creation part of a window involves 3 steps.

1.  Create a `Window` object
2.  Adding your Layout to the window
3.  Optional - Finalize if want to make changes prior to `Read` call

Over time the PySimpleGUI code has continued to compact, compress, so that as little code as possible will need to be written by the programmer.

### The Individual Calls

This is the "long form" as each method is called individually.

    window = sg.Window('My Title')
    window.Layout(layout)
    window.Finalize()

### Chaining The Calls (the old method)

The next level of compression that was done was to chain the calls together into a single line of code.

    window = sg.Window('My Title').Layout(layout).Finalize()

### Using Parameters Instead of Calls (New Preferred Method)

Here's a novel concept, instead of using chaining, something that's foreign to beginners, use parameters to the `Window` call. And that is exactly what's happened as of 4.2 of the PySimpleGUI port.

    window = sg.Window('My Title', layout, finalize=True)

Rather than pushing the work onto the user of doing the layout and finalization calls, let the Window initialization code do it for you. Yea, it sounds totally obvious now, but it didn't a few months ago.

This capability has been added to all 4 PySimpleGUI ports but none are on PyPI just yet as there is some runtime required first to make sure nothing truly bad is going to happen.

Call to set the window layout. Must be called prior to `Read`. Most likely "chained" in line with the Window creation.

    window = sg.Window('My window title', layout)

#### `Finalize()` or `Window` parameter `finalize=True`

Call to force a window to go through the final stages of initialization. This will cause the tkinter resources to be allocated so that they can then be modified. This also causes your window to appear. If you do not want your window to appear when Finalize is called, then set the Alpha to 0 in your window's creation parameters.

If you want to call an element's `Update` method or call a `Graph` element's drawing primitives, you ***must*** either call `Read` or `Finalize` prior to making those calls.

#### Read(timeout=None, timeout\_key=TIMEOUT\_KEY)

Read the Window's input values and button clicks in a blocking-fashion

Returns event, values. Adding a timeout can be achieved by setting timeout=*number of milliseconds* before the Read times out after which a "timeout event" is returned. The value of timeout\_key will be returned as the event. If you do not specify a timeout key, then the value `TIMEOUT_KEY` will be returned.

If you set the timeout = 0, then the Read will immediately return rather than waiting for input or for a timeout. It's a truly non-blocking "read" of the window.



------------------------------------------------------------------------


