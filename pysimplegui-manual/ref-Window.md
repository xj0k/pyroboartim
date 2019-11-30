

Window
------

    Represents a single Window
    
    Window(title,
        layout=None,
        default_element_size=(45, 1),
        default_button_element_size=(None, None),
        auto_size_text=None,
        auto_size_buttons=None,
        location=(None, None),
        size=(None, None),
        element_padding=None,
        margins=(None, None),
        button_color=None,
        font=None,
        progress_bar_color=(None, None),
        background_color=None,
        border_depth=None,
        auto_close=False,
        auto_close_duration=3,
        icon=None,
        force_toplevel=False,
        alpha_channel=1,
        return_keyboard_events=False,
        use_default_focus=True,
        text_justification=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        resizable=False,
        disable_close=False,
        disable_minimize=False,
        right_click_menu=None,
        transparent_color=None,
        debugger_enabled=True,
        finalize=False,
        element_justification="left",
        ttk_theme=None,
        use_ttk_buttons=None,
        metadata=None)


Parameter Descriptions:

| Name                           | Meaning                                                      |
| ------------------------------ | ------------------------------------------------------------ |
| title                          | (str) The title that will be displayed in the Titlebar and on the Taskbar |
| layout                         | List\[List\[Elements\]\] The layout for the window. Can also be specified in the Layout method |
| default\_element\_size         | Tuple\[int, int\] (width, height) size in characters (wide) and rows (high) for all elements in this window |
| default\_button\_element\_size | Tuple\[int, int\] (width, height) size in characters (wide) and rows (high) for all Button elements in this window |
| auto\_size\_text               | (bool) True if Elements in Window should be sized to exactly fir the length of text |
| auto\_size\_buttons            | (bool) True if Buttons in this Window should be sized to exactly fit the text on this. |
| location                       | Tuple\[int, int\] (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen. |
| size                           | Tuple\[int, int\] (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user |
| element\_padding               | Tuple\[int, int\] or ((int, int),(int,int)) Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom)) |
| margins                        | Tuple\[int, int\] (left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown. |
| button\_color                  | Tuple\[str, str\] (text color, button color) Default button colors for all buttons in the window |
| font                           | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| progress\_bar\_color           | Tuple\[str, str\] (bar color, background color) Sets the default colors for all progress bars in the window |
| background\_color              | (str) color of background                                    |
| border\_depth                  | (int) Default border depth (width) for all elements in the window |
| auto\_close                    | (bool) If True, the window will automatically close itself   |
| auto\_close\_duration          | (int) Number of seconds to wait before closing the window    |
| icon                           | Union\[str, str\] Can be either a filename or Base64 value.  |
| force\_toplevel                | (bool) If True will cause this window to skip the normal use of a hidden master window |
| alpha\_channel                 | (float) Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change. |
| return\_keyboard\_events       | (bool) if True key presses on the keyboard will be returned as Events from Read calls |
| use\_default\_focus            | (bool) If True will use the default focus algorithm to set the focus to the "Correct" element |
| text\_justification            | (str) Union \['left', 'right', 'center'\] Default text justification for all Text Elements in window |
| no\_titlebar                   | (bool) If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar |
| grab\_anywhere                 | (bool) If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems |
| keep\_on\_top                  | (bool) If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm |
| resizable                      | (bool) If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing. |
| disable\_close                 | (bool) If True, the X button in the top right corner of the window will no work. Use with caution and always give a way out toyour users |
| disable\_minimize              | (bool) if True the user won't be able to minimize window. Good for taking over entire screen and staying that way. |
| right\_click\_menu             | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| transparent\_color             | (str) Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window. |
| debugger\_enabled              | (bool) If True then the internal debugger will be enabled    |
| finalize                       | (bool) If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code |
| element\_justification         | (str) All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values |
| ttk\_theme                     | (str) Set the tkinter ttk "theme" of the window. Default = DEFAULT\_TTK\_THEME. Sets all ttk widgets to this theme as their default |
| use\_ttk\_buttons              | (bool) Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons. None = use ttk buttons only if on a Mac |
| metadata                       | (Any) User metadata that can be set to ANYTHING              |

### AddRow

Adds a single row of elements to a window's self.Rows variables. Generally speaking this is NOT how users should be building Window layouts. Users, create a single layout (a list of lists) and pass as a parameter to Window object, or call Window.Layout(layout)

    AddRow(args)


Parameter Descriptions:

| Name   | Meaning          |
| ------ | ---------------- |
| \*args | List\[Elements\] |

### AddRows

Loops through a list of lists of elements and adds each row, list, to the layout. This is NOT the best way to go about creating a window. Sending the entire layout at one time and passing it as a parameter to the Window call is better.

    AddRows(rows)


Parameter Descriptions:

| Name | Meaning                                               |
| ---- | ----------------------------------------------------- |
| rows | List\[List\[Elements\]\] A list of a list of elements |

### AlphaChannel

#### property: AlphaChannel

A property that changes the current alpha channel value (internal value)

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (float) the current alpha channel setting according to self, not read directly from tkinter |

### BringToFront

Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay on top")

    BringToFront()


### Close

Closes window. Users can safely call even if window has been destroyed. Should always call when done with a window so that resources are properly freed up within your thread.

    Close()


### CurrentLocation

Get the current location of the window's top left corner

`CurrentLocation()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Tuple\[(int), (int)\] The x and y location in tuple form (x,y) |

### Disable

Disables window from taking any input from the user

    Disable()


### DisableDebugger

Disable the internal debugger. By default the debugger is ENABLED

    DisableDebugger()


### Disappear

Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha channel to 0. NOTE that on some platforms alpha is not supported. The window will remain showing on these platforms. The Raspberry Pi for example does not have an alpha setting

    Disappear()


### Elem

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    Elem(key, silent_on_error=False)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### Element

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    Element(key, silent_on_error=False)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### Enable

Re-enables window to take user input after having it be Disabled previously

    Enable()


### EnableDebugger

Enables the internal debugger. By default, the debugger IS enabled

    EnableDebugger()


### Fill

Fill in elements that are input fields with data based on a 'values dictionary'

    Fill(values_dict)


Parameter Descriptions:

| Name         | Meaning                                                    |
| ------------ | ---------------------------------------------------------- |
| values\_dict | (Dict\[Any:Any\]) {Element key : value} pairs              |
|              |                                                            |
| **return**   | (Window) returns self so can be chained with other methods |

### Finalize

Use this method to cause your layout to built into a real tkinter window. In reality this method is like Read(timeout=0). It doesn't block and uses your layout to create tkinter widgets to represent the elements. Lots of action!

`Finalize()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (Window) Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!) |

### Find

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    Find(key, silent_on_error=False)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### FindElement

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    FindElement(key, silent_on_error=False)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### FindElementWithFocus

Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

`FindElementWithFocus()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Element, None\] An Element if one has been found with focus or None if no element found |

### GetScreenDimensions

Get the screen dimensions. NOTE - you must have a window already open for this to work (blame tkinter not me)

`GetScreenDimensions()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Tuple\[None, None\], Tuple\[width, height\]\] Tuple containing width and height of screen in pixels |

### GrabAnyWhereOff

Turns off Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been Finalized or Read.

    GrabAnyWhereOff()


### GrabAnyWhereOn

Turns on Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been Finalized or Read.

    GrabAnyWhereOn()


### Hide

Hides the window from the screen and the task bar

    Hide()


### Layout

Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as a parameter to Window object. The parameter method is the currently preferred method. This call to Layout has been removed from examples contained in documents and in the Demo Programs. Trying to remove this call from history and replace with sending as a parameter to Window.

    Layout(rows)


Parameter Descriptions:

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| rows       | List\[List\[Elements\]\] Your entire layout      |
|            |                                                  |
| **return** | (Window} self so that you can chain method calls |

### LoadFromDisk

Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

    LoadFromDisk(filename)


Parameter Descriptions:

| Name     | Meaning                       |
| -------- | ----------------------------- |
| filename | (str) Pickle Filename to load |

### Maximize

Maximize the window. This is done differently on a windows system versus a linux or mac one. For non-Windows the root attribute '-fullscreen' is set to True. For Windows the "root" state is changed to "zoomed" The reason for the difference is the title bar is removed in some cases when using fullscreen option

    Maximize()


