import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4312_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4312   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '管家雷蒙德'),
    TXT(0x02, '希德中校'),
    TXT(0x03, '贝尔克副队长'),
    TXT(0x04, '西莫鲁'),
    TXT(0x05, '王国军士兵'),
    TXT(0x06, '妮娜'),
    TXT(0x07, '王国军士兵'),
    TXT(0x08, '王国军士兵'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4312.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3BEC
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
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
    ]

# id: 0x10002 offset: 0xDA
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -9300,
            z                   = 0,
            y                   = 400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 15260,
            z                   = 0,
            y                   = -1160,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 7340,
            z                   = 0,
            y                   = 58660,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -49260,
            z                   = 0,
            y                   = 20160,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -53120,
            z                   = 0,
            y                   = 20160,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10003 offset: 0x1DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 250,
            triggerY            = 70040,
            triggerRange        = 500,
            actorX              = 0,
            actorZ              = 1250,
            actorY              = 70040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1FE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_219',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_216',
    )

    ClearChrFlags(0x000C, 0x0080)

    def _loc_216(): pass

    label('loc_216')

    Jump('loc_2D2')

    def _loc_219(): pass

    label('loc_219')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_254',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 900, 0, 66800, 180)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_2D2')

    def _loc_254(): pass

    label('loc_254')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_299',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 900, 0, 66800, 270)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -840, 0, 66800, 90)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_2D2')

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2B2',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0010)

    Jump('loc_2D2')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 2, 0x1612)),
            Expr.Return,
        ),
        'loc_2C6',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_2D2')

    def _loc_2C6(): pass

    label('loc_2C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 4, 0x160C)),
            Expr.Return,
        ),
        'loc_2D2',
    )

    ClearChrFlags(0x000D, 0x0080)

    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2E8',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0012)

    Jump('loc_30C')

    def _loc_2E8(): pass

    label('loc_2E8')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2F4'),
        (-1, 'loc_30C'),
    )

    def _loc_2F4(): pass

    label('loc_2F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 4, 0x160C)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 5, 0x160D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_309',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    def _loc_309(): pass

    label('loc_309')

    Jump('loc_30C')

    def _loc_30C(): pass

    label('loc_30C')

    Return()

# id: 0x0001 offset: 0x30D
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_318',
    )

    OP_64(0x00, 0x0001)

    def _loc_318(): pass

    label('loc_318')

    Return()

# id: 0x0002 offset: 0x319
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
        'loc_33E',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_480')

    def _loc_33E(): pass

    label('loc_33E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_357',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_480')

    def _loc_357(): pass

    label('loc_357')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_370',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_480')

    def _loc_370(): pass

    label('loc_370')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_389',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_480')

    def _loc_389(): pass

    label('loc_389')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A2',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_480')

    def _loc_3A2(): pass

    label('loc_3A2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BB',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_480')

    def _loc_3BB(): pass

    label('loc_3BB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D4',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_480')

    def _loc_3D4(): pass

    label('loc_3D4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3ED',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_480')

    def _loc_3ED(): pass

    label('loc_3ED')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_406',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_480')

    def _loc_406(): pass

    label('loc_406')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41F',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_480')

    def _loc_41F(): pass

    label('loc_41F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_438',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_480')

    def _loc_438(): pass

    label('loc_438')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_451',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_480')

    def _loc_451(): pass

    label('loc_451')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_46A',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_480')

    def _loc_46A(): pass

    label('loc_46A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_480',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_480(): pass

    label('loc_480')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_495',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_480')

    def _loc_495(): pass

    label('loc_495')

    Return()

# id: 0x0003 offset: 0x496
@scena.Code('func_03_496')
def func_03_496():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_542',
    )

    OP_8E(0x00FE, 15260, 0, -1160, 2000, 0x00)
    OP_8E(0x00FE, -15260, 0, -1160, 2000, 0x00)
    OP_8E(0x00FE, -16660, 0, -2460, 2000, 0x00)
    OP_8E(0x00FE, -16660, 0, -3860, 2000, 0x00)
    OP_8E(0x00FE, -15260, 0, -5100, 2000, 0x00)
    OP_8E(0x00FE, 15260, 0, -5100, 2000, 0x00)
    OP_8E(0x00FE, 16660, 0, -3860, 2000, 0x00)
    OP_8E(0x00FE, 16660, 0, -2460, 2000, 0x00)

    Jump('func_03_496')

    def _loc_542(): pass

    label('loc_542')

    Return()

