

ELEMENT AND FUNCTION CALL REFERENCE
===================================

This reference section was previously intermixed with the text explanation, diagrams, code samples, etc. That was OK early on, but now that there are more Elements and more methods are being added on a fequent basis, it means that keeping this list updated is a difficult chore if it has a lot of text all around it.

Hoping this is a change for the better and that users will be able to find the information they seek quicker.

NOTE that this documentatiuopn section is created using the ***GitHUB released PySimpleGUI.py file***. Some of the calls may not be available to you or your port (Qt, Wx, Web). And some of the parameters may be different. We're working on adding docstrings to all the ports which will enable this kind of document to be available for each port.

Button Element
--------------

    Button Element - Defines all possible buttons. The shortcuts such as Submit, FileBrowse, ... each create a Button
    
    Button(button_text="",
        button_type=7,
        target=(None, None),
        tooltip=None,
        file_types=(('ALL Files', '*.*'),),
        initial_folder=None,
        disabled=False,
        change_submits=False,
        enable_events=False,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        use_ttk_buttons=None,
        font=None,
        bind_return_key=False,
        focus=False,
        pad=None,
        key=None,
        visible=True,
        metadata=None)

Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | (str) Text to be displayed on the button                     |
| button\_type       | (int) You should NOT be setting this directly. ONLY the shortcut functions set this |
| target             | Union\[str, Tuple\[int, int\]\] key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| file\_types        | Tuple\[Tuple\[str, str\], ...\] the filetypes that will be used to match files. To indicate all files: (("ALL Files", "*.*"),). Note - NOT SUPPORTED ON MAC |
| initial\_folder    | (str) starting path for folders and files                    |
| disabled           | (bool) If True button will be created disabled               |
| click\_submits     | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events     | (bool) Turns on the element specific events. If this button is a target, should it generate an event when filled in |
| image\_filename    | (str) image filename if there is a button image. GIFs and PNGs only. |
| image\_data        | Union\[bytes, str\] Raw or Base64 representation of the image to put on button. Choose either filename or data |
| image\_size        | Tuple\[int, int\] Size of the image in pixels (width, height) |
| image\_subsample   | (int) amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| border\_width      | (int) width of border around button in pixels                |
| size               | Tuple\[int, int\] (width, height) of the button in characters wide, rows high |
| auto\_size\_button | (bool) if True the button size is sized to fit the text      |
| button\_color      | Tuple\[str, str\] (text color, background color) of button. Easy to remember which is which if you say "ON" between colors. "red" on "green". |
| use\_ttk\_buttons  | (bool) True = use ttk buttons. False = do not use ttk buttons. None (Default) = use ttk buttons only if on a Mac and not with button images |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| bind\_return\_key  | (bool) If True the return key will cause this button to be pressed |
| focus              | (bool) if True, initial focus will be put on this button     |
| pad                | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| visible            | (bool) set visibility state of the element                   |
| metadata           | (Any) User metadata that can be set to ANYTHING              |

### ButtonCallBack

Not user callable! Called by tkinter when a button is clicked. This is where all the fun begins!

    ButtonCallBack()

### ButtonPressCallBack

Not a user callable method. Callback called by tkinter when a "realtime" button is pressed

    ButtonPressCallBack(parm)

Parameter Descriptions:

| Name | Meaning                         |
| ---- | ------------------------------- |
| parm | Event info passed in by tkinter |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)

Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### ButtonReleaseCallBack

Not a user callable function. Called by tkinter when a "realtime" button is released

    ButtonReleaseCallBack(parm)

Parameter Descriptions:

| Name | Meaning                     |
| ---- | --------------------------- |
| parm | the event info from tkinter |

### Click

Generates a click of the button as if the user clicked the button Calls the tkinter invoke method for the button

    Click()

### GetText

Returns the current text shown on a button

