import os.path, os

def run_as_browser(fn):
    def wrapped(*args, **kwargs):
        rv = fn(*args, **kwargs)
        return 'sudo -Hiu browser %s' % rv
    return wrapped

class Helpers:
    @property
    @run_as_browser
    def default_firefox_bin(self):
        candidates = [
            '/usr/local/lib/firefox3/firefox-bin'
        ]
        return self._pick(candidates, os.path.exists)
    
    @property
    @run_as_browser
    def default_firefox_wrapper(self):
        candidates = [
            'firefox', 'firefox3'
        ]
        return self._pick(candidates, self._wrapper_tester)
    
    default_firefox = default_firefox_wrapper
    
    @property
    def as_browser(self):
        return 'sudo -Hiu browser'
    
    @property
    def opera(self):
        return 'sudo -Hiu browser opera'
    
    def _wrapper_tester(self, candidate):
        dirs = os.environ['PATH'].split(':')
        for dir in dirs:
            path = os.path.join(dir, candidate)
            if os.path.exists(path):
                return True
        return False
        
    def _pick(self, candidates, tester):
        for candidate in candidates:
            if tester(candidate):
                return candidate
        # consider raising here
        return None
