Elements
========

You will find information on Elements and all other classes and functions are located near the end of this manual. They are in 1 large section of the readme, in alphabetical order for easy lookups. This section's discussion of Elements is meant to teach you how they work. The other section has detailed call signatures and parameter definitions.

"Elements" are the building blocks used to create windows. Some GUI APIs use the term "Widget" to describe these graphic elements.

-   Text
-   Single Line Input
-   Buttons including these types:
    -   File Browse
    -   Folder Browse
    -   Calendar picker
    -   Date Chooser
    -   Read window
    -   Close window ("Button" & all shortcut buttons)
    -   Realtime
-   Checkboxes
-   Radio Buttons
-   Listbox
-   Slider
-   Multi-line Text Input/Output
-   Multi-line Text Output (not on tkinter version)
-   Scroll-able Output
-   Vertical Separator
-   Progress Bar
-   Option Menu
-   Menu
-   ButtonMenu
-   Frame
-   Column
-   Graph
-   Image
-   Table
-   Tree
-   Tab, TabGroup
-   StatusBar
-   Pane
-   Stretch (Qt only)
-   Sizer (plain PySimpleGUI only)

Common Element Parameters
-------------------------

Some parameters that you will see on almost all Element creation calls include:

-   key - Used with window.FindElement and with return values
-   tooltip - Hover your mouse over the elemnt and you'll get a popup with this text
-   size - (width, height) - usually measured in characters-wide, rows-high. Sometimes they mean pixels
-   font - specifies the font family, size, etc
-   colors - Color name or \#RRGGBB string
-   pad - Amount of padding to put around element
-   enable\_events - Turns on the element specific events
-   visible - Make elements appear and disappear

#### Tooltip

Tooltips are text boxes that popup next to an element if you hold your mouse over the top of it. If you want to be extra kind to your window's user, then you can create tooltips for them by setting the parameter `tooltip` to some text string. You will need to supply your own line breaks / text wrapping. If you don't want to manually add them, then take a look at the standard library package `textwrap`.

Tooltips are one of those "polish" items that really dress-up a GUI and show's a level of sophistication. Go ahead, impress people, throw some tooltips into your GUI. You can change the color of the background of the tooltip on the tkinter version of PySimpleGUI by setting `TOOLTIP_BACKGROUND_COLOR` to the color string of your choice. The default value for the color is:

`TOOLTIP_BACKGROUND_COLOR = "#ffffe0"`

#### Size

Info on setting default element sizes is discussed in the Window section above.

Specifies the amount of room reserved for the Element. For elements that are character based, such a Text, it is (\# characters, \# rows). Sometimes it is a pixel measurement such as the Image element. And sometimes a mix like on the Slider element (characters long by pixels wide).

Some elements, Text and Button, have an auto-size setting that is `on` by default. It will size the element based on the contents. The result is that buttons and text fields will be the size of the string creating them. You can turn it off. For example, for Buttons, the effect will be that all buttons will be the same size in that window.

#### Element Sizes - Non-tkinter Ports (Qt, WxPython, Web)

In non-tkinter ports you can set the specific element sizes in 2 ways. One is to use the normal `size` parameter like you're used to using. This will be in characters and rows.

The other way is to use a new parameter, `size_px`. This parameter allows you to specify the size directly in pixels. A setting of `size_px=(300,200)` will create an Element that is 300 x 200 pixels.

Additionally, you can also indicate pixels using the `size` parameter, **if the size exceeds the threshold for conversion.** What does that mean? It means if your width is \> 20 (`DEFAULT_PIXEL_TO_CHARS_CUTOFF`), then it is assumed you're talking pixels, not characters. However, some of the "normally large" Elements have a cutoff value of 100. These include, for example, the `Multline` and `Output` elements.

If you're curious about the math used to do the character to pixels conversion, it's quite crude, but functional. The conversion is completed with the help of this variable:

`DEFAULT_PIXELS_TO_CHARS_SCALING = (10,26)`

The conversion simply takes your `size[0]` and multiplies by 10 and your `size[1]` and multiplies it by 26.

#### Colors

A string representing color. Anytime colors are involved, you can specify the tkinter color name such as 'lightblue' or an RGB hex value '\#RRGGBB'. For buttons, the color parameter is a tuple (text color, background color)

Anytime colors are written as a tuple in PySimpleGUI, the way to figure out which color is the background is to replace the "," with the word "on". ('white', 'red') specifies a button that is "white on red". Works anywhere there's a color tuple.

#### Pad

The amount of room around the element in pixels. The default value is (5,3) which means leave 5 pixels on each side of the x-axis and 3 pixels on each side of the y-axis. You can change this on a global basis using a call to SetOptions, or on an element basis.

If you want more pixels on one side than the other, then you can split the number into 2 number. If you want 200 pixels on the left side, and 3 pixels on the right, the pad would be ((200,3), 3). In this example, only the x-axis is split.

#### Font

Specifies the font family, size, and style. Font families on Windows include: \* Arial \* Courier \* Comic, \* Fixedsys \* Times \* Verdana \* Helvetica (the default I think)

The fonts will vary from system to system, however, Tk 8.0 automatically maps Courier, Helvetica and Times to their corresponding native family names on all platforms. Also, font families cannot cause a font specification to fail on Tk 8.0 and greater.

If you wish to leave the font family set to the default, you can put anything not a font name as the family. The PySimpleGUI Demo programs and documentation use the family 'Any' to demonstrate this fact.. You could use "default" if that's more clear to you.

There are 2 formats that can be used to specify a font... a string, and a tuple Tuple - (family, size, styles) String - "Family Size Styles"

To specify an underlined, Helvetica font with a size of 15 the values: ('Helvetica', 15, 'underline italics') 'Helvetica 15 underline italics'

#### Key

If you are going to do anything beyond the basic stuff with your GUI, then you need to understand keys. Keys are a way for you to "tag" an Element with a value that will be used to identify that element. After you put a key in an element's definition, the values returned from Read will use that key to tell you the value. For example, if you have an input field:

`Input(key='mykey')`

And your read looks like this: `event, values = Read()`

Then to get the input value from the read it would be: `values['mykey']`

You also use the same key if you want to call Update on an element. Please see the section below on Updates to understand that usage.

Keys can be ANYTHING. Let's say you have a window with a grid of input elements. You could use their row and column location as a key (a tuple)

`key=(row, col)`

Then when you read the `values` variable that's returned to you from calling `Window.Read()`, the key in the `values` variable will be whatever you used to create the element. In this case you would read the values as: `values[(row, col)]`

Most of the time they are simple text strings. In the Demo Programs, keys are written with this convention: `_KEY_NAME_` (underscore at beginning and end with all caps letters) or '-KEY\_NAME-. You don't have to follow that convention. It's used so that you can quickly spot when a key is being used.

To find an element's key, access the member variable `.Key` for the element. This assumes you've got the element in a variable already.

    text_elem = sg.Text('', key='-TEXT-')
    
    the_key = text_elem.Key

#### Visible

Beginning in version 3.17 you can create Elements that are initially invisible that you can later make visible.

To create an invisible Element, place the element in the layout like you normally would and add the parameter

`visible=False`.

Later when you want to make that Element visible you simply call the Element's `Update` method and pass in the parameter `visible=True`

This feature works best on Qt, but does work on the tkinter version as well. The visible parameter can also be used with the Column and Frame "container" Elements.

Note - Tkiner elements behave differently than Qt elements in how they arrange themselves when going from invisible to visible.

Tkinet elements tend to STACK themselves.

One workaround is to place the element in a Column with other elements on its row. This will hold the place of the row it is to be placed on. It will move the element to the end of the row however.

If you want to not only make the element invisible, on tkinter you can call \`Element.

Qt elements tend to hold their place really well and the window resizes itself nicely. It is more precise and less klunky.

Shortcut Functions / Multiple Function Names
--------------------------------------------

Perhaps not the best idea, but one that's done none the less is the naming of methods and functions. Some of the more "Heavily Travelled Elements" (and methods/functions) have "shortcuts".

In other words, I am lazy and don't like to type. The result is multiple ways to do exactly the same thing. Typically, the Demo Programs and other examples use the full name, or at least a longer name. Thankfully PyCharm will show you the same documentation regardless which you use.

This enables you to code much quicker once you are used to using the SDK. The Text Element, for example, has 3 different names `Text`, `Txt` or`T`. InputText can also be written `Input` or `In` .

The shortcuts aren't limited to Elements. The `Window` method `Window.FindElement` can be written as `Window.Element` because it's such a commonly used function. BUT,even that has now been shortened.

It's an ongoing thing. If you don't stay up to date and one of the newer shortcuts is used, you'll need to simply rename that shortcut in the code. For examples Replace sg.T with sg.Text if your version doesn't have sg.T in it.

Text Element \| `T == Txt == Text`
----------------------------------

Basic Element. It displays text.

    layout = [
                [sg.Text('This is what a Text Element looks like')],
             ]

<span class="image">simple text</span>

When creating a Text Element that you will later update, make sure you reserve enough characters for the new text. When a Text Element is created without a size parameter, it is created to exactly fit the characters provided.

With proportional spaced fonts (normally the default) the pixel size of one set of characters will differ from the pixel size of a different set of characters even though the set is of the same number of characters. In other words, not all letters use the same number of pixels. Look at the text you're reading right now and you will see this. An "i" takes up a less space then an "A".

------------------------------------------------------------------------

`Window.FindElement(key)` Shortcut `Window[key]`
------------------------------------------------

There's been a fantastic leap forward in making PySimpleGUI code more compact.

Instead of writing:

    window.FindElement(key).Update(new_value)
     ```
    
    You can now write it as:
    
    ```python
    window[key].Update(new_value)
     ```
    
    This change has been released to PyPI for PySimpleGUI
    
    MANY Thanks is owed to the person that suggested and showed me how to do this.  It's an incredible find.
    
    ## `Element.Update()` ->  `Element()` shortcut
    
    This has to be one of the strangest syntactical contructs I've ever written.  
    
    It is best used in combination with `FindElement` (see prior section on how to shortcut `FindElement`).  
    
    Normally to change an element, you "find" it, then call its `update` method.  The code usually looks like this, as you saw in the previous section:
    
    ```python
    window[key].update(new_value)

The code can be further compressed by removing the `.update` characters, resulting in this very compact looking call:

    window[key](new_value)

Yes, that's a valid statement in Python.

What's happening is that the element itself is being called. You can also writing it like this:

    elem = sg.Text('Some text', key='-TEXT-')
    elem('new text value')

Side note - you can also call your `window` variable directly. If you "call" it it will actually call `Window.read`.

    window = sg.Window(....)
    event, values = window()
    
    # is the same as
    window = sg.Window(....)
    event, values = window.read()

It is confusing looking however so when used, it might be a good idea to write a comment at the end of the statement to help out the poor beginner programmer coming along behind you.

Because it's such a foreign construct that someone with 1 week of Python classes will not reconize, the demos will continue to use the `.update` method.

It does not have to be used in conjuction with `FindElement`. The call works on any previously made Element. Sometimes elements are created, stored into a variable and then that variable is used in the layout. For example.

    graph_element = sg.Graph(...... lots of parms ......)
    
    layout = [[graph_element]]
    .
    .
    .
    graph_element(background_color='blue')      # this calls Graph.Update for the previously defined element

Hopefully this isn't too confusing. Note that the methods these shortcuts replace will not be removed. You can continue to use the old constructs without changes.

------------------------------------------------------------------------

### Fonts

Already discussed in the common parameters section. Either string or a tuple.

### Color in PySimpleGUI are in one of two formats - color name or RGB value.

Individual colors are specified using either the color names as defined in tkinter or an RGB string of this format:

    "#RRGGBB"        or          "darkblue"

### `auto_size_text`

A `True` value for `auto_size_text`, when placed on Text Elements, indicates that the width of the Element should be shrunk do the width of the text. The default setting is True. You need to remember this when you create `Text` elements that you are using for output.

`Text('', key='_TXTOUT_)` will create a `Text` Element that has 0 length. If you try to output a string that's 5 characters, it won't be shown in the window because there isn't enough room. The remedy is to manually set the size to what you expect to output

`Text('', size=(15,1), key='_TXTOUT_)` creates a `Text` Element that can hold 15 characters.

### Chortcut functions

The shorthand functions for `Text` are `Txt` and `T`

### Events `enable_events`

If you set the parameter `enable_events` then you will get an event if the user clicks on the Text.

Multiline Element
-----------------

This Element doubles as both an input and output Element.

    layout = [[sg.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))]]