### Minimize

Minimize this window to the task bar

    Minimize()


### Move

Move the upper left corner of this window to the x,y coordinates provided

    Move(x, y)


Parameter Descriptions:

| Name | Meaning                      |
| ---- | ---------------------------- |
| x    | (int) x coordinate in pixels |
| y    | (int) y coordinate in pixels |

### Normal

Restore a window to a non-maximized state. Does different things depending on platform. See Maximize for more.

    Normal()


### Read

THE biggest deal method in the Window class! This is how you get all of your data from your Window. Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout\_key if no other GUI events happen first.

    Read(timeout=None, timeout_key="__TIMEOUT__")


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>timeout</td><td>(int) Milliseconds to wait until the Read will return IF no other GUI events happen first</td></tr><tr class="even"><td>timeout_key</td><td>(Any) The value that will be returned from the call if the timer expired</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Tuple[(Any), Union[Dict[Any:Any]], List[Any], None] (event, values)<br />
(event or timeout_key or None, Dictionary of values or List of values from all elements in the Window)</td></tr></tbody></table>

### Reappear

Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

    Reappear()


### Refresh

Refreshes the window by calling tkroot.update(). Can sometimes get away with a refresh instead of a Read. Use this call when you want something to appear in your Window immediately (as soon as this function is called). Without this call your changes to a Window will not be visible to the user until the next Read call

`Refresh()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (Window) `self` so that method calls can be easily "chained" |

### SaveToDisk

Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a call to Read. It takes these results and saves them to disk using pickle

    SaveToDisk(filename)


Parameter Descriptions:

| Name     | Meaning                                              |
| -------- | ---------------------------------------------------- |
| filename | (str) Filename to save the values to in pickled form |

### SendToBack

Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

    SendToBack()


### SetAlpha

Sets the Alpha Channel for a window. Values are between 0 and 1 where 0 is completely transparent

    SetAlpha(alpha)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| alpha | (float) 0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through) |

### SetIcon

Sets the icon that is shown on the title bar and on the task bar. Can pass in: \* a filename which must be a .ICO icon file for windows \* a bytes object \* a BASE64 encoded file held in a variable

    SetIcon(icon=None, pngbase64=None)


Parameter Descriptions:

| Name      | Meaning                              |
| --------- | ------------------------------------ |
| icon      | (str) Filename or bytes object       |
| pngbase64 | (str) Base64 encoded GIF or PNG file |

### SetTransparentColor

Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

    SetTransparentColor(color)


Parameter Descriptions:

| Name  | Meaning                                               |
| ----- | ----------------------------------------------------- |
| color | (str) Color string that defines the transparent color |

### Size

#### property: Size

Return the current size of the window in pixels

| Name       | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| **return** | Tuple\[(int), (int)\] the (width, height) of the window |

### UnHide

Used to bring back a window that was previously hidden using the Hide method

    UnHide()


### VisibilityChanged

This is a completely dummy method that does nothing. It is here so that PySimpleGUIQt programs can make this call and then have that same source run on plain PySimpleGUI.

`VisibilityChanged()`

| Name       | Meaning |
| ---------- | ------- |
| **return** |         |

### add\_row

Adds a single row of elements to a window's self.Rows variables. Generally speaking this is NOT how users should be building Window layouts. Users, create a single layout (a list of lists) and pass as a parameter to Window object, or call Window.Layout(layout)

    add_row(args)


Parameter Descriptions:

| Name   | Meaning          |
| ------ | ---------------- |
| \*args | List\[Elements\] |

### add\_rows

Loops through a list of lists of elements and adds each row, list, to the layout. This is NOT the best way to go about creating a window. Sending the entire layout at one time and passing it as a parameter to the Window call is better.

    add_rows(rows)


Parameter Descriptions:

| Name | Meaning                                               |
| ---- | ----------------------------------------------------- |
| rows | List\[List\[Elements\]\] A list of a list of elements |

### alpha\_channel

#### property: alpha\_channel

A property that changes the current alpha channel value (internal value)

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (float) the current alpha channel setting according to self, not read directly from tkinter |

### bring\_to\_front

Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay on top")

    bring_to_front()


### close

Closes window. Users can safely call even if window has been destroyed. Should always call when done with a window so that resources are properly freed up within your thread.

    close()


### current\_location

Get the current location of the window's top left corner

`current_location()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Tuple\[(int), (int)\] The x and y location in tuple form (x,y) |

### disable

Disables window from taking any input from the user

    disable()


### disable\_debugger

Disable the internal debugger. By default the debugger is ENABLED

    disable_debugger()


### disappear

Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha channel to 0. NOTE that on some platforms alpha is not supported. The window will remain showing on these platforms. The Raspberry Pi for example does not have an alpha setting

    disappear()


### elem

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    elem(key, silent_on_error=False)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### element

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    element(key, silent_on_error=False)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### enable

Re-enables window to take user input after having it be Disabled previously

    enable()


### enable\_debugger

Enables the internal debugger. By default, the debugger IS enabled

    enable_debugger()


### fill

Fill in elements that are input fields with data based on a 'values dictionary'

    fill(values_dict)


Parameter Descriptions:

| Name         | Meaning                                                    |
| ------------ | ---------------------------------------------------------- |
| values\_dict | (Dict\[Any:Any\]) {Element key : value} pairs              |
|              |                                                            |
| **return**   | (Window) returns self so can be chained with other methods |

### finalize

Use this method to cause your layout to built into a real tkinter window. In reality this method is like Read(timeout=0). It doesn't block and uses your layout to create tkinter widgets to represent the elements. Lots of action!

`finalize()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (Window) Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!) |

### find

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    find(key, silent_on_error=False)

Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### find\_element

Find element object associated with the provided key. THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement: element = window\[key\]

You can drop the entire "FindElement" function name and use \[ \] instead.

Typically used in combination with a call to element's Update method (or any other element method!): window\[key\].Update(new\_value)

Versus the "old way" window.FindElement(key).Update(new\_value)

This call can be abbreviated to any of these: FindElement == Element == Find Rememeber that this call will return None if no match is found which may cause your code to crash if not checked for.

    find_element(key, silent_on_error=False)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>key</td><td>(Any) Used with window.FindElement and with return values to uniquely identify this element</td></tr><tr class="even"><td>silent_on_error</td><td>(bool) If True do not display popup nor print warning of key errors</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[Element, Error Element, None] Return value can be:<br />
* the Element that matches the supplied key if found<br />
* an Error Element if silent_on_error is False<br />
* None if silent_on_error True</td></tr></tbody></table>

### find\_element\_with\_focus

Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

`find_element_with_focus()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Element, None\] An Element if one has been found with focus or None if no element found |

### get\_screen\_dimensions

Get the screen dimensions. NOTE - you must have a window already open for this to work (blame tkinter not me)

