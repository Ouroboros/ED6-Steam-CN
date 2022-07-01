import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '提妲'),
    TXT(0x02, '科洛丝'),
    TXT(0x03, '阿加特'),
    TXT(0x04, '雪拉扎德'),
    TXT(0x05, '金'),
    TXT(0x06, '凯文'),
    TXT(0x07, '拉赛尔博士'),
    TXT(0x08, '尤莉亚上尉'),
    TXT(0x09, '奈尔'),
    TXT(0x0A, '朵洛希'),
    TXT(0x0B, '库莱泽'),
    TXT(0x0C, '安东尼'),
    TXT(0x0D, 'lift'),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0301.x'
    header.mapIndex       = 1
    header.bgm            = 116
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4445
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
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
    ]

# id: 0x10002 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1540,
            z                   = 3000,
            y                   = 17550,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -20,
            z                   = 2500,
            y                   = 15640,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -2430,
            z                   = 2500,
            y                   = 12850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -1830,
            z                   = 1500,
            y                   = -7470,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2B2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2B2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_2E6',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2E3',
    )

    SetChrPos(0x000A, -60, 3000, 19860, 0)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)

    def _loc_2E3(): pass

    label('loc_2E3')

    Jump('loc_3D6')

    def _loc_2E6(): pass

    label('loc_2E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_2FA',
    )

    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)

    Jump('loc_3D6')

    def _loc_2FA(): pass

    label('loc_2FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_32E',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_32B',
    )

    SetChrPos(0x0008, 3490, 1500, -6210, 90)
    ClearChrFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x06, 0x0002)

    def _loc_32B(): pass

    label('loc_32B')

    Jump('loc_3D6')

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_399',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_35F',
    )

    SetChrPos(0x000B, -1920, 1500, -9370, 270)
    ClearChrFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x06, 0x0002)

    def _loc_35F(): pass

    label('loc_35F')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_396',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 6, 0x1E26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_379',
    )

    SetChrFlags(0x0009, 0x0010)

    def _loc_379(): pass

    label('loc_379')

    SetChrPos(0x0009, 2300, 2500, 14260, 90)
    ClearChrFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x00, 0x06, 0x0002)

    def _loc_396(): pass

    label('loc_396')

    Jump('loc_3D6')

    def _loc_399(): pass

    label('loc_399')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D6',
    )

    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrChipByIndex(0x0011, 10)
    SetChrSubChip(0x0011, 0)
    SetChrPos(0x000B, 3490, 1500, -6210, 90)
    ClearChrFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x06, 0x0002)

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3EC',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x000D)

    Jump('loc_457')

    def _loc_3EC(): pass

    label('loc_3EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_402',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 0x000E)

    Jump('loc_457')

    def _loc_402(): pass

    label('loc_402')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_418',
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 0x000F)

    Jump('loc_457')

    def _loc_418(): pass

    label('loc_418')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_42E',
    )

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 0x0010)

    Jump('loc_457')

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_444',
    )

    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 0x0011)

    Jump('loc_457')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_457',
    )

    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 0x001D)

    def _loc_457(): pass

    label('loc_457')

    Return()

# id: 0x0001 offset: 0x458
@scena.Code('Init')
def Init():
    OP_22(0x01C3, 0x00, 0x64)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_471',
    )

    OP_22(0x0075, 0x01, 0x5A)

    Jump('loc_482')

    def _loc_471(): pass

    label('loc_471')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_482',
    )

    OP_22(0x0125, 0x01, 0x50)

    def _loc_482(): pass

    label('loc_482')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_49C',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_49C(): pass

    label('loc_49C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 4, 0x1E24)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    OP_B1('E0301_1')

    Jump('loc_518')

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_4C2',
    )

    OP_B1('E0301_3')

    Jump('loc_518')

    def _loc_4C2(): pass

    label('loc_4C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_4D5',
    )

    OP_B1('E0301_4')

    Jump('loc_518')

    def _loc_4D5(): pass

    label('loc_4D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_4E8',
    )

    OP_B1('E0301_5')

    Jump('loc_518')

    def _loc_4E8(): pass

    label('loc_4E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_4FB',
    )

    OP_B1('E0301_2')

    Jump('loc_518')

    def _loc_4FB(): pass

    label('loc_4FB')

    OP_B1('E0301_1')
    LoadEffect(0x00, 'map\\\\mp032_00.eff')

    def _loc_518(): pass

    label('loc_518')

    Return()

# id: 0x0002 offset: 0x519
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_74D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74D',
    )

    def _loc_531(): pass

    label('loc_531')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_74D',
    )

    OP_8F(0x0011, -20, 2500, 14180, 2000, 0x00)
    Sleep(500)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_8F(0x0011, 1850, 2500, 14180, 2000, 0x00)
    Sleep(500)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_8F(0x0011, 1850, 2500, 14940, 2000, 0x00)
    Sleep(500)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_8F(0x0011, -1800, 2500, 14940, 2000, 0x00)
    Sleep(500)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_8F(0x0011, -1800, 2500, 15580, 2000, 0x00)
    Sleep(500)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_8F(0x0011, -20, 2500, 15640, 2000, 0x00)
    Sleep(500)

    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0011, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Jump('loc_531')

    def _loc_74D(): pass

    label('loc_74D')

    Return()

