import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1101   ._SN')

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
    header.mapModel       = 'R1101.x'
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
            x                   = -10250,
            z                   = 0,
            y                   = -8450,
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
            x                   = -106260,
            z                   = 0,
            y                   = -32340,
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
            x           = -46450,
            z           = 30,
            y           = 2310,
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
            x           = -72920,
            z           = -30,
            y           = 51450,
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
            x           = -97850,
            z           = -30,
            y           = 45380,
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
            x           = -90070,
            z           = 1040,
            y           = 27970,
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
            x           = -114180,
            z           = 80,
            y           = -40,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00DD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -57540,
            z           = 60,
            y           = 34670,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00DE,
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
            triggerX            = -85040,
            triggerZ            = 1000,
            triggerY            = 31580,
            triggerRange        = 1000,
            actorX              = -84380,
            actorZ              = 1000,
            actorY              = 31580,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -57040,
            triggerZ            = 0,
            triggerY            = 47160,
            triggerRange        = 1000,
            actorX              = -56420,
            actorZ              = -10,
            actorY              = 47170,
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
    OP_16(0x02, 0x00000FA0, 0xFFFCE708, 0xFFFE4698, 0x00230016)
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
