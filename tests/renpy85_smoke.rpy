## Ren'Py 8.5.3-only automated smoke test.
## The CI workflow copies this file to game/ for the test command.
## It stays outside game/ in the repository so 8.2 can parse the template.

testsuite global:
    teardown:
        exit

testcase starter_gui_smoke:
    $ _test.transition_timeout = 0.05

    # Main-menu navigation and return actions.
    click "Preferences"
    click "Return"
    click "About"
    click "Return"

    # Exercise the starter's dialogue, custom input, and choice screen.
    click "Start"
    advance until screen "input"
    type "yes\n"
    advance until screen "choice"
    click "Choice 1"