`GetText()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | (str) The text currently displayed on the button |

### SetFocus

Sets the current focus to be on this element

    SetFocus(force=False)

Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### SetTooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    SetTooltip(tooltip_text)

Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### Update

Changes some of the settings for the Button Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(text=None,
        button_color=(None, None),
        disabled=None,
        image_data=None,
        image_filename=None,
        visible=None,
        image_subsample=None,
        image_size=None)


Parameter Descriptions:

| Name             | Meaning                                                      |
| ---------------- | ------------------------------------------------------------ |
| text             | (str) sets button text                                       |
| button\_color    | Tuple\[str, str\] (text color, background color) of button. Easy to remember which is which if you say "ON" between colors. "red" on "green" |
| disabled         | (bool) disable or enable state of the element                |
| image\_data      | Union\[bytes, str\] Raw or Base64 representation of the image to put on button. Choose either filename or data |
| image\_filename  | (str) image filename if there is a button image. GIFs and PNGs only. |
| visible          | (bool) control visibility of element                         |
| image\_subsample | (int) amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| image\_size      | Tuple\[int, int\] Size of the image in pixels (width, height) |

### button\_rebound\_callback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    button_rebound_callback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### click

Generates a click of the button as if the user clicked the button Calls the tkinter invoke method for the button

    click()

### expand

Causes the Element to expand to fill available space in the X and Y directions. Can specify which or both directions

    expand(expand_x=False, expand_y=False)

Parameter Descriptions:

| Name      | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| expand\_x | (Bool) If True Element will expand in the Horizontal directions |
| expand\_y | (Bool) If True Element will expand in the Vertical directions |

### get\_size

Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size but will return pixels when calling this get\_size method.

`get_size()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | Tuple\[int, int\] - Width, Height of the element |

### get\_text

Returns the current text shown on a button

`get_text()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | (str) The text currently displayed on the button |

### hide\_row

Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an element, including the row container

    hide_row()

### set\_focus

Sets the current focus to be on this element

    set_focus(force=False)

Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### set\_size

Changes the size of an element to a specific size. It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

    set_size(size=(None, None))

Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| size | Tuple\[int, int\] The size in characters, rows typically. In some cases they are pixels |

### set\_tooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    set_tooltip(tooltip_text)

Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()

### update

Changes some of the settings for the Button Element. Must call `Window.Read` or `Window.Finalize` prior

    update(text=None,
        button_color=(None, None),
        disabled=None,
        image_data=None,
        image_filename=None,
        visible=None,
        image_subsample=None,
        image_size=None)

Parameter Descriptions:

| Name             | Meaning                                                      |
| ---------------- | ------------------------------------------------------------ |
| text             | (str) sets button text                                       |
| button\_color    | Tuple\[str, str\] (text color, background color) of button. Easy to remember which is which if you say "ON" between colors. "red" on "green" |
| disabled         | (bool) disable or enable state of the element                |
| image\_data      | Union\[bytes, str\] Raw or Base64 representation of the image to put on button. Choose either filename or data |
| image\_filename  | (str) image filename if there is a button image. GIFs and PNGs only. |
| visible          | (bool) control visibility of element                         |
| image\_subsample | (int) amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| image\_size      | Tuple\[int, int\] Size of the image in pixels (width, height) |

Frame Element
-------------

    A Frame Element that contains other Elements. Encloses with a line around elements and a text label.
    
    Frame(title,
        layout,
        title_color=None,
        background_color=None,
        title_location=None,
        relief="groove",
        size=(None, None),
        font=None,
        pad=None,
        border_width=None,
        key=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        element_justification="left",
        metadata=None)


Parameter Descriptions:

| Name                   | Meaning                                                      |
| ---------------------- | ------------------------------------------------------------ |
| title                  | (str) text that is displayed as the Frame's "label" or title |
| layout                 | List\[List\[Elements\]\] The layout to put inside the Frame  |
| title\_color           | (str) color of the title text                                |
| background\_color      | (str) background color of the Frame                          |
| title\_location        | (enum) location to place the text title. Choices include: TITLE\_LOCATION\_TOP TITLE\_LOCATION\_BOTTOM TITLE\_LOCATION\_LEFT TITLE\_LOCATION\_RIGHT TITLE\_LOCATION\_TOP\_LEFT TITLE\_LOCATION\_TOP\_RIGHT TITLE\_LOCATION\_BOTTOM\_LEFT TITLE\_LOCATION\_BOTTOM\_RIGHT |
| relief                 | (enum) relief style. Values are same as other elements with reliefs. Choices include RELIEF\_RAISED RELIEF\_SUNKEN RELIEF\_FLAT RELIEF\_RIDGE RELIEF\_GROOVE RELIEF\_SOLID |
| size                   | Tuple\[int, int\] (width in characters, height in rows) (note this parameter may not always work) |
| font                   | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                    | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| border\_width          | (int) width of border around element in pixels               |
| key                    | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| tooltip                | (str) text, that will appear when mouse hovers over the element |
| right\_click\_menu     | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible                | (bool) set visibility state of the element                   |
| element\_justification | (str) All elements inside the Frame will have this justification 'left', 'right', 'center' are valid values |
| metadata               | (Any) User metadata that can be set to ANYTHING              |

### AddRow

Not recommended user call. Used to add rows of Elements to the Frame Element.

    AddRow(args)


Parameter Descriptions:

| Name   | Meaning                                           |
| ------ | ------------------------------------------------- |
| \*args | List\[Element\] The list of elements for this row |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Layout

Can use like the Window.Layout method, but it's better to use the layout parameter when creating

    Layout(rows)


Parameter Descriptions:

| Name       | Meaning                                      |
| ---------- | -------------------------------------------- |
| rows       | List\[List\[Element\]\] The rows of Elements |
|            |                                              |
| **return** | (Frame) Used for chaining                    |

### SetFocus

Sets the current focus to be on this element

    SetFocus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### SetTooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    SetTooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### Update

Changes some of the settings for the Frame Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None, visible=None)


Parameter Descriptions:

| Name    | Meaning                               |
| ------- | ------------------------------------- |
| value   | (Any) New text value to show on frame |
| visible | (bool) control visibility of element  |

### add\_row

Not recommended user call. Used to add rows of Elements to the Frame Element.

    add_row(args)


Parameter Descriptions:

| Name   | Meaning                                           |
| ------ | ------------------------------------------------- |
| \*args | List\[Element\] The list of elements for this row |

### button\_rebound\_callback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    button_rebound_callback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### expand

Causes the Element to expand to fill available space in the X and Y directions. Can specify which or both directions

    expand(expand_x=False, expand_y=False)


Parameter Descriptions:

| Name      | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| expand\_x | (Bool) If True Element will expand in the Horizontal directions |
| expand\_y | (Bool) If True Element will expand in the Vertical directions |

### get\_size

Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size but will return pixels when calling this get\_size method.

`get_size()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | Tuple\[int, int\] - Width, Height of the element |

