from ED6ScenarioHelper import *

def main():
    # 巴伦诺灯塔

    CreateScenaFile(
        FileName            = 'C2200_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C2200.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60031",
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
