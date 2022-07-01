import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0011_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0011   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '12530待机'),
    TXT(0x02, '12531移动'),
    TXT(0x03, '12532攻击'),
    TXT(0x04, '12533伤害'),
    TXT(0x05, '12534倒下'),
    TXT(0x06, '12540待机'),
    TXT(0x07, '12541移动'),
    TXT(0x08, '12542攻击'),
    TXT(0x09, '12543伤害'),
    TXT(0x0A, '12544倒下'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0030.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x31B
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
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
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
        ('ED6_DT29/CH12530._CH', 'ED6_DT29/CH12530P._CP'),
        ('ED6_DT29/CH12531._CH', 'ED6_DT29/CH12531P._CP'),
        ('ED6_DT29/CH12532._CH', 'ED6_DT29/CH12532P._CP'),
        ('ED6_DT29/CH12533._CH', 'ED6_DT29/CH12533P._CP'),
        ('ED6_DT29/CH12534._CH', 'ED6_DT29/CH12534P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12540._CH', 'ED6_DT29/CH12540P._CP'),
        ('ED6_DT29/CH12541._CH', 'ED6_DT29/CH12541P._CP'),
        ('ED6_DT29/CH12542._CH', 'ED6_DT29/CH12542P._CP'),
        ('ED6_DT29/CH12543._CH', 'ED6_DT29/CH12543P._CP'),
        ('ED6_DT29/CH12544._CH', 'ED6_DT29/CH12544P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x28A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x28A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x28A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x28A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x28B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x28C
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_2B9'),
        (0x00000001, 'loc_2C1'),
        (0x00000002, 'loc_2C9'),
        (0x00000003, 'loc_2D1'),
        (0x00000004, 'loc_2D9'),
        (0x00000005, 'loc_2E1'),
        (-1, 'loc_2E9'),
    )

    def _loc_2B9(): pass

    label('loc_2B9')

    Sleep(100)

    Jump('loc_2E9')

    def _loc_2C1(): pass

    label('loc_2C1')

    Sleep(100)

    Jump('loc_2E9')

    def _loc_2C9(): pass

    label('loc_2C9')

    Sleep(200)

    Jump('loc_2E9')

    def _loc_2D1(): pass

    label('loc_2D1')

    Sleep(300)

    Jump('loc_2E9')

    def _loc_2D9(): pass

    label('loc_2D9')

    Sleep(400)

    Jump('loc_2E9')

    def _loc_2E1(): pass

    label('loc_2E1')

    Sleep(500)

    Jump('loc_2E9')

    def _loc_2E9(): pass

    label('loc_2E9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2FE',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_2E9')

    def _loc_2FE(): pass

    label('loc_2FE')

    Return()

# id: 0x0003 offset: 0x2FF
@scena.Code('func_03_2FF')
def func_03_2FF():
    Return()

# id: 0x0004 offset: 0x300
@scena.Code('func_04_300')
def func_04_300():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗷—',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
