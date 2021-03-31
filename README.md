![GitHub Workflow Status](https://img.shields.io/github/workflow/status/YooUp/RS232-Monitor-Commands/Pipeline)

# RS232 Monitor Commands

This is a public database for all the known RS232 commands for professionnal screens, monitors and projectors. Feel free to contribute !

## Supported monitors

Check the [MONITORS.md](https://github.com/YooUp/RS232-Monitor-Commands/blob/master/MONITORS.md) file for a full list of supported monitors.

## Restful API

You can acces the latest database from your third party application by doing a GET request at the following url : https://yooup.github.io/RS232-Monitor-Commands/monitors.json
You can also query by monitor (eg. : https://yooup.github.io/RS232-Monitor-Commands/monitors/benq.json).

## Database structure

The database is a [json file](https://github.com/YooUp/RS232-Monitor-Commands/blob/master/database/monitors.json). Its structure is the following :

#### General structure

- `version` : Integer representing the database version. This integer is incremented everytime the file is updated.
- `monitors` : List of monitors.

#### Monitor structure

- `name` : Name of the manufacturer.
- `doc` : Link to the official documentation where the RS232 codes are taken from.
- `baudrate` : Baudrate of the RS232 transmission.
- `commands` : List of RS232 commands. Each key is associated with an RS232 code in decimal.

#### Command structure

- `key` : String representing the action to do:
  - `SET\_CATEGORY\_VALUE`
  - `GET\_CATEGORY`

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
- Create a new json file in the [following directory](https://github.com/YooUp/RS232-Monitor-Commands/tree/master/database/monitors). Make sure that the structure is correct.
- Commit
- Pull request

#### Fix/Add RS232 codes

It can happen that some RS232 are wrong or missing. If so, you can help us to fix it:

- Fork
- Edit the json file corresponding to your monitor
- Commit
- Pull request

## FAQ

#### The `^M` character keeps showing when I run the `git diff` command

Unix and Windows does handle line endings the same way. Windows use `CR` `LF` while Unix use `LF`.
Run the following command to automatically convert line endings for your platform :

```
git config --global core.autocrlf true
```
