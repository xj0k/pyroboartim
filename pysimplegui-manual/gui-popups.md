High Level API Calls - Popup's
==============================

"High level calls" are those that start with "Popup". They are the most basic form of communications with the user. They are named after the type of window they create, a pop-up window. These windows are meant to be short lived while, either delivering information or collecting it, and then quickly disappearing.

Think of Popups as your first windows, sorta like your first bicycle. It worked well, but was limited. It probably wasn't long before you wanted more features and it seemed too limiting for your newly found sense of adventure.

When you've reached the point with Popups that you are thinking of filing a GitHub "Enhancement Issue" to get the Popup call extended to include a new feature that you think would be helpful.... not just to you but others is what you had in mind, right? For the good of others.

It's at THIS time that you should immediately turn to the section entitled "Custom Window API Calls - Your First Window". Congratulations, you just graduated and are not an official "GUI Designer". Oh, nevermind that you only started learning Python 2 weeks ago, you're a real GUI Designer now so buck up and start acting like one.

But, for now, let's stick with these 1-line window calls, the Popups.

Popup Output
------------

Think of the `Popup` call as the GUI equivalent of a `print` statement. It's your way of displaying results to a user in the windowed world. Each call to Popup will create a new Popup window.

`Popup` calls are normally blocking. your program will stop executing until the user has closed the Popup window. A non-blocking window of Popup discussed in the async section.

Just like a print statement, you can pass any number of arguments you wish. They will all be turned into strings and displayed in the popup window.

There are a number of Popup output calls, each with a slightly different look (e.g. different button labels).

The list of Popup output functions are: - Popup - PopupOk - PopupYesNo - PopupCancel - PopupOkCancel - PopupError - PopupTimed, PopupAutoClose - PopupNoWait, PopupNonBlocking

The trailing portion of the function name after Popup indicates what buttons are shown. `PopupYesNo` shows a pair of button with Yes and No on them. `PopupCancel` has a Cancel button, etc.

While these are "output" windows, they do collect input in the form of buttons. The Popup functions return the button that was clicked. If the Ok button was clicked, then Popup returns the string 'Ok'. If the user clicked the X button to close the window, then the button value returned is `None`.

The function `PopupTimed` or `PopupAutoClose` are popup windows that will automatically close after come period of time.

Here is a quick-reference showing how the Popup calls look.

    sg.Popup('Popup')  # Shows OK button
    sg.PopupOk('PopupOk')  # Shows OK button
    sg.PopupYesNo('PopupYesNo')  # Shows Yes and No buttons
    sg.PopupCancel('PopupCancel')  # Shows Cancelled button
    sg.PopupOKCancel('PopupOKCancel')  # Shows OK and Cancel buttons
    sg.PopupError('PopupError')  # Shows red error button
    sg.PopupTimed('PopupTimed')  # Automatically closes
    sg.PopupAutoClose('PopupAutoClose')  # Same as PopupTimed

Preview of popups:

<span class="image"></span> <span class="image"></span> <span class="image"></span>

<span class="image"></span> <span class="image"></span> <span class="image"></span> <span class="image"></span>