### hide\_row

Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an element, including the row container

    hide_row()


### layout

Can use like the Window.Layout method, but it's better to use the layout parameter when creating

    layout(rows)


Parameter Descriptions:

| Name       | Meaning                                      |
| ---------- | -------------------------------------------- |
| rows       | List\[List\[Element\]\] The rows of Elements |
|            |                                              |
| **return** | (Frame) Used for chaining                    |

### set\_focus

Sets the current focus to be on this element

    set_focus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### set\_size

Changes the size of an element to a specific size. It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

    set_size(size=(None, None))


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| size | Tuple\[int, int\] The size in characters, rows typically. In some cases they are pixels |

### set\_tooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    set_tooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Frame Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None, visible=None)


Parameter Descriptions:

| Name    | Meaning                               |
| ------- | ------------------------------------- |
| value   | (Any) New text value to show on frame |
| visible | (bool) control visibility of element  |


-------------

Image Element
-------------

    Image Element - show an image in the window. Should be a GIF or a PNG only
    
    Image(filename=None,
        data=None,
        background_color=None,
        size=(None, None),
        pad=None,
        key=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        enable_events=False,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| filename           | (str) image filename if there is a button image. GIFs and PNGs only. |
| data               | Union\[bytes, str\] Raw or Base64 representation of the image to put on button. Choose either filename or data |
| background\_color  | color of background                                          |
| size               | Tuple\[int, int\] (width, height) size of image in pixels    |
| pad                | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| right\_click\_menu | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible            | (bool) set visibility state of the element                   |
| enable\_events     | (bool) Turns on the element specific events. For an Image element, the event is "image clicked" |
| metadata           | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### SetFocus

Sets the current focus to be on this element

    SetFocus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### SetTooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    SetTooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### Update

Changes some of the settings for the Image Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(filename=None,
        data=None,
        size=(None, None),
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| filename | (str) filename to the new image to display.                  |
| data     | Union\[str, tkPhotoImage\] Base64 encoded string OR a tk.PhotoImage object |
| size     | Tuple\[int,int\] size of a image (w,h) w=characters-wide, h=rows-high |
| visible  | (bool) control visibility of element                         |

### UpdateAnimation

Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time. NOTE - does NOT perform a sleep call to delay

    UpdateAnimation(source, time_between_frames=0)


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| source                | Union\[str,bytes\] Filename or Base64 encoded string containing Animated GIF |
| time\_between\_frames | (int) Number of milliseconds to wait between showing frames  |

### button\_rebound\_callback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    button_rebound_callback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### expand

Causes the Element to expand to fill available space in the X and Y directions. Can specify which or both directions

    expand(expand_x=False, expand_y=False)


Parameter Descriptions:

| Name      | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| expand\_x | (Bool) If True Element will expand in the Horizontal directions |
| expand\_y | (Bool) If True Element will expand in the Vertical directions |

### get\_size

Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size but will return pixels when calling this get\_size method.

`get_size()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | Tuple\[int, int\] - Width, Height of the element |

### hide\_row

Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an element, including the row container

    hide_row()


### set\_focus

Sets the current focus to be on this element

    set_focus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### set\_size

Changes the size of an element to a specific size. It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

    set_size(size=(None, None))


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| size | Tuple\[int, int\] The size in characters, rows typically. In some cases they are pixels |

### set\_tooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    set_tooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Image Element. Must call `Window.Read` or `Window.Finalize` prior

    update(filename=None,
        data=None,
        size=(None, None),
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| filename | (str) filename to the new image to display.                  |
| data     | Union\[str, tkPhotoImage\] Base64 encoded string OR a tk.PhotoImage object |
| size     | Tuple\[int,int\] size of a image (w,h) w=characters-wide, h=rows-high |
| visible  | (bool) control visibility of element                         |

### update\_animation

Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time. NOTE - does NOT perform a sleep call to delay

    update_animation(source, time_between_frames=0)


Parameter Descriptions:

| Name                  | Meaning                                                      |
| --------------------- | ------------------------------------------------------------ |
| source                | Union\[str,bytes\] Filename or Base64 encoded string containing Animated GIF |
| time\_between\_frames | (int) Number of milliseconds to wait between showing frames  |

InputText Element
-----------------

    Display a single text input field.  Based on the tkinter Widget `Entry`
    
    InputText(default_text="",
        size=(None, None),
        disabled=False,
        password_char="",
        justification=None,
        background_color=None,
        text_color=None,
        font=None,
        tooltip=None,
        change_submits=False,
        enable_events=False,
        do_not_clear=True,
        key=None,
        focus=False,
        pad=None,
        use_readonly_for_disable=True,
        right_click_menu=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name                        | Meaning                                                      |
| --------------------------- | ------------------------------------------------------------ |
| default\_text               | (str) Text initially shown in the input box as a default value(Default value = '') |
| size                        | Tuple\[int, int\] (width, height) w=characters-wide, h=rows-high |
| disabled                    | (bool) set disable state for element (Default = False)       |
| password\_char              | (char) Password character if this is a password field (Default value = '') |
| justification               | (str) justification for data display. Valid choices - left, right, center |
| background\_color           | (str) color of background in one of the color formats        |
| text\_color                 | (str) color of the text                                      |
| font                        | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| tooltip                     | (str) text, that will appear when mouse hovers over the element |
| change\_submits             | (bool) \* DEPRICATED DO NOT USE! Same as enable\_events      |
| enable\_events              | (bool) If True then changes to this element are immediately reported as an event. Use this instead of change\_submits (Default = False) |
| do\_not\_clear              | (bool) If False then the field will be set to blank after ANY event (button, any event) (Default = True) |
| key                         | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| focus                       | (bool) Determines if initial focus should go to this element. |
| pad                         | (int, int) or ((int, int), (int, int)) Tuple(s). Amount of padding to put around element. Normally (horizontal pixels, vertical pixels) but can be split apart further into ((horizontal left, horizontal right), (vertical above, vertical below)) |
| use\_readonly\_for\_disable | (bool) If True (the default) tkinter state set to 'readonly'. Otherwise state set to 'disabled' |
| right\_click\_menu          | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible                     | (bool) set visibility state of the element (Default = True)  |
| metadata                    | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Get

Read and return the current value of the input element. Must call `Window.Read` or `Window.Finalize` prior

`Get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (str) current value of Input field or '' if error encountered |

### SetFocus

Sets the current focus to be on this element

    SetFocus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### SetTooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    SetTooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### Update

Changes some of the settings for the Input Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        disabled=None,
        select=None,
        visible=None,
        text_color=None,
        background_color=None,
        move_cursor_to="end")


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| value             | (str) new text to display as default text in Input field     |
| disabled          | (bool) disable or enable state of the element (sets Entry Widget to readonly or normal) |
| select            | (bool) if True, then the text will be selected               |
| visible           | (bool) change visibility of element                          |
| text\_color       | (str) change color of text being typed                       |
| background\_color | (str) change color of the background                         |
| move\_cursor\_to  | Union\[int, str\] Moves the cursor to a particular offset. Defaults to 'end' |

### button\_rebound\_callback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    button_rebound_callback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### expand

Causes the Element to expand to fill available space in the X and Y directions. Can specify which or both directions

    expand(expand_x=False, expand_y=False)


Parameter Descriptions:

| Name      | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| expand\_x | (Bool) If True Element will expand in the Horizontal directions |
| expand\_y | (Bool) If True Element will expand in the Vertical directions |

### get

Read and return the current value of the input element. Must call `Window.Read` or `Window.Finalize` prior

`get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (str) current value of Input field or '' if error encountered |

### get\_size

Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size but will return pixels when calling this get\_size method.

`get_size()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | Tuple\[int, int\] - Width, Height of the element |

### hide\_row

Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an element, including the row container

    hide_row()


### set\_focus

Sets the current focus to be on this element

    set_focus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### set\_size

Changes the size of an element to a specific size. It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

    set_size(size=(None, None))


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| size | Tuple\[int, int\] The size in characters, rows typically. In some cases they are pixels |

### set\_tooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    set_tooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Input Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        disabled=None,
        select=None,
        visible=None,
        text_color=None,
        background_color=None,
        move_cursor_to="end")


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| value             | (str) new text to display as default text in Input field     |
| disabled          | (bool) disable or enable state of the element (sets Entry Widget to readonly or normal) |
| select            | (bool) if True, then the text will be selected               |
| visible           | (bool) change visibility of element                          |
| text\_color       | (str) change color of text being typed                       |
| background\_color | (str) change color of the background                         |
| move\_cursor\_to  | Union\[int, str\] Moves the cursor to a particular offset. Defaults to 'end' |