<span class="image">multiline</span>

Text Input Element \| `InputText == Input == In`
------------------------------------------------

    layout = [[sg.InputText('Default text')]]

<span class="image">inputtext 2</span>

------------------------------------------------------------------------

#### Note about the `do_not_clear` parameter

This used to really trip people up, but don't think so anymore. The `do_not_clear` parameter is initialized when creating the InputText Element. If set to False, then the input field's contents will be erased after every `Window.Read()` call. Use this setting for when your window is an "Input Form" type of window where you want all of the fields to be erased and start over again every time.

Combo Element \| `Combo == InputCombo == DropDown == Drop`
----------------------------------------------------------

Also known as a drop-down list. Only required parameter is the list of choices. The return value is a string matching what's visible on the GUI.

    layout = [[sg.Combo(['choice 1', 'choice 2'])]]

<span class="image">combobox</span>

Listbox Element
---------------

The standard listbox like you'll find in most GUIs. Note that the return values from this element will be a ***list of results, not a single result***. This is because the user can select more than 1 item from the list (if you set the right mode).

    layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]

<span class="image">listbox 2</span>

------------------------------------------------------------------------

ListBoxes can cause a window to return from a Read call. If the flag `enable_events` is set, then when a user makes a selection, the Read immediately returns.

Another way ListBoxes can cause Reads to return is if the flag bind\_return\_key is set. If True, then if the user presses the return key while an entry is selected, then the Read returns. Also, if this flag is set, if the user double-clicks an entry it will return from the Read.

Slider Element
--------------

Sliders have a couple of slider-specific settings as well as appearance settings. Examples include the `orientation` and `range` settings.

    layout = [[sg.Slider(range=(1,500),
             default_value=222,
             size=(20,15),
             orientation='horizontal',
             font=('Helvetica', 12))]]

<span class="image">slider</span>



Radio Button Element
--------------------

Creates one radio button that is assigned to a group of radio buttons. Only 1 of the buttons in the group can be selected at any one time.

    layout =  [
        [sg.Radio('My first Radio!', "RADIO1", default=True),
        sg.Radio('My second radio!', "RADIO1")]
    ]

<span class="image">radio</span>

Checkbox Element \| `CBox == CB == Check`
-----------------------------------------

Checkbox elements are like Radio Button elements. They return a bool indicating whether or not they are checked.

    layout =  [[sg.Checkbox('My first Checkbox!', default=True), sg.Checkbox('My second Checkbox!')]]

<span class="image">checkbox</span>

Spin Element
------------

An up/down spinner control. The valid values are passed in as a list.

    layout =  [[sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('Volume level')]]

<span class="image">spinner</span>

Image Element
-------------

Images can be placed in your window provide they are in PNG, GIF, PPM/PGM format. JPGs cannot be shown because tkinter does not naively support JPGs. You can use the Python Imaging Library (PIL) package to convert your image to PNG prior to calling PySimpleGUI if your images are in JPG format.

    layout = [
                [sg.Image(r'C:\PySimpleGUI\Logos\PySimpleGUI_Logo_320.png')],
             ]

<span class="image">image</span>

You can specify an animated GIF as an image and can animate the GIF by calling `UpdateAnimation`. Exciting stuff!

<span class="image">loading animation</span>

You can call the method without setting the `time_between_frames` value and it will show a frame and immediately move on to the next frame. This enables you to do the inter-frame timing.

Button Element
--------------

**MAC USERS** - Macs suck when it comes to tkinter and button colors. It sucks so badly with colors that the `LookAndFeel` call is disabled. You cannot change button colors for Macs. You're stuck with the system default color if you are using the tkinter version of PySimpleGUI. The Qt version does not have this issue.

Buttons are the most important element of all! They cause the majority of the action to happen. After all, it's a button press that will get you out of a window, whether it be Submit or Cancel, one way or another a button is involved in all windows. The only exception is to this is when the user closes the window using the "X" in the upper corner which means no button was involved.

The Types of buttons include: \* Folder Browse \* File Browse \* Files Browse \* File SaveAs \* File Save \* Close window (normal button) \* Read window \* Realtime \* Calendar Chooser \* Color Chooser

Close window - Normal buttons like Submit, Cancel, Yes, No, do NOT close the window... they used to. Now to close a window you need to use a CloseButton / CButton.

Folder Browse - When clicked a folder browse dialog box is opened. The results of the Folder Browse dialog box are written into one of the input fields of the window.

File Browse - Same as the Folder Browse except rather than choosing a folder, a single file is chosen.

Calendar Chooser - Opens a graphical calendar to select a date.

Color Chooser - Opens a color chooser dialog

Read window - This is a window button that will read a snapshot of all of the input fields, but does not close the window after it's clicked.

Realtime - This is another async window button. Normal button clicks occur after a button's click is released. Realtime buttons report a click the entire time the button is held down.

Most programs will use a combination of shortcut button calls (Submit, Cancel, etc), normal Buttons which leave the windows open and CloseButtons that close the window when clicked.

Sometimes there are multiple names for the same function. This is simply to make the job of the programmer quicker and easier. Or they are old names that are no longer used but kept around so that existing programs don't break.

The 4 primary windows of PySimpleGUI buttons and their names are:

1.  `Button`= `ReadButton` = `RButton` = `ReadFormButton` (Use `Button`, others are old methods)
2.  `CloseButton` = `CButton`
3.  `RealtimeButton`
4.  `DummyButton`

You will find the long-form names in the older programs. ReadButton for example.

In Oct 2018, the definition of Button changed. Previously Button would CLOSE the window when clicked. It has been changed so the Button calls will leave the window open in exactly the same way as a ReadButton. They are the same calls now. To enables windows to be closed using buttons, a new button was added... `CloseButton` or `CButton`.

Your PySimpleGUI program is most likely going to contain only `Button` calls. The others are generally not foundin user code.

The most basic Button element call to use is `Button`

    layout =  [[sg.Button('Ok'), sg.Button('Cancel')]]

<span class="image">ok cancel 3</span>

You will rarely see these 2 buttons in particular written this way. Recall that PySimpleGUI is focused on YOU (which generally directly means.... less typing). As a result, the code for the above window is normally written using shortcuts found in the next section.

You will typically see this instead of calls to `Button`:

    layout =  [[sg.Ok(), sg.Cancel()]]

In reality `Button` is in fact being called on your behalf. Behind the scenes, `sg.Ok` and `sg.Cancel` call `Button` with the text set to `Ok` and `Cancel` and returning the results that then go into the layout. If you were to print the layout it will look identical to the first layout shown that has `Button` shown specifically in the layout.

### Button Element Shortcuts

These Pre-made buttons are some of the most important elements of all because they are used so much. They all basically do the same thing, **set the button text to match the function name and set the parameters to commonly used values**. If you find yourself needing to create a custom button often because it's not on this list, please post a request on GitHub. . They include:

-   OK
-   Ok
-   Submit
-   Cancel
-   Yes
-   No
-   Exit
-   Quit
-   Help
-   Save
-   SaveAs
-   Open

### "Chooser" Buttons

These buttons are used to show dialog boxes that choose something like a filename, date, color, etc. that are filled into an `InputText` Element (or some other "target".... see below regarding targets)

