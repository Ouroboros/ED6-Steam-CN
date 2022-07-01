import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3115_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3115   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '玛多克工房长'),
    TXT(0x02, '康丝坦茨'),
    TXT(0x03, '米优'),
    TXT(0x04, '格斯塔夫维修长'),
    TXT(0x05, '雨果'),
    TXT(0x06, '普罗梅笛'),
    TXT(0x07, '拉赛尔博士'),
    TXT(0x08, '露依赛'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3115.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x497B
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
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02623._CH', 'ED6_DT07/CH02623P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4380,
            z                   = 0,
            y                   = 2370,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = -107400,
            z                   = 0,
            y                   = -90,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -104390,
            z                   = 0,
            y                   = 8560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -103940,
            z                   = 0,
            y                   = 98950,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -102540,
            z                   = 0,
            y                   = 97610,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -103430,
            z                   = 0,
            y                   = 108150,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 2430,
            z                   = 0,
            y                   = 2850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -102520,
            z                   = 0,
            y                   = 96150,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
    )

# id: 0x10003 offset: 0x1F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1F2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1F2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1F2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 3, 0x1483)),
            Expr.Return,
        ),
        'loc_1FE',
    )

    ClearChrFlags(0x000B, 0x0010)

    def _loc_1FE(): pass

    label('loc_1FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_25F',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    TerminateThread(0x0008, 0x00)
    SetChrChipByIndex(0x0008, 1)
    SetChrPos(0x0008, 2430, 200, 5330, 180)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x000D, -103580, 0, 99360, 180)
    ClearChrFlags(0x000F, 0x0080)
    OP_8C(0x000F, 270, 0)
    ClearChrFlags(0x000F, 0x0010)
    OP_8C(0x000C, 270, 0)

    Jump('loc_341')

    def _loc_25F(): pass

    label('loc_25F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2C8',
    )

    TerminateThread(0x0008, 0x00)
    SetChrChipByIndex(0x0008, 1)
    SetChrPos(0x0008, 2430, 200, 5330, 180)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0009, -104980, 0, 640, 0)
    SetChrFlags(0x0009, 0x0010)
    SetChrPos(0x000A, -104980, 0, 1980, 180)
    SetChrFlags(0x000A, 0x0010)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)

    Jump('loc_341')

    def _loc_2C8(): pass

    label('loc_2C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2F7',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, -103480, 0, 99640, 180)

    Jump('loc_341')

    def _loc_2F7(): pass

    label('loc_2F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_324',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000C, 0x0010)
    OP_8C(0x000C, 180, 0)
    ClearChrFlags(0x000F, 0x0080)

    Jump('loc_341')

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_341',
    )

    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000C, 0x0010)
    OP_8C(0x000C, 180, 0)
    ClearChrFlags(0x000F, 0x0080)

    def _loc_341(): pass

    label('loc_341')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x34C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BA',
    )

    OP_6F(0x0000, 29)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0001, 29)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0002, 29)
    OP_72(0x0002, 0x0010)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_7A(0x18, 0x0002)
    OP_7A(0x19, 0x0002)
    OP_7A(0x1A, 0x0002)
    OP_7B()
    OP_72(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)

    def _loc_3BA(): pass

    label('loc_3BA')

    Return()

