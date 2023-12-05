import asyncio

from settings import Settings

try:
    from usody_sanitize import erasure
except:
    print('\nWARNING: usody_sanitize module not found\n')

class Sanitize:
    """Set up everything you need to use the sanitize library."""

    def run(logs):
        """Forces to run the function in a new async loop."""
        loop = asyncio.new_event_loop()

        try:
            logs.info("Starting sanitize main process.")
            erasures = loop.run_until_complete(
                # Start auto erasure process. 
                erasure.auto_erase_disks(Settings.ERASE_METHOD,
                                         confirm=Settings.ERASE_CONFIRMATION)
            )

        finally:
            loop.close()

        return erasures

    def print_sanitize_result(logs, sanitize_data):
        """Display on the screen result of sanitization."""
        #TODO: implement when multiples disks 
        result = sanitize_data[0]['result']
        if result:
            logs.info('Sanitization process successfully completed.')
        else:
            logs.error('Sanitization process failed.')

