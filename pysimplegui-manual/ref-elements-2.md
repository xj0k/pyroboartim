





ButtonMenu Element
------------------

    The Button Menu Element.  Creates a button that when clicked will show a menu similar to right click menu
    
    ButtonMenu(button_text,
        menu_def,
        tooltip=None,
        disabled=False,
        image_filename=None,
        image_data=None,
        image_size=(None, None),
        image_subsample=None,
        border_width=None,
        size=(None, None),
        auto_size_button=None,
        button_color=None,
        font=None,
        pad=None,
        key=None,
        tearoff=False,
        visible=True,
        metadata=None)

Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| button\_text       | (str) Text to be displayed on the button                     |
| menu\_def          | List\[List\[str\]\] A list of lists of Menu items to show when this element is clicked. See docs for format as they are the same for all menu types |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| disabled           | (bool) If True button will be created disabled               |
| image\_filename    | (str) image filename if there is a button image. GIFs and PNGs only. |
| image\_data        | Union\[bytes, str\] Raw or Base64 representation of the image to put on button. Choose either filename or data |
| image\_size        | Tuple\[int, int\] Size of the image in pixels (width, height) |
| image\_subsample   | (int) amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| border\_width      | (int) width of border around button in pixels                |
| size               | Tuple\[int, int\] (width, height) of the button in characters wide, rows high |
| auto\_size\_button | (bool) if True the button size is sized to fit the text      |
| button\_color      | Tuple\[str, str\] (text color, background color) of button. Easy to remember which is which if you say "ON" between colors. "red" on "green" |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| tearoff            | (bool) Determines if menus should allow them to be torn off  |
| visible            | (bool) set visibility state of the element                   |
| metadata           | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)

Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Click

Generates a click of the button as if the user clicked the button Calls the tkinter invoke method for the button

    Click()

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

Changes some of the settings for the ButtonMenu Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(menu_definition, visible=None)

Parameter Descriptions:

| Name             | Meaning                                                      |
| ---------------- | ------------------------------------------------------------ |
| menu\_definition | (List\[List\]) New menu definition (in menu definition format) |
| visible          | (bool) control visibility of element                         |

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

Changes some of the settings for the ButtonMenu Element. Must call `Window.Read` or `Window.Finalize` prior

    update(menu_definition, visible=None)


Parameter Descriptions:

| Name             | Meaning                                                      |
| ---------------- | ------------------------------------------------------------ |
| menu\_definition | (List\[List\]) New menu definition (in menu definition format) |
| visible          | (bool) control visibility of element                         |

Canvas Element
--------------

    Canvas(canvas=None,
        background_color=None,
        size=(None, None),
        pad=None,
        key=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        metadata=None)

Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| canvas             | (tk.Canvas) Your own tk.Canvas if you already created it. Leave blank to create a Canvas |
| background\_color  | (str) color of background                                    |
| size               | Tuple\[int,int\] (width in char, height in rows) size in pixels to make canvas |
| pad                | Amount of padding to put around element                      |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element |
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

### TKCanvas

#### property: TKCanvas

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

### tk\_canvas

#### property: tk\_canvas

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