Multiline Element
-----------------

    Multiline Element - Display and/or read multiple lines of text.  This is both an input and output element.
    Other PySimpleGUI ports have a separate MultilineInput and MultilineOutput elements.  May want to split this
    one up in the future too.
    
    Multiline(default_text="",
        enter_submits=False,
        disabled=False,
        autoscroll=False,
        border_width=None,
        size=(None, None),
        auto_size_text=None,
        background_color=None,
        text_color=None,
        change_submits=False,
        enable_events=False,
        do_not_clear=True,
        key=None,
        focus=False,
        font=None,
        pad=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        metadata=None)

Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| default\_text      | (str) Initial text to show                                   |
| enter\_submits     | (bool) if True, the Window.Read call will return is enter key is pressed in this element |
| disabled           | (bool) set disable state                                     |
| autoscroll         | (bool) If True the contents of the element will automatically scroll as more data added to the end |
| border\_width      | (int) width of border around element in pixels               |
| size               | Tuple\[int, int\] (width, height) width = characters-wide, height = rows-high |
| auto\_size\_text   | (bool) if True will size the element to match the length of the text |
| background\_color  | (str) color of background                                    |
| text\_color        | (str) color of the text                                      |
| change\_submits    | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events     | (bool) Turns on the element specific events. Spin events happen when an item changes |
| do\_not\_clear     | if False the element will be cleared any time the Window.Read call returns |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| focus              | (bool) if True initial focus will go to this element         |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| right\_click\_menu | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible            | (bool) set visibility state of the element                   |
| metadata           | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Get