`get_screen_dimensions()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Tuple\[None, None\], Tuple\[width, height\]\] Tuple containing width and height of screen in pixels |

### get\_screen\_size

Returns the size of the "screen" as determined by tkinter. This can vary depending on your operating system and the number of monitors installed on your system. For Windows, the primary monitor's size is returns. On some multi-monitored Linux systems, the monitors are combined and the total size is reported as if one screen.

    get_screen_size() -> Tuple[int, int] - Size of the screen in pixels as determined by tkinter


### grab\_any\_where\_off

Turns off Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been Finalized or Read.

    grab_any_where_off()


### grab\_any\_where\_on

Turns on Grab Anywhere functionality AFTER a window has been created. Don't try on a window that's not yet been Finalized or Read.

    grab_any_where_on()


### hide

Hides the window from the screen and the task bar

    hide()


### layout

Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as a parameter to Window object. The parameter method is the currently preferred method. This call to Layout has been removed from examples contained in documents and in the Demo Programs. Trying to remove this call from history and replace with sending as a parameter to Window.

    layout(rows)


Parameter Descriptions:

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| rows       | List\[List\[Elements\]\] Your entire layout      |
|            |                                                  |
| **return** | (Window} self so that you can chain method calls |

### load\_from\_disk

Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

    load_from_disk(filename)


Parameter Descriptions:

| Name     | Meaning                       |
| -------- | ----------------------------- |
| filename | (str) Pickle Filename to load |

### maximize

Maximize the window. This is done differently on a windows system versus a linux or mac one. For non-Windows the root attribute '-fullscreen' is set to True. For Windows the "root" state is changed to "zoomed" The reason for the difference is the title bar is removed in some cases when using fullscreen option

    maximize()


### minimize

Minimize this window to the task bar

    minimize()


### move

Move the upper left corner of this window to the x,y coordinates provided

    move(x, y)


Parameter Descriptions:

| Name | Meaning                      |
| ---- | ---------------------------- |
| x    | (int) x coordinate in pixels |
| y    | (int) y coordinate in pixels |

### normal

Restore a window to a non-maximized state. Does different things depending on platform. See Maximize for more.

    normal()


### read

THE biggest deal method in the Window class! This is how you get all of your data from your Window. Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout\_key if no other GUI events happen first.

    read(timeout=None, timeout_key="__TIMEOUT__")


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>timeout</td><td>(int) Milliseconds to wait until the Read will return IF no other GUI events happen first</td></tr><tr class="even"><td>timeout_key</td><td>(Any) The value that will be returned from the call if the timer expired</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Tuple[(Any), Union[Dict[Any:Any]], List[Any], None] (event, values)<br />
(event or timeout_key or None, Dictionary of values or List of values from all elements in the Window)</td></tr></tbody></table>

### reappear

Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

    reappear()


### refresh

Refreshes the window by calling tkroot.update(). Can sometimes get away with a refresh instead of a Read. Use this call when you want something to appear in your Window immediately (as soon as this function is called). Without this call your changes to a Window will not be visible to the user until the next Read call

`refresh()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (Window) `self` so that method calls can be easily "chained" |

### save\_to\_disk

Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a call to Read. It takes these results and saves them to disk using pickle

    save_to_disk(filename)


Parameter Descriptions:

| Name     | Meaning                                              |
| -------- | ---------------------------------------------------- |
| filename | (str) Filename to save the values to in pickled form |

### send\_to\_back

Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

    send_to_back()


### set\_alpha

Sets the Alpha Channel for a window. Values are between 0 and 1 where 0 is completely transparent

    set_alpha(alpha)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| alpha | (float) 0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through) |

### set\_icon

Sets the icon that is shown on the title bar and on the task bar. Can pass in: \* a filename which must be a .ICO icon file for windows \* a bytes object \* a BASE64 encoded file held in a variable

    set_icon(icon=None, pngbase64=None)


Parameter Descriptions:

| Name      | Meaning                              |
| --------- | ------------------------------------ |
| icon      | (str) Filename or bytes object       |
| pngbase64 | (str) Base64 encoded GIF or PNG file |

### set\_transparent\_color

Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

    set_transparent_color(color)


Parameter Descriptions:

| Name  | Meaning                                               |
| ----- | ----------------------------------------------------- |
| color | (str) Color string that defines the transparent color |

### size

#### property: size

Return the current size of the window in pixels

| Name       | Meaning                                                 |
| ---------- | ------------------------------------------------------- |
| **return** | Tuple\[(int), (int)\] the (width, height) of the window |

### un\_hide

Used to bring back a window that was previously hidden using the Hide method

    un_hide()


### visibility\_changed

This is a completely dummy method that does nothing. It is here so that PySimpleGUIQt programs can make this call and then have that same source run on plain PySimpleGUI.

`visibility_changed()`

