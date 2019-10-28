# ericnuno
common_modules

## Function Examples

### pwait

> [!NOTE]
> Function used to wait/sleep until given character(s) are returned in the Paramiko session command output string.

```python
...
channel = ssh.invoke_shell()
# Send Paramiko command to session
channel.send('show running config')
# Wait for # character in returned command output
pwait('#', channel)
```
