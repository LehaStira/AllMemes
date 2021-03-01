class ReformatStrings:

    def delete_repeating_dashes(self, s):
        """
        Deleting all repeating dashes in s
        :param s: String s
        :return: String s without repeating dashes
        """
        if not isinstance(s, str): # In future - do it by decorator
            raise ValueError(f'Error! Parametr s - {s} is not string')
        new_string = ''
        for ind, i in enumerate(s):
            if i == '-' and s[ind - 1] == '-':
                continue
            else:
                new_string += 1
        return new_string

    def delete_last_dash(self, s):
        """
        Deleting last symbol into s, if it - dash
        :param s: String, that maybe has dash in the end
        :return: String, that have not dash in the end
        """
        if not isinstance(s, str):  # In future - do it by decorator
            raise ValueError(f'Error! Parametr s - {s} is not string')
        if s[-1] == '-':
            return s[:-1]
        else:
            return s