| Name       | Meaning |
| ---------- | ------- |
| **return** |         |

    CButton(button_text,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        font=None,
        bind_return_key=False,
        disabled=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button                                           |
| image\_filename    | image filename if there is a button image                    |
| image\_data        | in-RAM image to be displayed on button                       |
| image\_size        | size of button image in pixels                               |
| image\_subsample   | amount to reduce the size of the image                       |
| border\_width      | width of border around element                               |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| disabled           | set disable state for element (Default = False)              |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    CalendarButton(button_text,
        target=(None, None),
        close_when_date_chosen=True,
        default_date_m_d_y=(None, None, None),
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        tooltip=None,
        border_width=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        locale=None,
        format=None,
        metadata=None)


Parameter Descriptions:

| Name                      | Meaning                                                      |
| ------------------------- | ------------------------------------------------------------ |
| button\_text              | text in the button                                           |
| target                    |                                                              |
| close\_when\_date\_chosen | (Default = True)                                             |
| default\_date\_m\_d\_y    | (Default = (None))                                           |
| None                      |                                                              |
| image\_filename           | image filename if there is a button image                    |
| image\_data               | in-RAM image to be displayed on button                       |
| image\_size               | (Default = (None))                                           |
| image\_subsample          | amount to reduce the size of the image                       |
| tooltip                   | (str) text, that will appear when mouse hovers over the element |
| border\_width             | width of border around element                               |
| size                      | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button        | True if button size is determined by button text             |
| button\_color             | button color (foreground, background)                        |
| disabled                  | set disable state for element (Default = False)              |
| font                      | specifies the font family, size, etc                         |
| bind\_return\_key         | (Default = False)                                            |
| focus                     | if focus should be set to this                               |
| pad                       | Amount of padding to put around element                      |
| key                       | Used with window.FindElement and with return values to uniquely identify this element |
| locale                    |                                                              |
| format                    |                                                              |
|                           |                                                              |
| **return**                | (Button)                                                     |

    Cancel(button_text="Cancel",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        tooltip=None,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Cancel')                |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |

Change the "color scheme" of all future PySimpleGUI Windows. The scheme are string names that specify a group of colors. Background colors, text colors, button colors. There are 13 different color settings that are changed at one time using a single call to ChangeLookAndFeel The look and feel table itself has these indexes into the dictionary LOOK\_AND\_FEEL\_TABLE. The original list was (prior to a major rework and renaming)... these names still work... SystemDefault SystemDefaultForReal Material1 Material2 Reddit Topanga GreenTan Dark LightGreen Dark2 Black Tan TanBlue DarkTanBlue DarkAmber DarkBlue Reds Green BluePurple Purple BlueMono GreenMono BrownBlue BrightColors NeutralBlue Kayak SandyBeach TealMono

In Nov 2019 a new Theme Formula was devised to make choosing a theme easier: The "Formula" is: \["Dark" or "Light"\] Color Number Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black The number will vary for each pair. There are more DarkGrey entries than there are LightYellow for example. Default = The default settings (only button color is different than system default) Default1 = The full system default including the button (everything's gray... how sad... don't be all gray... please....)

    ChangeLookAndFeel(index, force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| index | (str) the name of the index into the Look and Feel table     |
| force | (bool) if True allows Macs to use the look and feel feature. Otherwise Macs are blocked due to problems with button colors |

    CloseButton(button_text,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        font=None,
        bind_return_key=False,
        disabled=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button                                           |
| image\_filename    | image filename if there is a button image                    |
| image\_data        | in-RAM image to be displayed on button                       |
| image\_size        | size of button image in pixels                               |
| image\_subsample   | amount to reduce the size of the image                       |
| border\_width      | width of border around element                               |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| disabled           | set disable state for element (Default = False)              |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    ColorChooserButton(button_text,
        target=(None, None),
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        tooltip=None,
        border_width=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button                                           |
| target             |                                                              |
| image\_filename    | image filename if there is a button image                    |
| image\_data        | in-RAM image to be displayed on button                       |
| image\_size        | (Default = (None))                                           |
| image\_subsample   | amount to reduce the size of the image                       |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| border\_width      | width of border around element                               |
| size               | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    Debug(button_text="",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        font=None,
        tooltip=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = '')                      |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| font               | specifies the font family, size, etc                         |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    DummyButton(button_text,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        font=None,
        disabled=False,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button                                           |
| image\_filename    | image filename if there is a button image                    |
| image\_data        | in-RAM image to be displayed on button                       |
| image\_size        | size of button image in pixels                               |
| image\_subsample   | amount to reduce the size of the image                       |
| border\_width      | width of border around element                               |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| font               | specifies the font family, size, etc                         |
| disabled           | set disable state for element (Default = False)              |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    EasyPrint(args,
        size=(None, None),
        end=None,
        sep=None,
        location=(None, None),
        font=None,
        no_titlebar=False,
        no_button=False,
        grab_anywhere=False,
        keep_on_top=False,
        do_not_reroute_stdout=True)


Parameter Descriptions:

| Name                     | Meaning                                                      |
| ------------------------ | ------------------------------------------------------------ |
| \*args                   |                                                              |
| size                     | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| end                      |                                                              |
| sep                      |                                                              |
| location                 | Location on screen to display                                |
| font                     | specifies the font family, size, etc                         |
| no\_titlebar             | (Default = False)                                            |
| no\_button               | (Default = False)                                            |
| grab\_anywhere           | If True can grab anywhere to move the window (Default = False) |
| do\_not\_reroute\_stdout | (Default = True)                                             |

    EasyPrintClose()
    
    Exit(button_text="Exit",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        tooltip=None,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Exit')                  |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |

    FileBrowse(button_text="Browse",
        target=(555666777, -1),
        file_types=(('ALL Files', '*.*'),),
        initial_folder=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        change_submits=False,
        enable_events=False,
        font=None,
        disabled=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Browse')                |
| target             | key or (row,col) target for the button (Default value = (ThisRow, -1)) |
| file\_types        | (Default value = (("ALL Files", "*.*")))                     |
| initial\_folder    | starting path for folders and files                          |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| change\_submits    | If True, pressing Enter key submits window (Default = False) |
| enable\_events     | Turns on the element specific events.(Default = False)       |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| disabled           | set disable state for element (Default = False)              |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    FileSaveAs(button_text="Save As...",
        target=(555666777, -1),
        file_types=(('ALL Files', '*.*'),),
        initial_folder=None,
        disabled=False,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        change_submits=False,
        enable_events=False,
        font=None,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Save As...')            |
| target             | key or (row,col) target for the button (Default value = (ThisRow, -1)) |
| file\_types        | (Default value = (("ALL Files", "*.*")))                     |
| initial\_folder    | starting path for folders and files                          |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| change\_submits    | If True, pressing Enter key submits window (Default = False) |
| enable\_events     | Turns on the element specific events.(Default = False)       |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    FilesBrowse(button_text="Browse",
        target=(555666777, -1),
        file_types=(('ALL Files', '*.*'),),
        disabled=False,
        initial_folder=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        change_submits=False,
        enable_events=False,
        font=None,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Browse')                |
| target             | key or (row,col) target for the button (Default value = (ThisRow, -1)) |
| file\_types        | (Default value = (("ALL Files", "*.*")))                     |
| disabled           | set disable state for element (Default = False)              |
| initial\_folder    | starting path for folders and files                          |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| change\_submits    | If True, pressing Enter key submits window (Default = False) |
| enable\_events     | Turns on the element specific events.(Default = False)       |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

Fills a window with values provided in a values dictionary { element\_key : new\_value }

    FillFormWithValues(window, values_dict)

Parameter Descriptions:

| Name         | Meaning                                                      |
| ------------ | ------------------------------------------------------------ |
| window       | (Window) The window object to fill                           |
| values\_dict | (Dict\[Any:Any\]) A dictionary with element keys as key and value is values parm for Update call |

    FolderBrowse(button_text="Browse",
        target=(555666777, -1),
        initial_folder=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        change_submits=False,
        enable_events=False,
        font=None,
        pad=None,
        key=None,
        metadata=None)

Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Browse')                |
| target             | key or (row,col) target for the button (Default value = (ThisRow, -1)) |
| initial\_folder    | starting path for folders and files                          |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| change\_submits    | If True, pressing Enter key submits window (Default = False) |
| enable\_events     | Turns on the element specific events.(Default = False)       |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    Help(button_text="Help",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        font=None,
        tooltip=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Help')                  |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| font               | specifies the font family, size, etc                         |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

Get a list of the valid values to pass into your call to change\_look\_and\_feel

    ListOfLookAndFeelValues() -> List[str] - list of valid string values
    
    No(button_text="No",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        tooltip=None,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'No')                    |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |

    OK(button_text="OK",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        bind_return_key=True,
        tooltip=None,
        font=None,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'OK')                    |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| bind\_return\_key  | (Default = True)                                             |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables in human form

    ObjToString(obj, extra="    ")


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| obj   | (Any) The object to display                                  |
| extra | (Default value = ' ') returns (str) Formatted output of the object's values |

Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables in human form Returns only the top-most object's variables instead of drilling down to dispolay more

    ObjToStringSingleObj(obj)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| obj  | (Any) The object to display returns (str) Formatted output of the object's values |

    Ok(button_text="Ok",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        bind_return_key=True,
        tooltip=None,
        font=None,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Ok')                    |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| bind\_return\_key  | (Default = True)                                             |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    OneLineProgressMeter(title,
        current_value,
        max_value,
        key,
        args,
        orientation="v",
        bar_color=(None, None),
        button_color=None,
        size=(20, 20),
        border_width=None,
        grab_anywhere=False)


Parameter Descriptions:

| Name           | Meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| title          | text to display                                              |
| current\_value | current progressbar value                                    |
| max\_value     | max value of progressbar                                     |
| key            | Used with window.FindElement and with return values to uniquely identify this element |
| \*args         | stuff to output.                                             |
| orientation    | 'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical')(Default value = 'v') |
| bar\_color     |                                                              |
| button\_color  | button color (foreground, background)                        |
| size           | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT\_PROGRESS\_BAR\_SIZE) |
| border\_width  | width of border around element                               |
| grab\_anywhere | If True can grab anywhere to move the window (Default = False) |

    OneLineProgressMeterCancel(key)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| key  | Used with window.FindElement and with return values to uniquely identify this element |

    Open(button_text="Open",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        bind_return_key=True,
        tooltip=None,
        font=None,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Open')                  |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| bind\_return\_key  | (Default = True)                                             |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |

Show Popup box that doesn't block and closes itself

    PopupQuick(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=True,
        auto_close_duration=2,
        non_blocking=True,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)                         |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = True)                                             |
| auto\_close\_duration | (Default value = 2)                                          |
| non\_blocking         | (Default = True)                                             |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Show Popup window with no titlebar, doesn't block, and auto closes itself.

    PopupQuickMessage(args,
        title=None,
        button_type=5,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=True,
        auto_close_duration=2,
        non_blocking=True,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=True,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_NO\_BUTTONS)                |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = True)                                             |
| auto\_close\_duration | (Default value = 2)                                          |
| non\_blocking         | (Default = True)                                             |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = True)                                             |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you want, just like a print statement.

    PopupScrolled(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        yes_no=False,
        auto_close=False,
        auto_close_duration=None,
        size=(None, None),
        location=(None, None),
        non_blocking=False,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        font=None)

Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                | (Any) Variable number of items to display                    |
| title                 | (str) Title to display in the window.                        |
| button\_color         | Tuple\[str, str\] button color (foreground, background)      |
| yes\_no               | (bool) If True, displays Yes and No buttons instead of Ok    |
| auto\_close           | (bool) if True window will close itself                      |
| auto\_close\_duration | Union\[int, float\] Older versions only accept int. Time in seconds until window will close |
| size                  | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| location              | Tuple\[int, int\] Location on the screen to place the upper left corner of the window |
| non\_blocking         | (bool) if True the call will immediately return rather than waiting on user input |
|                       |                                                              |
| **return**            | Union\[str, None, TIMEOUT\_KEY\] Returns text of the button that was pressed. None will be returned if user closed window with X |

Popup that closes itself after some time period

    PopupTimed(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=True,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)                         |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = True)                                             |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Display Popup with Yes and No buttons

    PopupYesNo(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              | Location on screen to display                                |
|                       |                                                              |
| **return**            | Union\["Yes", "No", None\]                                   |

    Print(args,
        size=(None, None),
        end=None,
        sep=None,
        location=(None, None),
        font=None,
        no_titlebar=False,
        no_button=False,
        grab_anywhere=False,
        keep_on_top=False,
        do_not_reroute_stdout=True)


Parameter Descriptions:

| Name                     | Meaning                                                      |
| ------------------------ | ------------------------------------------------------------ |
| \*args                   |                                                              |
| size                     | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| end                      |                                                              |
| sep                      |                                                              |
| location                 | Location on screen to display                                |
| font                     | specifies the font family, size, etc                         |
| no\_titlebar             | (Default = False)                                            |
| no\_button               | (Default = False)                                            |
| grab\_anywhere           | If True can grab anywhere to move the window (Default = False) |
| do\_not\_reroute\_stdout | (Default = True)                                             |

    PrintClose()
    
    Quit(button_text="Quit",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        tooltip=None,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Quit')                  |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    RButton(button_text,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        font=None,
        bind_return_key=False,
        disabled=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button                                           |
| image\_filename    | image filename if there is a button image                    |
| image\_data        | in-RAM image to be displayed on button                       |
| image\_size        | size of button image in pixels                               |
| image\_subsample   | amount to reduce the size of the image                       |
| border\_width      | width of border around element                               |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| disabled           | set disable state for element (Default = False)              |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |

    ReadButton(button_text,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        font=None,
        bind_return_key=False,
        disabled=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button                                           |
| image\_filename    | image filename if there is a button image                    |
| image\_data        | in-RAM image to be displayed on button                       |
| image\_size        | size of button image in pixels                               |
| image\_subsample   | amount to reduce the size of the image                       |
| border\_width      | width of border around element                               |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| disabled           | set disable state for element (Default = False)              |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |

    RealtimeButton(button_text,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        font=None,
        disabled=False,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button                                           |
| image\_filename    | image filename if there is a button image                    |
| image\_data        | in-RAM image to be displayed on button                       |
| image\_size        | size of button image in pixels                               |
| image\_subsample   | amount to reduce the size of the image                       |
| border\_width      | width of border around element                               |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high (Default = (None))      |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| font               | specifies the font family, size, etc                         |
| disabled           | set disable state for element (Default = False)              |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |

    Save(button_text="Save",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        bind_return_key=True,
        disabled=False,
        tooltip=None,
        font=None,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Save')                  |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| bind\_return\_key  | (Default = True)                                             |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

    SaveAs(button_text="Save As...",
        target=(555666777, -1),
        file_types=(('ALL Files', '*.*'),),
        initial_folder=None,
        disabled=False,
        tooltip=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        change_submits=False,
        enable_events=False,
        font=None,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Save As...')            |
| target             | key or (row,col) target for the button (Default value = (ThisRow, -1)) |
| file\_types        | (Default value = (("ALL Files", "*.*")))                     |
| initial\_folder    | starting path for folders and files                          |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| change\_submits    | If True, pressing Enter key submits window (Default = False) |
| enable\_events     | Turns on the element specific events.(Default = False)       |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you want, just like a print statement.

    ScrolledTextBox(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        yes_no=False,
        auto_close=False,
        auto_close_duration=None,
        size=(None, None),
        location=(None, None),
        non_blocking=False,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        font=None)


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                | (Any) Variable number of items to display                    |
| title                 | (str) Title to display in the window.                        |
| button\_color         | Tuple\[str, str\] button color (foreground, background)      |
| yes\_no               | (bool) If True, displays Yes and No buttons instead of Ok    |
| auto\_close           | (bool) if True window will close itself                      |
| auto\_close\_duration | Union\[int, float\] Older versions only accept int. Time in seconds until window will close |
| size                  | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| location              | Tuple\[int, int\] Location on the screen to place the upper left corner of the window |
| non\_blocking         | (bool) if True the call will immediately return rather than waiting on user input |
|                       |                                                              |
| **return**            | Union\[str, None, TIMEOUT\_KEY\] Returns text of the button that was pressed. None will be returned if user closed window with X |

Sets the icon which will be used any time a window is created if an icon is not provided when the window is created.

    SetGlobalIcon(icon)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| icon | Union\[bytes, str\] Either a Base64 byte string or a filename |

    SetOptions(icon=None,
        button_color=None,
        element_size=(None, None),
        button_element_size=(None, None),
        margins=(None, None),
        element_padding=(None, None),
        auto_size_text=None,
        auto_size_buttons=None,
        font=None,
        border_width=None,
        slider_border_width=None,
        slider_relief=None,
        slider_orientation=None,
        autoclose_time=None,
        message_box_line_width=None,
        progress_meter_border_depth=None,
        progress_meter_style=None,
        progress_meter_relief=None,
        progress_meter_color=None,
        progress_meter_size=None,
        text_justification=None,
        background_color=None,
        element_background_color=None,
        text_element_background_color=None,
        input_elements_background_color=None,
        input_text_color=None,
        scrollbar_color=None,
        text_color=None,
        element_text_color=None,
        debug_win_size=(None, None),
        window_location=(None, None),
        error_button_color=(None, None),
        tooltip_time=None,
        use_ttk_buttons=None,
        ttk_theme=None)


Parameter Descriptions:

| Name                               | Meaning                                                      |
| ---------------------------------- | ------------------------------------------------------------ |
| icon                               | filename of icon used for taskbar and title bar              |
| button\_color                      | button color (foreground, background)                        |
| element\_size                      | Tuple\[int, int\] element size (width, height) in characters |
| button\_element\_size              | Tuple\[int, int\]                                            |
| margins                            | tkinter margins around outsize (Default = (None))            |
| element\_padding                   | (Default = (None))                                           |
| auto\_size\_text                   | True if size should fit the text length                      |
| auto\_size\_buttons                |                                                              |
| font                               | specifies the font family, size, etc                         |
| border\_width                      | width of border around element                               |
| slider\_border\_width              |                                                              |
| slider\_relief                     |                                                              |
| slider\_orientation                |                                                              |
| autoclose\_time                    |                                                              |
| message\_box\_line\_width          |                                                              |
| progress\_meter\_border\_depth     |                                                              |
| progress\_meter\_style             |                                                              |
| progress\_meter\_relief            |                                                              |
| progress\_meter\_color             |                                                              |
| progress\_meter\_size              | Tuple\[int, int\]                                            |
| text\_justification                |                                                              |
| background\_color                  | color of background                                          |
| element\_background\_color         |                                                              |
| text\_element\_background\_color   |                                                              |
| input\_elements\_background\_color |                                                              |
| input\_text\_color                 |                                                              |
| scrollbar\_color                   |                                                              |
| text\_color                        | color of the text                                            |
| element\_text\_color               |                                                              |
| debug\_win\_size                   | Tuple\[int, int\] (Default = (None))                         |
| window\_location                   | (Default = (None))                                           |
| error\_button\_color               | (Default = (None))                                           |
| tooltip\_time                      | time in milliseconds to wait before showing a tooltip. Default is 400ms |
| use\_ttk\_buttons                  | (bool) if True will cause all buttons to be ttk buttons      |
| ttk\_theme                         | (str) Theme to use with ttk widgets. Choices (on Windows) include - 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative' |

    Submit(button_text="Submit",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        bind_return_key=True,
        tooltip=None,
        font=None,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Submit')                |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| bind\_return\_key  | (Default = True)                                             |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

Time your code easily.... start the timer.

    TimerStart()

Time your code easily.... stop the timer and print the number of ms since the timer start

    TimerStop()
    
    Yes(button_text="Yes",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        tooltip=None,
        font=None,
        bind_return_key=True,
        focus=False,
        pad=None,
        key=None,
        metadata=None)

Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Yes')                   |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = True)                                             |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

Change the "color scheme" of all future PySimpleGUI Windows. The scheme are string names that specify a group of colors. Background colors, text colors, button colors. There are 13 different color settings that are changed at one time using a single call to ChangeLookAndFeel The look and feel table itself has these indexes into the dictionary LOOK\_AND\_FEEL\_TABLE. The original list was (prior to a major rework and renaming)... these names still work... SystemDefault SystemDefaultForReal Material1 Material2 Reddit Topanga GreenTan Dark LightGreen Dark2 Black Tan TanBlue DarkTanBlue DarkAmber DarkBlue Reds Green BluePurple Purple BlueMono GreenMono BrownBlue BrightColors NeutralBlue Kayak SandyBeach TealMono

In Nov 2019 a new Theme Formula was devised to make choosing a theme easier: The "Formula" is: \["Dark" or "Light"\] Color Number Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black The number will vary for each pair. There are more DarkGrey entries than there are LightYellow for example. Default = The default settings (only button color is different than system default) Default1 = The full system default including the button (everything's gray... how sad... don't be all gray... please....)

    change_look_and_feel(index, force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| index | (str) the name of the index into the Look and Feel table     |
| force | (bool) if True allows Macs to use the look and feel feature. Otherwise Macs are blocked due to problems with button colors |

    easy_print(args,
        size=(None, None),
        end=None,
        sep=None,
        location=(None, None),
        font=None,
        no_titlebar=False,
        no_button=False,
        grab_anywhere=False,
        keep_on_top=False,
        do_not_reroute_stdout=True)

Parameter Descriptions:

| Name                     | Meaning                                                      |
| ------------------------ | ------------------------------------------------------------ |
| \*args                   |                                                              |
| size                     | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| end                      |                                                              |
| sep                      |                                                              |
| location                 | Location on screen to display                                |
| font                     | specifies the font family, size, etc                         |
| no\_titlebar             | (Default = False)                                            |
| no\_button               | (Default = False)                                            |
| grab\_anywhere           | If True can grab anywhere to move the window (Default = False) |
| do\_not\_reroute\_stdout | (Default = True)                                             |

    easy_print_close()
    
    eprint(args,
        size=(None, None),
        end=None,
        sep=None,
        location=(None, None),
        font=None,
        no_titlebar=False,
        no_button=False,
        grab_anywhere=False,
        keep_on_top=False,
        do_not_reroute_stdout=True)

Parameter Descriptions:

| Name                     | Meaning                                                      |
| ------------------------ | ------------------------------------------------------------ |
| \*args                   |                                                              |
| size                     | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| end                      |                                                              |
| sep                      |                                                              |
| location                 | Location on screen to display                                |
| font                     | specifies the font family, size, etc                         |
| no\_titlebar             | (Default = False)                                            |
| no\_button               | (Default = False)                                            |
| grab\_anywhere           | If True can grab anywhere to move the window (Default = False) |
| do\_not\_reroute\_stdout | (Default = True)                                             |

Fills a window with values provided in a values dictionary { element\_key : new\_value }

    fill_form_with_values(window, values_dict)


Parameter Descriptions:

| Name         | Meaning                                                      |
| ------------ | ------------------------------------------------------------ |
| window       | (Window) The window object to fill                           |
| values\_dict | (Dict\[Any:Any\]) A dictionary with element keys as key and value is values parm for Update call |

Get a list of the valid values to pass into your call to change\_look\_and\_feel

    list_of_look_and_feel_values() -> List[str] - list of valid string values


The PySimpleGUI "Test Harness". This is meant to be a super-quick test of the Elements.

    main()


Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables in human form

    obj_to_string(obj, extra="    ")


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| obj   | (Any) The object to display                                  |
| extra | (Default value = ' ') returns (str) Formatted output of the object's values |

Dumps an Object's values as a formatted string. Very nicely done. Great way to display an object's member variables in human form Returns only the top-most object's variables instead of drilling down to dispolay more

    obj_to_string_single_obj(obj)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| obj  | (Any) The object to display returns (str) Formatted output of the object's values |

    one_line_progress_meter(title,
        current_value,
        max_value,
        key,
        args,
        orientation="v",
        bar_color=(None, None),
        button_color=None,
        size=(20, 20),
        border_width=None,
        grab_anywhere=False)


Parameter Descriptions:

| Name           | Meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| title          | text to display                                              |
| current\_value | current progressbar value                                    |
| max\_value     | max value of progressbar                                     |
| key            | Used with window.FindElement and with return values to uniquely identify this element |
| \*args         | stuff to output.                                             |
| orientation    | 'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical')(Default value = 'v') |
| bar\_color     |                                                              |
| button\_color  | button color (foreground, background)                        |
| size           | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT\_PROGRESS\_BAR\_SIZE) |
| border\_width  | width of border around element                               |
| grab\_anywhere | If True can grab anywhere to move the window (Default = False) |

    one_line_progress_meter_cancel(key)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| key  | Used with window.FindElement and with return values to uniquely identify this element |

Popup - Display a popup Window with as many parms as you wish to include. This is the GUI equivalent of the "print" statement. It's also great for "pausing" your program's flow until the user can read some error messages.

    popup(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        button_type=0,
        auto_close=False,
        auto_close_duration=None,
        custom_text=(None, None),
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                | (Any) Variable number of your arguments. Load up the call with stuff to see! |
| title                 | (str) Optional title for the window. If none provided, the first arg will be used instead. |
| button\_color         | Tuple\[str, str\] Color of the buttons shown (text color, button color) |
| background\_color     | (str) Window's background color                              |
| text\_color           | (str) text color                                             |
| button\_type          | (enum) NOT USER SET! Determines which pre-defined buttons will be shown (Default value = POPUP\_BUTTONS\_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect. |
| auto\_close           | (bool) If True the window will automatically close           |
| auto\_close\_duration | (int) time in seconds to keep window open before closing it automatically |
| custom\_text          | Union\[Tuple\[str, str\], str\] A string or pair of strings that contain the text to display on the buttons |
| non\_blocking         | (bool) If True then will immediately return from the function without waiting for the user's input. |
| icon                  | Union\[str, bytes\] icon to display on the window. Same format as a Window call |
| line\_width           | (int) Width of lines in characters. Defaults to MESSAGE\_BOX\_LINE\_WIDTH |
| font                  | Union\[str, tuple(font name, size, modifiers) specifies the font family, size, etc |
| no\_titlebar          | (bool) If True will not show the frame around the window and the titlebar across the top |
| grab\_anywhere        | (bool) If True can grab anywhere to move the window. If no\_titlebar is True, grab\_anywhere should likely be enabled too |
| location              | Tuple\[int, int\] Location on screen to display the top left corner of window. Defaults to window centered on screen |
|                       |                                                              |
| **return**            | Union\[str, None\] Returns text of the button that was pressed. None will be returned if user closed window with X |

Show animation one frame at a time. This function has its own internal clocking meaning you can call it at any frequency and the rate the frames of video is shown remains constant. Maybe your frames update every 30 ms but your event loop is running every 10 ms. You don't have to worry about delaying, just call it every time through the loop.

    popup_animated(image_source,
        message=None,
        background_color=None,
        text_color=None,
        font=None,
        no_titlebar=True,
        grab_anywhere=True,
        keep_on_top=True,
        location=(None, None),
        alpha_channel=None,
        time_between_frames=0,
        transparent_color=None)


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| image\_source         | Union\[str, bytes\] Either a filename or a base64 string.    |
| message               | (str) An optional message to be shown with the animation     |
| background\_color     | (str) color of background                                    |
| text\_color           | (str) color of the text                                      |
| font                  | Union\[str, tuple) specifies the font family, size, etc      |
| no\_titlebar          | (bool) If True then the titlebar and window frame will not be shown |
| grab\_anywhere        | (bool) If True then you can move the window just clicking anywhere on window, hold and drag |
| keep\_on\_top         | (bool) If True then Window will remain on top of all other windows currently shownn |
| location              | (int, int) (x,y) location on the screen to place the top left corner of your window. Default is to center on screen |
| alpha\_channel        | (float) Window transparency 0 = invisible 1 = completely visible. Values between are see through |
| time\_between\_frames | (int) Amount of time in milliseconds between each frame      |
| transparent\_color    | (str) This color will be completely see-through in your window. Can even click through |

Display a Popup without a titlebar. Enables grab anywhere so you can move it

    popup_annoying(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        grab_anywhere=True,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                               |
| --------------------- | ------------------------------------- |
| \*args                |                                       |
| title                 |                                       |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)  |
| button\_color         | button color (foreground, background) |
| background\_color     | color of background                   |
| text\_color           | color of the text                     |
| auto\_close           | (Default = False)                     |
| auto\_close\_duration |                                       |
| non\_blocking         | (Default = False)                     |
| icon                  | Icon to display                       |
| line\_width           | Width of lines in characters          |
| font                  | specifies the font family, size, etc  |
| grab\_anywhere        | (Default = True)                      |
| location              |                                       |

Popup that closes itself after some time period

    popup_auto_close(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=True,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)                         |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = True)                                             |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Display Popup with "cancelled" button text

    popup_cancel(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Popup with colored button and 'Error' as button text

    popup_error(args,
        title=None,
        button_color=(None, None),
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              | (Default = (None))                                           |

Display popup window with text entry field and browse button so that a file can be chosen by user.

    popup_get_file(message,
        title=None,
        default_path="",
        default_extension="",
        save_as=False,
        multiple_files=False,
        file_types=(('ALL Files', '*.*'),),
        no_window=False,
        size=(None, None),
        button_color=None,
        background_color=None,
        text_color=None,
        icon=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None),
        initial_folder=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| message            | (str) message displayed to user                              |
| title              | (str) Window title                                           |
| default\_path      | (str) path to display to user as starting point (filled into the input field) |
| default\_extension | (str) If no extension entered by user, add this to filename (only used in saveas dialogs) |
| save\_as           | (bool) if True, the "save as" dialog is shown which will verify before overwriting |
| multiple\_files    | (bool) if True, then allows multiple files to be selected that are returned with ';' between each filename |
| file\_types        | Tuple\[Tuple\[str,str\]\] List of extensions to show using wildcards. All files (the default) = (("ALL Files", "*.*"),) |
| no\_window         | (bool) if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
| size               | Tuple\[int, int\] (width, height) of the InputText Element   |
| button\_color      | Tuple\[str, str\] Color of the button (text, background)     |
| background\_color  | (str) background color of the entire window                  |
| text\_color        | (str) color of the message text                              |
| icon               | Union\[bytes, str\] filename or base64 string to be used for the window's icon |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| no\_titlebar       | (bool) If True no titlebar will be shown                     |
| grab\_anywhere     | (bool) If True can click and drag anywhere in the window to move the window |
| keep\_on\_top      | (bool) If True the window will remain above all current windows |
| location           | Tuyple\[int, int\] (x,y) Location on screen to display the upper left corner of window |
| initial\_folder    | (str) location in filesystem to begin browsing               |
|                    |                                                              |
| **return**         | Union\[str, None\] string representing the file(s) chosen, None if cancelled or window closed with X |

Display popup with text entry field and browse button so that a folder can be chosen.

    popup_get_folder(message,
        title=None,
        default_path="",
        no_window=False,
        size=(None, None),
        button_color=None,
        background_color=None,
        text_color=None,
        icon=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None),
        initial_folder=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| message           | (str) message displayed to user                              |
| title             | (str) Window title                                           |
| default\_path     | (str) path to display to user as starting point (filled into the input field) |
| no\_window        | (bool) if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
| size              | Tuple\[int, int\] (width, height) of the InputText Element   |
| button\_color     | Tuple\[str, str\] Color of the button (text, background)     |
| background\_color | (str) background color of the entire window                  |
| text\_color       | (str) color of the message text                              |
| icon              | Union\[bytes, str\] filename or base64 string to be used for the window's icon |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| no\_titlebar      | (bool) If True no titlebar will be shown                     |
| grab\_anywhere    | (bool) If True can click and drag anywhere in the window to move the window |
| keep\_on\_top     | (bool) If True the window will remain above all current windows |
| location          | Tuyple\[int, int\] (x,y) Location on screen to display the upper left corner of window |
| initial\_folder   | (str) location in filesystem to begin browsing               |
|                   |                                                              |
| **return**        | Union\[str, None\] string representing the path chosen, None if cancelled or window closed with X |

Display Popup with text entry field. Returns the text entered or None if closed / cancelled

    popup_get_text(message,
        title=None,
        default_text="",
        password_char="",
        size=(None, None),
        button_color=None,
        background_color=None,
        text_color=None,
        icon=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| message           | (str) message displayed to user                              |
| title             | (str) Window title                                           |
| default\_text     | (str) default value to put into input area                   |
| password\_char    | (str) character to be shown instead of actually typed characters |
| size              | Tuple\[int, int\] (width, height) of the InputText Element   |
| button\_color     | Tuple\[str, str\] Color of the button (text, background)     |
| background\_color | (str) background color of the entire window                  |
| text\_color       | (str) color of the message text                              |
| icon              | Union\[bytes, str\] filename or base64 string to be used for the window's icon |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| no\_titlebar      | (bool) If True no titlebar will be shown                     |
| grab\_anywhere    | (bool) If True can click and drag anywhere in the window to move the window |
| keep\_on\_top     | (bool) If True the window will remain above all current windows |
| location          | Tuyple\[int, int\] (x,y) Location on screen to display the upper left corner of window |
|                   |                                                              |
| **return**        | Union\[str, None\] Text entered or None if window was closed or cancel button clicked |

Display a Popup without a titlebar. Enables grab anywhere so you can move it

    popup_no_border(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        grab_anywhere=True,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                               |
| --------------------- | ------------------------------------- |
| \*args                |                                       |
| title                 |                                       |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)  |
| button\_color         | button color (foreground, background) |
| background\_color     | color of background                   |
| text\_color           | color of the text                     |
| auto\_close           | (Default = False)                     |
| auto\_close\_duration |                                       |
| non\_blocking         | (Default = False)                     |
| icon                  | Icon to display                       |
| line\_width           | Width of lines in characters          |
| font                  | specifies the font family, size, etc  |
| grab\_anywhere        | (Default = True)                      |
| location              |                                       |

Show a Popup but without any buttons

    popup_no_buttons(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Display a Popup without a titlebar. Enables grab anywhere so you can move it

    popup_no_frame(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        grab_anywhere=True,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                               |
| --------------------- | ------------------------------------- |
| \*args                |                                       |
| title                 |                                       |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)  |
| button\_color         | button color (foreground, background) |
| background\_color     | color of background                   |
| text\_color           | color of the text                     |
| auto\_close           | (Default = False)                     |
| auto\_close\_duration |                                       |
| non\_blocking         | (Default = False)                     |
| icon                  | Icon to display                       |
| line\_width           | Width of lines in characters          |
| font                  | specifies the font family, size, etc  |
| grab\_anywhere        | (Default = True)                      |
| location              |                                       |

Display a Popup without a titlebar. Enables grab anywhere so you can move it

    popup_no_titlebar(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        grab_anywhere=True,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                               |
| --------------------- | ------------------------------------- |
| \*args                |                                       |
| title                 |                                       |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)  |
| button\_color         | button color (foreground, background) |
| background\_color     | color of background                   |
| text\_color           | color of the text                     |
| auto\_close           | (Default = False)                     |
| auto\_close\_duration |                                       |
| non\_blocking         | (Default = False)                     |
| icon                  | Icon to display                       |
| line\_width           | Width of lines in characters          |
| font                  | specifies the font family, size, etc  |
| grab\_anywhere        | (Default = True)                      |
| location              |                                       |

Show Popup window and immediately return (does not block)

    popup_no_wait(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=True,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))

Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)                         |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = True)                                             |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Show Popup window and immediately return (does not block)

    popup_non_blocking(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=True,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))

Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)                         |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = True)                                             |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Display Popup with OK button only

    popup_ok(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Show Popup box that doesn't block and closes itself

    popup_quick(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=True,
        auto_close_duration=2,
        non_blocking=True,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)                         |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = True)                                             |
| auto\_close\_duration | (Default value = 2)                                          |
| non\_blocking         | (Default = True)                                             |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Show Popup window with no titlebar, doesn't block, and auto closes itself.

    popup_quick_message(args,
        title=None,
        button_type=5,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=True,
        auto_close_duration=2,
        non_blocking=True,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=True,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_NO\_BUTTONS)                |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = True)                                             |
| auto\_close\_duration | (Default value = 2)                                          |
| non\_blocking         | (Default = True)                                             |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = True)                                             |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you want, just like a print statement.

    popup_scrolled(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        yes_no=False,
        auto_close=False,
        auto_close_duration=None,
        size=(None, None),
        location=(None, None),
        non_blocking=False,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        font=None)

Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                | (Any) Variable number of items to display                    |
| title                 | (str) Title to display in the window.                        |
| button\_color         | Tuple\[str, str\] button color (foreground, background)      |
| yes\_no               | (bool) If True, displays Yes and No buttons instead of Ok    |
| auto\_close           | (bool) if True window will close itself                      |
| auto\_close\_duration | Union\[int, float\] Older versions only accept int. Time in seconds until window will close |
| size                  | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| location              | Tuple\[int, int\] Location on the screen to place the upper left corner of the window |
| non\_blocking         | (bool) if True the call will immediately return rather than waiting on user input |
|                       |                                                              |
| **return**            | Union\[str, None, TIMEOUT\_KEY\] Returns text of the button that was pressed. None will be returned if user closed window with X |

Popup that closes itself after some time period

    popup_timed(args,
        title=None,
        button_type=0,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=True,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_type          | (Default value = POPUP\_BUTTONS\_OK)                         |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = True)                                             |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              |                                                              |

Display Popup with Yes and No buttons

    popup_yes_no(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        auto_close=False,
        auto_close_duration=None,
        non_blocking=False,
        icon=None,
        line_width=None,
        font=None,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        location=(None, None))


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                |                                                              |
| title                 |                                                              |
| button\_color         | button color (foreground, background)                        |
| background\_color     | color of background                                          |
| text\_color           | color of the text                                            |
| auto\_close           | (Default = False)                                            |
| auto\_close\_duration |                                                              |
| non\_blocking         | (Default = False)                                            |
| icon                  | Icon to display                                              |
| line\_width           | Width of lines in characters                                 |
| font                  | specifies the font family, size, etc                         |
| no\_titlebar          | (Default = False)                                            |
| grab\_anywhere        | If True can grab anywhere to move the window (Default = False) |
| location              | Location on screen to display                                |
|                       |                                                              |
| **return**            | Union\["Yes", "No", None\]                                   |

    quit(button_text="Quit",
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        disabled=False,
        tooltip=None,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | text in the button (Default value = 'Quit')                  |
| size               | (w,h) w=characters-wide, h=rows-high                         |
| auto\_size\_button | True if button size is determined by button text             |
| button\_color      | button color (foreground, background)                        |
| disabled           | set disable state for element (Default = False)              |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| font               | specifies the font family, size, etc                         |
| bind\_return\_key  | (Default = False)                                            |
| focus              | if focus should be set to this                               |
| pad                | Amount of padding to put around element                      |
| key                | Used with window.FindElement and with return values to uniquely identify this element |
|                    |                                                              |
| **return**         | (Button)                                                     |

Sets the icon which will be used any time a window is created if an icon is not provided when the window is created.

    set_global_icon(icon)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| icon | Union\[bytes, str\] Either a Base64 byte string or a filename |

    set_options(icon=None,
        button_color=None,
        element_size=(None, None),
        button_element_size=(None, None),
        margins=(None, None),
        element_padding=(None, None),
        auto_size_text=None,
        auto_size_buttons=None,
        font=None,
        border_width=None,
        slider_border_width=None,
        slider_relief=None,
        slider_orientation=None,
        autoclose_time=None,
        message_box_line_width=None,
        progress_meter_border_depth=None,
        progress_meter_style=None,
        progress_meter_relief=None,
        progress_meter_color=None,
        progress_meter_size=None,
        text_justification=None,
        background_color=None,
        element_background_color=None,
        text_element_background_color=None,
        input_elements_background_color=None,
        input_text_color=None,
        scrollbar_color=None,
        text_color=None,
        element_text_color=None,
        debug_win_size=(None, None),
        window_location=(None, None),
        error_button_color=(None, None),
        tooltip_time=None,
        use_ttk_buttons=None,
        ttk_theme=None)


Parameter Descriptions:

| Name                               | Meaning                                                      |
| ---------------------------------- | ------------------------------------------------------------ |
| icon                               | filename of icon used for taskbar and title bar              |
| button\_color                      | button color (foreground, background)                        |
| element\_size                      | Tuple\[int, int\] element size (width, height) in characters |
| button\_element\_size              | Tuple\[int, int\]                                            |
| margins                            | tkinter margins around outsize (Default = (None))            |
| element\_padding                   | (Default = (None))                                           |
| auto\_size\_text                   | True if size should fit the text length                      |
| auto\_size\_buttons                |                                                              |
| font                               | specifies the font family, size, etc                         |
| border\_width                      | width of border around element                               |
| slider\_border\_width              |                                                              |
| slider\_relief                     |                                                              |
| slider\_orientation                |                                                              |
| autoclose\_time                    |                                                              |
| message\_box\_line\_width          |                                                              |
| progress\_meter\_border\_depth     |                                                              |
| progress\_meter\_style             |                                                              |
| progress\_meter\_relief            |                                                              |
| progress\_meter\_color             |                                                              |
| progress\_meter\_size              | Tuple\[int, int\]                                            |
| text\_justification                |                                                              |
| background\_color                  | color of background                                          |
| element\_background\_color         |                                                              |
| text\_element\_background\_color   |                                                              |
| input\_elements\_background\_color |                                                              |
| input\_text\_color                 |                                                              |
| scrollbar\_color                   |                                                              |
| text\_color                        | color of the text                                            |
| element\_text\_color               |                                                              |
| debug\_win\_size                   | Tuple\[int, int\] (Default = (None))                         |
| window\_location                   | (Default = (None))                                           |
| error\_button\_color               | (Default = (None))                                           |
| tooltip\_time                      | time in milliseconds to wait before showing a tooltip. Default is 400ms |
| use\_ttk\_buttons                  | (bool) if True will cause all buttons to be ttk buttons      |
| ttk\_theme                         | (str) Theme to use with ttk widgets. Choices (on Windows) include - 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative' |

    sgprint(args,
        size=(None, None),
        end=None,
        sep=None,
        location=(None, None),
        font=None,
        no_titlebar=False,
        no_button=False,
        grab_anywhere=False,
        keep_on_top=False,
        do_not_reroute_stdout=True)

Parameter Descriptions:

| Name                     | Meaning                                                      |
| ------------------------ | ------------------------------------------------------------ |
| \*args                   |                                                              |
| size                     | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| end                      |                                                              |
| sep                      |                                                              |
| location                 | Location on screen to display                                |
| font                     | specifies the font family, size, etc                         |
| no\_titlebar             | (Default = False)                                            |
| no\_button               | (Default = False)                                            |
| grab\_anywhere           | If True can grab anywhere to move the window (Default = False) |
| do\_not\_reroute\_stdout | (Default = True)                                             |

    sgprint_close()

Shows the smaller "popout" window. Default location is the upper right corner of your screen

    show_debugger_popout_window(location=(None, None), args)

Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| location | Tuple\[int, int\] Locations (x,y) on the screen to place upper left corner of the window |
| \*args   | Not used                                                     |

Shows the large main debugger window

    show_debugger_window(location=(None, None), args)

Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| location | Tuple\[int, int\] Locations (x,y) on the screen to place upper left corner of the window |
| \*args   | Not used                                                     |

Show a scrolled Popup window containing the user's text that was supplied. Use with as many items to print as you want, just like a print statement.

    sprint(args,
        title=None,
        button_color=None,
        background_color=None,
        text_color=None,
        yes_no=False,
        auto_close=False,
        auto_close_duration=None,
        size=(None, None),
        location=(None, None),
        non_blocking=False,
        no_titlebar=False,
        grab_anywhere=False,
        keep_on_top=False,
        font=None)

Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| \*args                | (Any) Variable number of items to display                    |
| title                 | (str) Title to display in the window.                        |
| button\_color         | Tuple\[str, str\] button color (foreground, background)      |
| yes\_no               | (bool) If True, displays Yes and No buttons instead of Ok    |
| auto\_close           | (bool) if True window will close itself                      |
| auto\_close\_duration | Union\[int, float\] Older versions only accept int. Time in seconds until window will close |
| size                  | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| location              | Tuple\[int, int\] Location on the screen to place the upper left corner of the window |
| non\_blocking         | (bool) if True the call will immediately return rather than waiting on user input |
|                       |                                                              |
| **return**            | Union\[str, None, TIMEOUT\_KEY\] Returns text of the button that was pressed. None will be returned if user closed window with X |

The PySimpleGUI "Test Harness". This is meant to be a super-quick test of the Elements.

    test()

------------------------------------------------------------------------