Popup - Display a popup Window with as many parms as you wish to include. This is the GUI equivalent of the "print" statement. It's also great for "pausing" your program's flow until the user can read some error messages.

    Popup(args,
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

The other output Popups are variations on parameters. Usually the button\_type parameter is the primary one changed.

The other output Popups are variations on parameters. Usually the button\_type parameter is the primary one changed.

The choices for button\_type are:

    POPUP_BUTTONS_YES_NO
    POPUP_BUTTONS_CANCELLED
    POPUP_BUTTONS_ERROR
    POPUP_BUTTONS_OK_CANCEL
    POPUP_BUTTONS_OK
    POPUP_BUTTONS_NO_BUTTONS

**Note that you should not call Popup yourself with different button\_types.** Rely on the Popup function named that sets that value for you. For example PopupYesNo will set the button type to POPUP\_BUTTONS\_YES\_NO for you.

#### Scrolled Output

There is a scrolled version of Popups should you have a lot of information to display.

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

    PopupScrolled(*args, button_color=None, yes_no=False, auto_close=False, auto_close_duration=None, size=(None, None), location=(None, None), title=None, non_blocking=False)

Typical usage:

    sg.PopupScrolled(my_text)

<span class="image">scrolledtextbox 2</span>

The `PopupScrolled` will auto-fit the window size to the size of the text. Specify `None` in the height field of a `size` parameter to get auto-sized height.

This call will create a scrolled box 80 characters wide and a height dependent upon the number of lines of text.

`sg.PopupScrolled(my_text, size=(80, None))`

Note that the default max number of lines before scrolling happens is set to 50. At 50 lines the scrolling will begin.

If `non_blocking` parameter is set, then the call will not blocking waiting for the user to close the window. Execution will immediately return to the user. Handy when you want to dump out debug info without disrupting the program flow.

### PopupNoWait

Show Popup window and immediately return (does not block)

    PopupNoWait(args,
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

The Popup call PopupNoWait or PopupNonBlocking will create a popup window and then immediately return control back to you. All other popup functions will block, waiting for the user to close the popup window.

This function is very handy for when you're **debugging** and want to display something as output but don't want to change the programs's overall timing by blocking. Think of it like a `print` statement. There are no return values on one of these Popups.

Popup Input
-----------

There are Popup calls for single-item inputs. These follow the pattern of `Popup` followed by `Get` and then the type of item to get. There are 3 of these input Popups to choose from, each with settings enabling customization. - `PopupGetText` - get a single line of text - `PopupGetFile` - get a filename - `PopupGetFolder` - get a folder name

Use these Popups instead of making a custom window to get one data value, call the Popup input function to get the item from the user. If you find the parameters are unable to create the kind of window you are looking for, then it's time for you to create your own window.

### PopupGetText

Use this Popup to get a line of text from the user.

Display Popup with text entry field. Returns the text entered or None if closed / cancelled

    PopupGetText(message,
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

    import PySimpleGUI as sg
    text = sg.PopupGetText('Title', 'Please input something')
    sg.Popup('Results', 'The value returned from PopupGetText', text)

<span class="image">popupgettext</span>

<span class="image">popup gettext response</span>

### PopupGetFile

Gets a filename from the user. There are options to configure the type of dialog box to show. Normally an "Open File" dialog box is shown.

Display popup window with text entry field and browse button so that a file can be chosen by user.

    PopupGetFile(message,
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

If configured as an Open File Popup then (save\_as is not True) the dialog box will look like this.

<span class="image">snag-0060</span>

If you set the parameter save\_As to True, then the dialog box looks like this:

<span class="image">snag-0061</span>

If you choose a filename that already exists, you'll get a warning popup box asking if it's OK. You can also specify a file that doesn't exist. With an "Open" dialog box you cannot choose a non-existing file.

A typical call produces this window.

    text = sg.PopupGetFile('Please enter a file name')
    sg.Popup('Results', 'The value returned from PopupGetFile', text)

<span class="image">popupgetfile</span>

### PopupGetFolder

The window created to get a folder name looks the same as the get a file name. The difference is in what the browse button does. `PopupGetFile` shows an Open File dialog box while `PopupGetFolder` shows an Open Folder dialog box.

Display popup with text entry field and browse button so that a folder can be chosen.

    PopupGetFolder(message,
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

This is a typpical call

        text = sg.PopupGetFolder('Please enter a folder name')
        sg.Popup('Results', 'The value returned from PopupGetFolder', text)

<span class="image">popupgetfolder</span>

### PopupAnimated

<span class="image">ring</span>

The animated Popup enables you to easily display a "loading" style animation specified through a GIF file that is either stored in a file or a base64 variable.

Show animation one frame at a time. This function has its own internal clocking meaning you can call it at any frequency and the rate the frames of video is shown remains constant. Maybe your frames update every 30 ms but your event loop is running every 10 ms. You don't have to worry about delaying, just call it every time through the loop.

    PopupAnimated(image_source,
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

***To close animated popups***, call PopupAnimated with `image_source=None`. This will close all of the currently open PopupAnimated windows.