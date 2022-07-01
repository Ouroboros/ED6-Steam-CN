import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'Verte Bridge - Checkpoint'),
    TXT(0x02, 'Bose'),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1102.x'
    header.mapIndex       = 55
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2A4
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10290._CH', 'ED6_DT09/CH10290P._CP'),
        ('ED6_DT09/CH10291._CH', 'ED6_DT09/CH10291P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10320._CH', 'ED6_DT09/CH10320P._CP'),
        ('ED6_DT09/CH10321._CH', 'ED6_DT09/CH10321P._CP'),
        ('ED6_DT09/CH10330._CH', 'ED6_DT09/CH10330P._CP'),
        ('ED6_DT09/CH10331._CH', 'ED6_DT09/CH10331P._CP'),
        ('ED6_DT09/CH10350._CH', 'ED6_DT09/CH10350P._CP'),
        ('ED6_DT09/CH10351._CH', 'ED6_DT09/CH10351P._CP'),
        ('ED6_DT09/CH10540._CH', 'ED6_DT09/CH10540P._CP'),
        ('ED6_DT09/CH10541._CH', 'ED6_DT09/CH10541P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
        ('ED6_DT09/CH10900._CH', 'ED6_DT09/CH10900P._CP'),
        ('ED6_DT09/CH10901._CH', 'ED6_DT09/CH10901P._CP'),
    ]

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -105840,
            z                   = 0,
            y                   = -23910,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -226090,
            z                   = 0,
            y                   = -15420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x17A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -105060,
            z           = 140,
            y           = -56470,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -112490,
            z           = 20,
            y           = -60920,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00DF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -150760,
            z           = 550,
            y           = -35150,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -183300,
            z           = 90,
            y           = -41900,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -168950,
            z           = -20,
            y           = -29930,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00E1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -177370,
            z           = 0,
            y           = -16920,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00DD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x222
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x222
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -166760,
            triggerZ            = 130,
            triggerY            = -21010,
            triggerRange        = 1000,
            actorX              = -166150,
            actorZ              = 220,
            actorY              = -20910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -184260,
            triggerZ            = 1040,
            triggerY            = -55990,
            triggerRange        = 1000,
            actorX              = -184720,
            actorZ              = 1040,
            actorY              = -56460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x26B
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFB9718, 0xFFFD8730, 0x00230017)
    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0000)
    OP_71(0x0000, 0x0004)
    OP_64(0x01, 0x0001)
    OP_71(0x0001, 0x0000)
    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0002 offset: 0x29A
@scena.Code('ReInit')
def ReInit():
    Return()

# id: 0x0003 offset: 0x29B
@scena.Code('func_03_29B')
def func_03_29B():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
