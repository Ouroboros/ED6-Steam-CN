import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'East Bose Highway'),
    TXT(0x02, 'Haken Gate'),
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
    header.mapModel       = 'R1300.x'
    header.mapIndex       = 57
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x270
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
        ('ED6_DT09/CH10370._CH', 'ED6_DT09/CH10370P._CP'),
        ('ED6_DT09/CH10371._CH', 'ED6_DT09/CH10371P._CP'),
        ('ED6_DT09/CH10360._CH', 'ED6_DT09/CH10360P._CP'),
        ('ED6_DT09/CH10361._CH', 'ED6_DT09/CH10361P._CP'),
    ]

# id: 0x10002 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -207930,
            z                   = -20,
            y                   = -167750,
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
            x                   = -204120,
            z                   = -200,
            y                   = 1430,
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

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -203250,
            z           = 10,
            y           = -130620,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0106,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -218580,
            z           = -40,
            y           = -112680,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0106,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -226560,
            z           = -30,
            y           = -88140,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0106,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -200780,
            z           = -20,
            y           = -50350,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0106,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -188950,
            z           = -20,
            y           = -42080,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0106,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -194620,
            z           = -30,
            y           = -34740,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0105,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -222450,
            triggerZ            = -80,
            triggerY            = -128449,
            triggerRange        = 1000,
            actorX              = -222890,
            actorZ              = -10,
            actorY              = -128990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -185450,
            triggerZ            = -120,
            triggerY            = -39580,
            triggerRange        = 1000,
            actorX              = -184980,
            actorZ              = 40,
            actorY              = -39110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1FA
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1FB
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFADF80, 0xFFFCCBB0, 0x00230013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 0, 0x1B10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_226')

    def _loc_21F(): pass

    label('loc_21F')

    OP_6F(0x0002, 60)

    def _loc_226(): pass

    label('loc_226')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 1, 0x1B11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_238',
    )

    OP_6F(0x0003, 0)

    Jump('loc_23F')

    def _loc_238(): pass

    label('loc_238')

    OP_6F(0x0003, 60)

    def _loc_23F(): pass

    label('loc_23F')

    OP_64(0x00, 0x0001)
    OP_71(0x0002, 0x0000)
    OP_71(0x0002, 0x0004)
    OP_64(0x01, 0x0001)
    OP_71(0x0003, 0x0000)
    OP_71(0x0003, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0002 offset: 0x266
@scena.Code('ReInit')
def ReInit():
    Return()

# id: 0x0003 offset: 0x267
@scena.Code('func_03_267')
def func_03_267():
    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
