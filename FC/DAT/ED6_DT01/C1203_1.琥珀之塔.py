from ED6ScenarioHelper import *

def main():
    # 琥珀之塔

    CreateScenaFile(
        FileName            = 'C1203_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C1203.x',
        MapIndex            = 51,
        MapDefaultBGM       = "ed60033",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    ScpFunction(
    )


    SaveToFile()

Try(main)
