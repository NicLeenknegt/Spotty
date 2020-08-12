
class Option:

    def __init__(self, long_option:str, with_args:bool, short_option:str = None):
        self.long_option = long_option
        self.with_args = with_args
        if short_option is not None:
            self.short_option = short_option
        else:
            self.short_option = ""
            for option in long_option.split('-'):
                self.short_option += list(option)[0].lower()

    def get_long_option(self) -> str:
        return self.long_option + ( '=' if self.with_args else '')
    
    def get_short_option(self) -> str:
        return self.short_option + ( ':' if self.with_args else '')
