import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4400   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拉利'),
    TXT(0x02, '游客'),
    TXT(0x03, '游客'),
    TXT(0x04, '游客'),
    TXT(0x05, '港口工人'),
    TXT(0x06, '港口工人'),
    TXT(0x07, '港口工人'),
    TXT(0x08, '作业员'),
    TXT(0x09, '作业员'),
    TXT(0x0A, '港口工人'),
    TXT(0x0B, '王都格兰赛尔·西街区'),
    TXT(0x0C, '王都格兰赛尔·码头北'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4400.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1506
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
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT06/CH20159._CH', 'ED6_DT06/CH20159P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -8750,
            z                   = 0,
            y                   = -3530,
            direction           = 268,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 22130,
            z                   = 0,
            y                   = -5230,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 24260,
            z                   = 0,
            y                   = -5500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 23230,
            z                   = 0,
            y                   = -5500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 13390,
            z                   = 0,
            y                   = 2850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 14890,
            z                   = 0,
            y                   = 2850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -22680,
            z                   = 0,
            y                   = -15490,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -18690,
            z                   = 0,
            y                   = 6110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -17670,
            z                   = 0,
            y                   = 7510,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -15960,
            z                   = 0,
            y                   = 25420,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 60310,
            z                   = 0,
            y                   = -1230,
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
            x                   = -9950,
            z                   = 0,
            y                   = 71270,
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

# id: 0x10003 offset: 0x27A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x27A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x27A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x27A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2AD',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0010, -14520, 0, -5650, 262)

    def _loc_2AD(): pass

    label('loc_2AD')

    Jump('loc_2BC')

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2BC',
    )

    SetChrFlags(0x0010, 0x0010)

    def _loc_2BC(): pass

    label('loc_2BC')

    Return()

# id: 0x0001 offset: 0x2BD
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE3AE0, 0xFFFE69C0, 0x0023006D)
    OP_22(0x01C5, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F4',
    )

    OP_B1('t4400_y')

    Jump('loc_2FD')

    def _loc_2F4(): pass

    label('loc_2F4')

    OP_B1('t4400_n')

    def _loc_2FD(): pass

    label('loc_2FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_317',
    )

    OP_72(0x000C, 0x0004)

    def _loc_317(): pass

    label('loc_317')

    OP_71(0x000B, 0x0004)
    OP_1C(0x03, 0x00, 0x000E)

    Return()

# id: 0x0002 offset: 0x322
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_347',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_489')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_360',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_489')

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_379',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_489')

    def _loc_379(): pass

    label('loc_379')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_392',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_489')

    def _loc_392(): pass

    label('loc_392')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AB',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_489')

    def _loc_3AB(): pass

    label('loc_3AB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C4',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_489')

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DD',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_489')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F6',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_489')

    def _loc_3F6(): pass

    label('loc_3F6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40F',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_489')

    def _loc_40F(): pass

    label('loc_40F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_428',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_489')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_441',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_489')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45A',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_489')

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_473',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_489')

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_489',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_489(): pass

    label('loc_489')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_49E',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_489')

    def _loc_49E(): pass

    label('loc_49E')

    Return()

# id: 0x0003 offset: 0x49F
@scena.Code('func_03_49F')
def func_03_49F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4C7',
    )

    OP_8D(0x00FE, -8750, -2900, -6330, -5850, 1500)
    Sleep(2000)

    Jump('func_03_49F')

    def _loc_4C7(): pass

    label('loc_4C7')

    Return()

