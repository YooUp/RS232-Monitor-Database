![GitHub Workflow Status](https://img.shields.io/github/workflow/status/YooUp/RS232-Monitor-Database/Pipeline)

# RS232 Monitor Commands

This is a public database for all the known RS232 commands for professionnal screens, monitors and projectors. Feel free to contribute !

## Supported monitors

Check the [MONITORS.md](https://github.com/YooUp/RS232-Monitor-Database/blob/master/MONITORS.md) file for a full list of supported monitors.

## Restful API

You can acces the latest database from your third party application by doing a GET request at the following url : https://yooup.github.io/RS232-Monitor-Database/monitors.json
You can also query by monitor (eg. : https://yooup.github.io/RS232-Monitor-Database/monitors/benq.json).

## Database structure

The database is a [json file](https://github.com/YooUp/RS232-Monitor-Database/blob/master/database/monitors.json). Its structure is the following :

#### General structure

- `version` : Integer representing the database version. This integer is incremented everytime the file is updated.
- `monitors` : List of monitors.

#### Monitor structure

- `name` : Name of the manufacturer.
- `doc` : Link to the official documentation where the RS232 codes are taken from.
- `baudrate` : Baudrate of the RS232 transmission.
- `commands` : List of RS232 commands. Each key is associated with a RS232 code in decimal.

#### Command structure

- `key` : String representing the action to do:
  - `SET_CATEGORY_VALUE`
  - `GET_CATEGORY`

- `value` : List of integers to send via RS232 to perform this action.

> Example:
> 
> ```json
> "SET_POWER_ON":[1,2,3,4,5,6,7,8,9],
> "SET_INPUT_HDMI1":[1,2,3,4,5,6,7,8,9],
> "GET_VOLUME":[1,2,3,4,5,6,7,8,9],
> ```
> 
> - `SET_POWER_ON` : To power on the monitor.
> - `SET_INPUT_HDMI1` : To set the input to HDMI1.
> - `GET_VOLUME` : To get the current volume.


## Contribution

#### Add a new monitor

If the monitor you want to work on is not in the database, please share the RS232 codes with us by adding it:

- Fork
- Create a new json file in the [following directory](https://github.com/YooUp/RS232-Monitor-Database/tree/master/database/monitors)
- Check the json syntax with [JsonLint](https://jsonlint.com/)
- Commit
- Pull request

#### Fix/Add RS232 codes

Some RS232 codes could be wrong or missing. If so, you can help us to fix it:

- Fork
- Edit the json file corresponding to your monitor
- Commit
- Pull request

## FAQ

#### The `^M` character keeps showing when I run the `git diff` command

Unix and Windows doesn't handle line endings the same way. Windows use `CR` `LF` while Unix use `LF`.
Run the following command to automatically convert line endings for your platform :

```
git config --global core.autocrlf true
```

#### How can I test the RS232 codes ?

- Buy a [USB to RS232 adapter](https://www.google.com/search?q=rs232+usb+adapter&source=lnms&tbm=shop&sa=X&ved=2ahUKEwj59o3d0t3vAhV6RhUIHVg4CUkQ_AUoAXoECAEQAw&biw=1908&bih=926) (DB9 or Jack)
- Use a software like [Docklight](https://docklight.de/information/) to send the codes. You can choose between ASCII, HEX, DEC or BINARY as input.

_The RS232 DB9 input on monitors can be either male or female. Make sure to have the right adapter or buy a [RS232 gender changer](https://www.google.com/search?q=RS232+gender+changer&biw=1908&bih=926&tbm=shop&ei=2A5mYIr5EPTUxgOQrraoBg&oq=RS232+gender+changer&gs_lcp=Cgtwcm9kdWN0cy1jYxADMgQIABATMggIABAeEBMQGDIICAAQHhATEBgyCAgAEB4QExAYMggIABAeEBMQGDIICAAQHhATEBgyCAgAEB4QExAYMggIABAeEBMQGDIICAAQHhATEBgyCggAEAUQHhATEBhQuQlY8gpgyxNoAHAAeACAAWGIAY8CkgEBM5gBAKABAcABAQ&sclient=products-cc&ved=0ahUKEwiKxY7A1N3vAhV0qnEKHRCXDWUQ4dUDCAs&uact=5)._