# id: 0x0002 offset: 0x3BB
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4C0',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0008)
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_456',
    )

    Jump('loc_498')

    def _loc_456(): pass

    label('loc_456')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_472',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_498')

    def _loc_472(): pass

    label('loc_472')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_48E',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_498')

    def _loc_48E(): pass

    label('loc_48E')

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_498(): pass

    label('loc_498')

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0008, 0x0010)

    Jump('loc_4C3')

    def _loc_4C0(): pass

    label('loc_4C0')

    TalkBegin(0x0008)
    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_789',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_726',
    )

    ChrTalk(
        0x0008,
        (
            '#0550370059V#802F喔喔，是你们吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370060V温泉的泵\n',
            '修理好了吗？',
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
        'loc_591',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370061V#061F是的，已经修理好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370062V#1006F嗯，现在随时\n',
            '都可以去泡温泉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F5')

    def _loc_591(): pass

    label('loc_591')

    ChrTalk(
        0x0101,
        (
            '#0010370063V#1006F嗯，现在随时\n',
            '都可以去泡温泉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370064V#1015F嗯，这全是提妲\n',
            '的功劳啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F5(): pass

    label('loc_5F5')

    ChrTalk(
        0x0008,
        (
            '#0550370065V#801F噢噢！那可太让人高兴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370066V等工作告一段落之后\n',
            '我要赶快去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370067V#1049F嗯嗯，偶尔\n',
            '也要好好休息一下。',
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
        'loc_6E8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370068V#560F说的对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370069V不管是什么机械\n',
            '也都要定期维护的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E8(): pass

    label('loc_6E8')

    ChrTalk(
        0x0008,
        (
            '#0550370070V#801F哈哈，多谢忠告。\n',
            '我会牢记在心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_786')

    def _loc_726(): pass

    label('loc_726')

    ChrTalk(
        0x0008,
        (
            '#0550370071V#800F水泵的修理\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370072V#806F呵，早点去温泉里\n',
            '泡一泡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_786(): pass

    label('loc_786')

    Jump('loc_1F55')

    def _loc_789(): pass

    label('loc_789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_FDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 5, 0x20CD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C85',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_820',
    )

    ChrTalk(
        0x0008,
        (
            '#0550370073V#802F喔喔……\n',
            '艾丝蒂尔，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370074V还有提妲也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070370075V#067F嘿嘿，我们回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_852')

    def _loc_820(): pass

    label('loc_820')

    ChrTalk(
        0x0008,
        (
            '#0550370076V#802F喔喔……\n',
            '艾丝蒂尔，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_852(): pass

    label('loc_852')

    ChrTalk(
        0x0101,
        (
            '#0010370077V#1000F工房长先生，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370078V#1040F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550370079V#801F嗯，平安回来了\n',
            '就比什么都好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370080V博士的发明品\n',
            '还有用吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370081V#1011F那个发生器吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370082V#1001F当然啊，帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370083V#1040F王国军可能比我们\n',
            '更加感激你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370084V在通讯系统恢复之前\n',
            '各个据点都已经完全被孤立了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550370085V#801F呵呵，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370086V看来这东西充分发挥了\n',
            '预想中的效果啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370087V#1015F嗯，这虽然很好，\n',
            '不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370088V#1002F工房长先生，\n',
            '……中央工房现在怎么样了？',
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
        'loc_ADC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370089V#063F这、这么漆黑一团…\n',
            '实在没办法再继续研究了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B13')

    def _loc_ADC(): pass

    label('loc_ADC')

    ChrTalk(
        0x0102,
        (
            '#0020370090V#1043F像现在这种状况\n',
            '什么也干不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B13(): pass

    label('loc_B13')

    ChrTalk(
        0x0008,
        (
            '#0550370091V#805F啊啊……\n',
            '很严峻的状况啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370092V现在的问题堆积如山，\n',
            '已经都忙不过来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370093V不过我们能做的也只有\n',
            '尽力解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370094V#1007F是吗，真是不得了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370095V#1040F要是有什么我们可以帮忙的事\n',
            '请一定别客气啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370096V遇到什么困难的话\n',
            '和协会联络就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550370097V#800F嗯，谢谢啦。\n',
            '你们也要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20CD)

    Jump('loc_FD7')

    def _loc_C85(): pass

    label('loc_C85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 1, 0x2011)),
            Expr.Return,
        ),
        'loc_E12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DA2',
    )

    ChrTalk(
        0x0008,
        (
            '#0550370098V#802F喔喔、这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370099V汽油已经拿到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370100V#1006F嗯，拿到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370101V#1040F介绍信……\n',
            '还麻烦您，真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550370102V#801F哪里哪里～这是应当的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370103V那么，修理水泵的事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_E0F')

    def _loc_DA2(): pass

    label('loc_DA2')

    ChrTalk(
        0x0008,
        (
            '#0550370104V#800F修理水泵的事\n',
            '就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370105V我也很喜欢温泉呢，\n',
            '修理设施的事就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E0F(): pass

    label('loc_E0F')

    Jump('loc_FD7')

    def _loc_E12(): pass

    label('loc_E12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 0, 0x2010)),
            Expr.Return,
        ),
        'loc_F5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EEB',
    )

    ChrTalk(
        0x0008,
        (
            '#0550370106V#800F介绍信里已经写清\n',
            '的负责人就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370107V如果汽油已经送到的话，\n',
            '要交给你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370108V街道的路灯都已经熄灭了，\n',
            '现在哪条路都很危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370109V路上要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_F58')

    def _loc_EEB(): pass

    label('loc_EEB')

    ChrTalk(
        0x0008,
        (
            '#0550370106V#800F介绍信里已经写清\n',
            '的负责人就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370111V如果汽油已经送到的话，\n',
            '要交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F58(): pass

    label('loc_F58')

    Jump('loc_FD7')

    def _loc_F5B(): pass

    label('loc_F5B')

    ChrTalk(
        0x0008,
        (
            '#0550370112V#805F虽然很想早点开始研究，\n',
            '但现在问题堆积如山。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550370113V#806F呼～总之还是\n',
            '先把这些文件整理一下吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_FD7(): pass

    label('loc_FD7')

    Jump('loc_1F55')

    def _loc_FDA(): pass

    label('loc_FDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 1, 0x1481)),
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_154E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_140D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_10A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 2, 0x1642)),
            Expr.Return,
        ),
        'loc_10A2',
    )

    ChrTalk(
        0x0008,
        (
            '#0550240188V#800F我已经以自己的名义\n',
            '发表了有关地震的安全宣言。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550240189V现在最重要的就是\n',
            '消除市民们的不安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550240190V要去王都的话，\n',
            '路上一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10A6')

    def _loc_10A2(): pass

    label('loc_10A2')

    Call(0, 0x0005)

    def _loc_10A6(): pass

    label('loc_10A6')

    Jump('loc_140A')

    def _loc_10A9(): pass

    label('loc_10A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_11B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_111A',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220781V#800F那么亚尔摩村那边\n',
            '就先让我去把事情做个说明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220782V那么，多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B4')

    def _loc_111A(): pass

    label('loc_111A')

    ChrTalk(
        0x0008,
        (
            '#0550220781V#800F那么亚尔摩村那边\n',
            '就先让我去把事情做个说明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220784V等你们过去以后麻绪婆婆\n',
            '会尽力帮你们忙的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220782V那么，多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_11B4(): pass

    label('loc_11B4')

    Jump('loc_140A')

    def _loc_11B7(): pass

    label('loc_11B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_12F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1276',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220776V#800F拉赛尔博士的头脑\n',
            '在关键的时刻\n',
            '才能体现出真正的价值。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220777V正因如此才会\n',
            '被称作天才吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220778V#806F哈，博士的才能有时\n',
            '也会引起『天灾』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F6')

    def _loc_1276(): pass

    label('loc_1276')

    ChrTalk(
        0x0008,
        (
            '#0550220779V#800F这次的地震太奇妙了。\n',
            '研究者对此也很有兴趣呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220780V如果拉赛尔博士的实验\n',
            '能成为突破口就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_12F6(): pass

    label('loc_12F6')

    Jump('loc_140A')

    def _loc_12F9(): pass

    label('loc_12F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_139E',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220765V#800F刚收到联络，\n',
            '好像连圣海姆门那里\n',
            '也遭遇了地震。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220766V不过从这里完全\n',
            '感觉不到摇晃。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220767V看来这次地震\n',
            '好象有点特别呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_140A')

    def _loc_139E(): pass

    label('loc_139E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_140A',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220768V#800F市内的情报收集\n',
            '由我去做吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220769V近来街道也很危险，\n',
            '路上要小心谨慎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_140A(): pass

    label('loc_140A')

    Jump('loc_154B')

    def _loc_140D(): pass

    label('loc_140D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1482',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220770V#800F中央工房也会全力\n',
            '配合协会的调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220741V虽然很麻烦，\n',
            '不过还是要请你们多帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154B')

    def _loc_1482(): pass

    label('loc_1482')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_14DF',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220772V#800F拉赛尔博士\n',
            '正在找你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220773V是不是应该回\n',
            '协会看看？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154B')

    def _loc_14DF(): pass

    label('loc_14DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_154B',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220768V#800F市内的情报收集\n',
            '由我去做吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220769V近来街道也很危险，\n',
            '路上要小心谨慎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_154B(): pass

    label('loc_154B')

    Jump('loc_1F55')

    def _loc_154E(): pass

    label('loc_154E')

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_175D',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220717V#801F啊，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0106, 400)

    ChrTalk(
        0x0008,
        (
            '#0550220718V#801F阿加特也在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050220719V#051F你好，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220720V#1006F工房长先生，好久不见。\n',
            '好像是从诞辰庆典以来就没见过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0550220721V#801F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220722V听说你遇到了很多事……\n',
            '还能这么打起精神来真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220723V#1008F啊哈哈……\n',
            '谢谢你，工房长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_175A',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220724V#800F你们好像会为了协助\n',
            '蔡斯支部而逗留一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220725V有你们在我就放心了。\n',
            '请你们多帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_175A(): pass

    label('loc_175A')

    Jump('loc_1A1B')

    def _loc_175D(): pass

    label('loc_175D')

    ChrTalk(
        0x0008,
        (
            '#0550220726V#801F哟……\n',
            '艾丝蒂尔，你来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220720V#1006F工房长先生，好久不见。\n',
            '好像是从诞辰庆典以来就没见过了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550220721V#801F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220722V听说你遇到了很多事……\n',
            '还能这么打起精神来真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220723V#1008F啊哈哈……\n',
            '谢谢你，工房长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '#0550220731V#802F请问这位是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220732V#1006F嗯，她是雪拉姐……\n',
            '支部的前辈…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030220733V#020F我是洛连特支部的游击士，\n',
            '雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220734V虽然可能是短期的\n',
            '麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1989',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220735V#801F艾丝蒂尔的前辈啊。\n',
            '也请你多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A1B')

    def _loc_1989(): pass

    label('loc_1989')

    ChrTalk(
        0x0008,
        (
            '#0550220736V#801F也请你多关照。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220724V#800F你们好像会为了协助\n',
            '蔡斯支部而逗留一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220738V我也代表整个城市\n',
            '期待着你们的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A1B(): pass

    label('loc_1A1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1B53',
    )

    ChrTalk(
        0x0008,
        (
            '#0550220739V#800F听说你们已经开始\n',
            '协助拉赛尔博士的实验了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220740V中央工房也会全力\n',
            '配合协会的调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220741V虽然很麻烦，\n',
            '不过还是要请你们多帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0550220742V#800F嗯，如果有什么不方便的地方\n',
            '就立即联络我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220743V那么，你们也要当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220744V#1006F嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F4F')

    def _loc_1B53(): pass

    label('loc_1B53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1D14',
    )

    Call(0, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010220745V#1006F我们会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550220746V#802F说起来，拉赛尔博士\n',
            '好象在找你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220747V据说是完成了一个什么准备……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220748V#1004F哦，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1C58',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220749V#052F是不是应该先回\n',
            '仔细看着指南针前进啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C88')

    def _loc_1C58(): pass

    label('loc_1C58')

    ChrTalk(
        0x0103,
        (
            '#0030220750V#027F是不是应该先回\n',
            '确认一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C88(): pass

    label('loc_1C88')

    ChrTalk(
        0x0008,
        (
            '#0550220751V#800F嗯，这样比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220752V#806F呼，虽然很麻烦，\n',
            '不过还是请你们继续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220753V#1016F嗯、嗯，那么再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F4F')

    def _loc_1D14(): pass

    label('loc_1D14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1F4F',
    )

    Call(0, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010220754V#1006F嗯，我们会尽力的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220755V说起来，工房长先生你好像\n',
            '也在帮助协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0550220756V#800F嗯，刚才的地震之后\n',
            '收到了雾香的联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220757V她让我收集地震前后\n',
            '有没有发生过可疑情况的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220758V#806F我刚开始弄，\n',
            '并没有什么成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220759V#1015F是吗……\n',
            '嗯，结果也不会那么快就出来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220760V#1000F我们也马上要去\n',
            '沃尔费堡垒调查了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220761V工房长先生请继续\n',
            '做市内的调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550220762V#800F嗯，一有发现\n',
            '我就会联络协会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550220763V艾丝蒂尔你们也要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220744V#1006F嗯，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F4F(): pass

    label('loc_1F4F')

    OP_A2(0x1481)
    OP_A2(0x0000)
    def _loc_1F55(): pass

    label('loc_1F55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1F6B',
    )

    SetChrSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Jump('loc_1F6E')

    def _loc_1F6B(): pass

    label('loc_1F6B')

    TalkEnd(0x0008)

    def _loc_1F6E(): pass

    label('loc_1F6E')

    Return()

# id: 0x0003 offset: 0x1F6F
@scena.Code('func_03_1F6F')
def func_03_1F6F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1F9C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230854V#051F嗯，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FBF')

    def _loc_1F9C(): pass

    label('loc_1F9C')

    ChrTalk(
        0x0103,
        (
            '#0030230855V#525F嗯，请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FBF(): pass

    label('loc_1FBF')

    Return()

# id: 0x0004 offset: 0x1FC0
@scena.Code('func_04_1FC0')
def func_04_1FC0():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2053',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 2, 0x1642)),
            Expr.Return,
        ),
        'loc_204F',
    )

    ChrTalk(
        0x000E,
        (
            '#0540230819V#100F看来那个『结社』的技术力量\n',
            '已经高得没话说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540230820V嗯，好久没碰到\n',
            '这么有挑战性的研究课题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2053')

    def _loc_204F(): pass

    label('loc_204F')

    Call(0, 0x0005)

    def _loc_2053(): pass

    label('loc_2053')

    TalkEnd(0x000E)

    Return()

# id: 0x0005 offset: 0x2057
@scena.Code('func_05_2057')
def func_05_2057():
    OP_4A(0x000E, 255)

    ChrTalk(
        0x0008,
        (
            '#0550240165V#802F哟，这不是艾丝蒂尔你们吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 500)

    ChrTalk(
        0x000E,
        (
            '#0540240166V#103F还没有出发吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240167V#1000F嗯，稍微有点事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240168V#1015F……不过你们好像在谈话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0540240169V#100F嗯，王国军那边送来了\n',
            '调查报告书。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540240170V是有关那个投影装置的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240171V#1011F投影装置……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_21DC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240172V#050F就是在卢安的敌人使用的\n',
            '那个制造幻影的装置吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2220')

    def _loc_21DC(): pass

    label('loc_21DC')

    ChrTalk(
        0x0103,
        (
            '#0030240173V#022F就是在卢安的敌人使用的\n',
            '那个制造幻影的装置吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2220(): pass

    label('loc_2220')

    ChrTalk(
        0x000E,
        (
            '#0540240174V#104F嗯，就是你们\n',
            '告诉我的那个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540240175V#102F因为它是研究『福音』\n',
            '所不可或缺的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0101, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_22AE',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_22B3')

    def _loc_22AE(): pass

    label('loc_22AE')

    SetChrSubChip(0x00FE, 2)

    def _loc_22B3(): pass

    label('loc_22B3')

    OP_8C(0x0008, 180, 0)
    SetChrFlags(0x0008, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0550240176V#800F本来我正要去询问军方，\n',
            '不过他们倒先把报告书送来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550240177V我刚才立即看了一遍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240178V#1004F哟～调查报告都\n',
            '已经完成啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240179V看来军方对『结社』的调查\n',
            '也相当卖力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23D6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240180V#053F嗯，当然也肯定\n',
            '有做记号吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2408')

    def _loc_23D6(): pass

    label('loc_23D6')

    ChrTalk(
        0x0103,
        (
            '#0030240181V#026F嗯，当然也肯定\n',
            '有做记号吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2408(): pass

    label('loc_2408')

    ChrTalk(
        0x000E,
        (
            '#0540240182V#100F我也准备倾注全力在\n',
            '『福音』的解析上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540240183V#100F那么，提妲就\n',
            '拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2476')
    def lambda_2476():
        ChrTurnDirection(0x00F7, 0x000E, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2476)

    ChrTurnDirection(0x0101, 0x000E, 500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_24B6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240184V#051F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DF')

    def _loc_24B6(): pass

    label('loc_24B6')

    ChrTalk(
        0x0103,
        (
            '#0030240185V#020F嗯，请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24DF(): pass

    label('loc_24DF')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2522',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240186V#560F嗯……\n',
            '爷爷你们也要好好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2550')

    def _loc_2522(): pass

    label('loc_2522')

    ChrTalk(
        0x0101,
        (
            '#0010240187V#1006F嗯……你们也要好好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2550(): pass

    label('loc_2550')

    OP_4B(0x000E, 255)
    OP_A2(0x1642)

    Return()

# id: 0x0006 offset: 0x2558
@scena.Code('func_06_2558')
def func_06_2558():
    TalkBegin(0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x002F, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0030, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2576',
    )

    OP_A2(0x0004)

    def _loc_2576(): pass

    label('loc_2576')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2614',
    )

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
            TXT(0x00, '【◇在上半部完成过QST046、QST047、QST048其中之一】\n'),
            TXT(0x01, '【◇在上半部没完成过其中任何一个】\n'),
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
        (0x00000000, 'loc_2608'),
        (0x00000001, 'loc_260E'),
        (-1, 'loc_2614'),
    )

    def _loc_2608(): pass

    label('loc_2608')

    OP_A2(0x0004)

    Jump('loc_2614')

    def _loc_260E(): pass

    label('loc_260E')

    OP_A3(0x0004)

    Jump('loc_2614')

    def _loc_2614(): pass

    label('loc_2614')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 4, 0x142C)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_28EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2897',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_263A',
    )

    Call(0, 0x0008)

    Jump('loc_2894')

    def _loc_263A(): pass

    label('loc_263A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2709',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2695',
    )

    ChrTalk(
        0x00FE,
        (
            '那个新人现在在\n',
            '研究室里干活儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正那孩子做事\n',
            '一定很得要领。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2706')

    def _loc_2695(): pass

    label('loc_2695')

    ChrTalk(
        0x00FE,
        (
            '事务工作的实习\n',
            '大家都是从帮资料室工作\n',
            '来开始积累经验的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过像我这样\n',
            '起点直接成终点的人\n',
            '也是有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2706(): pass

    label('loc_2706')

    Jump('loc_2894')

    def _loc_2709(): pass

    label('loc_2709')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_27E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2780',
    )

    ChrTalk(
        0x00FE,
        (
            '那个新人好像是\n',
            '通过关系进入工房的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我们这边是能力至上主义，\n',
            '是如何进来的并不构成问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27E1')

    def _loc_2780(): pass

    label('loc_2780')

    ChrTalk(
        0x00FE,
        (
            '那个新人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是以前我们这儿\n',
            '一个工匠的孙女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是说……\n',
            '是通过关系进来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_27E1(): pass

    label('loc_27E1')

    Jump('loc_2894')

    def _loc_27E4(): pass

    label('loc_27E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2894',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2851',
    )

    ChrTalk(
        0x00FE,
        (
            '我们这儿也有有前途的\n',
            '新人被分配进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有点傻傻的，\n',
            '不过劳动能力很令人期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2894')

    def _loc_2851(): pass

    label('loc_2851')

    ChrTalk(
        0x00FE,
        (
            '唉，地震真是\n',
            '太讨厌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快让新人\n',
            '来整理倒塌的书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2894(): pass

    label('loc_2894')

    Jump('loc_28E7')

    def _loc_2897(): pass

    label('loc_2897')

    ChrTalk(
        0x00FE,
        (
            '现在交给新人在做，\n',
            '没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过如果碰到问题的话\n',
            '还是要拜托你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_28E7(): pass

    label('loc_28E7')

    Jump('loc_2A9E')

    def _loc_28EA(): pass

    label('loc_28EA')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，我说怎么这么面熟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你是以前帮我\n',
            '找过书的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊～我想起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F好、好像那是一段\n',
            '很不容易的过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，放心好了。\n',
            '暂时没有要委托的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好有个新人被分配过来了，\n',
            '现在杂物就交给那孩子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哟～挺好的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，暂时是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么事她做不好\n',
            '我还是会拜托协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到时候\n',
            '还请你们帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，你放心好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x142C)
    OP_A2(0x0002)
    def _loc_2A9E(): pass

    label('loc_2A9E')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x2AA2
@scena.Code('func_07_2AA2')
def func_07_2AA2():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_2B53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B04',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，真无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须到５楼\n',
            '去拿资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～……\n',
            '真讨厌爬楼梯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_2B50')

    def _loc_2B04(): pass

    label('loc_2B04')

    ChrTalk(
        0x00FE,
        (
            '没有电梯的话\n',
            '连回收资料也很麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的～明天\n',
            '要不要感冒一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B50(): pass

    label('loc_2B50')

    Jump('loc_2F55')

    def _loc_2B53(): pass

    label('loc_2B53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2C24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BDD',
    )

    ChrTalk(
        0x00FE,
        (
            '这么暗的话\n',
            '书的标题也看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的～让我\n',
            '怎么工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前辈也不知道去什么地方了，\n',
            '我也早点回去吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_2C21')

    def _loc_2BDD(): pass

    label('loc_2BDD')

    ChrTalk(
        0x00FE,
        (
            '这么暗的话\n',
            '书的标题也看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的～让我\n',
            '怎么工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C21(): pass

    label('loc_2C21')

    Jump('loc_2F55')

    def _loc_2C24(): pass

    label('loc_2C24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2C32',
    )

    Call(0, 0x0008)

    Jump('loc_2F55')

    def _loc_2C32(): pass

    label('loc_2C32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_2DCB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 5, 0x1435)),
            Expr.Return,
        ),
        'loc_2C95',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～这边结束以后\n',
            '就要去研究室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了提升第一印象\n',
            '就要保持可爱的笑容～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC8')

    def _loc_2C95(): pass

    label('loc_2C95')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0107, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，米优小姐。\n',
            '工作感觉怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像都是在做一些杂事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正是实习，\n',
            '也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F嘿嘿，大家开始时\n',
            '都要先从小事做起的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过米优小姐\n',
            '一定没问题的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢你，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也有目标，\n',
            '所以我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#061F嗯，请你加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1435)

    def _loc_2DC8(): pass

    label('loc_2DC8')

    Jump('loc_2F55')

    def _loc_2DCB(): pass

    label('loc_2DCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2E92',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2E32',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～搞定这个以后\n',
            '就要去研究室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '第一印象很重要，\n',
            '出门的时候总要保持微笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E8F')

    def _loc_2E32(): pass

    label('loc_2E32')

    ChrTalk(
        0x00FE,
        (
            '我的目标很明确，\n',
            '就是成为工房的接待处小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一定会通过踏实的努力\n',
            '来实现它的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2E8F(): pass

    label('loc_2E8F')

    Jump('loc_2F55')

    def _loc_2E92(): pass

    label('loc_2E92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2F55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2EEE',
    )

    ChrTalk(
        0x00FE,
        (
            '现在我正在进行业务实习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，一天到晚就是整理书籍，\n',
            '我受不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F55')

    def _loc_2EEE(): pass

    label('loc_2EEE')

    ChrTalk(
        0x00FE,
        (
            '唉～你们看看。\n',
            '这是因为刚才的地震倒塌的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '与其责怪地震，倒不如说\n',
            '是不干活儿的前辈造成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_2F55(): pass

    label('loc_2F55')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x2F59
@scena.Code('func_08_2F59')
def func_08_2F59():
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_2F82'),
        (0x00000001, 'loc_3043'),
        (0x00000002, 'loc_3108'),
        (0x00000003, 'loc_3262'),
        (0x00000004, 'loc_3373'),
        (0x00000005, 'loc_3517'),
        (-1, 'loc_3653'),
    )

    def _loc_2F82(): pass

    label('loc_2F82')

    ChrTalk(
        0x000A,
        (
            '所以呢，前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我真的能成为\n',
            '接待处小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我都说了，你问我还不如\n',
            '靠自己努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不是挺好吗？\n',
            '有目标是好事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '能够让人对未来充满憧憬的\n',
            '工作真是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3653')

    def _loc_3043(): pass

    label('loc_3043')

    ChrTalk(
        0x0009,
        (
            '不过海泽尔可是个劲敌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '处处都受到\n',
            '工房长的信赖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '海泽尔小姐\n',
            '年纪不小了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我觉得还是年轻又活跃的人\n',
            '更能受到大家的喜爱～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果我穿得漂亮点\n',
            '那胜利绝对是我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3653')

    def _loc_3108(): pass

    label('loc_3108')

    ChrTalk(
        0x000A,
        (
            '说起来，海泽尔小姐\n',
            '还没结婚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，还是独身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我和海泽尔一样\n',
            '都还是单身呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '啊，是吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，前辈～\n',
            '那样不会有压力吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '男人就是易耗品……\n',
            '好一点的也就是耐久度高的消耗品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '和那些消耗品定终身契约\n',
            '岂不是更有压力吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '已、已经无药可救了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3653')

    def _loc_3262(): pass

    label('loc_3262')

    ChrTalk(
        0x000A,
        (
            '对了，我刚才\n',
            '去了４楼的实验室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '前辈你不是说\n',
            '有好男人的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过那个白衣男人好像\n',
            '战战兢兢的，一副没用的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你说的是蒂亚利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不是还有一个人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊，还有一个人～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，我白努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '快要到午饭时间了，\n',
            '雷伊可能出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3653')

    def _loc_3373(): pass

    label('loc_3373')

    ChrTalk(
        0x0009,
        (
            '说起午饭，\n',
            '我肚子倒也饿起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要不要去『福格尔』？\n',
            '今天就我来请客吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哇～我太喜欢前辈了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对了，说起『福格尔』，\n',
            '那边的男服务员也不错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '咦，你不知道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那个男服务员正在和\n',
            '我们这儿的女研究员交往哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊───噢……\n',
            '挺打击人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '鲁伊泽你认识吗？\n',
            '在年轻人当中属于最有前途的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '外表虽然只能打５０分，\n',
            '不过考试能够拿那个分数两倍的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3653')

    def _loc_3517(): pass

    label('loc_3517')

    ChrTalk(
        0x000A,
        (
            '唔～工房的人是不是\n',
            '比较重视内涵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那方面的倾向确实很强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果工作不能得到认可\n',
            '谁都不会正眼瞧你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果成为接待处小姐\n',
            '会不会变得受欢迎～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '反正比呆在资料室\n',
            '要好很多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是吗～果然还是\n',
            '只有靠努力了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好～一定要成为\n',
            '接待处小姐～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '然后要猎取外观也ＯＫ的\n',
            '研究员的心～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3653')

    def _loc_3653(): pass

    label('loc_3653')

    OP_4B(0x0009, 255)
    OP_4B(0x000A, 255)

    Return()

# id: 0x0009 offset: 0x365C
@scena.Code('func_09_365C')
def func_09_365C():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 3, 0x1483)),
            Expr.Return,
        ),
        'loc_3963',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3867',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_37A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_36FC',
    )

    ChrTalk(
        0x000B,
        (
            '#0560230821V#690F新型引擎的换装工程\n',
            '预定在雷斯顿要塞进行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230822V让王都的『埃尔赛尤』返航，\n',
            '我们则派工程船过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_379D')

    def _loc_36FC(): pass

    label('loc_36FC')

    ChrTalk(
        0x000B,
        (
            '#0560230823V#690F很快新型引擎就能\n',
            '搭载到『埃尔赛尤』上面了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230824V必须赶快确定\n',
            '换装工程的计划了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230825V所以我最近也要\n',
            '一直呆在中央工房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_379D(): pass

    label('loc_379D')

    Jump('loc_3864')

    def _loc_37A0(): pass

    label('loc_37A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_380D',
    )

    ChrTalk(
        0x000B,
        (
            '#0560230826V#690F不过说起来地震\n',
            '倒是很久没碰上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230827V总之没什么大损失\n',
            '真是万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3864')

    def _loc_380D(): pass

    label('loc_380D')

    ChrTalk(
        0x000B,
        (
            '#0560230828V#690F嗯，我这边的招呼你们已经打过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230829V快点去见见小提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3864(): pass

    label('loc_3864')

    Jump('loc_3960')

    def _loc_3867(): pass

    label('loc_3867')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_38F0',
    )

    ChrTalk(
        0x000B,
        (
            '#0560230830V#691F有你们在真是\n',
            '以一敌万。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230831V如果有什么需要的话\n',
            '拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230832V到那时请一定多关照啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3960')

    def _loc_38F0(): pass

    label('loc_38F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_3960',
    )

    ChrTalk(
        0x000B,
        (
            '#0560230833V#691F小提妲热烈欢迎你们啊……\n',
            '哈哈，也难怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230834V因为小提妲那丫头\n',
            '很想念你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3960(): pass

    label('loc_3960')

    Jump('loc_3CFC')

    def _loc_3963(): pass

    label('loc_3963')

    ChrTalk(
        0x0101,
        (
            '#0010230835V#1018F啊，维修长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000B)
    ChrTurnDirection(0x000B, 0x0101, 500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3A05',
    )

    ChrTalk(
        0x000B,
        (
            '#0560230836V#692F哟……\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230837V#691F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A54')

    def _loc_3A05(): pass

    label('loc_3A05')

    ChrTalk(
        0x000B,
        (
            '#0560230838V#692F哟……\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230839V#691F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A54(): pass

    label('loc_3A54')

    ChrTalk(
        0x0101,
        (
            '#0010230840V#1001F嘿嘿，好久不见！\n',
            '维修长先生看起来也很精神呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0560230841V#691F怎么？这次又是工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230842V#1006F嗯，我们接到了蔡斯\n',
            '支部的支援请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230843V所以要在这里\n',
            '工作一阵子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0560230844V#691F哦，那真令人安心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230845V那我就不客气了，\n',
            '有什么事的话就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230846V#1001F嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_3C14',
    )

    ChrTurnDirection(0x000B, 0x0107, 400)

    ChrTalk(
        0x000B,
        (
            '#0560230847V#691F小提妲也在\n',
            '努力帮助博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230848V#060F哦，我明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF1')

    def _loc_3C14(): pass

    label('loc_3C14')

    ChrTalk(
        0x000B,
        (
            '#0560230849V#691F说起来，你们去见过\n',
            '博士了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230850V#1011F嗯，刚去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230851V#1008F受、受到了提妲的\n',
            '热烈欢迎呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0560230852V#693F哈哈，那是肯定的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560230853V因为小提妲那丫头\n',
            '很想念你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CF1(): pass

    label('loc_3CF1')

    OP_A2(0x1483)
    OP_A2(0x0006)
    ClearChrFlags(0x000B, 0x0010)
    def _loc_3CFC(): pass

    label('loc_3CFC')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x3D00
@scena.Code('func_0A_3D00')
def func_0A_3D00():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_3E0B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DB2',
    )

    ChrTalk(
        0x00FE,
        (
            '我们这些技术人员虽然\n',
            '在研究如何应对这种现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过越想越觉得这种\n',
            '现象很异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在只能对事实\n',
            '感到目瞪口呆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根本想不出\n',
            '有什么对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_3E08')

    def _loc_3DB2(): pass

    label('loc_3DB2')

    ChrTalk(
        0x00FE,
        (
            '现在只能对该现象的\n',
            '异常性感到震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超过了人类智慧的力量……\n',
            '只能这么想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E08(): pass

    label('loc_3E08')

    Jump('loc_40BD')

    def _loc_3E0B(): pass

    label('loc_3E0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3F35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3ED8',
    )

    ChrTalk(
        0x00FE,
        (
            '实在想不到事态\n',
            '会发展成这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』的性能评价\n',
            '已经告一段落，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为读取数据这种事\n',
            '没有导力器也能完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且现在对这种现象\n',
            '进行研究才是当务之急。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_3F32')

    def _loc_3ED8(): pass

    label('loc_3ED8')

    ChrTalk(
        0x00FE,
        (
            '实在想不到事态\n',
            '会发展成这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』的性能评价\n',
            '已经告一段落，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F32(): pass

    label('loc_3F32')

    Jump('loc_40BD')

    def _loc_3F35(): pass

    label('loc_3F35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3FA9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3FA2',
    )

    ChrTalk(
        0x00FE,
        (
            '插头的检查结束以后\n',
            '请立即做登船准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有足够时间准备的话\n',
            '一定会丢三落四的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FA6')

    def _loc_3FA2(): pass

    label('loc_3FA2')

    Call(0, 0x000D)

    def _loc_3FA6(): pass

    label('loc_3FA6')

    Jump('loc_40BD')

    def _loc_3FA9(): pass

    label('loc_3FA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_40BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_4012',
    )

    ChrTalk(
        0x00FE,
        (
            '很快『埃尔赛尤』上就要\n',
            '搭载新型引擎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们准备前往雷斯顿要塞，\n',
            '在那里施工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40BD')

    def _loc_4012(): pass

    label('loc_4012')

    ChrTalk(
        0x00FE,
        (
            '不久『埃尔赛尤』上就要\n',
            '搭载新型引擎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在维修长正在\n',
            '确定工程的次序。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才的地震没造成\n',
            '什么损失真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果使工程的准备\n',
            '推迟的话就不好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_40BD(): pass

    label('loc_40BD')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x40C1
@scena.Code('func_0B_40C1')
def func_0B_40C1():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_41A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4177',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么想都想\n',
            '不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个空中的浮游物体……\n',
            '以及这回的停止现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将两者结合的话应该\n',
            '能发现一些什么的……\n',
            '不过就是想不通那是什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_41A6')

    def _loc_4177(): pass

    label('loc_4177')

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不行啊……\n',
            '果然还是无法说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41A6(): pass

    label('loc_41A6')

    Jump('loc_44F2')

    def _loc_41A9(): pass

    label('loc_41A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_42CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_427A',
    )

    ChrTalk(
        0x00FE,
        (
            '现在的情况是所有的\n',
            '导力器都失去了导力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前也有过类似的事件，\n',
            '所以我尝试进行了理论上的解析……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过很遗憾，大部分\n',
            '还是没能理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能拉赛尔博士\n',
            '已经掌握了一些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_42CC')

    def _loc_427A(): pass

    label('loc_427A')

    ChrTalk(
        0x00FE,
        (
            '对我们来说这种现象\n',
            '现在还是一个大谜团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '目前根本无法从\n',
            '理论上来阐明它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_42CC(): pass

    label('loc_42CC')

    Jump('loc_44F2')

    def _loc_42CF(): pass

    label('loc_42CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_4376',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4335',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在整理\n',
            '地震的数据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了拉赛尔博士，\n',
            '『卡佩尔』里储存着\n',
            '庞大的记录。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4373')

    def _loc_4335(): pass

    label('loc_4335')

    ChrTalk(
        0x00FE,
        (
            '咦，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家刚刚出发\n',
            '前往了雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_4373(): pass

    label('loc_4373')

    Jump('loc_44F2')

    def _loc_4376(): pass

    label('loc_4376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_43E3',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士好像也在\n',
            '就地震进行调查呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，博士没问题的。\n',
            '即便是从石头里\n',
            '也能找出线索吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44F2')

    def _loc_43E3(): pass

    label('loc_43E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_44F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4446',
    )

    ChrTalk(
        0x00FE,
        (
            '现在还不知道\n',
            '刚才的地震的震源。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有可能是由于某种\n',
            '特别的原因引发的地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44F2')

    def _loc_4446(): pass

    label('loc_4446')

    ChrTalk(
        0x00FE,
        (
            '关于刚才的地震\n',
            '我查看了一下测量仪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这……还真是一次不寻常的地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和过去的所有地震\n',
            '都完全没有相似之处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有可能是由于某种\n',
            '特别的原因引发的地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_44F2(): pass

    label('loc_44F2')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x44F6
@scena.Code('func_0C_44F6')
def func_0C_44F6():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_45A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_456C',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，导力停止现象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我理论\n',
            '方面不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呆在这里可能\n',
            '也只是添乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)
    TalkEnd(0x000F)
    SetChrFlags(0x00FE, 0x0010)

    Return()

    def _loc_456C(): pass

    label('loc_456C')

    ChrTalk(
        0x00FE,
        (
            '唔，导力停止现象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '(……装作在思考的样子。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4857')

    def _loc_45A7(): pass

    label('loc_45A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4690',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_463A',
    )

    ChrTalk(
        0x00FE,
        (
            '据说『埃尔赛尤』降落在\n',
            '水中以后安然无恙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何总算让人松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从心底里感谢那些\n',
            '保护了船的船员们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_468D')

    def _loc_463A(): pass

    label('loc_463A')

    ChrTalk(
        0x00FE,
        (
            '据说『埃尔赛尤』降落在\n',
            '水中以后安然无恙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何总算让人松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_468D(): pass

    label('loc_468D')

    Jump('loc_4857')

    def _loc_4690(): pass

    label('loc_4690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_47C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_470B',
    )

    ChrTalk(
        0x00FE,
        (
            '好，登船准备完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概乌尔斯会照顾\n',
            '我妹妹乌缇的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是应该找一个\n',
            '会做家务的男朋友啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47BE')

    def _loc_470B(): pass

    label('loc_470B')

    ChrTalk(
        0x00FE,
        (
            '嗯，图纸全部打包\n',
            '放在箱子里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力系统的图纸\n',
            '由雨果负责……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了预备紧急的空腹状态\n',
            '还准备了点心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，准备完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，现在随时\n',
            '可以乘工程船了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_47BE(): pass

    label('loc_47BE')

    Jump('loc_4857')

    def _loc_47C1(): pass

    label('loc_47C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_4857',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_4853',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～检查结束以后终于\n',
            '要乘工程船出发了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了装配『埃尔赛尤』的引擎，\n',
            '竟然和我们交换……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好、好像还没\n',
            '回过神来～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4857')

    def _loc_4853(): pass

    label('loc_4853')

    Call(0, 0x000D)

    def _loc_4857(): pass

    label('loc_4857')

    TalkEnd(0x000F)

    Return()

# id: 0x000D offset: 0x485B
@scena.Code('func_0D_485B')
def func_0D_485B():
    OP_4A(0x000C, 255)
    OP_4A(0x000F, 255)

    ChrTalk(
        0x000F,
        (
            '『埃尔赛尤』的工程需要的\n',
            '备件都准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '接下来就是接受检查，\n',
            '然后搬进工程船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好，露依赛就负责\n',
            '插头的检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '因为那是你设计的，\n',
            '比让其他人做要来的准确。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '好，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我和维修长一起\n',
            '去看一下飞船坪的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000C, 255)
    OP_4B(0x000F, 255)
    OP_A2(0x0008)
    OP_A2(0x000B)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