Return current contents of the Multiline Element

`Get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (str) current contents of the Multiline Element (used as an input type of Multiline |

### SetFocus

Sets the current focus to be on this element

    SetFocus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### SetTooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    SetTooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### Update

Changes some of the settings for the Multiline Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        disabled=None,
        append=False,
        font=None,
        text_color=None,
        background_color=None,
        visible=None,
        autoscroll=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| value             | (str) new text to display                                    |
| disabled          | (bool) disable or enable state of the element                |
| append            | (bool) if True then new value will be added onto the end of the current value. if False then contents will be replaced. |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| text\_color       | (str) color of the text                                      |
| background\_color | (str) color of background                                    |
| visible           | (bool) set visibility state of the element                   |
| autoscroll        | (bool) if True then contents of element are scrolled down when new text is added to the end |

### button\_rebound\_callback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    button_rebound_callback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### expand

Causes the Element to expand to fill available space in the X and Y directions. Can specify which or both directions

    expand(expand_x=False, expand_y=False)


Parameter Descriptions:

| Name      | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| expand\_x | (Bool) If True Element will expand in the Horizontal directions |
| expand\_y | (Bool) If True Element will expand in the Vertical directions |

### get

Return current contents of the Multiline Element

`get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | (str) current contents of the Multiline Element (used as an input type of Multiline |

### get\_size

Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size but will return pixels when calling this get\_size method.

`get_size()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | Tuple\[int, int\] - Width, Height of the element |

### hide\_row

Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an element, including the row container

    hide_row()


### set\_focus

Sets the current focus to be on this element

    set_focus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### set\_size

Changes the size of an element to a specific size. It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

    set_size(size=(None, None))


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| size | Tuple\[int, int\] The size in characters, rows typically. In some cases they are pixels |

### set\_tooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    set_tooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()

### update

Changes some of the settings for the Multiline Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        disabled=None,
        append=False,
        font=None,
        text_color=None,
        background_color=None,
        visible=None,
        autoscroll=None)

Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| value             | (str) new text to display                                    |
| disabled          | (bool) disable or enable state of the element                |
| append            | (bool) if True then new value will be added onto the end of the current value. if False then contents will be replaced. |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| text\_color       | (str) color of the text                                      |
| background\_color | (str) color of background                                    |
| visible           | (bool) set visibility state of the element                   |
| autoscroll        | (bool) if True then contents of element are scrolled down when new text is added to the end |



Text Element
------------

    Text - Display some text in the window.  Usually this means a single line of text.  However, the text can also be multiple lines.  If multi-lined there are no scroll bars.
    
    Text(text="",
        size=(None, None),
        auto_size_text=None,
        click_submits=False,
        enable_events=False,
        relief=None,
        font=None,
        text_color=None,
        background_color=None,
        border_width=None,
        justification=None,
        pad=None,
        key=None,
        right_click_menu=None,
        tooltip=None,
        visible=True,
        metadata=None)

Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| text               | (str) The text to display. Can include /n to achieve multiple lines |
| size               | Tuple\[int, int\] (width, height) width = characters-wide, height = rows-high |
| auto\_size\_text   | (bool) if True size of the Text Element will be sized to fit the string provided in 'text' parm |
| click\_submits     | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events     | (bool) Turns on the element specific events. Text events happen when the text is clicked |
| relief             | (str/enum) relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with "RELIEF\_" - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID` |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| text\_color        | (str) color of the text                                      |
| background\_color  | (str) color of background                                    |
| border\_width      | (int) number of pixels for the border (if using a relief)    |
| justification      | (str) how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center` |
| pad                | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| right\_click\_menu | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| visible            | (bool) set visibility state of the element                   |
| metadata           | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### SetFocus

Sets the current focus to be on this element

    SetFocus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### SetTooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    SetTooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### Update

Changes some of the settings for the Text Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        background_color=None,
        text_color=None,
        font=None,
        visible=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| value             | (str) new text to show                                       |
| background\_color | (str) color of background                                    |
| text\_color       | (str) color of the text                                      |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| visible           | (bool) set visibility state of the element                   |

### button\_rebound\_callback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    button_rebound_callback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### expand

Causes the Element to expand to fill available space in the X and Y directions. Can specify which or both directions

    expand(expand_x=False, expand_y=False)


Parameter Descriptions:

| Name      | Meaning                                                      |
| --------- | ------------------------------------------------------------ |
| expand\_x | (Bool) If True Element will expand in the Horizontal directions |
| expand\_y | (Bool) If True Element will expand in the Vertical directions |

### get\_size

Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size but will return pixels when calling this get\_size method.

`get_size()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | Tuple\[int, int\] - Width, Height of the element |

### hide\_row

Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an element, including the row container

    hide_row()


### set\_focus

Sets the current focus to be on this element

    set_focus(force=False)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| force | (bool) if True will call focus\_force otherwise calls focus\_set |

### set\_size

Changes the size of an element to a specific size. It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

    set_size(size=(None, None))


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| size | Tuple\[int, int\] The size in characters, rows typically. In some cases they are pixels |

### set\_tooltip

Called by application to change the tooltip text for an Element. Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

    set_tooltip(tooltip_text)


Parameter Descriptions:

| Name          | Meaning                            |
| ------------- | ---------------------------------- |
| tooltip\_text | (str) the text to show in tooltip. |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Text Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        background_color=None,
        text_color=None,
        font=None,
        visible=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| value             | (str) new text to show                                       |
| background\_color | (str) color of background                                    |
| text\_color       | (str) color of the text                                      |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| visible           | (bool) set visibility state of the element                   |



