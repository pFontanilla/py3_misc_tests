test_new_tcis_data = {
    "ThalesPNBOM": ["99259766", "99259766", "99259766", "99259766", "706-3-11042", "706-3-11042", "706-3-11042",
                    "706-3-11042"],
    "ThalesPID": ["5004604", "5004606", "5004605", "5004607", "", "", "", ""],
    "BCNPrev": ["99259766", "92127378", "92127377", "92127379", "", "", "", ""],
    "BCNUpdated": ["99259766", "92127378", "92127377", "92127379", "", "", "", ""],
    "DescrPrev": ["SCREW-HEX HD CAP M12X30MM FT 18-8 SS", "SCREW-HEX HD CAP M12X30MM FT 18-8 SS",
                  "SCREW-HEX HD CAP M12X30MM FT 18-8 SS", "SCREW-HEX HD CAP M12X30MM FT 18-8 SS", "", "", "", ""],
    "DescrUpdated": ["SCREW-HEX HD CAP M12X30MM FT 18-8 SS", "SCREW-HEX HD CAP M12X30MM FT 18-8 SS",
                     "SCREW-HEX HD CAP M12X30MM FT 18-8 SS", "SCREW-HEX HD CAP M12X30MM FT 18-8 SS", "", "", "",
                     ""],
    "MPNPrev": ["SCREW-HEX HD CAP M12X30MM FT 18-8 SS ", "91287A189", "344-047", "1238248",
                "WASHER-LOCK SPLIT N3/4 SS ANSI B18.21.1", "W-2324", "WA3954", "92147A036"],
    "MPNUpdated": ["SCREW-HEX HD CAP M12X30MM FT 18-8 SS ", "91287A189", "344-047", "1238248",
                   "WASHER-LOCK SPLIT N3/4 SS ANSI B18.21.1", "W-2324", "WA3954", "92147A036"],
    "MFRPrev": ["", "McMaster-Carr", "Spaenaur", "Bossard", "", "Spaenaur", "McMaster-Carr", "Pencom"],
    "MFRUpdated": ["", "McMaster-Carr", "Spaenaur", "Bossard", "", "Spaenaur", "McMaster-Carr", "Pencom"],
    "AMLPrev": ["", "MA", "MA", "MA", "", "MA", "MA", "MA"],
    "AMLUpdated": ["", "MA", "MA", "MA", "", "MA", "MA", "MA"],
    "ApprovalPrev": ["", "Approved for Purchase", "Approved for Purchase", "Approved for Purchase", "",
                     "Approved for Purchase", "Approved for Purchase", "Approved for Purchase"],
    "ApprovalUpdated": ["", "Approved for Purchase", "Approved for Purchase", "Approved for Purchase", "",
                        "Approved for Purchase", "Approved for Purchase", "Approved for Purchase"],
    "InternalNotes": ["", "", "", "", "", "", "", ""],
    "Accepted": [True, True, True, True, True, True, True, True]
}
test_new_tcis_df = pd.DataFrame(test_new_tcis_data,
                                columns=["ThalesPNBOM", "ThalesPID", "BCNPrev", "BCNUpdated", "DescrPrev",
                                         "DescrUpdated", "MPNPrev",
                                         "MPNUpdated", "MFRPrev", "MFRUpdated", "AMLPrev", "AMLUpdated", "ApprovalPrev",
                                         "ApprovalUpdated", "InternalNotes", "Accepted"])