# id: 0x0004 offset: 0x543
@scena.Code('func_04_543')
def func_04_543():
    TalkBegin(0x0009)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_924',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 7, 0x165F)),
            Expr.Return,
        ),
        'loc_5C4',
    )

    ChrTalk(
        0x0009,
        (
            '#0620271547V#701F签字仪式的警备\n',
            '一定会完成好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271548V如果去柏斯地区\n',
            '一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_921')

    def _loc_5C4(): pass

    label('loc_5C4')

    ChrTalk(
        0x0009,
        (
            '#0620271549V#701F呀、是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271550V此次事件的解决要\n',
            '多谢你们的协助了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271551V也让我向你们道谢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271552V#1000F哪里，我们才是\n',
            '若没有尤莉亚小姐前来\n',
            '真不知道会变成怎样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010271553V希德中校把尤莉亚小姐\n',
            '叫来的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620271554V#701F哈哈，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271555V#703F不过，一切都是有你们\n',
            '配合才能成功的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271556V#701F希望今后军方和协会\n',
            '也能多多协作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271557V特别是在对付『结社』方面，对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271558V#1000F是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620271559V#701F艾丝蒂尔你们\n',
            '现在就要离开王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271560V#1000F嗯，预定接下来要去\n',
            '特务兵出现的柏斯地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620271561V#703F果然，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271562V#700F摩尔根将军似乎也在柏斯\n',
            '开始了大规模的搜索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620271563V你们也要\n',
            '多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271564V#1000F谢谢，希德中校\n',
            '也要在签字仪式的警备上加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620271565V#701F啊啊，谢谢。\n',
            '一定会完成好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x165F)

    def _loc_921(): pass

    label('loc_921')

    Jump('loc_D84')

    def _loc_924(): pass

    label('loc_924')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_CD4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 0, 0x1660)),
            Expr.Return,
        ),
        'loc_9C9',
    )

    ChrTalk(
        0x0009,
        (
            '#0620260398V#703F话说回来没想到情报部\n',
            '居然潜藏在柏斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260399V#700F能够逃过那个摩尔根将军的搜索，\n',
            '潜伏起来真不知是不是该佩服一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD1')

    def _loc_9C9(): pass

    label('loc_9C9')

    ChrTalk(
        0x0009,
        (
            '#0620260398V#703F话说回来没想到情报部\n',
            '居然潜藏在柏斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260399V#700F能够逃过那个摩尔根将军的搜索，\n',
            '潜伏起来真不知是不是该佩服一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220260402V#264F……那个情报部的\n',
            '很擅长躲猫猫吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x012F, 400)

    ChrTalk(
        0x0009,
        (
            '#0620260403V#701F因为他们是为了能在各种\n',
            '状况下都能收集情报\n',
            '而接受过特殊训练的部队嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260404V#700F潜伏在敌阵中的\n',
            '野外生存技术应该也很擅长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220260405V#265F那么，就让玲和特务兵\n',
            '用躲猫猫来决一胜负！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260406V#702F躲、躲猫猫？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x012F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260407V#1016F这、这实在有点勉强呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0101, 400)

    ChrTalk(
        0x012F,
        (
            '#0220260408V#264F哎呀，为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260409V#263F要是躲猫猫\n',
            '玲有自信绝对不会输的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260410V#1015F这个倒确实\n',
            '很可能是玲会赢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260411V#701F哈哈，虽然对不起小姑娘\n',
            '但那些人可不会陪你玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220260412V#267F是吗？\n',
            '真不好玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1660)

    def _loc_CD1(): pass

    label('loc_CD1')

    Jump('loc_D84')

    def _loc_CD4(): pass

    label('loc_CD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_D84',
    )

    ChrTalk(
        0x0009,
        (
            '#0620260413V#700F潜伏起来的情报部\n',
            '余党在这个时期现身……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260414V问题就是这个事件\n',
            '是否和签字仪式有关了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260415V#703F无论如何，都需要\n',
            '再进一步的材料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D84(): pass

    label('loc_D84')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xD88
@scena.Code('func_05_D88')
def func_05_D88():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_E1C',
    )

    ChrTalk(
        0x00FE,
        (
            '发现情报部的\n',
            '据说是２人组合的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是协会的王都支部，\n',
            '说不定会有新的信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们赶快\n',
            '返回格兰赛尔就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E68')

    def _loc_E1C(): pass

    label('loc_E1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_E68',
    )

    ChrTalk(
        0x00FE,
        (
            '现场虽说在柏斯，\n',
            '可能会要求支援哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须保持紧张才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E68(): pass

    label('loc_E68')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0xE6C
@scena.Code('func_06_E6C')
def func_06_E6C():
    TalkBegin(0x000B)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1017',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CB, 6, 0x165E)),
            Expr.Return,
        ),
        'loc_EB3',
    )

    ChrTalk(
        0x00FE,
        (
            '无论如何……这孩子\n',
            '就拜托大家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1014')

    def _loc_EB3(): pass

    label('loc_EB3')

    ChrTurnDirection(0x00FE, 0x012F, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哎呀，那孩子是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于～出来啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#261F哈哈哈，女佣姐姐\n',
            '躲猫猫真好玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#260F玲现在\n',
            '要去协会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在那里等爸爸和妈妈\n',
            '来接我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎……哎呀，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……想玩躲猫猫了，\n',
            '就再来这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会拜托雷蒙德先生的,\n',
            '你想玩多久就陪你多久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#261F真的？\n',
            '谢谢，大姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x165E)

    def _loc_1014(): pass

    label('loc_1014')

    Jump('loc_10F0')

    def _loc_1017(): pass

    label('loc_1017')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 2, 0x1612)),
            Expr.Return,
        ),
        'loc_10F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_107E',
    )

    ChrTalk(
        0x00FE,
        (
            '那孩子真是的，\n',
            '把大人耍着玩～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是出来了要打屁股一百下\n',
            '作为惩罚，哼哼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F0')

    def _loc_107E(): pass

    label('loc_107E')

    ChrTalk(
        0x00FE,
        (
            '嗯～似乎没有\n',
            '藏在这附近呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那孩子真是的，\n',
            '把大人耍着玩～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难不成已经被雷蒙德先生\n',
            '发现了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_10F0(): pass

    label('loc_10F0')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x10F4
@scena.Code('func_07_10F4')
def func_07_10F4():
    TalkBegin(0x000C)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_114D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_114A',
    )

    ChrTalk(
        0x00FE,
        (
            '一直收不到\n',
            '情报真是不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望导力器\n',
            '早日能够使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_114A(): pass

    label('loc_114A')

    Jump('loc_1255')

    def _loc_114D(): pass

    label('loc_114D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1255',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_11D7',
    )

    ChrTalk(
        0x00FE,
        (
            '发生事件那天柏斯\n',
            '似乎连空贼都出现了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼就是那次武术大会\n',
            '赢了不少场的家伙们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望别出大事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1255')

    def _loc_11D7(): pass

    label('loc_11D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1255',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上，去艾尔贝周游道\n',
            '扫荡了一下魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，就是在警备正式化之前\n',
            '类似演习一样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为热身\n',
            '应该正好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1255(): pass

    label('loc_1255')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x1259
@scena.Code('func_08_1259')
def func_08_1259():
    TalkBegin(0x000E)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_130A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_12B4',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校的话，\n',
            '在这个房间里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要去见他的话，\n',
            '请进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_130A')

    def _loc_12B4(): pass

    label('loc_12B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_12F1',
    )

    ChrTalk(
        0x00FE,
        (
            '据说要采取第２种警戒体制，\n',
            '到底发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_130A')

    def _loc_12F1(): pass

    label('loc_12F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_130A',
    )

    ChrTalk(
        0x00FE,
        (
            '工作辛苦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_130A(): pass

    label('loc_130A')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x130E
@scena.Code('func_09_130E')
def func_09_130E():
    TalkBegin(0x000F)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1418',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1370',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，你们和亲卫队配合\n',
            '逮捕了特务兵是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天找希德中校有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1418')

    def _loc_1370(): pass

    label('loc_1370')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_13D6',
    )

    ChrTalk(
        0x00FE,
        (
            '第２种警戒体制……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然是有妨碍\n',
            '签字仪式的家伙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像听到\n',
            '情报部什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1418')

    def _loc_13D6(): pass

    label('loc_13D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1418',
    )

    ChrTalk(
        0x00FE,
        (
            '副队长神色大变，\n',
            '冲进了房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底出什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1418(): pass

    label('loc_1418')

    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0x141C
@scena.Code('func_0A_141C')
def func_0A_141C():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1760',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_14B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1471',
    )

    ChrTalk(
        0x00FE,
        (
            '……嗯～\n',
            '擦的还不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须更加用力的磨！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14B4')

    def _loc_1471(): pass

    label('loc_1471')

    ChrTalk(
        0x00FE,
        (
            '露露露啦⊙\n',
            '露露露啦～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '擦得亮晶晶～⊙\n',
            '心情够舒畅～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_14B4(): pass

    label('loc_14B4')

    Jump('loc_1760')

    def _loc_14B7(): pass

    label('loc_14B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 4, 0x160C)),
            Expr.Return,
        ),
        'loc_1760',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1516',
    )

    ChrTalk(
        0x00FE,
        (
            '这里是举行互不侵犯条约签字仪式\n',
            '的纹章之间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以自然鼓起劲\n',
            '打扫了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1760')

    def _loc_1516(): pass

    label('loc_1516')

    ChrTalk(
        0x00FE,
        (
            '这里是举行互不侵犯条约签字仪式\n',
            '的纹章之间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F哦～是这样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是的，当天帝国\n',
            '和共和国的大使不用说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我利贝尔王国的代表\n',
            '也都在这里集合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F记得政变的时候来过，\n',
            '不过都没空好好看。',
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
        'loc_16A7',
    )

    ChrTalk(
        0x0105,
        (
            '#048F呵呵，真怀念啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在这里被抓住的我们\n',
            '多亏了大家帮助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在那个时候的房间里举行\n',
            '签字仪式真是感慨良深啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嗯嗯⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F不过看起来\n',
            '真是格调高贵的房间啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16D6')

    def _loc_16A7(): pass

    label('loc_16A7')

    ChrTalk(
        0x0101,
        (
            '#1006F这样重新来看\n',
            '真是格调高贵的房间啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16D6(): pass

    label('loc_16D6')

    ChrTalk(
        0x00FE,
        (
            '是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以自然鼓起劲\n',
            '打扫了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈，虽然我不擅长打扫,\n',
            '但很明白这种心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1001F那么，加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1760(): pass

    label('loc_1760')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x1764
@scena.Code('func_0B_1764')
def func_0B_1764():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_177B',
    )

    Call(0, 0x0013)
    Call(0, 0x0014)

    def _loc_177B(): pass

    label('loc_177B')

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 0, 0, -1790, 90)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    OP_69(0x0008, 0x00000000)
    FadeIn(2000, 0)
    CreateThread(0x0008, 0x01, 0x00, 0x000C)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2330240724V唉，不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240725V游击士就要来了,\n',
            '跑去哪里了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0101, 0, 0, -9300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010240726V#1P请问～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_8C(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#2330240727V啊，是是。\n',
            '怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18B2')
    def lambda_18B2():
        OP_6D(630, 0, -3120, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_18B2)

    CreateThread(0x0101, 0x01, 0x00, 0x000D)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, 0x000E)
    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, 0x000F)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, 0x0010)
    WaitForThreadExit(0x00F7, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19A6',
    )

    ChrTalk(
        0x0008,
        (
            '#2330240728V#5P咦！？\n',
            '你们不是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0108, 0x0001)

    ChrTalk(
        0x0108,
        (
            '#0080240729V#070F哟，好久不见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240730V#1016F嘿嘿，你好。\n',
            '看来记着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19FF')

    def _loc_19A6(): pass

    label('loc_19A6')

    ChrTalk(
        0x0008,
        (
            '#2330240731V#5P咦！？\n',
            '记得你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240730V#1016F嘿嘿，你好。\n',
            '看来记着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19FF(): pass

    label('loc_19FF')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BD4',
    )

    ChrTalk(
        0x0008,
        (
            '#2330240733V#5P哈哈、怎么可能忘记嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240734V#5P怎么说都是把艾尔贝离宫\n',
            '解放了的恩人嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0105, 400)

    ChrTalk(
        0x0008,
        (
            '#2330240735V#5P咦，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240736V#542F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240737V#5P呀，哈哈……\n',
            '没那回事啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240738V#5P一定是其他很像的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060240739V#048F呵呵，难不成是\n',
            '错认为你的恋人了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240740V#5P没、没有的事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2330240741V#5P嗯，那么你们\n',
            '是接受委托的游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C6F')

    def _loc_1BD4(): pass

    label('loc_1BD4')

    ChrTalk(
        0x0008,
        (
            '#2330240733V#5P哈哈、怎么可能忘记嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240743V#5P怎么说都是把艾尔贝离宫\n',
            '解放了的恩人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240744V#5P那么你们\n',
            '是接受委托的游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C6F(): pass

    label('loc_1C6F')

    ChrTalk(
        0x0101,
        (
            '#0010240745V#1011F嗯，是没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240746V到底怎么了？\n',
            '似乎有什么难处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240747V#5P那是……\n',
            '那个迷路的孩子的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240748V#5P突然说『玩躲猫猫吧』,\n',
            '然后就不见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240749V#5P我正在拼命找她呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240750V#1016F哎呀呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240751V#5P马、马上就会找到的,\n',
            '你们在谈话室等等哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240752V#5P知道地点吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240753V#1015F那倒是记得……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240754V看来你似乎陷入苦战了呢,\n',
            '要我们也帮忙找吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240755V#5P咦……这好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EC2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240756V#051F嗯，这也算是\n',
            '上了贼船了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240757V说一下那小鬼的名字和特征吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F2D')

    def _loc_1EC2(): pass

    label('loc_1EC2')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F2D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240758V#021F呵呵……\n',
            '打铁就要趁热。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240759V#020F说一下那孩子的名字和特征吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F2D(): pass

    label('loc_1F2D')

    ChrTalk(
        0x0008,
        (
            '#2330240760V#5P帮、帮大忙了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240761V#5P穿着轻飘飘的白裙子,\n',
            '头上扎着黑色的丝带\n',
            '１０岁左右的女孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240762V#5P就是不知道叫什么名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240763V#1004F不知道名字？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240764V#5P我怎么问她都说是『秘·密』\n',
            '就是不告诉我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240765V#5P以为她是和家人一起来的,\n',
            '可也找不到类似的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240766V#5P实在是发愁\n',
            '就向协会求助了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240767V#1016F是、是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240768V#1000F不过爱玩躲猫猫\n',
            '应该是挺精神的女孩子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240769V#5P嗯～说精神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240770V#5P倒是有点小大人样\n',
            '但又阴晴无常的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240771V#5P把大人耍着玩\n',
            '还觉得很开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21DB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240772V#035F哦哦……\n',
            '喜欢恶作剧的小猫型啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2265')

    def _loc_21DB(): pass

    label('loc_21DB')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2224',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240773V#027F就是那种喜欢恶作剧的\n',
            '小猫类型吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2265')

    def _loc_2224(): pass

    label('loc_2224')

    ChrTalk(
        0x0101,
        (
            '#0010240774V#1015F嗯～就是所谓的\n',
            '喜欢恶作剧的小猫那种感觉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2265(): pass

    label('loc_2265')

    ChrTalk(
        0x0008,
        (
            '#2330240775V#5P对、就是这种感觉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240776V#5P唉～真是的,\n',
            '到底跑哪里去了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240777V#5P大概，没出这栋\n',
            '建筑物吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_237C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240778V#030F这么说，包括中庭在内的\n',
            '所有房间就是搜索对象吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240779V#031F呼，说不定很适合\n',
            '给小猫咪躲猫猫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2484')

    def _loc_237C(): pass

    label('loc_237C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23FC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240780V#070F这么说，包括中庭在内的\n',
            '所有房间就是搜索对象吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240781V确实很适合\n',
            '躲猫猫也不一定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2484')

    def _loc_23FC(): pass

    label('loc_23FC')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2484',
    )

    ChrTalk(
        0x0105,
        (
            '#0060240782V#040F这么说，包括中庭在内的\n',
            '所有房间就是搜索对象吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240783V#041F呵呵，确实很适合\n',
            '躲猫猫也不一定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2484(): pass

    label('loc_2484')

    ChrTalk(
        0x0008,
        (
            '#2330240784V#5P我暂时回谈话室\n',
            '等那个孩子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330240785V#5P找到了希望能带来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201318V#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 270, 400)

    @scena.Lambda('lambda_250E')
    def lambda_250E():
        OP_6D(-1400, 0, -3120, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_250E)

    @scena.Lambda('lambda_2526')
    def lambda_2526():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2526')

    DispatchAsync2(0x0101, 0x0001, lambda_2526)

    @scena.Lambda('lambda_2537')
    def lambda_2537():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2537')

    DispatchAsync2(0x00F7, 0x0001, lambda_2537)

    @scena.Lambda('lambda_2548')
    def lambda_2548():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2548')

    DispatchAsync2(0x00F8, 0x0001, lambda_2548)

    @scena.Lambda('lambda_2559')
    def lambda_2559():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2559')

    DispatchAsync2(0x00F9, 0x0001, lambda_2559)

    OP_8E(0x0008, -9040, 0, -1330, 3000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    @scena.Lambda('lambda_259D')
    def lambda_259D():
        OP_6D(-260, 0, -4800, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_259D)

    @scena.Lambda('lambda_25B5')
    def lambda_25B5():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_25B5)

    Sleep(50)

    @scena.Lambda('lambda_25C8')
    def lambda_25C8():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_25C8)

    Sleep(50)

    @scena.Lambda('lambda_25DB')
    def lambda_25DB():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_25DB)

    Sleep(50)

    @scena.Lambda('lambda_25EE')
    def lambda_25EE():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_25EE)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010240787V#1006F#5P好了～来寻找\n',
            '逃跑的小猫咪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240788V说是穿着白色甩袖\n',
            '配有黑色丝带的礼服吧。',
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
        'loc_26D9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240789V#061F呵呵……\n',
            '似乎很快就能找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240790V是怎样的孩子呢，真令人期待啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2745')

    def _loc_26D9(): pass

    label('loc_26D9')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2745',
    )

    ChrTalk(
        0x0105,
        (
            '#0060240791V#041F呵呵，似乎是很快\n',
            '就能找到的外表呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240792V真想看看是怎样的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2745(): pass

    label('loc_2745')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2790',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240793V#051F总之还是在\n',
            '建筑物里搜索一遍看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27D8')

    def _loc_2790(): pass

    label('loc_2790')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27D8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030240794V#020F总之还是在\n',
            '建筑物里搜索一遍看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27D8(): pass

    label('loc_27D8')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(430, 0, -4710, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 430, 0, -4710, 0)
    SetChrPos(0x0001, 430, 0, -4710, 0)
    SetChrPos(0x0002, 430, 0, -4710, 0)
    SetChrPos(0x0003, 430, 0, -4710, 0)
    OP_69(0x0000, 0x00000000)
    OP_A2(0x160D)
    OP_28(0x0089, 0x01, 0x0002)
    OP_28(0x0089, 0x01, 0x0004)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x288B
@scena.Code('func_0C_288B')
def func_0C_288B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_28BD',
    )

    OP_8C(0x00FE, 0, 300)
    OP_8C(0x00FE, 270, 300)
    Sleep(1000)

    OP_8C(0x00FE, 0, 300)
    OP_8C(0x00FE, 90, 300)
    Sleep(1000)

    Jump('func_0C_288B')

    def _loc_28BD(): pass

    label('loc_28BD')

    Return()

# id: 0x000D offset: 0x28BE
@scena.Code('func_0D_28BE')
def func_0D_28BE():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 0, 0, -11240, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_28E5')
    def lambda_28E5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_28E5)

    OP_8E(0x00FE, 430, 0, -4710, 2500, 0x00)

    Return()

# id: 0x000E offset: 0x2906
@scena.Code('func_0E_2906')
def func_0E_2906():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 0, 0, -11240, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_292D')
    def lambda_292D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_292D)

    OP_8E(0x00FE, -660, 0, -4760, 2500, 0x00)

    Return()

# id: 0x000F offset: 0x294E
@scena.Code('func_0F_294E')
def func_0F_294E():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 0, 0, -11240, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_2975')
    def lambda_2975():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2975)

    OP_8F(0x00FE, -1660, 0, -5570, 2500, 0x00)

    Return()

# id: 0x0010 offset: 0x2996
@scena.Code('func_10_2996')
def func_10_2996():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 0, 0, -11240, 0)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_29BD')
    def lambda_29BD():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_29BD)

    OP_8F(0x00FE, 1080, 0, -5450, 2500, 0x00)

    Return()

# id: 0x0011 offset: 0x29DE
@scena.Code('func_11_29DE')
def func_11_29DE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 0, 0x1610)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B81',
    )

    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放着精致的讲台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '看看里面似乎没有任何人藏着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010240826V#1019F唔……\n',
            '本来以为猜对了的。',
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
        'loc_2ABD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060240827V#048F呼呼，挺厉害的\n',
            '小猫咪嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B73')

    def _loc_2ABD(): pass

    label('loc_2ABD')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B06',
    )

    ChrTalk(
        0x0108,
        (
            '#0080240828V#071F哈哈，看来没那么简单\n',
            '抓到尾巴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B73')

    def _loc_2B06(): pass

    label('loc_2B06')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B41',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240829V#051F嘿……\n',
            '挺厉害的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B73')

    def _loc_2B41(): pass

    label('loc_2B41')

    ChrTalk(
        0x0103,
        (
            '#0030240830V#027F呵呵……\n',
            '挺厉害的小猫咪嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B73(): pass

    label('loc_2B73')

    EventEnd(0x01)
    OP_A2(0x1610)
    OP_28(0x0089, 0x01, 0x0020)

    Jump('loc_2BE7')

    def _loc_2B81(): pass

    label('loc_2B81')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '放着精致的讲台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '看看里面似乎没有任何人藏着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_2BE7(): pass

    label('loc_2BE7')

    Return()

# id: 0x0012 offset: 0x2BE8
@scena.Code('func_12_2BE8')
def func_12_2BE8():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2BFB',
    )

    Call(0, 0x0013)

    def _loc_2BFB(): pass

    label('loc_2BFB')

    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x09, 0xFF)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2C16',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_2C1A')

    def _loc_2C16(): pass

    label('loc_2C16')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_2C1A(): pass

    label('loc_2C1A')

    OP_4A(0x0009, 255)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0101, -930, 0, 66950, 90)
    SetChrPos(0x00F7, -1030, 0, 65950, 90)
    SetChrPos(0x0009, 1000, 0, 66810, 270)
    SetChrFlags(0x000D, 0x0080)
    OP_6D(1460, 0, 74990, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)
    SetChrStatus(ChrTable['提妲'], 0xFE, 0)
    SetChrStatus(ChrTable['金'], 0xFE, 0)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    @scena.Lambda('lambda_2CE3')
    def lambda_2CE3():
        OP_6D(720, 0, 67490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2CE3)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#0620260289V#702F原来如此……\n',
            '这真是充实的报告书啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260290V#701F真是帮大忙了。\n',
            '竟然调查得这么细致。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211066V#1015F#6P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260292V这犯人最后不能确定,\n',
            '说实话，是有点遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260293V#701F作为调查报告已经充分过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260294V在这个阶段能找到恐吓犯\n',
            '我们也没想过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260295V要说起来，对今后的警备\n',
            '是必要的参考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2ECC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260296V#051F这么说我们就安心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260297V那么，王国军方面\n',
            '有什么进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F24')

    def _loc_2ECC(): pass

    label('loc_2ECC')

    ChrTalk(
        0x0103,
        (
            '#0030260298V#020F这么说我们就安心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260299V那么，王国军方面\n',
            '有什么进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F24(): pass

    label('loc_2F24')

    ChrTalk(
        0x0009,
        (
            '#0620260300V#701F嗯，昨天警备体制的\n',
            '第一阶段完成了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260301V此后，条约签字仪式结束之前\n',
            '这个艾尔贝离宫将成为警备本部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260302V#1006F#6P所以士兵们\n',
            '聚集了不少呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260303V这么说来，周游道上\n',
            '也几乎没有魔兽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260304V#701F今天早晨，刚刚实施过\n',
            '大规模的扫荡作战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260305V条约签字仪式之前\n',
            '应该会定期执行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_30C1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260306V#053F平时就这么做的话\n',
            '也帮了我们的大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30FD')

    def _loc_30C1(): pass

    label('loc_30C1')

    ChrTalk(
        0x0103,
        (
            '#0030260307V#027F平时就这么做的话\n',
            '也帮了协会的大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30FD(): pass

    label('loc_30FD')

    ChrTalk(
        0x0009,
        (
            '#0620260308V#701F哈哈……\n',
            '这话说得真刺耳啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260309V#702F对了，关于昨天说的\n',
            '女孩子的父母……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260310V通知发到了各地的关所\n',
            '但至今还没收到信息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260311V#1015F#6P这样啊……\n',
            '只有耐心等待了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260312V#701F我们如果收到情报，\n',
            '也会马上告知协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260313V总之，恐吓信的调查\n',
            '做到这份上就足够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260314V稍后会把报酬\n',
            '汇给协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260315V#1006F#6P嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260316V#1015F不过……\n',
            '今后打算怎样做？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260317V我们，也这样留在王都\n',
            '帮忙警戒好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260318V#700F如果留在王都\n',
            '能帮忙就再好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260319V#703F只是你们也很忙\n',
            '我们也能理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620260320V不会强人所难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260321V#1015F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260322V#1006F还有玲的事没解决，\n',
            '和艾南哥哥商量看看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3408',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260323V#051F啊啊，就这么试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3433')

    def _loc_3408(): pass

    label('loc_3408')

    ChrTalk(
        0x0103,
        (
            '#0030260324V#020F啊啊，就这么试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3433(): pass

    label('loc_3433')

    OP_4A(0x000A, 255)
    SetChrPos(0x000A, 970, 0, 58600, 0)
    ClearChrFlags(0x000A, 0x0080)

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#3170260325V#1P……打扰了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_349B')
    def lambda_349B():
        OP_6D(850, 0, 67000, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_349B)

    @scena.Lambda('lambda_34B3')
    def lambda_34B3():
        OP_8E(0x00FE, 1030, 0, 65420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_34B3)

    @scena.Lambda('lambda_34CE')
    def lambda_34CE():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34CE)

    Sleep(50)

    @scena.Lambda('lambda_34E1')
    def lambda_34E1():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_34E1)

    Sleep(50)

    @scena.Lambda('lambda_34F4')
    def lambda_34F4():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_34F4')

    DispatchAsync2(0x0101, 0x0002, lambda_34F4)

    @scena.Lambda('lambda_3505')
    def lambda_3505():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_3505')

    DispatchAsync2(0x00F7, 0x0002, lambda_3505)

    @scena.Lambda('lambda_3516')
    def lambda_3516():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_3516')

    DispatchAsync2(0x0009, 0x0001, lambda_3516)

    WaitForThreadExit(0x000A, 0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x0009, 0x01)
    OP_8C(0x0101, 90, 0)

    ChrTalk(
        0x0009,
        (
            '#0620260326V#702F怎么，出什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3170260327V那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 315, 400)
    Sleep(500)

    OP_8C(0x000A, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0620260328V#701F没问题，他们是来帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3170260329V是，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3170260330V刚才从雷斯顿要塞\n',
            '发来了导力通信联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3170260331V似乎是柏斯地区\n',
            '出现了情报部的余党。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010260332V#1020F咦咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_36EE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260333V#052F说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_370F')

    def _loc_36EE(): pass

    label('loc_36EE')

    ChrTalk(
        0x0103,
        (
            '#0030260334V#023F说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_370F(): pass

    label('loc_370F')

    ChrTalk(
        0x0009,
        (
            '#0620260335V#700F唔，详细说说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3170260336V那个，最初时发现的\n',
            '好像是协会的游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3170260337V确切的现场状况\n',
            '至今未能掌握。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3170260338V总之从司令部\n',
            '发来了全王国军部队进入\n',
            '第２种警戒体制的指示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260339V#703F是吗，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3815')
    def lambda_3815():
        OP_6D(720, 0, 67490, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3815)

    ChrTurnDirection(0x0009, 0x0101, 400)
    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#0620260340V#700F……看来我们彼此\n',
            '都要开始忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_38CD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260341V#053F啊啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0106, 0, 400)

    ChrTalk(
        0x0106,
        (
            '#0050260342V#050F艾丝蒂尔。\n',
            '赶快回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3927')

    def _loc_38CD(): pass

    label('loc_38CD')

    ChrTalk(
        0x0103,
        (
            '#0030260343V#020F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0103, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030260344V#022F艾丝蒂尔。\n',
            '立即返回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3927(): pass

    label('loc_3927')

    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260345V#1002F#5P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    OP_8C(0x00F7, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010260346V#1006F#6P希德中校。\n',
            '警备的工作，要加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0620260347V#701F啊啊，你们也要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(10, 0, 61900, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0009, 900, 0, 66800, 270)
    SetChrPos(0x000A, -840, 0, 66800, 90)
    SetChrPos(0x0101, 10, 0, 61900, 180)
    SetChrPos(0x00F7, 10, 0, 61900, 180)
    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)
    OP_A2(0x162A)
    OP_28(0x008B, 0x01, 0x8000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3A73',
    )

    OP_28(0x008A, 0x01, 0x0020)

    Jump('loc_3A80')

    def _loc_3A73(): pass

    label('loc_3A73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3A80',
    )

    OP_28(0x008A, 0x01, 0x0010)

    def _loc_3A80(): pass

    label('loc_3A80')

    OP_28(0x008A, 0x01, 0x0040)
    OP_28(0x008A, 0x01, 0x0080)
    OP_28(0x008A, 0x01, 0x0100)
    OP_28(0x00C4, 0x04, 0x40)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x3AA8
@scena.Code('func_13_3AA8')
def func_13_3AA8():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3B22'),
        (0x00000001, 'loc_3B28'),
        (-1, 'loc_3B2E'),
    )

    def _loc_3B22(): pass

    label('loc_3B22')

    OP_A2(0x1200)

    Jump('loc_3B2E')

    def _loc_3B28(): pass

    label('loc_3B28')

    OP_A2(0x1201)

    Jump('loc_3B2E')

    def _loc_3B2E(): pass

    label('loc_3B2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3B3C',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_3B40')

    def _loc_3B3C(): pass

    label('loc_3B3C')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_3B40(): pass

    label('loc_3B40')

    Return()

# id: 0x0014 offset: 0x3B41
@scena.Code('func_14_3B41')
def func_14_3B41():
    ClearMapFlags(0x00000001)
    OP_6D(-3960, 0, -27940, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3B84',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_3BA2')

    def _loc_3B84(): pass

    label('loc_3B84')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x00FF,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    def _loc_3BA2(): pass

    label('loc_3BA2')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