-   CalendarButton
-   ColorChooserButton
-   FileBrowse
-   FilesBrowse
-   FileSaveAs
-   FolderBrowse

**IMPORT NOTE ABOUT SHORTCUT BUTTONS** Prior to release 3.11.0, these buttons closed the window. Starting with 3.11 they will not close the window. They act like RButtons (return the button text and do not close the window)

If you are having trouble with these buttons closing your window, please check your installed version of PySimpleGUI by typing `pip list` at a command prompt. Prior to 3.11 these buttons close your window.

Using older versions, if you want a Submit() button that does not close the window, then you would instead use RButton('Submit'). Using the new version, if you want a Submit button that closes the window like the sold Submit() call did, you would write that as `CloseButton('Submit')` or `CButton('Submit')`

### Button targets

The `FileBrowse`, `FolderBrowse`, `FileSaveAs` , `FilesSaveAs`, `CalendarButton`, `ColorChooserButton` buttons all fill-in values into another element located on the window. The target can be a Text Element or an InputText Element or the button itself. The location of the element is specified by the `target` variable in the function call.

The Target comes in two forms. 1. Key 2. (row, column)

Targets that are specified using a key will find its target element by using the target's key value. This is the "preferred" method.

If the Target is specified using (row, column) then it utilizes a grid system. The rows in your GUI are numbered starting with 0. The target can be specified as a hard coded grid item or it can be relative to the button.

The (row, col) targeting can only target elements that are in the same "container". Containers are the Window, Column and Frame Elements. A File Browse button located inside of a Column is unable to target elements outside of that Column.

The default value for `target` is `(ThisRow, -1)`. `ThisRow` is a special value that tells the GUI to use the same row as the button. The Y-value of -1 means the field one value to the left of the button. For a File or Folder Browse button, the field that it fills are generally to the left of the button is most cases. (ThisRow, -1) means the Element to the left of the button, on the same row.

If a value of `(None, None)` is chosen for the target, then the button itself will hold the information. Later the button can be queried for the value by using the button's key.

Let's examine this window as an example:

<span class="image">file browse</span>

The `InputText` element is located at (1,0)... row 1, column 0. The `Browse` button is located at position (2,0). The Target for the button could be any of these values:

    Target = (1,0)
    Target = (-1,0)

The code for the entire window could be:

    layout = [[sg.T('Source Folder')],
                  [sg.In()],
                  [sg.FolderBrowse(target=(-1, 0)), sg.OK()]]

or if using keys, then the code would be:

    layout = [[sg.T('Source Folder')],
                  [sg.In(key='input')],
                  [sg.FolderBrowse(target='input'), sg.OK()]]

See how much easier the key method is?

#### Invisible Targets

One very handy trick is to make your target invisible. This will remove the ability to edit the chosen value like you normally would be able to with an Input Element. It's a way of making things look cleaner, less cluttered too perhaps.

### Save & Open Buttons

There are 4 different types of File/Folder open dialog box available. If you are looking for a file to open, the `FileBrowse` is what you want. If you want to save a file, `SaveAs` is the button. If you want to get a folder name, then `FolderBrowse` is the button to use. To open several files at once, use the `FilesBrowse` button. It will create a list of files that are separated by ';'

<span class="image">open</span>

<span class="image">folder</span>

<span class="image">saveas</span>

### Calendar Buttons

These buttons pop up a calendar chooser window. The chosen date is returned as a string.

<span class="image">calendar</span>

### Color Chooser Buttons

These buttons pop up a standard color chooser window. The result is returned as a tuple. One of the returned values is an RGB hex representation.

<span class="image">color</span>

### Custom Buttons

Not all buttons are created equal. A button that closes a window is different that a button that returns from the window without closing it. If you want to define your own button, you will generally do this with the Button Element `Button`, which closes the window when clicked.

    layout =  [[sg.Button('My Button')]]

<span class="image">button</span>

All buttons can have their text changed by changing the `button_text` parameter in the button call. It is this text that is returned when a window is read. This text will be what tells you which button was clicked. However, you can also use keys on your buttons so that they will be unique. If only the text were used, you would never be able to have 2 buttons in the same window with the same text.

    layout =  [[sg.Button('My Button', key='_BUTTON_KEY_')]]

With this layout, the event that is returned from a `Window.Read()` call when the button is clicked will be "`_BUTTON_KEY_`"

### Button Images

Now this is an exciting feature not found in many simplified packages.... images on buttons! You can make a pretty spiffy user interface with the help of a few button images.

Your button images need to be in PNG or GIF format. When you make a button with an image, set the button background to the same color as the background. There's a button color TRANSPARENT\_BUTTON that you can set your button color to in order for it to blend into the background. Note that this value is currently the same as the color as the default system background on Windows. If you want to set the button background color to the current system default, use the value COLOR\_SYSTEM\_DEFAULT as the background color.

This example comes from the `Demo Media Player.py` example program. Because it's a non-blocking button, it's defined as `RButton`. You also put images on blocking buttons by using `Button`.

    sg.Button('Restart Song', button_color=sg.TRANSPARENT_BUTTON,
                   image_filename=image_restart, image_size=(50, 50), image_subsample=2, border_width=0)

Three parameters are used for button images.

    image_filename - Filename. Can be a relative path
    image_size - Size of image file in pixels
    image_subsample - Amount to divide the size by.  2 means your image will be 1/2 the size.  3 means 1/3

Here's an example window made with button images.

<span class="image">media file player</span>

