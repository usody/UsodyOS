from hardware_metadata.core import Core
from sanitize import Sanitize


if '__main__' == __name__:
    software = 'UsodyOS'
    software_version = '2023.2.0-alpha'
    core = Core(software, software_version)

    print('-------------------------- [ STARTING ] --------------------------')

    core.print_snapshot_info()

    step1 = '________________| PHASE 1 - HARDWARE METADATA |__________________'
    print(step1)
    core.logs.debug('%s' %step1)

    snapshot = core.snapshot.generate_snapshot()
    json_file = core.snapshot.save_snapshot(snapshot)

    step2 = '________________| PHASE 2 - SANITIZE ALL DISKS |_________________'
    print(step2)
    core.logs.debug('%s' %step2)

    # Execute sanitization process
    sanitize_data = Sanitize.run(core.logs)

    # Print sanitization result
    Sanitize.print_sanitize_result(core.logs, sanitize_data)

    # Add sanitize information inside snapshot and saved again
    snapshot['sanitize'] = sanitize_data
    json_file = core.snapshot.save_snapshot(snapshot)

    step3 = '________________| PHASE 3 - UPLOAD SNAPSHOT |____________________'
    print(step3)
    core.logs.debug('%s' %step3)

    response = core.snapshot.post_snapshot(snapshot)

    print('-------------------------- [ FINISHED ] --------------------------')

    core.print_summary(json_file, response)