# id: 0x0003 offset: 0x74E
@scena.Code('func_03_74E')
def func_03_74E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_771',
    )

    OP_8D(0x00FE, -2580, -8230, -860, -6510, 1000)

    Jump('func_03_74E')

    def _loc_771(): pass

    label('loc_771')

    Return()

# id: 0x0004 offset: 0x772
@scena.Code('func_04_772')
def func_04_772():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_121F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 7, 0x1A6F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C23',
    )

    ChrTalk(
        0x0010,
        (
            '#0270310292V#141F哟，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310293V在龙出现之前\n',
            '在这里闲逛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310294V#1011F嗯，算是吧。\n',
            '奈尔你们这么快就来采访了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310295V#140F不，一样是在\n',
            '等待主角登场呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310296V暂时先照几张\n',
            '『埃尔赛尤』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310297V#147F……嘿嘿，话说回来\n',
            '这次真是幸运啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310298V#1000F的确……\n',
            '对通讯社来说可是一次很难得的机会呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310299V除了引起轰动的巨龙骚动事件之外，\n',
            '同时还能采访到到新锐军舰的情报呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310300V#141F光是龙和飞行舰队的对决\n',
            '就已经是不得了的大新闻了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310301V这次的随行采访，\n',
            '几乎全部的通讯社\n',
            '都挤破头了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310302V#1015F嗯～果然是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310303V不过，居然会选中你们啊。\n',
            '难不成是抽签抽中的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310304V#142F笨蛋……那怎么可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310305V#145F我们会被指名采访，\n',
            '似乎是因为过去的报道大受好评。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310306V在那次政变事件当中的实绩，\n',
            '在这里发挥了很大的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310307V#1004F哦～很厉害嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310308V王国军的人们也\n',
            '对你们评价很高嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310309V#141F只要写出好报道，\n',
            '总有一天会得到认可的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310310V嗯，就因为这样，\n',
            '这次也麻烦你们提供情报啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310311V要是有什么轶闻插曲之类的，\n',
            '刊登在版面上可是增色不少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310312V#1001F啊哈哈……\n',
            '嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A6F)

    Jump('loc_121F')

    def _loc_C23(): pass

    label('loc_C23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034E, 0, 0x1A70)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ED4',
    )

    ChrTalk(
        0x0010,
        (
            '#0270310313V#140F对了，艾丝蒂尔。\n',
            '你和那个尤莉亚上尉熟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310314V#1015F虽然还不能说是\n',
            '非常亲近……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310315V不过也还算是\n',
            '有颇深的交往啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310316V#141F那么你能不能\n',
            '帮我介绍一下？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310317V制作那位女队长的特辑，\n',
            '可是读者们的强烈要求哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310318V#1004F尤、尤莉亚队长\n',
            '那么有人气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310319V#140F嗯嗯，和科洛蒂娅殿下\n',
            '感觉上有得一拼哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310320V听说也有出版社\n',
            '正在计划出写真集呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310321V#1020F写、写真集～～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310322V#145F不过，这纯粹\n',
            '是我们业界的传闻啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310323V那种企划就算制订出来\n',
            '也得不到采访许可的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310324V#1013F……啊，那也是。\n',
            '（不过还真想看看。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A70)

    Jump('loc_121F')

    def _loc_ED4(): pass

    label('loc_ED4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034E, 4, 0x1A74)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11C7',
    )

    ChrTalk(
        0x0010,
        (
            '#0270310325V#141F尤莉亚上尉的采访请求……\n',
            '到时候就麻烦你啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310326V毕竟亲卫队对平民来说\n',
            '是个很有距离的组织嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310327V我想透过对上尉的采访\n',
            '报导出真实的情况来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 6, 0x1A6E)),
            Expr.Return,
        ),
        'loc_11C4',
    )

    ChrTalk(
        0x0101,
        (
            '#0010310328V#1007F嗯，关于这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310329V其实立刻\n',
            '就被拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#0270310330V#143F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310331V拒、拒绝了……这么快？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310332V#1016F啊哈哈～抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310333V好像有很多\n',
            '不方便的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310334V#145F唉……是、是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310335V可恶……\n',
            '防卫心比想象中更坚固啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310336V#1007F呼，对不起。\n',
            '完全没能帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270310337V#142F哪里，这也是没办法的。\n',
            '对方也有自己的立场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310338V不过，既然这样的话\n',
            '就得考虑一下别的招数了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310339V#1019F（嗯～还没死心啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)
    OP_A2(0x1A74)

    def _loc_11C4(): pass

    label('loc_11C4')

    Jump('loc_121F')

    def _loc_11C7(): pass

    label('loc_11C7')

    ChrTalk(
        0x0010,
        (
            '#0270310340V#145F透过熟人也不行吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270310341V还以为会是个\n',
            '对人情没辙的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_121F(): pass

    label('loc_121F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x1223
@scena.Code('func_05_1223')
def func_05_1223():
    TalkBegin(0x00FE)
    SetChrChipByIndex(0x0011, 9)
    SetChrSubChip(0x0011, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_1665',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034E, 1, 0x1A71)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15F5',
    )

    ChrTalk(
        0x0011,
        (
            '#0280310342V#150F呀嗬～艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310343V#1001F嗨～朵洛希。\n',
            '自从王都之后都没见过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310344V拍摄的情况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0280310345V#150F哈哈哈，完全没问题哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310346V这孩子真是太可爱了，\n',
            '从哪个角度拍都ＯＫ呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310347V#1011F这孩子……\n',
            '啊，是说『埃尔赛尤』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310348V#1016F真是的，朵洛希\n',
            '还是那么我行我素啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0280310349V#151F嘿嘿，艾丝蒂尔才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310350V和平常一样有精神，\n',
            '真是太好了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310351V#1008F啊哈哈……\n',
            '不用客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310352V#1017F咦，莫非……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310353V朵洛希也在担心我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0280310354V#150F嗯～那当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310355V#156F那张约修亚的照片\n',
            '可是我拍的哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310356V要是因为这个害小艾\n',
            '心情沮丧，我会很难过的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310357V#1003F是，是吗……\n',
            '抱歉哦，朵洛希。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0280310358V#151F哪里，别在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310359V我是姐姐嘛，\n',
            '鼓励小艾是应该的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310360V如果还有什么其它的烦恼，\n',
            '随时都可以来找我商量哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310361V#1016F啊、啊哈哈……\n',
            '谢谢，我会记住的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A71)

    Jump('loc_1665')

    def _loc_15F5(): pass

    label('loc_15F5')

    ChrTalk(
        0x0011,
        (
            '#0280310362V#150F在龙出来之前\n',
            '先来拍这孩子的表情～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280310363V#151F然后假装拍摄舰内，\n',
            '趁机来偷拍女队长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1665(): pass

    label('loc_1665')

    SetChrChipByIndex(0x0011, 10)
    SetChrSubChip(0x0011, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x1673
@scena.Code('func_06_1673')
def func_06_1673():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_1D19',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_16DB'),
        (0x00000001, 'loc_1CDF'),
        (0x00000002, 'loc_1D13'),
        (-1, 'loc_1D16'),
    )

    def _loc_16DB(): pass

    label('loc_16DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_1CDC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 7, 0x1E27)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C6D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1720',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030340894V#020F哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1745')

    def _loc_1720(): pass

    label('loc_1720')

    ChrTalk(
        0x00FE,
        (
            '#0030340895V#020F哎呀，是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1745(): pass

    label('loc_1745')

    ChrTalk(
        0x0101,
        (
            '#0010340896V#1011F啊，雪拉姐。\n',
            '你在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340897V#1040F在想什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#0030340898V#524F嗯嗯，这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340899V看着翡翠之塔，\n',
            '就会想起很多事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340900V#1008F听你这么一说……\n',
            '确实是一言难尽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340901V#1041F哈哈，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340902V不管怎么说\n',
            '这里是我们首次执行任务的地方嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18C9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340903V#560F哇……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1960')

    def _loc_18C9(): pass

    label('loc_18C9')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18F9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340904V#040F哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1960')

    def _loc_18F9(): pass

    label('loc_18F9')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1935',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340905V#051F这可是头一回听说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1960')

    def _loc_1935(): pass

    label('loc_1935')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1960',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340906V#070F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1960(): pass

    label('loc_1960')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#0030340907V#021F呵呵，是刚刚成为\n',
            '准游击士的时候吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340908V#1015F嗯，附近的孩子\n',
            '闯进塔里迷了路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340909V#1035F所以我们就\n',
            '前来救援了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340910V#1048F不过，最后的风头\n',
            '倒是都被父亲抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AA2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340911V#071F哈哈，果然是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080340912V完全像是大人的做法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC8')

    def _loc_1AA2(): pass

    label('loc_1AA2')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B00',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340913V#051F哈哈，果然是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340914V大叔也真像个小孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC8')

    def _loc_1B00(): pass

    label('loc_1B00')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B6B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340915V#045F啊，果然是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340916V嘻嘻……\n',
            '很像是卡西乌斯叔叔的风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC8')

    def _loc_1B6B(): pass

    label('loc_1B6B')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BC8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340917V#067F啊，果然是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340918V嘿嘿，很像是叔叔的风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BC8(): pass

    label('loc_1BC8')

    ChrTalk(
        0x00FE,
        (
            '#0030340919V#020F嗯，比起那时候，\n',
            '你们两人确实都成长了不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340920V这次要好好靠自己的力量\n',
            '坚持到最后哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340921V#1006F嗯！　包在我身上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E27)

    Jump('loc_1CDC')

    def _loc_1C6D(): pass

    label('loc_1C6D')

    ChrTalk(
        0x00FE,
        (
            '#0030340922V#020F没想到会以这样的形式\n',
            '回到翡翠之塔呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340923V我也会做好准备的。\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CDC(): pass

    label('loc_1CDC')

    Jump('loc_1D16')

    def _loc_1CDF(): pass

    label('loc_1CDF')

    ChrTalk(
        0x000B,
        (
            '#0030340489V#020F哎呀？要更换成员了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000C)

    Jump('loc_1D16')

    def _loc_1D13(): pass

    label('loc_1D13')

    Jump('loc_1D16')

    def _loc_1D16(): pass

    label('loc_1D16')

    Jump('loc_2311')

    def _loc_1D19(): pass

    label('loc_1D19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_2311',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 7, 0x1A1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_226B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010310261V#1011F啊，雪拉姐。\n',
            '你在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310262V#020F哎呀，艾丝蒂尔在散步？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310263V#1000F嗯，差不多吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310264V你是出来吹吹风的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310265V#021F嗯嗯，天气正好，\n',
            '我也顺便放松一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310266V休养生息以备随时出动，\n',
            '也是我们游击士的工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310267V特别是像这次一样的\n',
            '空闲时间就更不能白白浪费了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310268V#1002F嗯，我明白的，\n',
            '不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310269V雪拉姐觉得此次的作战\n',
            '会失败吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310270V#020F这个嘛，该怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310271V嗯，从常识上考虑的话，\n',
            '成功的可能性比较高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310272V毕竟昂贵的警备艇\n',
            '也出动了１２艘之多嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310273V任凭古代龙多么厉害，\n',
            '我想也难以逃脱才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310274V#1015F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310275V这次摩尔根将军也\n',
            '胜券在握的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310276V#027F不过，这单纯\n',
            '只是表面上的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310277V对于让游击士同行这件事，\n',
            '原本会有不少反对的声音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310278V但将军却抛开这些意见\n',
            '而允许我们一起同行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310279V#1002F……代表摩尔根将军\n',
            '心中也有所不安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310280V#020F会这么想也很合理吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310281V#525F嗯，正因为这样，\n',
            '现在才要放松一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310282V#1007F呼，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310283V那我也\n',
            '继续散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310284V#021F呵呵，就这么办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310285V毕竟搭乘王家飞船的机会\n',
            '可是很难得的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310286V#1006F嗯……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310287V那我走了，雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030310288V#020F嗯嗯，待会儿见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A1F)

    Jump('loc_2311')

    def _loc_226B(): pass

    label('loc_226B')

    ChrTalk(
        0x000B,
        (
            '#0030310289V#020F既然让我们同行，\n',
            '说明将军也有所不安哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310290V为了随时随地可以出动，\n',
            '必须事先做好准备才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030310291V不过，在那之前\n',
            '就先尽情放松吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2311(): pass

    label('loc_2311')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x2315
@scena.Code('func_07_2315')
def func_07_2315():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_28FF',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_237D'),
        (0x00000001, 'loc_28D0'),
        (0x00000002, 'loc_28FC'),
        (-1, 'loc_28FF'),
    )

    def _loc_237D(): pass

    label('loc_237D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_28CD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 6, 0x1E46)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_282D',
    )

    OP_4A(0x000A, 255)

    ChrTalk(
        0x000A,
        (
            '#0050341453V#552F下一个执行者是那个小鬼吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050341454V是在王都让我们\n',
            '吃尽苦头的对手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341455V#1002F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341456V那个巨大的人形兵器……\n',
            '这次也会出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341457V#1043F要看他们的战术而定，\n',
            '目前来说很难判断……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341458V#1043F但即使对手只有玲一个人\n',
            '必定也将会是一场严峻的战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341459V#1035F如果是面对面作战的话，\n',
            '她的实力应该在我之上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    @scena.Lambda('lambda_2529')
    def lambda_2529():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2529)

    Sleep(120)

    @scena.Lambda('lambda_253C')
    def lambda_253C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_253C)

    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010341460V#1020F约、约修亚之上……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341461V别，别开玩笑啦。\n',
            '再加上那样的人形兵器的话…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341462V#1035F和以隐密行动为主的我不同，\n',
            '玲可以说是万能型的执行者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341463V当然也拥有着能够\n',
            '独力排除敌人的战斗力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2683',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341464V#072F唔，看来下一个也不能大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272D')

    def _loc_2683(): pass

    label('loc_2683')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26BD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341465V#022F原来如此，说得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272D')

    def _loc_26BD(): pass

    label('loc_26BD')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26FA',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341466V#1064F呵～不愧是执行者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_272D')

    def _loc_26FA(): pass

    label('loc_26FA')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_272D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341467V#065F怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_272D(): pass

    label('loc_272D')

    ChrTalk(
        0x000A,
        (
            '#0050341468V#051F哼，求之不得啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050341469V我可要好好地\n',
            '教导一下那个小鬼来作为回礼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050341470V我随时都可以帮忙……\n',
            '需要的话就说一声吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010341471V#1006F嗯，谢谢。\n',
            '那就拜托了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341472V#1040F到时\n',
            '就请多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E46)

    Jump('loc_28CD')

    def _loc_282D(): pass

    label('loc_282D')

    ChrTalk(
        0x000A,
        (
            '#0050341473V#053F下一个对手是那个小鬼吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050341474V#051F我可要好好地\n',
            '教导一下那个小鬼来作为回礼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050341475V需要我的力量的话，\n',
            '随时来找我就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28CD(): pass

    label('loc_28CD')

    Jump('loc_28FF')

    def _loc_28D0(): pass

    label('loc_28D0')

    ChrTalk(
        0x000A,
        (
            '#0050340459V#050F要更换成员了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000C)

    Jump('loc_28FF')

    def _loc_28FC(): pass

    label('loc_28FC')

    Jump('loc_28FF')

    def _loc_28FF(): pass

    label('loc_28FF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x2903
@scena.Code('func_08_2903')
def func_08_2903():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_2DDC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C4, 6, 0x1E26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CDE',
    )

    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '#0060341501V#047F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341502V#1026F科洛丝……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29D8',
    )

    ChrTalk(
        0x0009,
        (
            '#0060341503V#043F啊，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060341504V#047F没什么，在想些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A24')

    def _loc_29D8(): pass

    label('loc_29D8')

    ChrTalk(
        0x0009,
        (
            '#0060341505V#043F啊，大家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060341504V#047F没什么，在想些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A24(): pass

    label('loc_2A24')

    ChrTalk(
        0x0101,
        (
            '#0010341507V#1003F……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341508V嗯……\n',
            '果然还是会烦恼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0060341509V#043F……对不起，在这种时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341510V#1000F哪里的话，你不用介意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341511V而且之前还是我\n',
            '害得大家一直在担心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341512V#1007F不过，我倒觉得一切\n',
            '都是某人的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341513V#1048F……是是，我会反省。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0060341514V#048F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341515V#1008F所以，科洛丝\n',
            '完全没必要在意这些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341516V困难的时候要互相帮助嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0060341517V#040F谢谢你，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060341518V不过，如果需要我的话\n',
            '请马上跟我说哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060341519V虽然力量微薄，\n',
            '但也请让我帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341520V#1006F嗯，当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341521V#1040F到时要麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0060341522V#041F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0010)
    OP_A2(0x1E26)

    Jump('loc_2DDC')

    def _loc_2CDE(): pass

    label('loc_2CDE')

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2D3C'),
        (0x00000001, 'loc_2DA2'),
        (0x00000002, 'loc_2DD9'),
        (-1, 'loc_2DDC'),
    )

    def _loc_2D3C(): pass

    label('loc_2D3C')

    ChrTalk(
        0x0009,
        (
            '#0060341523V#040F需要我的力量的话，\n',
            '请随时跟我说哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060341524V那么，请各位\n',
            '一定要小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DDC')

    def _loc_2DA2(): pass

    label('loc_2DA2')

    ChrTalk(
        0x0009,
        (
            '#0060340422V#040F明白了。\n',
            '要更换成员是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000C)

    Jump('loc_2DDC')

    def _loc_2DD9(): pass

    label('loc_2DD9')

    Jump('loc_2DDC')

    def _loc_2DDC(): pass

    label('loc_2DDC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x2DE0
@scena.Code('func_09_2DE0')
def func_09_2DE0():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2E41'),
        (0x00000001, 'loc_328D'),
        (0x00000002, 'loc_32B9'),
        (-1, 'loc_32BC'),
    )

    def _loc_2E41(): pass

    label('loc_2E41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 2, 0x1E42)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3227',
    )

    ChrTalk(
        0x0008,
        (
            '#0070340610V#060F啊，姐姐，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341478V#1011F咦，提妲……\n',
            '你怎么在甲板上？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0070341479V#063F嗯、嗯，我听说\n',
            '蔡斯被袭击了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070341480V不知道在城里的人们……\n',
            '是否平安呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341481V#1003F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341482V#1040F没问题，别担心啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341483V蔡斯离雷斯顿要塞很近，\n',
            '守备队的战力也很充足。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341484V而且协会里\n',
            '也有雾香在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341485V万一有事\n',
            '她应该会想办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341486V#1015F嗯，的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341487V一想到有雾香小姐在\n',
            '感觉就安心许多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0070341488V#560F嘿嘿，是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070341489V#067F嗯，一下子\n',
            '就感觉放松多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341490V#1040F我们如果能压制住塔\n',
            '城里的敌人应该也会撤退的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341491V毕竟城镇里发生的那些异变，\n',
            '应该都是配合塔的佯攻才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341492V#1002F这么说来，可不能\n',
            '再磨磨蹭蹭了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341493V#070F嗯，就是这样。\n',
            '马上过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341494V#1040F嗯嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341495V那么，提妲，我们先走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0070341496V#060F啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070341497V哥哥你们也\n',
            '要多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E42)

    Jump('loc_328A')

    def _loc_3227(): pass

    label('loc_3227')

    ChrTalk(
        0x0008,
        (
            '#0070341498V#060F我就待在这里，\n',
            '有需要帮忙的话尽管说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070341499V那么……\n',
            '大家都要当心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_328A(): pass

    label('loc_328A')

    Jump('loc_32BC')

    def _loc_328D(): pass

    label('loc_328D')

    ChrTalk(
        0x0008,
        (
            '#0070340636V#060F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000C)

    Jump('loc_32BC')

    def _loc_32B9(): pass

    label('loc_32B9')

    Jump('loc_32BC')

    def _loc_32BC(): pass

    label('loc_32BC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x32C0
@scena.Code('func_0A_32C0')
def func_0A_32C0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_337E',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，是各位游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我研究上遇到一些困难。\n',
            '试着来转换一下心情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说那个塔的异样情况\n',
            '到底是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真担心在卢安的弟弟。\n',
            '城镇能平安无事就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_33DE')

    def _loc_337E(): pass

    label('loc_337E')

    ChrTalk(
        0x00FE,
        (
            '话说那个塔的异样情况\n',
            '到底是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真担心在卢安的弟弟。\n',
            '城镇能平安无事就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33DE(): pass

    label('loc_33DE')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x33E2
@scena.Code('func_0B_33E2')
def func_0B_33E2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 6, 0x10BE)),
            Expr.Return,
        ),
        'loc_343E',
    )

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '呼啊～～喵呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_343B',
    )

    ChrTalk(
        0x0105,
        (
            '#040F看来好像在这里\n',
            '晒太阳的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_343B(): pass

    label('loc_343B')

    Jump('loc_371E')

    def _loc_343E(): pass

    label('loc_343E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C9, 4, 0x1E4C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3587',
    )

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1004F啊，安东尼！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34E5',
    )

    ChrTalk(
        0x0107,
        (
            '#067F嘿嘿嘿……\n',
            '很吃惊吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不管怎么看\n',
            '都像是雷伊哥哥带来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_350E')

    def _loc_34E5(): pass

    label('loc_34E5')

    ChrTalk(
        0x0102,
        (
            '#1044F是中央工房的人\n',
            '带来的吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_350E(): pass

    label('loc_350E')

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F嗯～为什么会在\n',
            '这种紧张的场合下再次见面呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F嗯，不管怎么说\n',
            '这阵子还请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E4C)

    Jump('loc_35AC')

    def _loc_3587(): pass

    label('loc_3587')

    ChrTalk(
        0x0101,
        (
            '#1001F安东尼，\n',
            '你在这里做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_35AC(): pass

    label('loc_35AC')

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喵呜喵呜喵呜喵呜咪！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F哈哈，好像\n',
            '在说什么似的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36FD',
    )

    ChrTalk(
        0x0105,
        (
            '#044F……看起来好像\n',
            '想交给我们什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喵嗄！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F啊……\n',
            '这本书要给我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 10卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 10卷'], 1)
    OP_A2(0x10BE)

    ChrTalk(
        0x0105,
        (
            '#048F呵呵，谢谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '咕喵～咕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F真、真不简单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_371E')

    def _loc_36FD(): pass

    label('loc_36FD')

    ChrTalk(
        0x0101,
        (
            '#1016F有人懂\n',
            '动物的语言吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_371E(): pass

    label('loc_371E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x3722
@scena.Code('func_0C_3722')
def func_0C_3722():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_376E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_3750',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0xFFFF,
        ),
    )

    Jump('loc_376B')

    def _loc_3750(): pass

    label('loc_3750')

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    def _loc_376B(): pass

    label('loc_376B')

    Jump('loc_37EC')

    def _loc_376E(): pass

    label('loc_376E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_3791',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    Jump('loc_37EC')

    def _loc_3791(): pass

    label('loc_3791')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_37B2',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_37EC')

    def _loc_37B2(): pass

    label('loc_37B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_37D3',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x0007,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0008,
            0xFFFF,
        ),
    )

    Jump('loc_37EC')

    def _loc_37D3(): pass

    label('loc_37D3')

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    def _loc_37EC(): pass

    label('loc_37EC')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_3822',
    )

    Jump('loc_38EF')

    def _loc_3822(): pass

    label('loc_3822')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_3856',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3853',
    )

    SetChrPos(0x000A, -60, 3000, 19860, 0)
    ClearChrFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x06, 0x0002)

    def _loc_3853(): pass

    label('loc_3853')

    Jump('loc_38EF')

    def _loc_3856(): pass

    label('loc_3856')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_3860',
    )

    Jump('loc_38EF')

    def _loc_3860(): pass

    label('loc_3860')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_3894',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3891',
    )

    SetChrPos(0x0008, 3490, 1500, -6210, 90)
    ClearChrFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x06, 0x0002)

    def _loc_3891(): pass

    label('loc_3891')

    Jump('loc_38EF')

    def _loc_3894(): pass

    label('loc_3894')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_38EF',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_38C5',
    )

    SetChrPos(0x000B, -1920, 1500, -9370, 270)
    ClearChrFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x06, 0x0002)

    def _loc_38C5(): pass

    label('loc_38C5')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_38EF',
    )

    SetChrPos(0x0009, 2300, 2500, 14260, 90)
    ClearChrFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x00, 0x06, 0x0002)

    def _loc_38EF(): pass

    label('loc_38EF')

    Return()

# id: 0x000D offset: 0x38F0
@scena.Code('func_0D_38F0')
def func_0D_38F0():
    EventBegin(0x00)
    Call(0, 0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 3, 0x1E03)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3904',
    )

    OP_A2(0x10F0)

    Jump('loc_3907')

    def _loc_3904(): pass

    label('loc_3904')

    OP_A2(0x10F1)

    def _loc_3907(): pass

    label('loc_3907')

    NewScene('ED6_DT21/R0303._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x3911
@scena.Code('func_0E_3911')
def func_0E_3911():
    EventBegin(0x00)
    Call(0, 0x001C)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R3104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x3924
@scena.Code('func_0F_3924')
def func_0F_3924():
    EventBegin(0x00)
    Call(0, 0x001C)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R2401._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x3937
@scena.Code('func_10_3937')
def func_10_3937():
    EventBegin(0x00)
    Call(0, 0x001C)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/R1402._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x394A
@scena.Code('func_11_394A')
def func_11_394A():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(70, 2500, 10950, 0)
    OP_67(0, 8380, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(414, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x0000003B)
    OP_73(0x0001)
    Sleep(500)

    @scena.Lambda('lambda_39C3')
    def lambda_39C3():
        OP_6D(600, 2500, 15570, 6500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_39C3)

    @scena.Lambda('lambda_39DB')
    def lambda_39DB():
        OP_67(0, 6000, -10000, 6500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_39DB)

    @scena.Lambda('lambda_39F3')
    def lambda_39F3():
        OP_6E(262, 6500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_39F3)

    CreateThread(0x0101, 0x01, 0x00, 0x0012)
    CreateThread(0x0102, 0x01, 0x00, 0x0013)
    CreateThread(0x000B, 0x01, 0x00, 0x0014)
    CreateThread(0x000A, 0x01, 0x00, 0x0015)
    CreateThread(0x0008, 0x01, 0x00, 0x0016)
    CreateThread(0x000C, 0x01, 0x00, 0x0017)
    CreateThread(0x000D, 0x01, 0x00, 0x0018)
    CreateThread(0x0009, 0x01, 0x00, 0x0019)
    CreateThread(0x000F, 0x01, 0x00, 0x001A)
    CreateThread(0x000E, 0x01, 0x00, 0x001B)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010341828V#1000F哪、哪里……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341829V#1030F从前方甲板\n',
            '看得最清楚的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    OP_8C(0x000D, 270, 400)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0180341830V#1060F……就是那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3AFB')
    def lambda_3AFB():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3AFB)

    @scena.Lambda('lambda_3B09')
    def lambda_3B09():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3B09)

    Sleep(50)

    @scena.Lambda('lambda_3B1C')
    def lambda_3B1C():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3B1C)

    @scena.Lambda('lambda_3B2A')
    def lambda_3B2A():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3B2A)

    Sleep(40)

    @scena.Lambda('lambda_3B3D')
    def lambda_3B3D():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3B3D)

    @scena.Lambda('lambda_3B4B')
    def lambda_3B4B():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3B4B)

    Sleep(50)

    @scena.Lambda('lambda_3B5E')
    def lambda_3B5E():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B5E)

    @scena.Lambda('lambda_3B6C')
    def lambda_3B6C():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3B6C)

    Sleep(40)

    @scena.Lambda('lambda_3B7F')
    def lambda_3B7F():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3B7F)

    @scena.Lambda('lambda_3B8D')
    def lambda_3B8D():
        OP_6D(-1820, 2500, 15470, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3B8D)

    @scena.Lambda('lambda_3BA5')
    def lambda_3BA5():
        OP_6C(340000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3BA5)

    Sleep(3500)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '◆浮游都市出现的过场动画',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xFF, 0x80, 0x00, 0x00000000)
    OP_6D(600, 2500, 15570, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6E(262, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010341831V#1000F什、什、什……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0060341832V#040F难不成那就是……\n',
            '……那座巨大的都市是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341833V#1030F嗯……不会错的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180341834V#1060F『辉之环』……\n',
            '是辉之环啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0540341835V#100F──糟糕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x000F, 400)
    Sleep(600)

    ChrTalk(
        0x000E,
        (
            '#0540341836V#100F尤莉亚上尉！\n',
            '赶快让军舰降落！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0100341837V#170F……咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0540341838V#100F卡西乌斯不是下达过\n',
            '紧急指令吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341839V再不快点的话就来不及了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0100341840V#170F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '◆浮游都市波浪扩散导力停止的过场动画',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/C5408._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x3E5D
@scena.Code('func_12_3E5D')
def func_12_3E5D():
    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -550, 3000, 17800, 4000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)
    OP_8C(0x00FE, 270, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)
    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)
    OP_8C(0x00FE, 270, 400)
    Sleep(500)

    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x3ED4
@scena.Code('func_13_3ED4')
def func_13_3ED4():
    Sleep(500)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 570, 3000, 17300, 4000, 0x00)

    Return()

# id: 0x0014 offset: 0x3F04
@scena.Code('func_14_3F04')
def func_14_3F04():
    Sleep(1000)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 960, 3000, 16410, 4000, 0x00)

    Return()

# id: 0x0015 offset: 0x3F34
@scena.Code('func_15_3F34')
def func_15_3F34():
    Sleep(1500)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -1840, 3000, 16660, 4000, 0x00)

    Return()

# id: 0x0016 offset: 0x3F64
@scena.Code('func_16_3F64')
def func_16_3F64():
    Sleep(2000)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 1260, 2500, 14840, 4000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x0017 offset: 0x3F9B
@scena.Code('func_17_3F9B')
def func_17_3F9B():
    Sleep(2500)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -350, 2500, 15420, 4000, 0x00)

    Return()

# id: 0x0018 offset: 0x3FCB
@scena.Code('func_18_3FCB')
def func_18_3FCB():
    Sleep(3000)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -2000, 2500, 14410, 4000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x0019 offset: 0x4002
@scena.Code('func_19_4002')
def func_19_4002():
    Sleep(3500)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -1100, 2500, 13410, 4000, 0x00)

    Return()

# id: 0x001A offset: 0x4032
@scena.Code('func_1A_4032')
def func_1A_4032():
    Sleep(4000)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 930, 2500, 12170, 4000, 0x00)

    Return()

# id: 0x001B offset: 0x4062
@scena.Code('func_1B_4062')
def func_1B_4062():
    Sleep(4500)

    SetChrPos(0x00FE, 100, 2500, 7780, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -140, 2500, 12500, 4000, 0x00)

    Return()

# id: 0x001C offset: 0x4092
@scena.Code('func_1C_4092')
def func_1C_4092():
    OP_6D(-1900, -9600, -11180, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(-550, -9330, -8150, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(48000, 0)
    OP_6E(262, 0)
    OP_72(0x0004, 0x0004)
    OP_A1(0x0014, 0x0004)
    SetChrPos(0x0014, 0, -7600, -7600, 0)
    SetChrPos(0x0101, -550, -7600, -8150, 270)
    SetChrPos(0x0102, 550, -7600, -8150, 270)
    SetChrPos(0x00F8, -550, -7600, -7050, 270)
    SetChrPos(0x00F9, 550, -7600, -7050, 270)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    SetChrFlags(0x0101, 0x0020)
    SetChrFlags(0x0102, 0x0020)
    SetChrFlags(0x00F8, 0x0020)
    SetChrFlags(0x00F9, 0x0020)

    @scena.Lambda('lambda_4199')
    def lambda_4199():
        OP_67(0, 4700, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4199)

    @scena.Lambda('lambda_41B1')
    def lambda_41B1():
        OP_91(0x00FE, 0, -20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_41B1)

    @scena.Lambda('lambda_41CC')
    def lambda_41CC():
        OP_91(0x00FE, 0, -20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_41CC)

    @scena.Lambda('lambda_41E7')
    def lambda_41E7():
        OP_91(0x00FE, 0, -20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_41E7)

    @scena.Lambda('lambda_4202')
    def lambda_4202():
        OP_91(0x00FE, 0, -20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4202)

    @scena.Lambda('lambda_421D')
    def lambda_421D():
        OP_91(0x00FE, 0, -20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_421D)

    ClearMapFlags(0x00100000)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(2000)

    Return()

# id: 0x001D offset: 0x4257
@scena.Code('func_1D_4257')
def func_1D_4257():
    EventBegin(0x00)
    OP_67(0, 4700, -10000, 0)
    OP_6D(-550, -9330, -8150, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(48000, 0)
    OP_6E(262, 0)
    OP_72(0x0004, 0x0004)
    OP_A1(0x0014, 0x0004)
    SetChrPos(0x0014, 0, -17600, -7600, 0)
    SetChrPos(0x0101, -550, -17600, -8150, 270)
    SetChrPos(0x0102, 550, -17600, -8150, 270)
    SetChrPos(0x00F8, -550, -17600, -7050, 270)
    SetChrPos(0x00F9, 550, -17600, -7050, 270)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    SetChrFlags(0x0101, 0x0020)
    SetChrFlags(0x0102, 0x0020)
    SetChrFlags(0x00F8, 0x0020)
    SetChrFlags(0x00F9, 0x0020)

    @scena.Lambda('lambda_4334')
    def lambda_4334():
        OP_6D(-550, -9330, -8150, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4334)

    @scena.Lambda('lambda_434C')
    def lambda_434C():
        OP_91(0x00FE, 0, 20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_434C)

    @scena.Lambda('lambda_4367')
    def lambda_4367():
        OP_91(0x00FE, 0, 20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4367)

    @scena.Lambda('lambda_4382')
    def lambda_4382():
        OP_91(0x00FE, 0, 20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4382)

    @scena.Lambda('lambda_439D')
    def lambda_439D():
        OP_91(0x00FE, 0, 20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_439D)

    @scena.Lambda('lambda_43B8')
    def lambda_43B8():
        OP_91(0x00FE, 0, 20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_43B8)

    SetMapFlags(0x00100000)
    OP_22(0x0068, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(2000)

    OP_23(0x01C3)
    OP_23(0x0075)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0313._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
