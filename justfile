# For see all this list of commands run:
# ```bash
# just --list
# ```
# All docs is only "one-liner".
#
# Plugin: https://plugins.jetbrains.com/plugin/18658-just
#


import 'just/quality.just'

# List of all commands
[private]
@default:
    just --list --justfile {{ justfile() }}