You'll find the source code in the file Demo Media Player. Here is what the button calls look like to create media player window \`\`\`python sg.Button('Pause', button\_color=sg.TRANSPARENT\_BUTTON, image\_filename=image\_pause, image\_size=(50, 50), image\_subsample=2, border\_width=0)

    Experimentation is sometimes required for these concepts to really sink in.
    
    ### Realtime Buttons
    
    Normally buttons are considered "clicked" when the mouse button is let UP after a downward click on the button.  What about times when you need to read the raw up/down button values.  A classic example for this is a robotic remote control.  Building a remote control using a GUI is easy enough.  One button for each of the directions is a start.  Perhaps something like this:
    
    ![robot remote](https://user-images.githubusercontent.com/13696193/44959958-ff9b7000-aec4-11e8-99ea-7450926409be.jpg)
    
    This window has 2 button types.  There's the normal "Read Button" (Quit) and 4 "Realtime Buttons".
    
    Here is the code to make, show and get results from this window:
    
    ```python
    import PySimpleGUI as sg
    
    gui_rows = [[sg.Text('Robotics Remote Control')],
                [sg.T(' '  * 10), sg.RealtimeButton('Forward')],
                [sg.RealtimeButton('Left'), sg.T(' '  * 15), sg.RealtimeButton('Right')],
                [sg.T(' '  * 10), sg.RealtimeButton('Reverse')],
                [sg.T('')],
                [sg.Quit(button_color=('black', 'orange'))]
                ]
    
    window = sg.Window('Robotics Remote Control', gui_rows)
    
    #
    # Some place later in your code...
    # You need to perform a Read or Refresh call on your window every now and then or
    # else it will apprear as if the program has locked up.
    #
    # your program's main loop
    while (True):
        # This is the code that reads and updates your window
        event, values = window.Read(timeout=50)
        print(event)
        if event in ('Quit', None):
            break
    
    window.Close()  # Don't forget to close your window!

This loop will read button values and print them. When one of the Realtime buttons is clicked, the call to `window.Read` will return a button name matching the name on the button that was depressed or the key if there was a key assigned to the button. It will continue to return values as long as the button remains depressed. Once released, the Read will return timeout events until a button is again clicked.

**File Types** The `FileBrowse` & `SaveAs` buttons have an additional setting named `file_types`. This variable is used to filter the files shown in the file dialog box. The default value for this setting is

    FileTypes=(("ALL Files", "*.*"),)

This code produces a window where the Browse button only shows files of type .TXT

    layout =  [[sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),))]]

NOTE - Mac users will not be able to use the file\_types parameter. tkinter has a bug on Macs that will crash the program is a file\_type is attempted so that feature had to be removed. Sorry about that!

***The ENTER key*** The ENTER key is an important part of data entry for windows. There's a long tradition of the enter key being used to quickly submit windows. PySimpleGUI implements this by tying the ENTER key to the first button that closes or reads a window.

The Enter Key can be "bound" to a particular button so that when the key is pressed, it causes the window to return as if the button was clicked. This is done using the `bind_return_key` parameter in the button calls. If there are more than 1 button on a window, the FIRST button that is of type Close window or Read window is used. First is determined by scanning the window, top to bottom and left to right.

ButtonMenu Element
------------------

The ButtonMenu element produces a unique kind of effect. It's a button, that when clicked, shows you a menu. It's like clicking one of the top-level menu items on a MenuBar. As a result, the menu definition take the format of a single menu entry from a normal menu definition. A normal menu definition is a list of lists. This definition is one of those lists.

     ['Menu', ['&Pause Graph', 'Menu item::optional_key']]

The very first string normally specifies what is shown on the menu bar. In this case, the value is **not used**. You set the text for the button using a different parameter, the `button_text` parm.

One use of this element is to make a "fake menu bar" that has a colored background. Normal menu bars cannot have their background color changed. Not so with ButtonMenus.

<span class="image">buttonmenu</span>

Return values for ButtonMenus are sent via the return values dictionary. If a selection is made, then an event is generated that will equal the ButtonMenu's key value. Use that key value to look up the value selected by the user. This is the same mechanism as the Menu Bar Element, but differs from the pop-up (right click) menu.

VerticalSeparator Element
-------------------------

This element has limited usefulness and is being included more for completeness than anything else. It will draw a line between elements.

It works best when placed between columns or elements that span multiple rows. If on a "normal" row with elements that are only 1 row high, then it will only span that one row.

    VerticalSeparator(pad=None)

<span class="image">snag-0129</span>

HorizontalSeparator Element
---------------------------

In PySimpleGUI, the tkinter port, there is no `HorizontalSeparator` Element. One will be added as a "stub" so that code is portable. It will likely do nothing just like the `Stretch` Element.

An easy way to get a horizontal line in PySimpleGUI is to use a `Text` Element that contains a line of underscores

    sg.Text('_'*30)             # make a horizontal line stretching 30 characters

ProgressBar Element
-------------------

The `ProgressBar` element is used to build custom Progress Bar windows. It is HIGHLY recommended that you use OneLineProgressMeter that provides a complete progress meter solution for you. Progress Meters are not easy to work with because the windows have to be non-blocking and they are tricky to debug.

The **easiest** way to get progress meters into your code is to use the `OneLineProgressMeter` API. This consists of a pair of functions, `OneLineProgressMeter` and `OneLineProgressMeterCancel`. You can easily cancel any progress meter by calling it with the current value = max value. This will mark the meter as expired and close the window. You've already seen OneLineProgressMeter calls presented earlier in this readme.

    sg.OneLineProgressMeter('My Meter', i+1, 1000,  'key', 'Optional message')

The return value for `OneLineProgressMeter` is: `True` if meter updated correctly `False` if user clicked the Cancel button, closed the window, or vale reached the max value.

#### Progress Meter in Your window

Another way of using a Progress Meter with PySimpleGUI is to build a custom window with a `ProgressBar` Element in the window. You will need to run your window as a non-blocking window. When you are ready to update your progress bar, you call the `UpdateBar` method for the `ProgressBar` element itself.

    import PySimpleGUI as sg
    
    # layout the window
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
              [sg.Cancel()]]
    
    # create the window`
    window = sg.Window('Custom Progress Meter', layout)
    progress_bar = window['progressbar']
    # loop that would normally do something useful
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.read(timeout=10)
        if event == 'Cancel'  or event is None:
            break
      # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i + 1)
    # done with loop... need to destroy the window as it's still open
    window.close()

<span class="image">progress custom</span>

Output Element
--------------

The Output Element is a re-direction of Stdout.

If you are looking for a way to quickly add the ability to show scrolling text within your window, then adding an `Output` Element is about as quick and easy as it gets.

**Anything "printed" will be displayed in this element.** This is the "trivial" way to show scrolling text in your window. It's as easy as dropping an Output Element into your window and then calling print as much as you want. The user will see a scrolling area of text inside their window.

***IMPORTANT*** You will NOT see what you `print` until you call either `window.Read` or `window.Refresh`. If you want to immediately see what was printed, call `window.Refresh()` immediately after your print statement.

    Output(size=(80,20))

<span class="image">output</span>

------------------------------------------------------------------------

Here's a complete solution for a chat-window using an Output Element. To display data that's received, you would to simply "print" it and it will show up in the output area. You'll find this technique used in several Demo Programs including the HowDoI application.

    import PySimpleGUI as sg
    
    def ChatBot():
        layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
                  [sg.Output(size=(80, 20))],
                  [sg.Multiline(size=(70, 5), enter_submits=True),
                   sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
                   sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
    
        window = sg.Window('Chat Window', layout, default_element_size=(30, 2))
    
        # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
        while True:
            event, value = window.read()
            if event == 'SEND':
                print(value)
            else:
                break
        window.close()
    ChatBot()

Column Element & Frame, Tab "Container" Elements
------------------------------------------------

Columns and Frames and Tabs are all "Container Elements" and behave similarly. This section focuses on Columns but can be applied elsewhere.

Starting in version 2.9 you'll be able to do more complex layouts by using the Column Element. Think of a Column as a window within a window. And, yes, you can have a Column within a Column if you want.

Columns are specified, like all "container elements", in exactly the same way as a window, as a list of lists.

Columns are needed when you want to specify more than 1 element in a single row.

For example, this layout has a single slider element that spans several rows followed by 7 `Text` and `Input` elements on the same row.

<span class="image">column</span>

Without a Column Element you can't create a layout like this. But with it, you should be able to closely match any layout created using tkinter only.

    import PySimpleGUI as sg
    
    # Demo of how columns work
    # window has on row 1 a vertical slider followed by a COLUMN with 7 rows
    # Prior to the Column element, this layout was not possible
    # Columns layouts look identical to window layouts, they are a list of lists of elements.
    
    window = sg.Window('Columns')                                   # blank window
    
    # Column layout
    col = [[sg.Text('col Row 1')],
           [sg.Text('col Row 2'), sg.Input('col input 1')],
           [sg.Text('col Row 3'), sg.Input('col input 2')],
           [sg.Text('col Row 4'), sg.Input('col input 3')],
           [sg.Text('col Row 5'), sg.Input('col input 4')],
           [sg.Text('col Row 6'), sg.Input('col input 5')],
           [sg.Text('col Row 7'), sg.Input('col input 6')]]
    
    layout = [[sg.Slider(range=(1,100), default_value=10, orientation='v', size=(8,20)), sg.Column(col)],
              [sg.In('Last input')],
              [sg.OK()]]
    
    # Display the window and get values
    
    window = sg.Window('Compact 1-line window with column', layout)
    event, values = window.read()
    window.Close()
    
    sg.Popup(event, values, line_width=200)

### Column, Frame, Tab, Window element\_justification

Beginning in Release 4.3 you can set the justification for any container element. This is done through the `element_justification` parameter. This will greatly help anyone that wants to center all of their content in a window. Previously it was difficult to do these kinds of layouts, if not impossible.

justify the `Column` element's row by setting the `Column`'s `justification` parameter.

You can also justify the entire contents within a `Column` by using the Column's `element_justification` parameter.

With these parameter's it is possible to create windows that have their contents centered. Previously this was very difficult to do.

This is currently only available in the primary PySimpleGUI port.

They can also be used to justify a group of elements in a particular way.

Placing `Column` elements inside `Columns` elements make it possible to create a multitude of

Sizer Element
-------------

New in 4.3 is the `Sizer` Element. This element is used to help create a container of a particular size. It can be placed inside of these PySimpleGUI items:

-   Column
-   Frame
-   Tab
-   Window

The implementation of a `Sizer` is quite simple. It returns an empty `Column` element that has a pad value set to the values passed into the `Sizer`. Thus isn't not a class but rather a "Shortcut function" similar to the pre-defined Buttons.

This feature is only available in the tkinter port of PySimpleGUI at the moment. A cross port is needed.

------------------------------------------------------------------------

Frame Element (Labelled Frames, Frames with a title)
----------------------------------------------------

Frames work exactly the same way as Columns. You create layout that is then used to initialize the Frame. Like a Column element, it's a "Container Element" that holds one or more elements inside.

<span class="image">frame element</span>

Notice how the Frame layout looks identical to a window layout. A window works exactly the same way as a Column and a Frame. They all are "container elements" - elements that contain other elements.

*These container Elements can be nested as deep as you want.* That's a pretty spiffy feature, right? Took a lot of work so be appreciative. Recursive code isn't trivial.

This code creates a window with a Frame and 2 buttons.

    frame_layout = [
                      [sg.T('Text inside of a frame')],
                      [sg.CB('Check 1'), sg.CB('Check 2')],
                   ]
    layout = [
              [sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='blue')],
              [sg.Submit(), sg.Cancel()]
             ]
    
    window = sg.Window('Frame with buttons', layout, font=("Helvetica", 12))

Canvas Element
--------------

In my opinion, the tkinter Canvas Widget is the most powerful of the tkinter widget. While I try my best to completely isolate the user from anything that is tkinter related, the Canvas Element is the one exception. It enables integration with a number of other packages, often with spectacular results.

However, there's another way to get that power and that's through the Graph Element, an even MORE powerful Element as it uses a Canvas that you can directly access if needed. The Graph Element has a large number of drawing methods that the Canvas Element does not have. Plus, if you need to, you can access the Graph Element's "Canvas" through a member variable.

### Matplotlib, Pyplot Integration

**NOTE - The newest version of Matplotlib (3.1.0) no longer works with this technique.** You must install 3.0.3 in order to use the Demo Matplotlib programs provided in the Demo Programs section.

One such integration is with Matploplib and Pyplot. There is a Demo program written that you can use as a design pattern to get an understanding of how to use the Canvas Widget once you get it.

    def Canvas(canvas - a tkinter canvasf if you created one. Normally not set
             background_color - canvas color
             size - size in pixels
             pad - element padding for packing
             key - key used to lookup element
             tooltip - tooltip text)

The order of operations to obtain a tkinter Canvas Widget is:

        figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
        # define the window layout
        layout = [[sg.Text('Plot test')],
                  [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
                  [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]
    
        # create the window and show it without the plot
        window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout).Finalize()
    
        # add the plot to the window
        fig_photo = draw_figure(window.FindElement('canvas').TKCanvas, fig)
    
        # show it all again and get buttons
        event, values = window.read()

To get a tkinter Canvas Widget from PySimpleGUI, follow these steps: \* Add Canvas Element to your window \* Layout your window \* Call `window.Finalize()` - this is a critical step you must not forget \* Find the Canvas Element by looking up using key \* Your Canvas Widget Object will be the found\_element.TKCanvas \* Draw on your canvas to your heart's content \* Call `window.read()` - Nothing will appear on your canvas until you call Read

See `Demo_Matplotlib.py` for a Recipe you can copy.

### Methods & Properties

TKCanvas - not a method but a property. Returns the tkinter Canvas Widget

Graph Element
-------------

All you math fans will enjoy this Element... and all you non-math fans will enjoy it even more.

I've found nothing to be less fun than dealing with a graphic's coordinate system from a GUI Framework. It's always upside down from what I want. (0,0) is in the upper left hand corner.... sometimes... or was it in the lower left? In short, it's a **pain in the ass**.

How about the ability to get your own location of (0,0) and then using those coordinates instead of what tkinter provides? This results in a very powerful capability - working in your own units, and then displaying them in an area defined in pixels.

If you've ever been frustrated with where (0,0) is located on some surface you draw on, then fear not, your frustration ends right here. You get to draw using whatever coordinate system you want. Place (0,0) anywhere you want, including not anywhere on your Graph. You could define a Graph that's all negative numbers between -2.1 and -3.5 in the X axis and -3 to -8.2 in the Y axis

There are 3 values you'll need to supply the Graph Element. They are:

-   Size of the canvas in pixels
-   The lower left (x,y) coordinate of your coordinate system
-   The upper right (x,y) coordinate of your coordinate system

After you supply those values you can scribble all of over your graph by creating Graph Figures. Graph Figures are created, and a Figure ID is obtained by calling:

-   DrawCircle
-   DrawLine
-   DrawPoint
-   DrawRectangle
-   DrawOval
-   DrawImage

You can move your figures around on the canvas by supplying the Figure ID the **x,y delta** to move. It does not move to an absolute position, but rather an offset from where the figure is now. (Use Relocate to move to a specific location)

    graph.MoveFigure(my_circle, 10, 10)

You'll also use this ID to delete individual figures you've drawn:

    graph.DeleteFigure(my_circle)

### Mouse Events Inside Graph Elements

If you have eneabled events for your Graph Element, then you can receive mouse click events. If you additionally enable `drag_submits` in your creation of the Graph Element, then you will also get events when you "DRAG" inside of a window. A "Drag" is defined as a left button down and then the mouse is moved.

When a drag event happens, the event will be the Graph Element's key. The `value` returned in the values dictionary is a tuple of the (x,y) location of the mouse currently.

This means you'll get a "stream" of events. If the mouse moves, you'll get at LEAST 1 and likely a lot more than 1 event.

### Mouse Up Event for Drags

When you've got `drag_submits` enabled, there's a sticky situation that arises.... what happens when you're done dragging and you've let go of the mouse button? How is the "Mouse Up" event relayed back to your code.

The "Mouse Up" will generate an event to you with the value: `Graph_key` + `'+UP'`. Thus, if your Graph Element has a key of `'_GRAPH_'`, then the event you will receive when the mouse button is released is: `'_GRAPH_+UP'`

Yea, it's a little weird, but it works. It's SIMPLE too. I recommend using the `.startswith` and `.endswith` built-ins when dealing with these kinds of string values.

Here is an example of the `events` and the `values dictionary` that was generated by clicking and dragging inside of a Graph Element with the key == 'graph':

    graph {'graph': (159, 256)}
    graph {'graph': (157, 256)}
    graph {'graph': (157, 256)}
    graph {'graph': (157, 254)}
    graph {'graph': (157, 254)}
    graph {'graph': (154, 254)}
    graph {'graph': (154, 254)}
    graph+UP {'graph': (154, 254)}

Table Element
-------------

Table and Tree Elements are of the most complex in PySimpleGUI. They have a lot of options and a lot of unusual characteristics.

### `window.read()` return values from Table Element

The values returned from a `Window.Read` call for the Table Element are a list of row numbers that are currently highlighted.

### The Qt `Table.Get()` call

New in **PySimpleGUIQt** is the addition of the `Table` method `Get`. This method returns the table that is currently being shown in the GUI. This method was required in order to obtain any edits the user may have made to the table.

For the tkinter port, it will return the same values that was passed in when the table was created because tkinter Tables cannot be modified by the user (please file an Issue if you know a way).

### Known `Table` visualization problem....

There has been an elusive problem where clicking on or near the table's header caused tkinter to go crazy and resize the columns continuously as you moved the mouse.

This problem has existed since the first release of the `Table` element. It was fixed in release 4.3.

### Known table colors in Python 3.7.3, 3.7.4, 3.8, ?

The tkinter that's been released in the past several releases of Python has a bug. Table colors of all types are not working, at all. The background of the rows never change. If that's important to you, you'll need to **downgrade** your Python version. 3.6 works really well with PySimpleGUI and tkinter.

### Empty Tables

If you wish to start your table as being an empty one, you will need to specify an empty table. This list comprehension will create an empty table with 15 rows and 6 columns.

    data = [['' for row in range(15)]for col in range(6)]

### Events from Tables

There are two ways to get events generated from Table Element.  
`change_submits` event generated as soon as a row is clicked on `bind_return_key` event generate when a row is double clicked or the return key is press while on a row.

Tree Element
------------

The Tree Element and Table Element are close cousins. Many of the parameters found in the Table Element apply to Tree Elements. In particular the heading information, column widths, etc.

Unlike Tables there is no standard format for trees. Thus the data structure passed to the Tree Element must be constructed. This is done using the TreeData class. The process is as follows:

-   Get a TreeData Object
-   "Insert" data into the tree
-   Pass the filled in TreeData object to Tree Element

#### TreeData format

    def TreeData()
    def Insert(self, parent, key, text, values, icon=None)

To "insert" data into the tree the TreeData method Insert is called.

    Insert(parent_key, key, display_text, values)

To indicate insertion at the head of the tree, use a parent key of "". So, every top-level node in the tree will have a parent node = ""

This code creates a TreeData object and populates with 3 values

    treedata = sg.TreeData()
    
    treedata.Insert("", '_A_', 'A', [1,2,3])
    treedata.Insert("", '_B_', 'B', [4,5,6])
    treedata.Insert("_A_", '_A1_', 'A1', ['can','be','anything'])

Note that you ***can*** use the same values for display\_text and keys. The only thing you have to watch for is that you cannot repeat keys.

When Reading a window the Table Element will return a list of rows that are selected by the user. The list will be empty is no rows are selected.

#### Icons on Tree Entries

If you wish to show an icon next to a tree item, then you specify the icon in the call to `Insert`. You pass in a filename or a Base64 bytes string using the optional `icon` parameter.

Here is the result of showing an icon with a tree entry.

<span class="image">image</span>

Tab and Tab Group Elements
--------------------------

Tabs are another of PySimpleGUI "Container Elements". It is capable of "containing" a layout just as a window contains a layout. Other container elements include the `Column` and `Frame` elements.

Just like windows and the other container elements, the `Tab` Element has a layout consisting of any desired combination of Elements in any desired layouts. You can have Tabs inside of Tabs inside of Columns inside of Windows, etc.

`Tab` layouts look exactly like Window layouts, that is they are **a list of lists of Elements**.

*How you place a Tab element into a window is different than all other elements.* You cannot place a Tab directly into a Window's layout.

Also, tabs cannot be made invisible at this time. They have a visibily parameter but calling update will not change it.

Tabs are contained in TabGroups. They are **not** placed into other layouts. To get a Tab into your window, first place the `Tab` Element into a `TabGroup` Element and then place the `TabGroup` Element into the Window layout.

Let's look at this Window as an example:

<span class="image">tabbed 1</span>

View of second tab:

<span class="image">tabbed 2</span>

    tab1_layout =  [[sg.T('This is inside tab 1')]]
    
    tab2_layout = [[sg.T('This is inside tab 2')],
                   [sg.In(key='in')]]

The layout for the entire window looks like this:

    layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
                  [sg.Button('Read')]]

The Window layout has the TabGroup and within the tab Group are the two Tab elements.

One important thing to notice about all of these container Elements and Windows layouts... they all take a "list of lists" as the layout. They all have a layout that looks like this `[[   ]]`

You will want to keep this `[[ ]]` construct in your head a you're debugging your tabbed windows. It's easy to overlook one or two necessary \['s

As mentioned earlier, the old-style Tabs were limited to being at the Window-level only. In other words, the tabs were equal in size to the entire window. This is not the case with the "new-style" tabs. This is why you're not going to be upset when you discover your old code no longer works with the new PySimpleGUI release. It'll be worth the few moments it'll take to convert your code.

Check out what's possible with the NEW Tabs!

<span class="image">tabs tabs tabs</span>

Check out Tabs 7 and 8. We've got a Window with a Column containing Tabs 5 and 6. On Tab 6 are... Tabs 7 and 8.

As of Release 3.8.0, not all of *options* shown in the API definitions of the Tab and TabGroup Elements are working. They are there as placeholders.

First we have the Tab layout definitions. They mirror what you see in the screen shots. Tab 1 has 1 Text Element in it. Tab 2 has a Text and an Input Element.

### Reading Tab Groups

Tab Groups now return a value when a Read returns. They return which tab is currently selected. There is also a `enable_events` parameter that can be set that causes a Read to return if a Tab in that group is selected / changed. The key or title belonging to the Tab that was switched to will be returned as the value

x\#\# Pane Element

New in version 3.20 is the Pane Element, a super-cool tkinter feature. You won't find this one in PySimpleGUIQt, only PySimpleGUI. It's difficult to describe one of these things. Think of them as "Tabs without labels" that you can slide.

<span class="image">pane3</span>

***Each "Pane" of a Pane Element must be a Column Element***. The parameter `pane_list` is a list of Column Elements.

Calls can get a little hairy looking if you try to declare everything in-line as you can see in this example.

    sg.Pane([col5, sg.Column([[sg.Pane([col1, col2, col4], handle_size=15, orientation='v',  background_color=None, show_handle=True, visible=True, key='_PANE_', border_width=0,  relief=sg.RELIEF_GROOVE),]]),col3 ], orientation='h', background_color=None, size=(160,160), relief=sg.RELIEF_RAISED, border_width=0)

Combing these with *visibility* make for an interesting interface with entire panes being hidden from view until neded by the user. It's one way of producing "dynamic" windows.

Colors
------

Starting in version 2.5 you can change the background colors for the window and the Elements.

Your windows can go from this:

<span class="image">snap0155</span>

to this... with one function call...

<span class="image">snap0156</span>

While you can do it on an element by element or window level basis, the easiest way, by far, is a call to `SetOptions`.

Be aware that once you change these options they are changed for the rest of your program's execution. All of your windows will have that look and feel, until you change it to something else (which could be the system default colors.

This call sets all of the different color options.

    SetOptions(background_color='#9FB8AD',
           text_element_background_color='#9FB8AD',
           element_background_color='#9FB8AD',
           scrollbar_color=None,
           input_elements_background_color='#F7F3EC',
           progress_meter_color = ('green', 'blue')
           button_color=('white','#475841'))

SystemTray
==========

This is a PySimpleGUIQt and PySimpleGUIWx only feature. Don't know of a way to do it using tkinter. Your source code for SystemTray is identical for the Qt and Wx implementations. You can switch frameworks by simply changing your import statement.

In addition to running normal windows, it's now also possible to have an icon down in the system tray that you can read to get menu events. There is a new SystemTray object that is used much like a Window object. You first get one, then you perform Reads in order to get events.

Here is the definition of the SystemTray object.

    SystemTray(menu=None, filename=None, data=None, data_base64=None, tooltip=None):
            '''
     SystemTray - create an icon in the system tray
     :param menu: Menu definition
     :param filename: filename for icon
     :param data: in-ram image for icon
     :param data_base64: basee-64 data for icon
     :param tooltip: tooltip string '''

You'll notice that there are 3 different ways to specify the icon image. The base-64 parameter allows you to define a variable in your .py code that is the encoded image so that you do not need any additional files. Very handy feature.

System Tray Design Pattern
--------------------------

Here is a design pattern you can use to get a jump-start.

This program will create a system tray icon and perform a blocking Read. If the item "Open" is chosen from the system tray, then a popup is shown.

    import PySimpleGUIQt as sg
    
    menu_def = ['BLANK', ['&Open', '---', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]
    
    tray = sg.SystemTray(menu=menu_def, filename=r'default_icon.ico')
    
    while True:  # The event loop
      menu_item = tray.Read()
        print(menu_item)
        if menu_item == 'Exit':
            break
        elif menu_item == 'Open':
            sg.Popup('Menu item chosen', menu_item)

The design pattern creates an icon that will display this menu: <span class="image">snag-0293</span>

### Icons

When specifying "icons", you can use 3 different formats. \* `filename`- filename \* `data_base64` - base64 byte string \* '`data` - in-ram bitmap or other "raw" image

You will find 3 parameters used to specify these 3 options on both the initialize statement and on the Update method.

Menu Definition
---------------

    menu_def = ['BLANK', ['&Open', '&Save', ['1', '2', ['a', 'b']], '!&Properties', 'E&xit']]

A menu is defined using a list. A "Menu entry" is a string that specifies: \* text shown \* keyboard shortcut \* key

See section on Menu Keys for more information on using keys with menus.

An entry without a key and keyboard shortcut is a simple string `'Menu Item'`

If you want to make the "M" be a keyboard shortcut, place an `&` in front of the letter that is the shortcut. `'&Menu Item'`

You can add "keys" to make menu items unique or as another way of identifying a menu item than the text shown. The key is added to the text portion by placing `::` after the text.

`'Menu Item::key'`

The first entry can be ignored.`'BLANK`' was chosen for this example. It's this way because normally you would specify these menus under some heading on a menu-bar. But here there is no heading so it's filled in with any value you want.

**Separators** If you want a separator between 2 items, add the entry `'---'` and it will add a separator item at that place in your menu.

**Disabled menu entries**

If you want to disable a menu entry, place a `!` before the menu entry

SystemTray Methods
------------------

### Read - Read the context menu or check for events

    def Read(timeout=None)
        '''
     Reads the context menu
     :param timeout: Optional.  Any value other than None indicates a non-blocking read
     :return:   String representing meny item chosen. None if nothing read.
        '''

The `timeout` parameter specifies how long to wait for an event to take place. If nothing happens within the timeout period, then a "timeout event" is returned. These types of reads make it possible to run asynchronously. To run non-blocked, specify `timeout=0`on the Read call.

Read returns the menu text, complete with key, for the menu item chosen. If you specified `Open::key` as the menu entry, and the user clicked on `Open`, then you will receive the string `Open::key` upon completion of the Read.

#### Read special return values

In addition to Menu Items, the Read call can return several special values. They include:

EVENT\_SYSTEM\_TRAY\_ICON\_DOUBLE\_CLICKED - Tray icon was double clicked EVENT\_SYSTEM\_TRAY\_ICON\_ACTIVATED - Tray icon was single clicked EVENT\_SYSTEM\_TRAY\_MESSAGE\_CLICKED - a message balloon was clicked TIMEOUT\_KEY is returned if no events are available if the timeout value is set in the Read call

### Hide

Hides the icon. Note that no message balloons are shown while an icon is hidden.

    def Hide()

### Close

Does the same thing as hide

    def Close()

### UnHide

Shows a previously hidden icon

    def UnHide()

### ShowMessage

Shows a balloon above the icon in the system tray area. You can specify your own icon to be shown in the balloon, or you can set `messageicon` to one of the preset values.

This message has a custom icon.

<span class="image">snag-0286</span>

The preset `messageicon` values are:

    SYSTEM_TRAY_MESSAGE_ICON_INFORMATION
    SYSTEM_TRAY_MESSAGE_ICON_WARNING
    SYSTEM_TRAY_MESSAGE_ICON_CRITICAL
    SYSTEM_TRAY_MESSAGE_ICON_NOICON
    
    ShowMessage(title, message, filename=None, data=None, data_base64=None, messageicon=None, time=10000):
    '''
     Shows a balloon above icon in system tray
     :param title:  Title shown in balloon
     :param message: Message to be displayed
     :param filename: Optional icon filename
     :param data: Optional in-ram icon
     :param data_base64: Optional base64 icon
     :param time: How long to display message in milliseconds  :return:
     '''

Note, on windows it may be necessary to make a registry change to enable message balloons to be seen. To fix this, you must create the DWORD you see in this screenshot.

<span class="image">snag-0285</span>

### Update

You can update any of these items within a SystemTray object \* Menu definition \* Icon \* Tooltip

Change them all or just 1.

Global Settings
===============

There are multiple ways to customize PySimpleGUI. The call with the most granularity (allows access to specific and precise settings). The `ChangeLookAndFeel` call is in reality a single call to `SetOptions` where it changes 13 different settings.

**Mac Users** - You can't call `ChangeLookAndFeel` but you can call `SetOptions` with any sets of values you want. Nothing is being blocked or filtered.

**These settings apply to all windows that are created in the future.**

`SetOptions`. The options and Element options will take precedence over these settings. Settings can be thought of as levels of settings with the window-level being the highest and the Element-level the lowest. Thus the levels are:

-   Global
-   Window
-   Element

Each lower level overrides the settings of the higher level. Once settings have been changed, they remain changed for the duration of the program (unless changed again).

Persistent windows (Window stays open after button click)
=========================================================

Apologies that the next few pages are perhaps confusing. There have been a number of changes recently in PySimpleGUI's Read calls that added some really cool stuff, but at the expense of being not so simple. Part of the issue is an attempt to make sure existing code doesn't break. These changes are all in the area of non-blocking reads and reads with timeouts.

There are 2 ways to keep a window open after the user has clicked a button. One way is to use non-blocking windows (see the next section). The other way is to use buttons that 'read' the window instead of 'close' the window when clicked. The typical buttons you find in windows, including the shortcut buttons, close the window. These include OK, Cancel, Submit, etc. The Button Element also closes the window.

The `RButton` Element creates a button that when clicked will return control to the user, but will leave the window open and visible. This button is also used in Non-Blocking windows. The difference is in which call is made to read the window. The normal `Read` call with no parameters will block, a call with a `timeout` value of zero will not block.

Note that `InputText` and `MultiLine` Elements will be **cleared** when performing a `Read`. If you do not want your input field to be cleared after a `Read` then you can set the `do_not_clear` parameter to True when creating those elements. The clear is turned on and off on an element by element basis.

The reasoning behind this is that Persistent Windows are often "forms". When "submitting" a form you want to have all of the fields left blank so the next entry of data will start with a fresh window. Also, when implementing a "Chat Window" type of interface, after each read / send of the chat data, you want the input field cleared. Think of it as a Texting application. Would you want to have to clear your previous text if you want to send a second text?

The design pattern for Persistent Windows was already shown to you earlier in the document... here it is for your convenience.

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
    
    window.Close()

Read(timeout = t, timeout\_key=TIMEOUT\_KEY)
--------------------------------------------

Read with a timeout is a very good thing for your GUIs to use in a read non-blocking situation, you can use them. If your device can wait for a little while, then use this kind of read. The longer you're able to add to the timeout value, the less CPU time you'll be taking.

One way of thinking of reads with timeouts:

> During the timeout time, you are "yielding" the processor to do other tasks.

But it gets better than just being a good citizen....**your GUI will be more responsive than if you used a non-blocking read**

Let's say you had a device that you want to "poll" every 100ms. The "easy way out" and the only way out until recently was this:

    # YOU SHOULD NOT DO THIS....
    while True:             # Event Loop
        event, values = window.ReadNonBlocking()   # DO NOT USE THIS CALL ANYMORE
        read_my_hardware() # process my device here
        time.sleep(.1)     # sleep 1/10 second

This program will quickly test for user input, then deal with the hardware. Then it'll sleep for 100ms, while your gui is non-responsive, then it'll check in with your GUI again. I fully realize this is a crude way of doing things. We're talking dirt simple stuff without trying to use threads, etc to 'get it right'. It's for demonstration purposes.

The new and better way.... using the Read Timeout mechanism, the sleep goes away.

    # This is the right way to poll for hardware
    while True:             # Event Loop
        event, values = window.Read(timeout = 100)
        read_my_hardware() # process my device here

This event loop will run every 100 ms. You're making a Read call, so anything that the use does will return back to you immediately, and you're waiting up to 100ms for the user to do something. If the user doesn't do anything, then the read will timeout and execution will return to the program.

Non-Blocking Windows (Asynchronous reads, timeouts)
---------------------------------------------------

You can easily spot a non-blocking call in PySimpleGUI. If you see a call to `Window.Read()` with a timeout parameter set to a value other than `None`, then it is a non-blocking call.

This call to read is asynchronous as it has a timeout value:

    The new way
    ```python
    event, values = sg.Read(timeout=20)

You should use the new way if you're reading this for the first time.

The difference in the 2 calls is in the value of event. For ReadNonBlocking, event will be `None` if there are no other events to report. There is a "problem" with this however. With normal Read calls, an event value of None signified the window was closed. For ReadNonBlocking, the way a closed window is returned is via the values variable being set to None.

sg.TIMEOUT\_KEY
---------------

If you're using the new, timeout=0 method, then an event value of None signifies that the window was closed, just like a normal Read. That leaves the question of what it is set to when not other events are happening. This value will be the value of `timeout_key`. If you did not specify a timeout\_key value in your call to read, then it will be set to a default value of: `TIMEOUT_KEY = __timeout__`

If you wanted to test for "no event" in your loop, it would be written like this:

    while True:
        event, value = window.Read(timeout=0)
        if event is None:
            break # the use has closed the window
        if event == sg.TIMEOUT_KEY:
            print("Nothing happened")

Use async windows sparingly. It's possible to have a window that appears to be async, but it is not. **Please** try to find other methods before going to async windows. The reason for this plea is that async windows poll tkinter over and over. If you do not have a timeout in your Read and yuou've got nothing else your program will block on, then you will eat up 100% of the CPU time. It's important to be a good citizen. Don't chew up CPU cycles needlessly. Sometimes your mouse wants to move ya know?

Non-blocking (timeout=0) is generally reserved as a "last resort". Too many times people use non-blocking reads when a blocking read will do just fine.

### Small Timeout Values (under 10ms)

***Do Not*** use a timeout of less than 10ms. Otherwise you will simply thrash, spending your time trying to do some GUI stuff, only to be interruped by a timeout timer before it can get anything done. The results are potentially disasterous.

There is a hybrid approach... a read with a timeout. You'll score much higher points on the impressive meter if you're able to use a lot less CPU time by using this type of read.

The most legit time to use a non-blocking window is when you're working directly with hardware. Maybe you're driving a serial bus. If you look at the Event Loop in the Demo\_OpenCV\_Webcam.py program, you'll see that the read is a non-blocking read. However, there is a place in the event loop where blocking occurs. The point in the loop where you will block is the call to read frames from the webcam. When a frame is available you want to quickly deliver it to the output device, so you don't want your GUI blocking. You want the read from the hardware to block.

Another example can be found in the demo for controlling a robot on a Raspberry Pi. In that application you want to read the direction buttons, forward, backward, etc, and immediately take action. If you are using RealtimeButtons, your only option at the moment is to use non-blocking windows. You have to set the timeout to zero if you want the buttons to be real-time responsive.

However, with these buttons, adding a sleep to your event loop will at least give other processes time to execute. It will, however, starve your GUI. The entire time you're sleeping, your GUI isn't executing.

### Periodically Calling`Read`

Let's say you do end up using non-blocking reads... then you've got some housekeeping to do. It's up to you to periodically "refresh" the visible GUI. The longer you wait between updates to your GUI the more sluggish your windows will feel. It is up to you to make these calls or your GUI will freeze.

There are 2 methods of interacting with non-blocking windows. 1. Read the window just as you would a normal window 2. "Refresh" the window's values without reading the window. It's a quick operation meant to show the user the latest values

With asynchronous windows the window is shown, user input is read, but your code keeps right on chugging. YOUR responsibility is to call `PySimpleGUI.Read` on a periodic basis. Several times a second or more will produce a reasonably snappy GUI.

\#\# Exiting (Closing) a Persistent Window

If your window has a button that closes the window, then PySimpleGUI will automatically close the window for you. If all of your buttons are ReadButtons, then it'll be up to you to close the window when done. To close a window, call the `Close` method.

    window.Close()

Persistent Window Example - Running timer that updates
------------------------------------------------------

See the sample code on the GitHub named Demo Media Player for another example of Async windows. We're going to make a window and update one of the elements of that window every .01 seconds. Here's the entire code to do that.

    import PySimpleGUI as sg
    import time
    
    # ----------------  Create Form  ----------------
    sg.ChangeLookAndFeel('Black')
    sg.SetOptions(element_padding=(0, 0))
    
    layout = [[sg.Text('')],
             [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
             [sg.ReadButton('Pause', key='button', button_color=('white', '#001480')),
              sg.ReadButton('Reset', button_color=('white', '#007339'), key='Reset'),
              sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]
    
    window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)
    
    # ----------------  main loop  ----------------
    current_time = 0
    paused = False
    start_time = int(round(time.time() * 100))
    while (True):
        # --------- Read and update window --------
        event, values = window.Read(timeout=10)
        current_time = int(round(time.time() * 100)) - start_time
        # --------- Display timer in window --------
        window.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                      (current_time // 100) % 60,
                                                                      current_time % 100))

Previously this program was implemented using a sleep in the loop to control the clock tick. This version uses the new timeout parameter. The result is a window that reacts quicker then the one with the sleep and the accuracy is just as good.

Instead of a Non-blocking Read --- Use `enable_events = True` or `return_keyboard_events = True`
------------------------------------------------------------------------------------------------

Any time you are thinking "I want an X Element to cause a Y Element to do something", then you want to use the `enable_events` option.

***Instead of polling, try options that cause the window to return to you.*** By using non-blocking windows, you are *polling*. You can indeed create your application by polling. It will work. But you're going to be maxing out your processor and may even take longer to react to an event than if you used another technique.

**Examples**

One example is you have an input field that changes as you press buttons on an on-screen keypad.

<span class="image">keypad 3</span>

Updating Elements (changing element's values in an active window)
=================================================================

If you want to change an Element's settings in your window after the window has been created, then you will call the Element's Update method.

**NOTE** a window **must be Read or Finalized** before any Update calls can be made. Also, not all settings available to you when you created the Element are available to you via its `Update` method.

Here is an example of updating a Text Element

    import PySimpleGUI as sg
    
    layout = [ [sg.Text('My layout', key='_TEXT_')],
               [sg.Button('Read')]]
    
    window = sg.Window('My new window', layout)
    
    while True:             # Event Loop
        event, values = window.read()
        if event is None:
            break
        window.Element('_TEXT_').Update('My new text value')

Notice the placement of the Update call. If you wanted to Update the Text Element *prior* to the Read call, outside of the event loop, then you must call Finalize on the window first.

In this example, the Update is done prior the Read. Because of this, the Finalize call is added to the Window creation.

    import PySimpleGUI as sg
    
    layout = [ [sg.Text('My layout', key='_TEXT_')],
               [sg.Button('Read')]
             ]
    
    window = sg.Window('My new window', layout).Finalize()
    
    window.Element('_TEXT_').Update('My new text value')
    
    while True:             # Event Loop
      event, values = window.read()
        if event is None:
            break

Persistent windows remain open and thus continue to interact with the user after the Read has returned. Often the program wishes to communicate results (output information) or change an Element's values (such as populating a List Element).

You can use Update to do things like: \* Have one Element (appear to) make a change to another Element \* Disable a button, slider, input field, etc \* Change a button's text \* Change an Element's text or background color \* Add text to a scrolling output window \* Change the choices in a list \* etc

The way this is done is via an Update method that is available for nearly all of the Elements. Here is an example of a program that uses a persistent window that is updated.

<span class="image">snap0272</span>

In some programs these updates happen in response to another Element. This program takes a Spinner and a Slider's input values and uses them to resize a Text Element. The Spinner and Slider are on the left, the Text element being changed is on the right.

    # Testing async window, see if can have a slider
    # that adjusts the size of text displayed
    
    import PySimpleGUI as sg
    fontSize = 12
    layout = [[sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin'),
               sg.Slider(range=(6,172), orientation='h', size=(10,20),
               change_submits=True, key='slider', font=('Helvetica 20')),
               sg.Text("Aa", size=(2, 1), font="Helvetica "  + str(fontSize), key='text')]]
    
    sz = fontSize
    window = sg.Window("Font size selector", layout, grab_anywhere=False)
    # Event Loop
    while True:
        event, values= window.read()
        if event is None:
            break
        sz_spin = int(values['spin'])
        sz_slider = int(values['slider'])
        sz = sz_spin if sz_spin != fontSize else sz_slider
        if sz != fontSize:
            fontSize = sz
            font = "Helvetica "  + str(fontSize)
            window.FindElement('text').Update(font=font)
            window.FindElement('slider').Update(sz)
            window.FindElement('spin').Update(sz)
    
    print("Done.")

Inside the event loop we read the value of the Spinner and the Slider using those Elements' keys. For example, `values['slider']` is the value of the Slider Element.

This program changes all 3 elements if either the Slider or the Spinner changes. This is done with these statements:

    window.FindElement('text').Update(font=font)
    window.FindElement('slider').Update(sz)
    window.FindElement('spin').Update(sz)

Remember this design pattern because you will use it OFTEN if you use persistent windows.

It works as follows. The call to `window.FindElement` returns the Element object represented by they provided `key`. This element is then updated by calling it's `Update` method. This is another example of Python's "chaining" feature. We could write this code using the long-form:

    text_element = window.FindElement('text')
    text_element.Update(font=font)

The takeaway from this exercise is that keys are key in PySimpleGUI's design. They are used to both read the values of the window and also to identify elements. As already mentioned, they are used as targets in Button calls.

### Locating Elements (FindElement == Element == Elem)

The Window method call that's used to find an element is: `FindElement` or the shortened version `Element` or even shorter (version 4.1+) `Elem`

When you see a call to window.FindElement or window.Element, then you know an element is being addressed. Normally this is done so you can call the element's Update method.

### ProgressBar / Progress Meters

Note that to change a progress meter's progress, you call `UpdateBar`, not `Update`.

Keyboard & Mouse Capture
========================

NOTE - keyboard capture is currently formatted uniquely among the ports. For basic letters and numbers there is no great differences, but when you start adding Shift and Control or special keyus, they all behave slightly differently. Your best bet is to simply print what is being returned to you to determine what the format for the particular port is.

Beginning in version 2.10 you can capture keyboard key presses and mouse scroll-wheel events. Keyboard keys can be used, for example, to detect the page-up and page-down keys for a PDF viewer. To use this feature, there's a boolean setting in the Window call `return_keyboard_events` that is set to True in order to get keys returned along with buttons.

Keys and scroll-wheel events are returned in exactly the same way as buttons.

For scroll-wheel events, if the mouse is scrolled up, then the `button` text will be `MouseWheel:Up`. For downward scrolling, the text returned is `MouseWheel:Down`

Keyboard keys return 2 types of key events. For "normal" keys (a,b,c, etc), a single character is returned that represents that key. Modifier and special keys are returned as a string with 2 parts:

    Key Sym:Key Code

Key Sym is a string such as 'Control\_L'. The Key Code is a numeric representation of that key. The left control key, when pressed will return the value 'Control\_L:17'

    import PySimpleGUI as sg
    
    # Recipe for getting keys, one at a time as they are released
    # If want to use the space bar, then be sure and disable the "default focus"
    
    text_elem = sg.Text("", size=(18, 1))
    
    layout = [[sg.Text("Press a key or scroll mouse")],
              [text_elem],
              [sg.Button("OK")]]
    
    window = sg.Window("Keyboard Test", layout,  return_keyboard_events=True, use_default_focus=False)
    
    # ---===--- Loop taking in user input --- #
    while True:
        event, value = window.read()
    
        if event == "OK" or event is None:
            print(event, "exiting")
            break
        text_elem.Update(event)

You want to turn off the default focus so that there no buttons that will be selected should you press the spacebar.

Menus
=====

MenuBar
-------

Beginning in version 3.01 you can add a MenuBar to your window. You specify the menus in much the same way as you do window layouts, with lists. Menu selections are returned as events and as of 3.17, also as in the values dictionary. The value returned will be the entire menu entry, including the key if you specified one.

        menu_def = [['File', ['Open', 'Save', 'Exit',]],
                    ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                    ['Help', 'About...'],]

<span class="image">menu</span>

Note the placement of ',' and of \[\]. It's tricky to get the nested menus correct that implement cascading menus. See how paste has Special and Normal as a list after it. This means that Paste has a cascading menu with items Special and Normal.

Methods
-------

------------------------------------------------------------------------

To add a menu to a Window place the `Menu` or `MenuBar` element into your layout.

    layout = [[sg.Menu(menu_def)]]

It doesn't really matter where you place the Menu Element in your layout as it will always be located at the top of the window.

When the user selects an item, it's returns as the event (along with the menu item's key if one was specified in the menu definition)

ButtonMenus
-----------

Button menus were introduced in version 3.21, having been previously released in PySimpleGUIQt. They work exactly the same and are source code compatible between PySimpleGUI and PySimpleGUIQt. These types of menus take a single menu entry where a Menu Bar takes a list of menu entries.

**Return values for ButtonMenus are different than Menu Bars.**

You will get back the ButtonMenu's KEY as the event. To get the actual item selected, you will look it up in the values dictionary. This can be done with the expression `values[event]`

Right Click Menus
-----------------

Right Click Menus were introduced in version 3.21. Almost every element has a right\_click\_menu parameter and there is a window-level setting for rich click menu that will attach a right click menu to all elements in the window.

The menu definition is the same as the button menu definition, a single menu entry.

    right_click_menu = ['&Right', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]

The first string in a right click menu and a button menu is ***ignored***. It is not used. Normally you would put the string that is shown on the menu bar in that location.

**Return values for right click menus are the same as MenuBars.** The value chosen is returned as the event.

Menu Shortcut keys
------------------

You have used ALT-key in other Windows programs to navigate menus. For example Alt-F+X exits the program. The Alt-F pulls down the File menu. The X selects the entry marked Exit.

The good news is that PySimpleGUI allows you to create the same kind of menus! Your program can play with the big-boys. And, it's trivial to do.

All that's required is for your to add an "&" in front of the letter you want to appear with an underscore. When you hold the Alt key down you will see the menu with underlines that you marked.

One other little bit of polish you can add are separators in your list. To add a line in your list of menu choices, create a menu entry that looks like this: `'---'`

This is an example Menu with underlines and a separator.

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'E&xit'  ]],
                ['&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['&Help', '&About...'],]

And this is the spiffy menu it produced: <span class="image">menus with shortcuts</span>

Disabled Menu Entries
---------------------

If you want one of your menu items to be disabled, then place a '!' in front of the menu entry. To disable the Paste menu entry in the previous examples, the entry would be: `['!&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],]`

If your want to change the disabled menu item flag / character from '!' to something else, change the variable `MENU_DISABLED_CHARACTER`

Keys for Menus
--------------

Beginning in version 3.17 you can add a `key` to your menu entries. The `key` value will be removed prior to be inserted into the menu. When you receive Menu events, the entire menu entry, including the `key` is returned. A key is indicated by adding `::` after a menu entry, followed by the key.

To add the `key` `_MY_KEY_` to the Special menu entry, the code would be:

`['&Edit', ['Paste', ['Special::_MY_KEY_', 'Normal',], 'Undo'],]`

If you want to change the characters that indicate a key follows from '::' to something else, change the variable `MENU_KEY_SEPARATOR`

The Menu Definitions
--------------------

Having read through the Menu section, you may have noticed that the right click menu and the button menu have a format that is a little odd as there is a part of it that is not utilized (the first very string). Perhaps the words "Not Used" should be in the examples.... But, there's a reason to retain words there that make sense.

The reason for this is an architectural one, but it also has a convienence for the user. You can put the individual menu items (button and right click) into a list and you'll have a menu bar definition.

This would work to make a menu bar from a series of these individual menu defintions:

    menu_bar = [right_click_menu_1, right_click_menu_2, button_menu_def ]

And, of course, the direction works the opposite too. You can take a Menu Bar definition and pull out an individual menu item to create a right click or button menu.

Running Multiple Windows
========================

This is where PySimpleGUI continues to be simple, but the problem space just went into the realm of "Complex".

If you wish to run multiple windows in your event loop, then there are 2 methods for doing this.

1.  First window does not remain active while second window is visible
2.  First window remains active while second window is visible

You will find the 2 design matters in 2 demo programs in the Demo Program area of the GitHub (http://www.PySimpleGUI.com)

***Critically important*** When creating a new window you must use a "fresh" layout every time. You cannot reuse a layout from a previous window. As a result you will see the layout for window 2 being defined inside of the larger event loop.

If you have a window layout that you used with a window and you've closed the window, you cannot use the specific elements that were in that window. You must RE-CREATE your `layout` variable every time you create a new window. Read that phrase again.... You must RE-CREATE your `layout` variable every time you create a new window. That means you should have a statemenat that begins with `layout =`. Sorry to be stuck on this point, but so many people seem to have trouble following this simple instruction.

THE GOLDEN RULE OF WINDOW LAYOUTS
---------------------------------

***Thou shalt not re-use a windows's layout.... ever!***

Or more explicitly put....

> If you are calling `Window` then you should define your window layout in the statement just prior to the `Window` call.

Demo Programs For Multiple Windows
----------------------------------

There are several "Demo Programs" that will help you run multiple windows. Please download these programs and FOLLOW the example they have created for you.

Here is ***some*** of the code patterns you'll find when looking through the demo programs.

Multi-Window Design Pattern 1 - both windows active
---------------------------------------------------

    import PySimpleGUI as sg
    
    # Design pattern 2 - First window remains active
    
    layout = [[ sg.Text('Window 1'),],
              [sg.Input(do_not_clear=True)],
              [sg.Text('', key='_OUTPUT_')],
              [sg.Button('Launch 2'), sg.Button('Exit')]]
    
    win1 = sg.Window('Window 1', layout)
    
    win2_active = False
    while True:
        ev1, vals1 = win1.Read(timeout=100)
        win1.FindElement('_OUTPUT_').Update(vals1[0])
        if ev1 is None or ev1 == 'Exit':
            break
    
         if not win2_active and ev1 == 'Launch 2':
            win2_active = True
            layout2 = [[sg.Text('Window 2')],
                       [sg.Button('Exit')]]
    
            win2 = sg.Window('Window 2', layout2)
    
        if win2_active:
            ev2, vals2 = win2.Read(timeout=100)
            if ev2 is None or ev2 == 'Exit':
                win2_active  = False
                win2.Close()

Multi-Window Design Pattern 2 - only 1 active window
----------------------------------------------------

    import PySimpleGUIQt as sg
    
    # Design pattern 1 - First window does not remain active
    
    layout = [[ sg.Text('Window 1'),],
              [sg.Input(do_not_clear=True)],
              [sg.Text('', key='_OUTPUT_')],
              [sg.Button('Launch 2')]]
    
    win1 = sg.Window('Window 1', layout)
    win2_active=False
    while True:
        ev1, vals1 = win1.Read(timeout=100)
        if ev1 is None:
            break
        win1.FindElement('_OUTPUT_').Update(vals1[0])
    
        if ev1 == 'Launch 2'  and not win2_active:
            win2_active = True
            win1.Hide()
            layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
                       [sg.Button('Exit')]]
    
            win2 = sg.Window('Window 2', layout2)
            while True:
                ev2, vals2 = win2.Read()
                if ev2 is None or ev2 == 'Exit':
                    win2.Close()
                    win2_active = False
                    win1.UnHide()
                    break

------------------------------------------------------------------------

