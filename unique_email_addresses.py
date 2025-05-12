from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = []

        for email in emails:
            name, domain = email.split("@")
            name = name.replace(".", "")

            if "+" in name:
                plus_index = name.index("+")
                name = name[:plus_index]

            the_email = name + "@" + domain

            if the_email not in unique_emails:
                unique_emails.append(the_email)

        return len(unique_emails)
