class ReformatStrings:

    def delete_repeating_dashes(self, s):
        """
        Deleting all repeating dashes in s
        :param s: String s
        :return: String s without repeating dashes
        """
        new_string = ''
        for ind, i in enumerate(s):
            if i == '-' and s[ind - 1] == '-':
                continue
            else:
                new_string += 1
        return new_string