# id: 0x0004 offset: 0x4C8
@scena.Code('func_04_4C8')
def func_04_4C8():
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_588',
    )

    ChrTalk(
        0x00FE,
        (
            '搬，搬运车无法开动\n',
            '就得用手搬运行李了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但是要搬运的行李\n',
            '都没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作能偷懒真幸运，\n',
            '现在可不是说这种话的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我，我的工资\n',
            '和三餐怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_588(): pass

    label('loc_588')

    Jump('loc_A73')

    def _loc_58B(): pass

    label('loc_58B')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A73',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_69B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5CB',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，当天不是夜班\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_698')

    def _loc_5CB(): pass

    label('loc_5CB')

    ChrTalk(
        0x00FE,
        (
            '事务所被袭击\n',
            '丹克和菲利奥\n',
            '似乎都很惨的样子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他、他们又没做坏事\n',
            '不觉得很可怜吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我当天\n',
            '不在事务所真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽、虽然也有过\n',
            '一点点这种念头，\n',
            '但那实在太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_698(): pass

    label('loc_698')

    Jump('loc_A73')

    def _loc_69B(): pass

    label('loc_69B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_7E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_705',
    )

    ChrTalk(
        0x00FE,
        (
            '我，我在这里工作\n',
            '只是吃点粗茶淡饭的\n',
            '无力的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但是勉强\n',
            '也算幸福的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E3')

    def _loc_705(): pass

    label('loc_705')

    ChrTalk(
        0x00FE,
        (
            '在找穿白裙子的女孩……？\n',
            '难、难道是什么事件吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我，我在这里工作\n',
            '只是吃点粗茶淡饭的\n',
            '无力的存在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但是勉强\n',
            '也算幸福的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个，偶然\n',
            '也会想和\n',
            '女孩子约会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但那种事\n',
            '怎么可能说出口嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_7E3(): pass

    label('loc_7E3')

    Jump('loc_A73')

    def _loc_7E6(): pass

    label('loc_7E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_832',
    )

    ChrTalk(
        0x00FE,
        (
            '反而……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '变得很、很成熟的样子\n',
            '真让人憧憬啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C2')

    def _loc_832(): pass

    label('loc_832')

    ChrTalk(
        0x00FE,
        (
            '今、今天我\n',
            '也要努力工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这种日子\n',
            '反而更让人想\n',
            '努力工作啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但是我\n',
            '也没喝过酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱，抱歉……\n',
            '只是想说说看而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_8C2(): pass

    label('loc_8C2')

    Jump('loc_A73')

    def _loc_8C5(): pass

    label('loc_8C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_952',
    )

    ChrTalk(
        0x00FE,
        (
            '你、你可别说出去，我本来\n',
            '想在飞船公社工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但、但是，不觉得很过分吗？\n',
            '那里竞争太激烈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我，我实在\n',
            '太没胆了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A73')

    def _loc_952(): pass

    label('loc_952')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_A73',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9AD',
    )

    ChrTalk(
        0x00FE,
        (
            '本、本来想摆摆\n',
            '前辈的架子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但对人生的前辈\n',
            '怎么可能那样做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A73')

    def _loc_9AD(): pass

    label('loc_9AD')

    ChrTalk(
        0x00FE,
        (
            '我、我在这里工作\n',
            '已经快两年了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近有了后辈\n',
            '稍、稍微有点迷惑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因、因为、又比我年纪大，\n',
            '还结了婚的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本、本来想摆摆\n',
            '前辈的架子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但对人生的前辈\n',
            '怎么可能那样做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_A73(): pass

    label('loc_A73')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xA77
@scena.Code('func_05_A77')
def func_05_A77():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A89',
    )

    Jump('loc_B68')

    def _loc_A89(): pass

    label('loc_A89')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_A9F',
    )

    Jump('loc_B68')

    def _loc_A9F(): pass

    label('loc_A9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_ADA',
    )

    ChrTalk(
        0x00FE,
        (
            '啊哈哈……\n',
            '和这些孩子们在一起就不会无聊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B68')

    def _loc_ADA(): pass

    label('loc_ADA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AFE',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，该回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B68')

    def _loc_AFE(): pass

    label('loc_AFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_B47',
    )

    ChrTalk(
        0x00FE,
        (
            '只是带到港口来\n',
            '竟然都这么高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么轻松真是得救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B68')

    def _loc_B47(): pass

    label('loc_B47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_B68',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～真是漂亮的湖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B68(): pass

    label('loc_B68')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xB6C
@scena.Code('func_06_B6C')
def func_06_B6C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B7E',
    )

    Jump('loc_C4C')

    def _loc_B7E(): pass

    label('loc_B7E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_B94',
    )

    Jump('loc_C4C')

    def _loc_B94(): pass

    label('loc_B94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_BC1',
    )

    ChrTalk(
        0x00FE,
        (
            '都说啦～！\n',
            '这里不是海是湖！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4C')

    def _loc_BC1(): pass

    label('loc_BC1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BEC',
    )

    ChrTalk(
        0x00FE,
        (
            '咦～我\n',
            '觉得还是肉好啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4C')

    def _loc_BEC(): pass

    label('loc_BEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_C2F',
    )

    ChrTalk(
        0x00FE,
        (
            '与其看鱼\n',
            '我更想看海鸥啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，但是这里是湖吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4C')

    def _loc_C2F(): pass

    label('loc_C2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_C4C',
    )

    ChrTalk(
        0x00FE,
        (
            '我喜欢这个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C4C(): pass

    label('loc_C4C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xC50
@scena.Code('func_07_C50')
def func_07_C50():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C62',
    )

    Jump('loc_D1F')

    def _loc_C62(): pass

    label('loc_C62')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_C78',
    )

    Jump('loc_D1F')

    def _loc_C78(): pass

    label('loc_C78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_CAB',
    )

    ChrTalk(
        0x00FE,
        (
            '大～海～啊，好～宽阔，\n',
            '好～大～啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D1F')

    def _loc_CAB(): pass

    label('loc_CAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CDC',
    )

    ChrTalk(
        0x00FE,
        (
            '今天晚饭吃什么呢。\n',
            '我想吃鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D1F')

    def _loc_CDC(): pass

    label('loc_CDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_CFE',
    )

    ChrTalk(
        0x00FE,
        (
            '对了对了，有鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D1F')

    def _loc_CFE(): pass

    label('loc_CFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_D1F',
    )

    ChrTalk(
        0x00FE,
        (
            '我是第一次来港口哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D1F(): pass

    label('loc_D1F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xD23
@scena.Code('func_08_D23')
def func_08_D23():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D56',
    )

    ChrTalk(
        0x00FE,
        (
            '到底什么时候\n',
            '船才能动呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E6C')

    def _loc_D56(): pass

    label('loc_D56')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_D6C',
    )

    Jump('loc_E6C')

    def _loc_D6C(): pass

    label('loc_D6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_DBD',
    )

    ChrTalk(
        0x00FE,
        (
            '这是卢安市长已经确定的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样港口的营业\n',
            '也马上就恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E6C')

    def _loc_DBD(): pass

    label('loc_DBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DFA',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，工作已经结束了。\n',
            '请大家去喝一杯吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E6C')

    def _loc_DFA(): pass

    label('loc_DFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_E26',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，不要急,\n',
            '先做能做的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E6C')

    def _loc_E26(): pass

    label('loc_E26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_E6C',
    )

    ChrTalk(
        0x00FE,
        (
            '差不多该是把仓库\n',
            '整理整齐的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后还会很忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E6C(): pass

    label('loc_E6C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xE70
@scena.Code('func_09_E70')
def func_09_E70():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EA2',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，身体变迟钝真是没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F80')

    def _loc_EA2(): pass

    label('loc_EA2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_EB8',
    )

    Jump('loc_F80')

    def _loc_EB8(): pass

    label('loc_EB8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_EED',
    )

    ChrTalk(
        0x00FE,
        (
            '市长选举，真希望\n',
            '波尔多斯氏能获胜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F80')

    def _loc_EED(): pass

    label('loc_EED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F28',
    )

    ChrTalk(
        0x00FE,
        (
            '最近大概是太忙了\n',
            '总觉得时间过得好快……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F80')

    def _loc_F28(): pass

    label('loc_F28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_F52',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，从哪个仓库开始整理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F80')

    def _loc_F52(): pass

    label('loc_F52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_F80',
    )

    ChrTalk(
        0x00FE,
        (
            '闲着当然不好\n',
            '太忙也是个问题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F80(): pass

    label('loc_F80')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0xF84
@scena.Code('func_0A_F84')
def func_0A_F84():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FE0',
    )

    ChrTalk(
        0x00FE,
        (
            '不能工作，\n',
            '只能钓钓鱼等着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你怎样？\n',
            '垂下钓线就会冷静下来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F7')

    def _loc_FE0(): pass

    label('loc_FE0')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_FF6',
    )

    Jump('loc_10F7')

    def _loc_FF6(): pass

    label('loc_FF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1056',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，给了我鱼竿的人\n',
            '来过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不太清楚\n',
            '但好像是叫钓公师团的团体的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F7')

    def _loc_1056(): pass

    label('loc_1056')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1085',
    )

    ChrTalk(
        0x00FE,
        (
            '现在这时候\n',
            '正是钓鱼的时候！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F7')

    def _loc_1085(): pass

    label('loc_1085')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_10AE',
    )

    ChrTalk(
        0x00FE,
        (
            '工作的间歇\n',
            '能钓鱼也不坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F7')

    def _loc_10AE(): pass

    label('loc_10AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_10F7',
    )

    ChrTalk(
        0x00FE,
        (
            '不认识的人\n',
            '硬把钓竿塞给了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '机会难得，\n',
            '想试着钓钓看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10F7(): pass

    label('loc_10F7')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x10FB
@scena.Code('func_0B_10FB')
def func_0B_10FB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1148',
    )

    ChrTalk(
        0x00FE,
        (
            '……真是的，导力器不能使用\n',
            '我们搞技术的就没法工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126F')

    def _loc_1148(): pass

    label('loc_1148')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_126F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_115E',
    )

    Jump('loc_126F')

    def _loc_115E(): pass

    label('loc_115E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_11B2',
    )

    ChrTalk(
        0x00FE,
        (
            '技术不外传\n',
            '是我的信念……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但如果对方是女孩子\n',
            '忍不住就会教了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126F')

    def _loc_11B2(): pass

    label('loc_11B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11F9',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，是，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，不行不行\n',
            '要严厉要严厉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126F')

    def _loc_11F9(): pass

    label('loc_11F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1245',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，人被称赞\n',
            '心情就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，对后辈\n',
            '还是要严厉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126F')

    def _loc_1245(): pass

    label('loc_1245')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_126F',
    )

    ChrTalk(
        0x00FE,
        (
            '技术是自然\n',
            '就能学到的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126F(): pass

    label('loc_126F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1273
@scena.Code('func_0C_1273')
def func_0C_1273():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12B2',
    )

    ChrTalk(
        0x00FE,
        (
            '哎～怎么\n',
            '不动啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好孩子，快动啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136E')

    def _loc_12B2(): pass

    label('loc_12B2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_136E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_12C8',
    )

    Jump('loc_136E')

    def _loc_12C8(): pass

    label('loc_12C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_12F5',
    )

    ChrTalk(
        0x00FE,
        (
            '前辈，那里的回路\n',
            '该怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136E')

    def _loc_12F5(): pass

    label('loc_12F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1320',
    )

    ChrTalk(
        0x00FE,
        (
            '好厉害啊～\n',
            '好崇拜你～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136E')

    def _loc_1320(): pass

    label('loc_1320')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1342',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～好出色的手法～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136E')

    def _loc_1342(): pass

    label('loc_1342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_136E',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～前辈的技术\n',
            '我真是望尘莫及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_136E(): pass

    label('loc_136E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1372
@scena.Code('func_0D_1372')
def func_0D_1372():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13C8',
    )

    ChrTalk(
        0x00FE,
        (
            '每天都来单位\n',
            '却一直不能工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后，\n',
            '到底会变成怎样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DD')

    def _loc_13C8(): pass

    label('loc_13C8')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_13DE',
    )

    Jump('loc_14DD')

    def _loc_13DE(): pass

    label('loc_13DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1421',
    )

    ChrTalk(
        0x00FE,
        (
            '呼哇～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊糟糕。\n',
            '疏忽大意是受伤的根源。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DD')

    def _loc_1421(): pass

    label('loc_1421')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1452',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～肚子好饿～\n',
            '今天吃什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DD')

    def _loc_1452(): pass

    label('loc_1452')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_14B4',
    )

    ChrTalk(
        0x00FE,
        (
            '好，这个结束了\n',
            '就去休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我们来说身体就是本钱嘛。\n',
            '休息也是很好的工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DD')

    def _loc_14B4(): pass

    label('loc_14B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_14DD',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是仓库街的管理事务所哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14DD(): pass

    label('loc_14DD')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x14E1
@scena.Code('func_0E_14E1')
def func_0E_14E1():
    TalkBegin(0x00FF)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
