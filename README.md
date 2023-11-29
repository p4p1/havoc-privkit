# havoc-privkit

A port of privkit beacon object files for havoc. The original bof files can be found [here](https://github.com/mertdas/PrivKit/tree/main)

```
 - Command       :  privkit
 - Description   :  Privilege Escalation Module

  Command                   Description
  ---------                 -------------
  all                       Run all possible checks.
  elevated                  Check if programs are always installed as elevated.
  autologon                 Check for autologon registry keys.
  credman                   Enumerate credential manager.
  paths                     Enumerate hijackable paths.
  autorun                   Find modifiable autoruns.
  token                     Check for token privileges.
  unquoted                  Check unquoted service paths.
```
![image](https://github.com/p4p1/havoc-privkit/assets/19672114/f19a1a53-b9a5-4507-9f7e-f6e5618659d7)

# Install:

Clone the repo including it's submodules:
```
$ git clone --recurse-submodules --remote-submodules https://github.com/p4p1/havoc-privkit
```
Load the privkit.py script inside of the havoc framework through the graphical
UI.