Checkbox Element
----------------

    Checkbox Element - Displays a checkbox and text next to it
    
    Checkbox(text,
        default=False,
        size=(None, None),
        auto_size_text=None,
        font=None,
        background_color=None,
        text_color=None,
        change_submits=False,
        enable_events=False,
        disabled=False,
        key=None,
        pad=None,
        tooltip=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| text              | (str) Text to display next to checkbox                       |
| default           | (bool). Set to True if you want this checkbox initially checked |
| size              | Tuple\[int, int\] (width, height) width = characters-wide, height = rows-high |
| auto\_size\_text  | (bool) if True will size the element to match the length of the text |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| background\_color | (str) color of background                                    |
| text\_color       | (str) color of the text                                      |
| change\_submits   | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events    | (bool) Turns on the element specific events. Checkbox events happen when an item changes |
| disabled          | (bool) set disable state                                     |
| key               | (Any) Used with window.FindElement and with return values to uniquely identify this element |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| tooltip           | (str) text, that will appear when mouse hovers over the element |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Get

Return the current state of this checkbox

`Get()`

| Name       | Meaning                          |
| ---------- | -------------------------------- |
| **return** | (bool) Current state of checkbox |

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

Changes some of the settings for the Checkbox Element. Must call `Window.Read` or `Window.Finalize` prior. Note that changing visibility may cause element to change locations when made visible after invisible

    Update(value=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                             |
| -------- | --------------------------------------------------- |
| value    | (bool) if True checks the checkbox, False clears it |
| disabled | (bool) disable or enable element                    |
| visible  | (bool) control visibility of element                |

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

Return the current state of this checkbox

`get()`

| Name       | Meaning                          |
| ---------- | -------------------------------- |
| **return** | (bool) Current state of checkbox |

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

Changes some of the settings for the Checkbox Element. Must call `Window.Read` or `Window.Finalize` prior. Note that changing visibility may cause element to change locations when made visible after invisible

    update(value=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                             |
| -------- | --------------------------------------------------- |
| value    | (bool) if True checks the checkbox, False clears it |
| disabled | (bool) disable or enable element                    |
| visible  | (bool) control visibility of element                |

Column Element
--------------

    A container element that is used to create a layout within your window's layout
    
    Column(layout,
        background_color=None,
        size=(None, None),
        pad=None,
        scrollable=False,
        vertical_scroll_only=False,
        right_click_menu=None,
        key=None,
        visible=True,
        justification="left",
        element_justification="left",
        metadata=None)


Parameter Descriptions:

| Name                   | Meaning                                                      |
| ---------------------- | ------------------------------------------------------------ |
| layout                 | List\[List\[Element\]\] Layout that will be shown in the Column container |
| background\_color      | (str) color of background of entire Column                   |
| size                   | Tuple\[int, int\] (width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter |
| pad                    | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| scrollable             | (bool) if True then scrollbars will be added to the column   |
| vertical\_scroll\_only | (bool) if Truen then no horizontal scrollbar will be shown   |
| right\_click\_menu     | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| key                    | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| visible                | (bool) set visibility state of the element                   |
| justification          | (str) set justification for the Column itself. Note entire row containing the Column will be affected |
| element\_justification | (str) All elements inside the Column will have this justification 'left', 'right', 'center' are valid values |
| metadata               | (Any) User metadata that can be set to ANYTHING              |

### AddRow

Not recommended user call. Used to add rows of Elements to the Column Element.

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
| **return** | (Column) Used for chaining                   |

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

Changes some of the settings for the Column Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(visible=None)

Parameter Descriptions:

| Name    | Meaning                              |
| ------- | ------------------------------------ |
| visible | (bool) control visibility of element |

### add\_row

Not recommended user call. Used to add rows of Elements to the Column Element.

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
| **return** | (Column) Used for chaining                   |

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

Changes some of the settings for the Column Element. Must call `Window.Read` or `Window.Finalize` prior

    update(visible=None)


Parameter Descriptions:

| Name    | Meaning                              |
| ------- | ------------------------------------ |
| visible | (bool) control visibility of element |

Combo Element
-------------

    ComboBox Element - A combination of a single-line input and a drop-down menu. User can type in their own value or choose from list.
    
    Combo(values,
        default_value=None,
        size=(None, None),
        auto_size_text=None,
        background_color=None,
        text_color=None,
        change_submits=False,
        enable_events=False,
        disabled=False,
        key=None,
        pad=None,
        tooltip=None,
        readonly=False,
        font=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| values            | List\[Any\] values to choose. While displayed as text, the items returned are what the caller supplied, not text |
| default\_value    | (Any) Choice to be displayed as initial value. Must match one of values variable contents |
| size              | Tuple\[int, int\] (width, height) width = characters-wide, height = rows-high |
| auto\_size\_text  | (bool) True if element should be the same size as the contents |
| background\_color | (str) color of background                                    |
| text\_color       | (str) color of the text                                      |
| change\_submits   | (bool) DEPRICATED DO NOT USE. Use `enable_events` instead    |
| enable\_events    | (bool) Turns on the element specific events. Combo event is when a choice is made |
| disabled          | (bool) set disable state for element                         |
| key               | (Any) Used with window.FindElement and with return values to uniquely identify this element |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| tooltip           | (str) text that will appear when mouse hovers over this element |
| readonly          | (bool) make element readonly (user can't change). True means user cannot change |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)

Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Get

Returns the current (right now) value of the Combo. DO NOT USE THIS AS THE NORMAL WAY OF READING A COMBO! You should be using values from your call to window.Read instead. Know what you're doing if you use it.

`Get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Any, None\] Returns the value of what is currently chosen |

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

Changes some of the settings for the Combo Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        values=None,
        set_to_index=None,
        disabled=None,
        readonly=None,
        font=None,
        visible=None)


Parameter Descriptions:

| Name           | Meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| value          | (Any) change which value is current selected hased on new list of previous list of choices |
| values         | List\[Any\] change list of choices                           |
| set\_to\_index | (int) change selection to a particular choice starting with index = 0 |
| disabled       | (bool) disable or enable state of the element                |
| readonly       | (bool) if True make element readonly (user cannot change any choices) |
| font           | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| visible        | (bool) control visibility of element                         |

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

Returns the current (right now) value of the Combo. DO NOT USE THIS AS THE NORMAL WAY OF READING A COMBO! You should be using values from your call to window.Read instead. Know what you're doing if you use it.

`get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Any, None\] Returns the value of what is currently chosen |

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

Changes some of the settings for the Combo Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        values=None,
        set_to_index=None,
        disabled=None,
        readonly=None,
        font=None,
        visible=None)

Parameter Descriptions:

| Name           | Meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| value          | (Any) change which value is current selected hased on new list of previous list of choices |
| values         | List\[Any\] change list of choices                           |
| set\_to\_index | (int) change selection to a particular choice starting with index = 0 |
| disabled       | (bool) disable or enable state of the element                |
| readonly       | (bool) if True make element readonly (user cannot change any choices) |
| font           | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| visible        | (bool) control visibility of element                         |




Graph Element
-------------

    Creates an area for you to draw on.  The MAGICAL property this Element has is that you interact
    with the element using your own coordinate system.  This is an important point!!  YOU define where the location
    is for (0,0).  Want (0,0) to be in the middle of the graph like a math 4-quadrant graph?  No problem!  Set your
    lower left corner to be (-100,-100) and your upper right to be (100,100) and you've got yourself a graph with
    (0,0) at the center.
    One of THE coolest of the Elements.
    You can also use float values. To do so, be sure and set the float_values parameter.
    Mouse click and drag events are possible and return the (x,y) coordinates of the mouse
    Drawing primitives return an "id" that is referenced when you want to operation on that item (e.g. to erase it)
    
    Graph(canvas_size,
        graph_bottom_left,
        graph_top_right,
        background_color=None,
        pad=None,
        change_submits=False,
        drag_submits=False,
        enable_events=False,
        key=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        float_values=False,
        metadata=None)


Parameter Descriptions:

| Name                | Meaning                                                      |
| ------------------- | ------------------------------------------------------------ |
| canvas\_size        | Tuple\[int, int\] (width, height) size of the canvas area in pixels |
| graph\_bottom\_left | Tuple\[int, int\] (x,y) The bottoms left corner of your coordinate system |
| graph\_top\_right   | Tuple\[int, int\] (x,y) The top right corner of your coordinate system |
| background\_color   | (str) background color of the drawing area                   |
| pad                 | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| change\_submits     | (bool) \* DEPRICATED DO NOT USE! Same as enable\_events      |
| drag\_submits       | (bool) if True and Events are enabled for the Graph, will report Events any time the mouse moves while button down |
| enable\_events      | (bool) If True then clicks on the Graph are immediately reported as an event. Use this instead of change\_submits |
| key                 | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| tooltip             | (str) text, that will appear when mouse hovers over the element |
| right\_click\_menu  | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible             | (bool) set visibility state of the element (Default = True)  |
| float\_values       | (bool) If True x,y coordinates are returned as floats, not ints |
| metadata            | (Any) User metadata that can be set to ANYTHING              |

### BringFigureToFront

Changes Z-order of figures on the Graph. Brings the indicated figure to the front of all other drawn figures

    BringFigureToFront(figure)


Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| figure | (int) value returned by tkinter when creating the figure / drawing |

### ButtonPressCallBack

Not a user callable method. Used to get Graph click events. Called by tkinter when button is released

    ButtonPressCallBack(event)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| event | (event) event info from tkinter. Contains the x and y coordinates of a click |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### ButtonReleaseCallBack

Not a user callable method. Used to get Graph click events. Called by tkinter when button is released

    ButtonReleaseCallBack(event)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| event | (event) event info from tkinter. Note not used in this method |

### DeleteFigure

Remove from the Graph the figure represented by id. The id is given to you anytime you call a drawing primitive

    DeleteFigure(id)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| id   | (int) the id returned to you when calling one of the drawing methods |

### DrawArc

Draws different types of arcs. Uses a "bounding box" to define location

    DrawArc(top_left,
        bottom_right,
        extent,
        start_angle,
        style=None,
        arc_color="black")


Parameter Descriptions:

| Name          | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| top\_left     | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the top left point of bounding rectangle |
| bottom\_right | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the bottom right point of bounding rectangle |
| extent        | (float) Andle to end drawing. Used in conjunction with start\_angle |
| start\_angle  | (float) Angle to begin drawing. Used in conjunction with extent |
| style         | (str) Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc', 'first', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter' |
| arc\_color    | (str) color to draw arc with                                 |
|               |                                                              |
| **return**    | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the arc |

### DrawCircle

Draws a circle, cenetered at the location provided. Can set the fill and outline colors

    DrawCircle(center_location,
        radius,
        fill_color=None,
        line_color="black")


Parameter Descriptions:

| Name             | Meaning                                                      |
| ---------------- | ------------------------------------------------------------ |
| center\_location | Union \[Tuple\[int, int\], Tuple\[float, float\]\] Center location using USER'S coordinate system |
| radius           | Union\[int, float\] Radius in user's coordinate values.      |
| fill\_color      | (str) color of the point to draw                             |
| line\_color      | (str) color of the outer line that goes around the circle (sorry, can't set thickness) |
|                  |                                                              |
| **return**       | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the circle |

### DrawImage

Places an image onto your canvas. It's a really important method for this element as it enables so much

    DrawImage(filename=None,
        data=None,
        location=(None, None),
        color="black",
        font=None,
        angle=0)


Parameter Descriptions:

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| filename   | (str) if image is in a file, path and filename for the image. (GIF and PNG only!) |
| data       | Union\[str, bytes\] if image is in Base64 format or raw? format then use instead of filename |
| location   | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the (x,y) location to place image's top left corner |
| color      | (str) text color                                             |
| font       | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| angle      | (float) Angle 0 to 360 to draw the text. Zero represents horizontal text |
|            |                                                              |
| **return** | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the image |

### DrawLine

Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line

    DrawLine(point_from,
        point_to,
        color="black",
        width=1)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>point_from</td><td>Union[Tuple[int, int], Tuple[float, float]] Starting point for line</td></tr><tr class="even"><td>point_to</td><td>Union[Tuple[int, int], Tuple[float, float]] Ending point for line</td></tr><tr class="odd"><td>color</td><td>(str) Color of the line</td></tr><tr class="even"><td>width</td><td>(int) width of line in pixels</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[int, None] id returned from tktiner or None if user closed the window. id is used when you<br />
want to manipulate the line</td></tr></tbody></table>

### DrawOval

Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"

    DrawOval(top_left,
        bottom_right,
        fill_color=None,
        line_color=None)


Parameter Descriptions:

| Name          | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| top\_left     | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the top left point of bounding rectangle |
| bottom\_right | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the bottom right point of bounding rectangle |
| fill\_color   | (str) color of the interrior                                 |
| line\_color   | (str) color of outline of oval                               |
|               |                                                              |
| **return**    | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the oval |

### DrawPoint

Draws a "dot" at the point you specify using the USER'S coordinate system

    DrawPoint(point,
        size=2,
        color="black")


Parameter Descriptions:

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| point      | Union \[Tuple\[int, int\], Tuple\[float, float\]\] Center location using USER'S coordinate system |
| size       | Union\[int, float\] Radius? (Or is it the diameter?) in user's coordinate values. |
| color      | (str) color of the point to draw                             |
|            |                                                              |
| **return** | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the point |

### DrawRectangle

Draw a rectangle given 2 points. Can control the line and fill colors

    DrawRectangle(top_left,
        bottom_right,
        fill_color=None,
        line_color=None,
        line_width=None)


Parameter Descriptions:

| Name          | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| top\_left     | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the top left point of rectangle |
| bottom\_right | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the bottom right point of rectangle |
| fill\_color   | (str) color of the interior                                  |
| line\_color   | (str) color of outline                                       |
|               |                                                              |
| **return**    | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the rectangle |

### DrawText

Draw some text on your graph. This is how you label graph number lines for example

    DrawText(text,
        location,
        color="black",
        font=None,
        angle=0,
        text_location="center")

Parameter Descriptions:

| Name           | Meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| text           | (str) text to display                                        |
| location       | Union\[Tuple\[int, int\], Tuple\[float, float\]\] location to place first letter |
| color          | (str) text color                                             |
| font           | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| angle          | (float) Angle 0 to 360 to draw the text. Zero represents horizontal text |
| text\_location | (enum) "anchor" location for the text. Values start with TEXT\_LOCATION\_ |
|                |                                                              |
| **return**     | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the text |

### Erase

Erase the Graph - Removes all figures previously "drawn" using the Graph methods (e.g. DrawText)

    Erase()

### MotionCallBack

Not a user callable method. Used to get Graph mouse motion events. Called by tkinter when mouse moved

    MotionCallBack(event)

Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| event | (event) event info from tkinter. Contains the x and y coordinates of a mouse |

### Move

Moves the entire drawing area (the canvas) by some delta from the current position. Units are indicated in your coordinate system indicated number of ticks in your coordinate system

    Move(x_direction, y_direction)


Parameter Descriptions:

| Name         | Meaning                                                      |
| ------------ | ------------------------------------------------------------ |
| x\_direction | Union\[int, float\] how far to move in the "X" direction in your coordinates |
| y\_direction | Union\[int, float\] how far to move in the "Y" direction in your coordinates |

### MoveFigure

Moves a previously drawn figure using a "delta" from current position

    MoveFigure(figure,
        x_direction,
        y_direction)


Parameter Descriptions:

| Name         | Meaning                                                      |
| ------------ | ------------------------------------------------------------ |
| figure       | (id) Previously obtained figure-id. These are returned from all Draw methods |
| x\_direction | Union\[int, float\] delta to apply to position in the X direction |
| y\_direction | Union\[int, float\] delta to apply to position in the Y direction |

### RelocateFigure

Move a previously made figure to an arbitrary (x,y) location. This differs from the Move methods because it uses absolute coordinates versus relative for Move

    RelocateFigure(figure,
        x,
        y)


Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| figure | (id) Previously obtained figure-id. These are returned from all Draw methods |
| x      | Union\[int, float\] location on X axis (in user coords) to move the upper left corner of the figure |
| y      | Union\[int, float\] location on Y axis (in user coords) to move the upper left corner of the figure |

### SendFigureToBack

Changes Z-order of figures on the Graph. Sends the indicated figure to the back of all other drawn figures

    SendFigureToBack(figure)


Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| figure | (int) value returned by tkinter when creating the figure / drawing |

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

### TKCanvas

#### property: TKCanvas

### Update

Changes some of the settings for the Graph Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(background_color=None, visible=None)


Parameter Descriptions:

| Name              | Meaning                              |
| ----------------- | ------------------------------------ |
| background\_color | color of background                  |
| visible           | (bool) control visibility of element |

### bring\_figure\_to\_front

Changes Z-order of figures on the Graph. Brings the indicated figure to the front of all other drawn figures

    bring_figure_to_front(figure)


Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| figure | (int) value returned by tkinter when creating the figure / drawing |

### button\_press\_call\_back

Not a user callable method. Used to get Graph click events. Called by tkinter when button is released

    button_press_call_back(event)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| event | (event) event info from tkinter. Contains the x and y coordinates of a click |

### button\_rebound\_callback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    button_rebound_callback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### button\_release\_call\_back

Not a user callable method. Used to get Graph click events. Called by tkinter when button is released

    button_release_call_back(event)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| event | (event) event info from tkinter. Note not used in this method |

### delete\_figure

Remove from the Graph the figure represented by id. The id is given to you anytime you call a drawing primitive

    delete_figure(id)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| id   | (int) the id returned to you when calling one of the drawing methods |

### draw\_arc

Draws different types of arcs. Uses a "bounding box" to define location

    draw_arc(top_left,
        bottom_right,
        extent,
        start_angle,
        style=None,
        arc_color="black")


Parameter Descriptions:

| Name          | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| top\_left     | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the top left point of bounding rectangle |
| bottom\_right | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the bottom right point of bounding rectangle |
| extent        | (float) Andle to end drawing. Used in conjunction with start\_angle |
| start\_angle  | (float) Angle to begin drawing. Used in conjunction with extent |
| style         | (str) Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc', 'first', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter' |
| arc\_color    | (str) color to draw arc with                                 |
|               |                                                              |
| **return**    | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the arc |

### draw\_circle

Draws a circle, cenetered at the location provided. Can set the fill and outline colors

    draw_circle(center_location,
        radius,
        fill_color=None,
        line_color="black")


Parameter Descriptions:

| Name             | Meaning                                                      |
| ---------------- | ------------------------------------------------------------ |
| center\_location | Union \[Tuple\[int, int\], Tuple\[float, float\]\] Center location using USER'S coordinate system |
| radius           | Union\[int, float\] Radius in user's coordinate values.      |
| fill\_color      | (str) color of the point to draw                             |
| line\_color      | (str) color of the outer line that goes around the circle (sorry, can't set thickness) |
|                  |                                                              |
| **return**       | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the circle |

### draw\_image

Places an image onto your canvas. It's a really important method for this element as it enables so much

    draw_image(filename=None,
        data=None,
        location=(None, None),
        color="black",
        font=None,
        angle=0)


Parameter Descriptions:

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| filename   | (str) if image is in a file, path and filename for the image. (GIF and PNG only!) |
| data       | Union\[str, bytes\] if image is in Base64 format or raw? format then use instead of filename |
| location   | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the (x,y) location to place image's top left corner |
| color      | (str) text color                                             |
| font       | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| angle      | (float) Angle 0 to 360 to draw the text. Zero represents horizontal text |
|            |                                                              |
| **return** | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the image |

### draw\_line

Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line

    draw_line(point_from,
        point_to,
        color="black",
        width=1)


Parameter Descriptions:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Name</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td>point_from</td><td>Union[Tuple[int, int], Tuple[float, float]] Starting point for line</td></tr><tr class="even"><td>point_to</td><td>Union[Tuple[int, int], Tuple[float, float]] Ending point for line</td></tr><tr class="odd"><td>color</td><td>(str) Color of the line</td></tr><tr class="even"><td>width</td><td>(int) width of line in pixels</td></tr><tr class="odd"><td></td><td></td></tr><tr class="even"><td><strong>return</strong></td><td>Union[int, None] id returned from tktiner or None if user closed the window. id is used when you<br />
want to manipulate the line</td></tr></tbody></table>

### draw\_oval

Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"

    draw_oval(top_left,
        bottom_right,
        fill_color=None,
        line_color=None)


Parameter Descriptions:

| Name          | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| top\_left     | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the top left point of bounding rectangle |
| bottom\_right | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the bottom right point of bounding rectangle |
| fill\_color   | (str) color of the interrior                                 |
| line\_color   | (str) color of outline of oval                               |
|               |                                                              |
| **return**    | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the oval |

### draw\_point

Draws a "dot" at the point you specify using the USER'S coordinate system

    draw_point(point,
        size=2,
        color="black")


Parameter Descriptions:

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| point      | Union \[Tuple\[int, int\], Tuple\[float, float\]\] Center location using USER'S coordinate system |
| size       | Union\[int, float\] Radius? (Or is it the diameter?) in user's coordinate values. |
| color      | (str) color of the point to draw                             |
|            |                                                              |
| **return** | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the point |

### draw\_rectangle

Draw a rectangle given 2 points. Can control the line and fill colors

    draw_rectangle(top_left,
        bottom_right,
        fill_color=None,
        line_color=None,
        line_width=None)

Parameter Descriptions:

| Name          | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| top\_left     | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the top left point of rectangle |
| bottom\_right | Union\[Tuple\[int, int\], Tuple\[float, float\]\] the bottom right point of rectangle |
| fill\_color   | (str) color of the interior                                  |
| line\_color   | (str) color of outline                                       |
|               |                                                              |
| **return**    | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the rectangle |

### draw\_text

Draw some text on your graph. This is how you label graph number lines for example

    draw_text(text,
        location,
        color="black",
        font=None,
        angle=0,
        text_location="center")

Parameter Descriptions:

| Name           | Meaning                                                      |
| -------------- | ------------------------------------------------------------ |
| text           | (str) text to display                                        |
| location       | Union\[Tuple\[int, int\], Tuple\[float, float\]\] location to place first letter |
| color          | (str) text color                                             |
| font           | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| angle          | (float) Angle 0 to 360 to draw the text. Zero represents horizontal text |
| text\_location | (enum) "anchor" location for the text. Values start with TEXT\_LOCATION\_ |
|                |                                                              |
| **return**     | Union\[int, None\] id returned from tkinter that you'll need if you want to manipulate the text |

### erase

Erase the Graph - Removes all figures previously "drawn" using the Graph methods (e.g. DrawText)

    erase()


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


### motion\_call\_back

Not a user callable method. Used to get Graph mouse motion events. Called by tkinter when mouse moved

    motion_call_back(event)


Parameter Descriptions:

| Name  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| event | (event) event info from tkinter. Contains the x and y coordinates of a mouse |

### move

Moves the entire drawing area (the canvas) by some delta from the current position. Units are indicated in your coordinate system indicated number of ticks in your coordinate system

    move(x_direction, y_direction)


Parameter Descriptions:

| Name         | Meaning                                                      |
| ------------ | ------------------------------------------------------------ |
| x\_direction | Union\[int, float\] how far to move in the "X" direction in your coordinates |
| y\_direction | Union\[int, float\] how far to move in the "Y" direction in your coordinates |

### move\_figure

Moves a previously drawn figure using a "delta" from current position

    move_figure(figure,
        x_direction,
        y_direction)


Parameter Descriptions:

| Name         | Meaning                                                      |
| ------------ | ------------------------------------------------------------ |
| figure       | (id) Previously obtained figure-id. These are returned from all Draw methods |
| x\_direction | Union\[int, float\] delta to apply to position in the X direction |
| y\_direction | Union\[int, float\] delta to apply to position in the Y direction |

### relocate\_figure

Move a previously made figure to an arbitrary (x,y) location. This differs from the Move methods because it uses absolute coordinates versus relative for Move

    relocate_figure(figure,
        x,
        y)

Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| figure | (id) Previously obtained figure-id. These are returned from all Draw methods |
| x      | Union\[int, float\] location on X axis (in user coords) to move the upper left corner of the figure |
| y      | Union\[int, float\] location on Y axis (in user coords) to move the upper left corner of the figure |

### send\_figure\_to\_back

Changes Z-order of figures on the Graph. Sends the indicated figure to the back of all other drawn figures

    send_figure_to_back(figure)

Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| figure | (int) value returned by tkinter when creating the figure / drawing |

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

### tk\_canvas

#### property: tk\_canvas

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Graph Element. Must call `Window.Read` or `Window.Finalize` prior

    update(background_color=None, visible=None)


Parameter Descriptions:

| Name              | Meaning                              |
| ----------------- | ------------------------------------ |
| background\_color | color of background                  |
| visible           | (bool) control visibility of element |




Listbox Element
---------------

    A List Box.  Provide a list of values for the user to choose one or more of.   Returns a list of selected rows
    when a window.Read() is executed.
    
    Listbox(values,
        default_values=None,
        select_mode=None,
        change_submits=False,
        enable_events=False,
        bind_return_key=False,
        size=(None, None),
        disabled=False,
        auto_size_text=None,
        font=None,
        no_scrollbar=False,
        background_color=None,
        text_color=None,
        key=None,
        pad=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| values             | List\[Any\] list of values to display. Can be any type including mixed types as long as they have **str** method |
| default\_values    | List\[Any\] which values should be initially selected        |
| select\_mode       | \[enum\] Select modes are used to determine if only 1 item can be selected or multiple and how they can be selected. Valid choices begin with "LISTBOX\_SELECT\_MODE\_" and include: LISTBOX\_SELECT\_MODE\_SINGLE LISTBOX\_SELECT\_MODE\_MULTIPLE LISTBOX\_SELECT\_MODE\_BROWSE LISTBOX\_SELECT\_MODE\_EXTENDED |
| change\_submits    | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events     | (bool) Turns on the element specific events. Listbox generates events when an item is clicked |
| bind\_return\_key  | (bool) If True, then the return key will cause a the Listbox to generate an event |
| size               | Tuple(int, int) (width, height) width = characters-wide, height = rows-high |
| disabled           | (bool) set disable state for element                         |
| auto\_size\_text   | (bool) True if element should be the same size as the contents |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| background\_color  | (str) color of background                                    |
| text\_color        | (str) color of the text                                      |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element |
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

### GetIndexes

Returns the items currently selected as a list of indexes

`GetIndexes()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | List\[int\] A list of offsets into values that is currently selected |

### GetListValues

Returns list of Values provided by the user in the user's format

`GetListValues()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | List\[Any\]. List of values. Can be any / mixed types -\> \[\] |

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

### SetValue

Set listbox highlighted choices

    SetValue(values)


Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| values | List\[Any\] new values to choose based on previously set values |

### Update

Changes some of the settings for the Listbox Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(values=None,
        disabled=None,
        set_to_index=None,
        scroll_to_index=None,
        visible=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| values            | List\[Any\] new list of choices to be shown to user          |
| disabled          | (bool) disable or enable state of the element                |
| set\_to\_index    | Union\[int, list, tuple\] highlights the item(s) indicated. If parm is an int one entry will be set. If is a list, then each entry in list is highlighted |
| scroll\_to\_index | (int) scroll the listbox so that this index is the first shown |
| visible           | (bool) control visibility of element                         |

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

### get\_indexes

Returns the items currently selected as a list of indexes

`get_indexes()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | List\[int\] A list of offsets into values that is currently selected |

### get\_list\_values

Returns list of Values provided by the user in the user's format

`get_list_values()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | List\[Any\]. List of values. Can be any / mixed types -\> \[\] |

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

### set\_value

Set listbox highlighted choices

    set_value(values)


Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| values | List\[Any\] new values to choose based on previously set values |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Listbox Element. Must call `Window.Read` or `Window.Finalize` prior

    update(values=None,
        disabled=None,
        set_to_index=None,
        scroll_to_index=None,
        visible=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| values            | List\[Any\] new list of choices to be shown to user          |
| disabled          | (bool) disable or enable state of the element                |
| set\_to\_index    | Union\[int, list, tuple\] highlights the item(s) indicated. If parm is an int one entry will be set. If is a list, then each entry in list is highlighted |
| scroll\_to\_index | (int) scroll the listbox so that this index is the first shown |
| visible           | (bool) control visibility of element                         |

Menu Element
------------

    Menu Element is the Element that provides a Menu Bar that goes across the top of the window, just below titlebar.
    Here is an example layout.  The "&" are shortcut keys ALT+key.
    Is a List of -  "Item String" + List
    Where Item String is what will be displayed on the Menubar itself.
    The List that follows the item represents the items that are shown then Menu item is clicked
    Notice how an "entry" in a mennu can be a list which means it branches out and shows another menu, etc. (resursive)
    menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
                ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Debugger', ['Popout', 'Launch Debugger']],
                ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]
    Finally, "keys" can be added to entries so make them unique.  The "Save" entry has a key associated with it. You
    can see it has a "::" which signifies the beginning of a key.  The user will not see the key portion when the
    menu is shown.  The key portion is returned as part of the event.
    
    Menu(menu_definition,
        background_color=None,
        size=(None, None),
        tearoff=False,
        pad=None,
        key=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| menu\_definition  | List\[List\[Tuple\[str, List\[str\]\]\]                      |
| background\_color | (str) color of the background                                |
| size              | Tuple\[int, int\] Not used in the tkinter port               |
| tearoff           | (bool) if True, then can tear the menu off from the window ans use as a floating window. Very cool effect |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key               | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

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

Update a menubar - can change the menu definition and visibility. The entire menu has to be specified

    Update(menu_definition=None, visible=None)


Parameter Descriptions:

| Name             | Meaning                                 |
| ---------------- | --------------------------------------- |
| menu\_definition | List\[List\[Tuple\[str, List\[str\]\]\] |
| visible          | (bool) control visibility of element    |

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

Update a menubar - can change the menu definition and visibility. The entire menu has to be specified

    update(menu_definition=None, visible=None)


Parameter Descriptions:

| Name             | Meaning                                 |
| ---------------- | --------------------------------------- |
| menu\_definition | List\[List\[Tuple\[str, List\[str\]\]\] |
| visible          | (bool) control visibility of element    |



OptionMenu Element
------------------

    Option Menu is an Element available ONLY on the tkinter port of PySimpleGUI.  It's is a widget that is unique
    to tkinter.  However, it looks much like a ComboBox.  Instead of an arrow to click to pull down the list of
    choices, another little graphic is shown on the widget to indicate where you click.  After clicking to activate,
    it looks like a Combo Box that you scroll to select a choice.
    
    OptionMenu(values,
        default_value=None,
        size=(None, None),
        disabled=False,
        auto_size_text=None,
        background_color=None,
        text_color=None,
        key=None,
        pad=None,
        tooltip=None,
        visible=True,
        metadata=None)

Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| values            | List\[Any\] Values to be displayed                           |
| default\_value    | (Any) the value to choose by default                         |
| size              | Tuple\[int, int\] (width, height) size in characters (wide) and rows (high) |
| disabled          | (bool) control enabled / disabled                            |
| auto\_size\_text  | (bool) True if size of Element should match the contents of the items |
| background\_color | (str) color of background                                    |
| text\_color       | (str) color of the text                                      |
| key               | (Any) Used with window.FindElement and with return values to uniquely identify this element |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| tooltip           | (str) text that will appear when mouse hovers over this element |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

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

Changes some of the settings for the OptionMenu Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        values=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                       |
| -------- | --------------------------------------------- |
| value    | (Any) the value to choose by default          |
| values   | List\[Any\] Values to be displayed            |
| disabled | (bool) disable or enable state of the element |
| visible  | (bool) control visibility of element          |

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

Changes some of the settings for the OptionMenu Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        values=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                       |
| -------- | --------------------------------------------- |
| value    | (Any) the value to choose by default          |
| values   | List\[Any\] Values to be displayed            |
| disabled | (bool) disable or enable state of the element |
| visible  | (bool) control visibility of element          |

Output Element
--------------

    Output Element - a multi-lined text area where stdout and stderr are re-routed to.
    
    Output(size=(None, None),
        background_color=None,
        text_color=None,
        pad=None,
        font=None,
        tooltip=None,
        key=None,
        right_click_menu=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name               | Meaning                                                      |
| ------------------ | ------------------------------------------------------------ |
| size               | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high       |
| background\_color  | (str) color of background                                    |
| text\_color        | (str) color of the text                                      |
| pad                | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| font               | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| tooltip            | (str) text, that will appear when mouse hovers over the element |
| key                | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
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

Returns the current contents of the output. Similar to Get method other Elements

`Get()`

| Name       | Meaning                               |
| ---------- | ------------------------------------- |
| **return** | (str) the current value of the output |

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

### TKOut

#### property: TKOut

### Update

Changes some of the settings for the Output Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None, visible=None)


Parameter Descriptions:

| Name    | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| value   | (str) string that will replace current contents of the output area |
| visible | (bool) control visibility of element                         |

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

### tk\_out

#### property: tk\_out

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Output Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None, visible=None)


Parameter Descriptions:

| Name    | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| value   | (str) string that will replace current contents of the output area |
| visible | (bool) control visibility of element                         |

Pane Element
------------

    A sliding Pane that is unique to tkinter.  Uses Columns to create individual panes
    
    Pane(pane_list,
        background_color=None,
        size=(None, None),
        pad=None,
        orientation="vertical",
        show_handle=True,
        relief="raised",
        handle_size=None,
        border_width=None,
        key=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| pane\_list        | List\[Column\] Must be a list of Column Elements. Each Column supplied becomes one pane that's shown |
| background\_color | (str) color of background                                    |
| size              | Tuple\[int, int\] (w,h) w=characters-wide, h=rows-high How much room to reserve for the Pane |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| orientation       | (str) 'horizontal' or 'vertical' or ('h' or 'v'). Direction the Pane should slide |
| show\_handle      | (bool) if True, the handle is drawn that makes it easier to grab and slide |
| relief            | (enum) relief style. Values are same as other elements that use relief values. RELIEF\_RAISED RELIEF\_SUNKEN RELIEF\_FLAT RELIEF\_RIDGE RELIEF\_GROOVE RELIEF\_SOLID |
| handle\_size      | (int) Size of the handle in pixels                           |
| border\_width     | (int) width of border around element in pixels               |
| key               | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

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

Changes some of the settings for the Pane Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(visible=None)


Parameter Descriptions:

| Name    | Meaning                              |
| ------- | ------------------------------------ |
| visible | (bool) control visibility of element |

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

Changes some of the settings for the Pane Element. Must call `Window.Read` or `Window.Finalize` prior

    update(visible=None)


Parameter Descriptions:

| Name    | Meaning                              |
| ------- | ------------------------------------ |
| visible | (bool) control visibility of element |

ProgressBar Element
-------------------

    Progress Bar Element - Displays a colored bar that is shaded as progress of some operation is made
    
    ProgressBar(max_value,
        orientation=None,
        size=(None, None),
        auto_size_text=None,
        bar_color=(None, None),
        style=None,
        border_width=None,
        relief=None,
        key=None,
        pad=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name             | Meaning                                                      |
| ---------------- | ------------------------------------------------------------ |
| max\_value       | (int) max value of progressbar                               |
| orientation      | (str) 'horizontal' or 'vertical'                             |
| size             | Tuple\[int, int\] Size of the bar. If horizontal (chars wide, pixels high), vert (pixels wide, rows high) |
| auto\_size\_text | (bool) Not sure why this is here                             |
| bar\_color       | Tuple\[str, str\] The 2 colors that make up a progress bar. One is the background, the other is the bar |
| style            | (str) Progress bar style defined as one of these 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative' |
| border\_width    | (int) The amount of pixels that go around the outside of the bar |
| relief           | (str) relief style. Values are same as progress meter relief values. Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID` (Default value = DEFAULT\_PROGRESS\_BAR\_RELIEF) |
| key              | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| pad              | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| visible          | (bool) set visibility state of the element                   |
| metadata         | (Any) User metadata that can be set to ANYTHING              |

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

Changes some of the settings for the ProgressBar Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(visible=None)


Parameter Descriptions:

| Name    | Meaning                              |
| ------- | ------------------------------------ |
| visible | (bool) control visibility of element |

### UpdateBar

Change what the bar shows by changing the current count and optionally the max count

    UpdateBar(current_count, max=None)


Parameter Descriptions:

| Name           | Meaning                      |
| -------------- | ---------------------------- |
| current\_count | (int) sets the current value |
| max            | (int) changes the max value  |

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

Changes some of the settings for the ProgressBar Element. Must call `Window.Read` or `Window.Finalize` prior

    update(visible=None)


Parameter Descriptions:

| Name    | Meaning                              |
| ------- | ------------------------------------ |
| visible | (bool) control visibility of element |

### update\_bar

Change what the bar shows by changing the current count and optionally the max count

    update_bar(current_count, max=None)


Parameter Descriptions:

| Name           | Meaning                      |
| -------------- | ---------------------------- |
| current\_count | (int) sets the current value |
| max            | (int) changes the max value  |

Radio Element
-------------

    Radio Button Element - Used in a group of other Radio Elements to provide user with ability to select only
    1 choice in a list of choices.
    
    Radio(text,
        group_id,
        default=False,
        disabled=False,
        size=(None, None),
        auto_size_text=None,
        background_color=None,
        text_color=None,
        font=None,
        key=None,
        pad=None,
        tooltip=None,
        change_submits=False,
        enable_events=False,
        visible=True,
        metadata=None)

Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| text              | (str) Text to display next to button                         |
| group\_id         | (Any) Groups together multiple Radio Buttons. Any type works |
| default           | (bool). Set to True for the one element of the group you want initially selected |
| disabled          | (bool) set disable state                                     |
| size              | Tuple\[int, int\] (width, height) width = characters-wide, height = rows-high |
| auto\_size\_text  | (bool) if True will size the element to match the length of the text |
| background\_color | (str) color of background                                    |
| text\_color       | (str) color of the text                                      |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| key               | (Any) Used with window.FindElement and with return values to uniquely identify this element |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| tooltip           | (str) text, that will appear when mouse hovers over the element |
| change\_submits   | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events    | (bool) Turns on the element specific events. Radio Button events happen when an item is selected |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Get

A snapshot of the value of Radio Button -\> (bool)

`Get()`

| Name       | Meaning                                      |
| ---------- | -------------------------------------------- |
| **return** | (bool) True if this radio button is selected |

### ResetGroup

Sets all Radio Buttons in the group to not selected

    ResetGroup()


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

Changes some of the settings for the Radio Button Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| value    | (bool) if True change to selected and set others in group to unselected |
| disabled | (bool) disable or enable state of the element                |
| visible  | (bool) control visibility of element                         |

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

A snapshot of the value of Radio Button -\> (bool)

`get()`

| Name       | Meaning                                      |
| ---------- | -------------------------------------------- |
| **return** | (bool) True if this radio button is selected |

### get\_size

Return the size of an element in Pixels. Care must be taken as some elements use characters to specify their size but will return pixels when calling this get\_size method.

`get_size()`

| Name       | Meaning                                          |
| ---------- | ------------------------------------------------ |
| **return** | Tuple\[int, int\] - Width, Height of the element |

### hide\_row

Hide the entire row an Element is located on. Use this if you must have all space removed when you are hiding an element, including the row container

    hide_row()


### reset\_group

Sets all Radio Buttons in the group to not selected

    reset_group()


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

Changes some of the settings for the Radio Button Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| value    | (bool) if True change to selected and set others in group to unselected |
| disabled | (bool) disable or enable state of the element                |
| visible  | (bool) control visibility of element                         |

Slider Element
--------------

    A slider, horizontal or vertical
    
    Slider(range=(None, None),
        default_value=None,
        resolution=None,
        tick_interval=None,
        orientation=None,
        disable_number_display=False,
        border_width=None,
        relief=None,
        change_submits=False,
        enable_events=False,
        disabled=False,
        size=(None, None),
        font=None,
        background_color=None,
        text_color=None,
        key=None,
        pad=None,
        tooltip=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name                     | Meaning                                                      |
| ------------------------ | ------------------------------------------------------------ |
| range                    | Union\[Tuple\[int, int\], Tuple\[float, float\]\] slider's range (min value, max value) |
| default\_value           | Union\[int, float\] starting value for the slider            |
| resolution               | Union\[int, float\] the smallest amount the slider can be moved |
| tick\_interval           | Union\[int, float\] how often a visible tick should be shown next to slider |
| orientation              | (str) 'horizontal' or 'vertical' ('h' or 'v' also work)      |
| disable\_number\_display | (bool) if True no number will be displayed by the Slider Element |
| border\_width            | (int) width of border around element in pixels               |
| relief                   | (enum) relief style. RELIEF\_RAISED RELIEF\_SUNKEN RELIEF\_FLAT RELIEF\_RIDGE RELIEF\_GROOVE RELIEF\_SOLID |
| change\_submits          | (bool) \* DEPRICATED DO NOT USE! Same as enable\_events      |
| enable\_events           | (bool) If True then moving the slider will generate an Event |
| disabled                 | (bool) set disable state for element                         |
| size                     | Tuple\[int, int\] (width in characters, height in rows)      |
| font                     | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| background\_color        | (str) color of slider's background                           |
| text\_color              | (str) color of the slider's text                             |
| key                      | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| pad                      | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| tooltip                  | (str) text, that will appear when mouse hovers over the element |
| visible                  | (bool) set visibility state of the element                   |
| metadata                 | (Any) User metadata that can be set to ANYTHING              |

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

Changes some of the settings for the Slider Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        range=(None, None),
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| value    | Union\[int, float\] sets current slider value                |
| range    | Union\[Tuple\[int, int\], Tuple\[float, float\] Sets a new range for slider |
| disabled | (bool) disable or enable state of the element                |
| visible  | (bool) control visibility of element                         |

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

Changes some of the settings for the Slider Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        range=(None, None),
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                                      |
| -------- | ------------------------------------------------------------ |
| value    | Union\[int, float\] sets current slider value                |
| range    | Union\[Tuple\[int, int\], Tuple\[float, float\] Sets a new range for slider |
| disabled | (bool) disable or enable state of the element                |
| visible  | (bool) control visibility of element                         |

Spin Element
------------

    A spinner with up/down buttons and a single line of text. Choose 1 values from list
    
    Spin(values,
        initial_value=None,
        disabled=False,
        change_submits=False,
        enable_events=False,
        size=(None, None),
        auto_size_text=None,
        font=None,
        background_color=None,
        text_color=None,
        key=None,
        pad=None,
        tooltip=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| values            | List\[Any\] List of valid values                             |
| initial\_value    | (Any) Initial item to show in window. Choose from list of values supplied |
| disabled          | (bool) set disable state                                     |
| change\_submits   | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events    | (bool) Turns on the element specific events. Spin events happen when an item changes |
| size              | Tuple\[int, int\] (width, height) width = characters-wide, height = rows-high |
| auto\_size\_text  | (bool) if True will size the element to match the length of the text |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| background\_color | (str) color of background                                    |
| text\_color       | (str) color of the text                                      |
| key               | (Any) Used with window.FindElement and with return values to uniquely identify this element |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| tooltip           | (str) text, that will appear when mouse hovers over the element |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Get

Return the current chosen value showing in spinbox. This value will be the same as what was provided as list of choices. If list items are ints, then the item returned will be an int (not a string)

`Get()`

| Name       | Meaning                           |
| ---------- | --------------------------------- |
| **return** | (Any) The currently visible entry |

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

Changes some of the settings for the Spin Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(value=None,
        values=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                          |
| -------- | ------------------------------------------------ |
| value    | (Any) set the current value from list of choices |
| values   | List\[Any\] set available choices                |
| disabled | (bool) disable or enable state of the element    |
| visible  | (bool) control visibility of element             |

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

Return the current chosen value showing in spinbox. This value will be the same as what was provided as list of choices. If list items are ints, then the item returned will be an int (not a string)

`get()`

| Name       | Meaning                           |
| ---------- | --------------------------------- |
| **return** | (Any) The currently visible entry |

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

Changes some of the settings for the Spin Element. Must call `Window.Read` or `Window.Finalize` prior

    update(value=None,
        values=None,
        disabled=None,
        visible=None)


Parameter Descriptions:

| Name     | Meaning                                          |
| -------- | ------------------------------------------------ |
| value    | (Any) set the current value from list of choices |
| values   | List\[Any\] set available choices                |
| disabled | (bool) disable or enable state of the element    |
| visible  | (bool) control visibility of element             |

StatusBar Element
-----------------

    A StatusBar Element creates the sunken text-filled strip at the bottom. Many Windows programs have this line
    
    StatusBar(text,
        size=(None, None),
        auto_size_text=None,
        click_submits=None,
        enable_events=False,
        relief="sunken",
        font=None,
        text_color=None,
        background_color=None,
        justification=None,
        pad=None,
        key=None,
        tooltip=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name              | Meaning                                                      |
| ----------------- | ------------------------------------------------------------ |
| text              | (str) Text that is to be displayed in the widget             |
| size              | Tuple\[(int), (int)\] (w,h) w=characters-wide, h=rows-high   |
| auto\_size\_text  | (bool) True if size should fit the text length               |
| click\_submits    | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events    | (bool) Turns on the element specific events. StatusBar events occur when the bar is clicked |
| relief            | (enum) relief style. Values are same as progress meter relief values. Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID` |
| font              | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| text\_color       | (str) color of the text                                      |
| background\_color | (str) color of background                                    |
| justification     | (str) how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center` |
| pad               | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key               | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| tooltip           | (str) text, that will appear when mouse hovers over the element |
| visible           | (bool) set visibility state of the element                   |
| metadata          | (Any) User metadata that can be set to ANYTHING              |

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

Changes some of the settings for the Status Bar Element. Must call `Window.Read` or `Window.Finalize` prior

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

Changes some of the settings for the Status Bar Element. Must call `Window.Read` or `Window.Finalize` prior

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

Tab Element
-----------

    Tab Element is another "Container" element that holds a layout and displays a tab with text. Used with TabGroup only
    Tabs are never placed directly into a layout.  They are always "Contained" in a TabGroup layout
    
    Tab(title,
        layout,
        title_color=None,
        background_color=None,
        font=None,
        pad=None,
        disabled=False,
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
| title                  | (str) text to show on the tab                                |
| layout                 | List\[List\[Element\]\] The element layout that will be shown in the tab |
| title\_color           | (str) color of the tab text (note not currently working on tkinter) |
| background\_color      | (str) color of background of the entire layout               |
| font                   | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| pad                    | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| disabled               | (bool) If True button will be created disabled               |
| border\_width          | (int) width of border around element in pixels               |
| key                    | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| tooltip                | (str) text, that will appear when mouse hovers over the element |
| right\_click\_menu     | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible                | (bool) set visibility state of the element                   |
| element\_justification | (str) All elements inside the Tab will have this justification 'left', 'right', 'center' are valid values |
| metadata               | (Any) User metadata that can be set to ANYTHING              |

### AddRow

Not recommended use call. Used to add rows of Elements to the Frame Element.

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

Not user callable. Use layout parameter instead. Creates the layout using the supplied rows of Elements

    Layout(rows)


Parameter Descriptions:

| Name       | Meaning                                  |
| ---------- | ---------------------------------------- |
| rows       | List\[List\[Element\]\] The list of rows |
|            |                                          |
| **return** | (Tab) used for chaining                  |

### Select

Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read first!

    Select()


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

Changes some of the settings for the Tab Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(disabled=None, visible=None)


Parameter Descriptions:

| Name     | Meaning                                       |
| -------- | --------------------------------------------- |
| disabled | (bool) disable or enable state of the element |
| visible  | (bool) control visibility of element          |

### add\_row

Not recommended use call. Used to add rows of Elements to the Frame Element.

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

Not user callable. Use layout parameter instead. Creates the layout using the supplied rows of Elements

    layout(rows)


Parameter Descriptions:

| Name       | Meaning                                  |
| ---------- | ---------------------------------------- |
| rows       | List\[List\[Element\]\] The list of rows |
|            |                                          |
| **return** | (Tab) used for chaining                  |

### select

Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read first!

    select()


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

Changes some of the settings for the Tab Element. Must call `Window.Read` or `Window.Finalize` prior

    update(disabled=None, visible=None)


Parameter Descriptions:

| Name     | Meaning                                       |
| -------- | --------------------------------------------- |
| disabled | (bool) disable or enable state of the element |
| visible  | (bool) control visibility of element          |

TabGroup Element
----------------

    TabGroup Element groups together your tabs into the group of tabs you see displayed in your window
    
    TabGroup(layout,
        tab_location=None,
        title_color=None,
        selected_title_color=None,
        background_color=None,
        font=None,
        change_submits=False,
        enable_events=False,
        pad=None,
        border_width=None,
        theme=None,
        key=None,
        tooltip=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name                   | Meaning                                                      |
| ---------------------- | ------------------------------------------------------------ |
| layout                 | List\[List\[Tab\]\] Layout of Tabs. Different than normal layouts. ALL Tabs should be on first row |
| tab\_location          | (str) location that tabs will be displayed. Choices are left, right, top, bottom, lefttop, leftbottom, righttop, rightbottom, bottomleft, bottomright, topleft, topright |
| title\_color           | (str) color of text on tabs                                  |
| selected\_title\_color | (str) color of tab when it is selected                       |
| background\_color      | (str) color of background of tabs                            |
| font                   | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| change\_submits        | (bool) \* DEPRICATED DO NOT USE! Same as enable\_events      |
| enable\_events         | (bool) If True then switching tabs will generate an Event    |
| pad                    | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| border\_width          | (int) width of border around element in pixels               |
| theme                  | (enum) DEPRICATED - You can only specify themes using set options or when window is created. It's not possible to do it on an element basis |
| key                    | (any) Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
| tooltip                | (str) text, that will appear when mouse hovers over the element |
| visible                | (bool) set visibility state of the element                   |
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

### FindKeyFromTabName

Searches through the layout to find the key that matches the text on the tab. Implies names should be unique

    FindKeyFromTabName(tab_name)


Parameter Descriptions:

| Name       | Meaning                                                    |
| ---------- | ---------------------------------------------------------- |
| tab\_name  |                                                            |
|            |                                                            |
| **return** | Union\[key, None\] Returns the key or None if no key found |

### Get

Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on the tab if no key is defined. Returns None if an error occurs. Note that this is exactly the same data that would be returned from a call to Window.Read. Are you sure you are using this method correctly?

`Get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Any, None\] The key of the currently selected tab or the tab's text if it has no key |

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

### find\_key\_from\_tab\_name

Searches through the layout to find the key that matches the text on the tab. Implies names should be unique

    find_key_from_tab_name(tab_name)


Parameter Descriptions:

| Name       | Meaning                                                    |
| ---------- | ---------------------------------------------------------- |
| tab\_name  |                                                            |
|            |                                                            |
| **return** | Union\[key, None\] Returns the key or None if no key found |

### get

Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on the tab if no key is defined. Returns None if an error occurs. Note that this is exactly the same data that would be returned from a call to Window.Read. Are you sure you are using this method correctly?

`get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | Union\[Any, None\] The key of the currently selected tab or the tab's text if it has no key |

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


Table Element
-------------

    Table(values,
        headings=None,
        visible_column_map=None,
        col_widths=None,
        def_col_width=10,
        auto_size_columns=True,
        max_col_width=20,
        select_mode=None,
        display_row_numbers=False,
        num_rows=None,
        row_height=None,
        font=None,
        justification="right",
        text_color=None,
        background_color=None,
        alternating_row_color=None,
        row_colors=None,
        vertical_scroll_only=True,
        hide_vertical_scroll=False,
        size=(None, None),
        change_submits=False,
        enable_events=False,
        bind_return_key=False,
        pad=None,
        key=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name                    | Meaning                                                      |
| ----------------------- | ------------------------------------------------------------ |
| values                  | List\[List\[Union\[str, int, float\]\]\]                     |
| headings                | List\[str\] The headings to show on the top line             |
| visible\_column\_map    | List\[bool\] One entry for each column. False indicates the column is not shown |
| col\_widths             | List\[int\] Number of characters that each column will occupy |
| def\_col\_width         | (int) Default column width in characters                     |
| auto\_size\_columns     | (bool) if True columns will be sized automatically           |
| max\_col\_width         | (int) Maximum width for all columns in characters            |
| select\_mode            | (enum) Select Mode. Valid values start with "TABLE\_SELECT\_MODE\_". Valid values are: TABLE\_SELECT\_MODE\_NONE TABLE\_SELECT\_MODE\_BROWSE TABLE\_SELECT\_MODE\_EXTENDED |
| display\_row\_numbers   | (bool) if True, the first column of the table will be the row \# |
| num\_rows               | (int) The number of rows of the table to display at a time   |
| row\_height             | (int) height of a single row in pixels                       |
| font                    | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| justification           | (str) 'left', 'right', 'center' are valid choices            |
| text\_color             | (str) color of the text                                      |
| background\_color       | (str) color of background                                    |
| alternating\_row\_color | (str) if set then every other row will have this color in the background. |
| row\_colors             |                                                              |
| vertical\_scroll\_only  | (bool) if True only the vertical scrollbar will be visible   |
| hide\_vertical\_scroll  | (bool) if True vertical scrollbar will be hidden             |
| size                    | Tuple\[int, int\] DO NOT USE! Use num\_rows instead          |
| change\_submits         | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events          | (bool) Turns on the element specific events. Table events happen when row is clicked |
| bind\_return\_key       | (bool) if True, pressing return key will cause event coming from Table, ALSO a left button double click will generate an event if this parameter is True |
| pad                     | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key                     | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| tooltip                 | (str) text, that will appear when mouse hovers over the element |
| right\_click\_menu      | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible                 | (bool) set visibility state of the element                   |
| metadata                | (Any) User metadata that can be set to ANYTHING              |

### ButtonReboundCallback

Used in combination with tkinter's widget.bind function. If you wish to have a double-click for a button to call back the button's normal callback routine, then you should target your call to tkinter's bind method to point to this function which will in turn call the button callback function that is normally called.

    ButtonReboundCallback(event)


Parameter Descriptions:

| Name  | Meaning                              |
| ----- | ------------------------------------ |
| event | (unknown) Not used in this function. |

### Get

Dummy function for tkinter port. In the Qt port you can read back the values in the table in case they were edited. Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by user when Table was created or Updated.

`Get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | List\[List\[Any\]\] the current table values (for now what was originally provided up updated) |

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

Changes some of the settings for the Table Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(values=None,
        num_rows=None,
        visible=None,
        select_rows=None,
        alternating_row_color=None,
        row_colors=None)


Parameter Descriptions:

| Name                    | Meaning                                                      |
| ----------------------- | ------------------------------------------------------------ |
| values                  | List\[List\[Union\[str, int, float\]\]\] A new 2-dimensional table to show |
| num\_rows               | (int) How many rows to display at a time                     |
| visible                 | (bool) if True then will be visible                          |
| select\_rows            | List\[int\] List of rows to select as if user did            |
| alternating\_row\_color | (str) the color to make every other row                      |
| row\_colors             | List\[Union\[Tuple\[int, str\], Tuple\[Int, str, str\]\] list of tuples of (row, background color) OR (row, foreground color, background color). Changes the colors of listed rows to the color(s) provided (note the optional foreground color) |

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

Dummy function for tkinter port. In the Qt port you can read back the values in the table in case they were edited. Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by user when Table was created or Updated.

`get()`

| Name       | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| **return** | List\[List\[Any\]\] the current table values (for now what was originally provided up updated) |

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

### treeview\_double\_click

Not user callable. Callback function that is called when something is selected from Table. Stores the selected rows in Element as they are being selected. If events enabled, then returns from Read

    treeview_double_click(event)


Parameter Descriptions:

| Name  | Meaning                                  |
| ----- | ---------------------------------------- |
| event | (unknown) event information from tkinter |

### treeview\_selected

Not user callable. Callback function that is called when something is selected from Table. Stores the selected rows in Element as they are being selected. If events enabled, then returns from Read

    treeview_selected(event)


Parameter Descriptions:

| Name  | Meaning                                  |
| ----- | ---------------------------------------- |
| event | (unknown) event information from tkinter |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Table Element. Must call `Window.Read` or `Window.Finalize` prior

    update(values=None,
        num_rows=None,
        visible=None,
        select_rows=None,
        alternating_row_color=None,
        row_colors=None)

Parameter Descriptions:

| Name                    | Meaning                                                      |
| ----------------------- | ------------------------------------------------------------ |
| values                  | List\[List\[Union\[str, int, float\]\]\] A new 2-dimensional table to show |
| num\_rows               | (int) How many rows to display at a time                     |
| visible                 | (bool) if True then will be visible                          |
| select\_rows            | List\[int\] List of rows to select as if user did            |
| alternating\_row\_color | (str) the color to make every other row                      |
| row\_colors             | List\[Union\[Tuple\[int, str\], Tuple\[Int, str, str\]\] list of tuples of (row, background color) OR (row, foreground color, background color). Changes the colors of listed rows to the color(s) provided (note the optional foreground color) |



Tree Element
------------

    Tree Element - Presents data in a tree-like manner, much like a file/folder browser.  Uses the TreeData class
    to hold the user's data and pass to the element for display.
    
    Tree(data=None,
        headings=None,
        visible_column_map=None,
        col_widths=None,
        col0_width=10,
        def_col_width=10,
        auto_size_columns=True,
        max_col_width=20,
        select_mode=None,
        show_expanded=False,
        change_submits=False,
        enable_events=False,
        font=None,
        justification="right",
        text_color=None,
        background_color=None,
        num_rows=None,
        row_height=None,
        pad=None,
        key=None,
        tooltip=None,
        right_click_menu=None,
        visible=True,
        metadata=None)


Parameter Descriptions:

| Name                 | Meaning                                                      |
| -------------------- | ------------------------------------------------------------ |
| data                 | (TreeData) The data represented using a PySimpleGUI provided TreeData class |
| headings             | List\[str\] List of individual headings for each column      |
| visible\_column\_map | List\[bool\] Determines if a column should be visible. If left empty, all columns will be shown |
| col\_widths          | List\[int\] List of column widths so that individual column widths can be controlled |
| col0\_width          | (int) Size of Column 0 which is where the row numbers will be optionally shown |
| def\_col\_width      | (int) default column width                                   |
| auto\_size\_columns  | (bool) if True, the size of a column is determined using the contents of the column |
| max\_col\_width      | (int) the maximum size a column can be                       |
| select\_mode         | (enum) Use same values as found on Table Element. Valid values include: TABLE\_SELECT\_MODE\_NONE TABLE\_SELECT\_MODE\_BROWSE TABLE\_SELECT\_MODE\_EXTENDED |
| show\_expanded       | (bool) if True then the tree will be initially shown with all nodes completely expanded |
| change\_submits      | (bool) DO NOT USE. Only listed for backwards compat - Use enable\_events instead |
| enable\_events       | (bool) Turns on the element specific events. Tree events happen when row is clicked |
| font                 | Union\[str, Tuple\[str, int\]\] specifies the font family, size, etc |
| justification        | (str) 'left', 'right', 'center' are valid choices            |
| text\_color          | (str) color of the text                                      |
| background\_color    | (str) color of background                                    |
| num\_rows            | (int) The number of rows of the table to display at a time   |
| row\_height          | (int) height of a single row in pixels                       |
| pad                  | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| key                  | (Any) Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
| tooltip              | (str) text, that will appear when mouse hovers over the element |
| right\_click\_menu   | List\[List\[Union\[List\[str\],str\]\]\] A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
| visible              | (bool) set visibility state of the element                   |
| metadata             | (Any) User metadata that can be set to ANYTHING              |

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

Changes some of the settings for the Tree Element. Must call `Window.Read` or `Window.Finalize` prior

    Update(values=None,
        key=None,
        value=None,
        text=None,
        icon=None,
        visible=None)


Parameter Descriptions:

| Name    | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| values  | (TreeData) Representation of the tree                        |
| key     | (Any) identifies a particular item in tree to update         |
| value   | (Any) sets the node identified by key to a particular value  |
| text    | (str) sets the node identified by ket to this string         |
| icon    | Union\[bytes, str\] can be either a base64 icon or a filename for the icon |
| visible | (bool) control visibility of element                         |

### add\_treeview\_data

Not a user function. Recursive method that inserts tree data into the tkinter treeview widget.

    add_treeview_data(node)


Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| node | (TreeData) The node to insert. Will insert all nodes from starting point downward, recursively |

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

### treeview\_selected

Not a user function. Callback function that happens when an item is selected from the tree. In this method, it saves away the reported selections so they can be properly returned.

    treeview_selected(event)


Parameter Descriptions:

| Name  | Meaning                                                 |
| ----- | ------------------------------------------------------- |
| event | (Any) An event parameter passed in by tkinter. Not used |

### unhide\_row

Unhides (makes visible again) the row container that the Element is located on. Note that it will re-appear at the bottom of the window / container, most likely.

    unhide_row()


### update

Changes some of the settings for the Tree Element. Must call `Window.Read` or `Window.Finalize` prior

    update(values=None,
        key=None,
        value=None,
        text=None,
        icon=None,
        visible=None)


Parameter Descriptions:

| Name    | Meaning                                                      |
| ------- | ------------------------------------------------------------ |
| values  | (TreeData) Representation of the tree                        |
| key     | (Any) identifies a particular item in tree to update         |
| value   | (Any) sets the node identified by key to a particular value  |
| text    | (str) sets the node identified by ket to this string         |
| icon    | Union\[bytes, str\] can be either a base64 icon or a filename for the icon |
| visible | (bool) control visibility of element                         |

TreeData Element
----------------

    Class that user fills in to represent their tree data. It's a very simple tree representation with a root "Node"
    with possibly one or more children "Nodes".  Each Node contains a key, text to display, list of values to display
    and an icon.  The entire tree is built using a single method, Insert.  Nothing else is required to make the tree.


Instantiate the object, initializes the Tree Data, creates a root node for you

    TreeData()


### Insert

Inserts a node into the tree. This is how user builds their tree, by Inserting Nodes This is the ONLY user callable method in the TreeData class

    Insert(parent,
        key,
        text,
        values,
        icon=None)


Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| parent | (Node) the parent Node                                       |
| key    | (Any) Used to uniquely identify this node                    |
| text   | (str) The text that is displayed at this node's location     |
| values | List\[Any\] The list of values that are displayed at this node |
| icon   | Union\[str, bytes\]                                          |

### Node

Contains information about the individual node in the tree

    Node(parent,
        key,
        text,
        values,
        icon=None)


### insert

Inserts a node into the tree. This is how user builds their tree, by Inserting Nodes This is the ONLY user callable method in the TreeData class

    insert(parent,
        key,
        text,
        values,
        icon=None)

Parameter Descriptions:

| Name   | Meaning                                                      |
| ------ | ------------------------------------------------------------ |
| parent | (Node) the parent Node                                       |
| key    | (Any) Used to uniquely identify this node                    |
| text   | (str) The text that is displayed at this node's location     |
| values | List\[Any\] The list of values that are displayed at this node |
| icon   | Union\[str, bytes\]                                          |

VerticalSeparator Element
-------------------------

    Vertical Separator Element draws a vertical line at the given location. It will span 1 "row". Usually paired with
    Column Element if extra height is needed
    
    VerticalSeparator(pad=None)

Parameter Descriptions:

| Name | Meaning                                                      |
| ---- | ------------------------------------------------------------ |
| pad  | (int, int) or ((int, int),(int,int)) Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |

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



"Demo Programs" Applications
============================

There are too many to list!!

There are over 170 sample programs to give you a jump start.

These programs are an integral part of the overall PySimpleGUI documentation and learning system. They will give you a headstart in a way you can learn from and understand. They also show you integration techiques to other packages that have been figured out for you.

You will find Demo Programs located in a subfolder named "Demo Programs" under the top level and each of the PySimpleGUI ports on GitHub.

Demo programs for plain PySimpleGUI (tkinter) https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms

Demo programs for PySimpleGUIQt: https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIQt/Demo%20Programs

Demo programs for PySimpleGUIWx: https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx/Demo%20Programs

Demo programs for PySimpleGUIWeb: https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb/Demo%20Programs

There are not many programs under each of the port's folders because the main Demo Programs should run on all of the other platforms with minimal changes (often only the import statement changes).

Packages Used In Demos
----------------------

While the core PySimpleGUI code does not utilize any 3rd party packages, some of the demos do. They add a GUI to a few popular packages. These packages include: \* [Chatterbot](https://github.com/gunthercox/ChatterBot) \* [Mido](https://github.com/olemb/mido) \* [Matplotlib](https://matplotlib.org/) \* [PyMuPDF](https://github.com/rk700/PyMuPDF) \* OpenCV \* pymunk \* psutil \* pygame \* Forecastio

Creating a Windows .EXE File
============================

It's possible to create a single .EXE file that can be distributed to Windows users. There is no requirement to install the Python interpreter on the PC you wish to run it on. Everything it needs is in the one EXE file, assuming you're running a somewhat up to date version of Windows.

Installation of the packages, you'll need to install PySimpleGUI and PyInstaller (you need to install only once)

    pip install PySimpleGUI
    pip install PyInstaller

To create your EXE file from your program that uses PySimpleGUI, `my_program.py`, enter this command in your Windows command prompt:

    pyinstaller -wF my_program.py

You will be left with a single file, `my_program.exe`, located in a folder named `dist` under the folder where you executed the `pyinstaller` command.

That's all... Run your `my_program.exe` file on the Windows machine of your choosing.

> "It's just that easy."

(famous last words that screw up just about anything being referenced)

Your EXE file should run without creating a "shell window". Only the GUI window should show up on your taskbar.

If you get a crash with something like:

    ValueError: script '.......\src\tkinter' not found

Then try adding **`--hidden-import tkinter`** to your command

Debug Output
============

Be sure and check out the EasyPrint (Print) function described in the high-level API section. Leave your code the way it is, route your stdout and stderror to a scrolling window.

For a fun time, add these lines to the top of your script

        import PySimpleGUI as sg
        print = sg.Print

This will turn all of your print statements into prints that display in a window on your screen rather than to the terminal.

Look and Feel
=============

You can change defaults and colors of a large number of things in PySimpleGUI quite easily.

`ChangleLookAndFeel`
--------------------

Want a quick way of making your windows look a LOT better? Try calling `ChangeLookAndFeel`. It will, in a single call, set various color values to widgets, background, text, etc.

Or dial in the look and feel (and a whole lot more) that you like with the `SetOptions` function. You can change all of the defaults in one function call. One line of code to customize the entire GUI.

        sg.ChangeLookAndFeel('GreenTan')

Valid look and feel values are currently:

    SystemDefault
    Reddit
    Topanga
    GreenTan
    Dark
    LightGreen
    Dark2
    Black
    Tan
    TanBlue
    DarkTanBlue
    DarkAmber
    DarkBlue
    Reds
    Green
    BluePurple
    Purple
    BlueMono
    GreenMono
    BrownBlue
    BrightColors
    NeutralBlue
    Kayak
    SandyBeach
    TealMono

The way this call actually works is that it calls `SetOptions` with a LOT of color settings. Here is the actual call that's made. As you can see lots of stuff is defined for you.

    SetOptions(background_color=colors['BACKGROUND'],
                text_element_background_color=colors['BACKGROUND'],
                element_background_color=colors['BACKGROUND'],
                text_color=colors['TEXT'],
                input_elements_background_color=colors['INPUT'],
                button_color=colors['BUTTON'],
                progress_meter_color=colors['PROGRESS'],
                border_width=colors['BORDER'],
                slider_border_width=colors['SLIDER_DEPTH'],
                progress_meter_border_depth=colors['PROGRESS_DEPTH'],
                scrollbar_color=(colors['SCROLL']),
                element_text_color=colors['TEXT'],
                input_text_color=colors['TEXT_INPUT'])

To see the latest list of color choices you can call `ListOfLookAndFeelValues()`

You can also combine the `ChangeLookAndFeel` function with the `SetOptions` function to quickly modify one of the canned color schemes. Maybe you like the colors but was more depth to your bezels. You can dial in exactly what you want.

**ObjToString** Ever wanted to easily display an objects contents easily? Use ObjToString to get a nicely formatted recursive walk of your objects. This statement:

    print(sg.ObjToSting(x))

And this was the output

    <class '__main__.X'>
        abc = abc
        attr12 = 12
        c = <class '__main__.C'>
            b = <class '__main__.B'>
                a = <class '__main__.A'>
                    attr1 = 1
                    attr2 = 2
                    attr3 = three
                attr10 = 10
                attrx = x

You'll quickly wonder how you ever coded without it.