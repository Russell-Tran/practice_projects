import os
import csv
from prettytable import PrettyTable
from simple_term_menu import TerminalMenu

def do_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

do_clear()
input("""

Hi, Travis! You have (202) unread messages. I've read them all and triaged your inbox.

Orange are RFQs and highest priority.
Yellow are correspondence with customers and medium priority.
Blue are messages from teammates and low priority.
""")
do_clear()

t = PrettyTable(['Label', 'Value'])
t.add_row(['Company', 'Adora Hardware Ltd.'])
t.add_row(['Logistics Manager', 'Adora Wang'])
t.add_row(['Source', 'Oakland, CA'])
t.add_row(['Destination', 'Chicago, IL'])
t.add_row(['Pallets', '7'])
t.add_row(['Weight', '20,000 lbs'])
t.add_row(['Vehicle', "53' truck"])
t.add_row(['Equipment', "dry"])
t.add_row(['Space', "FTL"])
t.add_row(['Pickup', "???"])
t.add_row(['Delivery', "11/28/2022 - 12/02/2022"])
print()
print("Identified email as a quote request.")
print("Identified the following info:")
print(t)
print()
print("Accept this quote?") # say yes
menu = TerminalMenu(['yes', 'no'])
menu.show()

print("They forgot to specify pickup date. Should I ask about that in the email?")
menu = TerminalMenu(['yes', 'no']) # say yes
menu.show()

print("Great! I've sent the following message to adorahardware@gmail.com:")
print("""

Hi Adora,

This is definitely something I can help you with. Let me get in touch with a few folks and follow up with a quote ASAP!

Quick question: Do you need any particular pickup date?

Regards,
Travis
Insightful Logistics LLC

""")
input()

# t = PrettyTable(['Carrier', 'Phone', 'Email', 'Lanes', 'FTL/LTL', 'Dry/reefer', 'Based', 'Notes'])
# with open("chicago.tsv") as fd:
#     rd = csv.reader(fd, delimiter="\t", quotechar='"')
#     for row in rd:
#         t.add_row(row)

t = PrettyTable(['Carrier', 'Email'])

emails = []
with open("chicago_short.tsv") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    for row in rd:
        t.add_row(row)
        emails.append(row[1])

do_clear()
print()
print("I thought these carriers might be a good fit for this load:")
print(t)
print()
print("Which of these carriers should I email? (All by default)")
print()
terminal_menu = TerminalMenu(
        emails,
        multi_select=True,
        show_multi_select_hint=True,
        preselected_entries=emails
    )
menu_entry_indices = terminal_menu.show()

do_clear()
print()

t = PrettyTable(['Label', 'Value'])
t.add_row(['Source', 'Oakland, CA'])
t.add_row(['Destination', 'Chicago, IL'])
t.add_row(['Pallets', '7'])
t.add_row(['Weight', '20,000 lbs'])
t.add_row(['Vehicle', "53' truck"])
t.add_row(['Equipment', "dry"])
t.add_row(['Space', "FTL"])
t.add_row(['Delivery', "11/28/2022 - 12/02/2022"])

chosen_emails = '; '.join(str(i) for i in terminal_menu.chosen_menu_entries)
print()
print("Great! I've sent the following message to {}:".format(chosen_emails))
print("""

Hi,

Looking to quote the following:

{}


Regards,
Travis
Insightful Logistics LLC


""".format(t))
