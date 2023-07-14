from hardware_metadata.core import Core
from settings import Settings
from sanitize import Sanitize
from tests import Tests


def run_hardware_metadata(core):
    step = '____________________| HARDWARE METADATA |________________________'
    print(step)
    core.logs.debug('%s' %step)

    snapshot = core.snapshot.generate_snapshot()
    json_file = core.snapshot.save_snapshot(snapshot)
    return snapshot, json_file

def run_tests(core, snapshot):
    step = '____________________| HARDWARE TESTS |____________________________'
    print(step)
    core.logs.debug('%s' %step)
    tests_data = Tests.run()

    # Add tests information inside snapshot and saved again
    snapshot['tests'] = tests_data
    core.snapshot.save_snapshot(snapshot)
    return snapshot

def run_sanitize(core, snapshot):
    step = '____________________| SANITIZE ALL DISKS |_______________________'
    print(step)
    core.logs.debug('%s' %step)

    # Execute sanitization process
    sanitize_data = Sanitize.run(core.logs)

    # Print sanitization result
    Sanitize.print_sanitize_result(core.logs, sanitize_data)

    # Add sanitize information inside snapshot and saved again
    #snapshot.update({'sanitize': sanitize_data})
    snapshot['sanitize'] = sanitize_data
    core.snapshot.save_snapshot(snapshot)
    return snapshot


if '__main__' == __name__:
    software = 'UsodyOS'
    software_version = '2023.4.0-alpha'
    core = Core(software, software_version)

    print('-------------------------- [ STARTING ] --------------------------')

    core.print_snapshot_info()

    snapshot, json_file = run_hardware_metadata(core)

    if Settings.TESTS:
        snapshot = run_tests(core, snapshot)

    if Settings.SANITIZE:
        snapshot = run_sanitize(core, snapshot)

    step = '____________________| UPLOADING SNAPSHOT |_______________________'
    print(step)
    core.logs.debug('%s' %step)

    response = core.snapshot.post_snapshot(snapshot)

    print('-------------------------- [ FINISHED ] --------------------------')

    core.print_summary(json_file, response)


