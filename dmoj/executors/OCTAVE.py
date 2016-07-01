from .base_executor import ScriptExecutor
from dmoj.judgeenv import env
from dmoj.cptbox.handlers import ACCESS_DENIED

class Executor(ScriptExecutor):
    ext = '.m'
    name = 'OCTAVE'
    command = env['runtime'].get('octave')
    address_grace = 131072
    test_program = "disp(input('', 's'))"
    syscalls = ['sched_getaffinity', ('socketcall', ACCESS_DENIED)]

    fs = ['.*\.(?:so|m)', '/lib/', '/dev/urandom$', '/sys/devices/system/cpu/online$', '/proc/stat$',
          '/etc/nsswitch\.conf$', '/etc/passwd$', '/etc/localtime$', '/usr/share/', '/usr/lib/', '/etc/fltk/']

    def get_cmdline(self):
        return [self.get_command(), '--no-gui', '--no-history', '--no-init-file', '--no-site-file',
                '--no-window-system', '--norc', '--quiet', self._code]
