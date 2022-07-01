import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3221_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3221   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '麻绪婆婆'),
    TXT(0x02, '艾缇'),
    TXT(0x03, '赫雷思老人'),
    TXT(0x04, '赫雷思老人'),
    TXT(0x05, '艾德'),
    TXT(0x06, '莉西亚'),
    TXT(0x07, '法尔茨'),
    TXT(0x08, '蔡尔德'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3221.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3221_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x47FC
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
        ('ED6_DT07/CH02430._CH', 'ED6_DT07/CH02430P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 2590,
            z                   = 250,
            y                   = 5360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 8490,
            z                   = 0,
            y                   = 340,
            direction           = 102,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 14140,
            z                   = 200,
            y                   = 2029,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0135,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -2490,
            z                   = 0,
            y                   = 40320,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -31490,
            z                   = -250,
            y                   = 8530,
            direction           = 270,
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
            x                   = 7590,
            z                   = 0,
            y                   = 73170,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 11190,
            z                   = 0,
            y                   = 2440,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 8780,
            z                   = 200,
            y                   = 6560,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10003 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2670,
            triggerZ            = 250,
            triggerY            = 3820,
            triggerRange        = 400,
            actorX              = 2590,
            actorZ              = 1750,
            actorY              = 5360,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9940,
            triggerZ            = 0,
            triggerY            = 90,
            triggerRange        = 400,
            actorX              = 8490,
            actorZ              = 1500,
            actorY              = 340,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 8960,
            triggerZ            = 250,
            triggerY            = 13840,
            triggerRange        = 1000,
            actorX              = 9100,
            actorZ              = 1750,
            actorY              = 13840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x256
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_28B',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000A, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_283',
    )

    SetChrPos(0x000D, -1150, 0, 40780, 0)

    Jump('loc_288')

    def _loc_283(): pass

    label('loc_283')

    SetChrFlags(0x000D, 0x0080)

    def _loc_288(): pass

    label('loc_288')

    Jump('loc_2D3')

    def _loc_28B(): pass

    label('loc_28B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_29A',
    )

    SetChrFlags(0x000D, 0x0080)

    Jump('loc_2D3')

    def _loc_29A(): pass

    label('loc_29A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2B8',
    )

    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)

    Jump('loc_2D3')

    def _loc_2B8(): pass

    label('loc_2B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2CC',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000A, 0x0080)

    Jump('loc_2D3')

    def _loc_2CC(): pass

    label('loc_2CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2D3',
    )

    def _loc_2D3(): pass

    label('loc_2D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2E9',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 0x0003)

    Jump('loc_2F7')

    def _loc_2E9(): pass

    label('loc_2E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_2F7',
    )

    OP_A3(0x10F1)
    Event(0, 0x000C)

    def _loc_2F7(): pass

    label('loc_2F7')

    Return()

# id: 0x0001 offset: 0x2F8
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x2F9
@scena.Code('ReInit')
def ReInit():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x2FE
@scena.Code('func_03_2FE')
def func_03_2FE():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0070, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0070, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0070, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0070, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0070, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_335',
    )

    Call(1, 0x0001)

    Jump('loc_339')

    def _loc_335(): pass

    label('loc_335')

    Call(1, 0x0000)

    def _loc_339(): pass

    label('loc_339')

    Jump('loc_1C26')

    def _loc_33C(): pass

    label('loc_33C')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 3, 0x2083)),
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 2, 0x1482)),
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Or,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_385',
    )

    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_374',
    )

    OP_A9(0xA1)
    TalkEnd(0x0008)

    Return()

    def _loc_374(): pass

    label('loc_374')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_385',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_95A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 3, 0x2083)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_641',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(2590, 250, 4210, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 3260, 250, 3540, 0)
    SetChrPos(0x0102, 2200, 250, 3530, 0)
    SetChrPos(0x00F8, 3750, 250, 2330, 0)
    SetChrPos(0x00F9, 2210, 250, 2420, 0)
    OP_8C(0x0008, 180, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010370252V#1000F好久不见，麻绪婆婆。',
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
        'loc_4E2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370253V#061F你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370254V#680F哟，艾丝蒂尔，还有提妲。\n',
            '欢迎来我这儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370255V#683F哟，这位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_545')

    def _loc_4E2(): pass

    label('loc_4E2')

    ChrTalk(
        0x0008,
        (
            '#0570370256V#680F哟，艾丝蒂尔，还有你们几个。\n',
            '欢迎来我这儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370255V#683F哟，这位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_545(): pass

    label('loc_545')

    ChrTalk(
        0x0102,
        (
            '#0020370258V#1040F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370259V#681F我想怎么这么面熟呢，\n',
            '果然是约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370260V好久没见到你们\n',
            '一起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370261V#680F不巧，澡堂不能用，\n',
            '不过还是请你们好好放松一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370262V饭菜什么的\n',
            '还是和平常一样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2083)
    EventEnd(0x00)

    Jump('loc_956')

    def _loc_641(): pass

    label('loc_641')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F2',
    )

    ChrTalk(
        0x0008,
        (
            '#0570370696V#680F不巧，因为导力器停了，\n',
            '澡堂也不能用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370697V不过饭菜什么的\n',
            '还是和平常一样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370698V知道你们很忙，可还是\n',
            '希望你们能好好放松一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_956')

    def _loc_6F2(): pass

    label('loc_6F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_830',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B8',
    )

    ChrTalk(
        0x0008,
        (
            '#0570370699V#680F哟，你们几个。\n',
            '这次真是辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370700V在你们的帮助下旅馆\n',
            '也恢复往常的营业了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370701V虽然客人可能还要\n',
            '过一阵子才会回来，\n',
            '总之我会耐心地等的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_82D')

    def _loc_7B8(): pass

    label('loc_7B8')

    ChrTalk(
        0x0008,
        (
            '#0570370702V#680F在你们的帮助下旅馆\n',
            '也能像往常一样营业了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370703V接下来就是等客人在\n',
            '王国的混乱平息回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_82D(): pass

    label('loc_82D')

    Jump('loc_956')

    def _loc_830(): pass

    label('loc_830')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 7, 0x2007)),
            Expr.Return,
        ),
        'loc_951',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8DF',
    )

    ChrTalk(
        0x0008,
        (
            '#0570370704V#680F水泵小屋在村子的广场\n',
            '北边的高地上哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370705V如果那个不能用\n',
            '这里也就没法做生意了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370706V有什么好办法\n',
            '一定要告诉我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_94E')

    def _loc_8DF(): pass

    label('loc_8DF')

    ChrTalk(
        0x0008,
        (
            '#0570370704V#680F水泵小屋在村子的广场\n',
            '北边的高地上哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370708V如果那个不能用\n',
            '这里也就没法做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_94E(): pass

    label('loc_94E')

    Jump('loc_956')

    def _loc_951(): pass

    label('loc_951')

    Call(0, 0x000B)

    Return()

    def _loc_956(): pass

    label('loc_956')

    TalkEnd(0x0008)

    Return()

    def _loc_95A(): pass

    label('loc_95A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 2, 0x1482)),
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_E99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_A13',
    )

    ChrTalk(
        0x0008,
        (
            '#0570240191V#680F反正无论如何，\n',
            '要是自然造成的也没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570240192V如果再出现的话\n',
            '我就一定会联络协会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570240193V那么，你们几个，\n',
            '有事我会再找你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E96')

    def _loc_A13(): pass

    label('loc_A13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E4A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_B8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_AC8',
    )

    ChrTalk(
        0x0008,
        (
            '#0570240194V#680F地震看来也停止了，\n',
            '这样一来事情总算是平息了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570240195V有空的时候\n',
            '大家一起过来住下休息休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570240196V我这里随时\n',
            '欢迎你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B88')

    def _loc_AC8(): pass

    label('loc_AC8')

    ChrTalk(
        0x0008,
        (
            '#0570240197V#680F哟，你们几个。\n',
            '上回真是谢谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570240198V在你们的帮助下温泉\n',
            '也完全复原了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570240195V有空的时候\n',
            '大家一起过来住下休息休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570240196V我这里随时\n',
            '欢迎你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_B88(): pass

    label('loc_B88')

    Jump('loc_E47')

    def _loc_B8B(): pass

    label('loc_B8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_C00',
    )

    ChrTalk(
        0x0008,
        (
            '#0570231365V#680F源泉所在的洞窟\n',
            '可以从后面的栅门进入。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231366V用刚才的钥匙\n',
            '应该能打开栅门的锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E47')

    def _loc_C00(): pass

    label('loc_C00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_CF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_C88',
    )

    ChrTalk(
        0x0008,
        (
            '#0570231367V#680F听说好多地方\n',
            '都发生了地震啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231368V不过我觉得在这片土地上应该\n',
            '不会如此频繁地发生地震吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF4')

    def _loc_C88(): pass

    label('loc_C88')

    ChrTalk(
        0x0008,
        (
            '#0570231369V#680F最近好像在蔡斯\n',
            '也发生了地震吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231370V我几乎不记得在这片\n',
            '土地上发生过地震。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_CF4(): pass

    label('loc_CF4')

    Jump('loc_E47')

    def _loc_CF7(): pass

    label('loc_CF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_DF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D6D',
    )

    ChrTalk(
        0x0008,
        (
            '#0570231371V#680F互不侵犯条约就是大家\n',
            '和平共处的约定吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231372V为什么不早点\n',
            '缔结条约呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF1')

    def _loc_D6D(): pass

    label('loc_D6D')

    ChrTalk(
        0x0008,
        (
            '#0570231373V#680F那个什么互不侵犯条约\n',
            '的签字仪式很快就要举行了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231374V据说还有共和国的来宾，\n',
            '说不定客人会增加呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_DF1(): pass

    label('loc_DF1')

    Jump('loc_E47')

    def _loc_DF4(): pass

    label('loc_DF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_E47',
    )

    ChrTalk(
        0x0008,
        (
            '#0570231375V#680F你们随时可以\n',
            '去洗澡哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231376V总之小心一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E47(): pass

    label('loc_E47')

    Jump('loc_E96')

    def _loc_E4A(): pass

    label('loc_E4A')

    ChrTalk(
        0x0008,
        (
            '#0570231375V#680F你们随时可以\n',
            '去洗澡哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231376V总之小心一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E96(): pass

    label('loc_E96')

    Jump('loc_1C26')

    def _loc_E99(): pass

    label('loc_E99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_15DB',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0570231379V#680F哟，你们来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231380V#680F怎么？提妲也在？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231381V#560F您好，麻绪婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231382V#1006F麻绪婆婆，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231383V#680F嗯，艾丝蒂尔，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230859V与以前来的时候相比\n',
            '一下子变得更像大人了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231385V#1008F嘿嘿……是吗。',
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
        'loc_13DC',
    )

    ChrTalk(
        0x0104,
        (
            '#0040231386V#030F老板娘，上次麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0104, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231387V#683F哟，我还说怎么这么脸熟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231388V这不是奥利维尔先生吗？\n',
            '怎么连你也来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231389V#064F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040231390V#035F呵呵，说来话长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231391V现在我作为协力人员\n',
            '和他们一起行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231392V#1004F你、你们认识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231393V#680F嗯，不久前他\n',
            '在这里住宿过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231394V#685F我还是第一次看到有客人\n',
            '在泡澡时还弹琴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_11FB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231395V#551F看来这家伙无论到哪里\n',
            '都会做同样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_123F')

    def _loc_11FB(): pass

    label('loc_11FB')

    ChrTalk(
        0x0103,
        (
            '#0030231396V#025F唉，这个笨蛋好像无论到哪里\n',
            '都在做同样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_123F(): pass

    label('loc_123F')

    ChrTalk(
        0x0104,
        (
            '#0040231397V#031F哼哼，这是我们艺术家的宿命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231398V对为美的女神服务的人来说，\n',
            '时间和空间根本就是无关紧要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231399V#1007F即便如此，在全裸的\n',
            '状态下弹琴也太那个什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231400V#1013F啊……不好……\n',
            '在脑中想象了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070231401V#562F姐、姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570231402V#680F算啦，无论如何，\n',
            '你能喜欢我很高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231403V这样的话大家\n',
            '一起住下来怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_143B')

    def _loc_13DC(): pass

    label('loc_13DC')

    ChrTalk(
        0x0008,
        (
            '#0570231404V#680F话虽这么说，难得\n',
            '大家都来了',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231405V既然这样好好歇息\n',
            '一晚上怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_143B(): pass

    label('loc_143B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_14A5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231406V#051F我们倒是想这样，\n',
            '可不巧的是现在是在工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231407V下次有机会再讨教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1509')

    def _loc_14A5(): pass

    label('loc_14A5')

    ChrTalk(
        0x0103,
        (
            '#0030231408V#020F我们倒是想这样，\n',
            '可不巧的是现在是在工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231409V下次有机会再讨饶吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1509(): pass

    label('loc_1509')

    ChrTurnDirection(0x0008, 0x00F7, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231436V#680F怎么？又是工作？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231437V那么至少\n',
            '去泡个澡吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231438V我这里你们可以随时\n',
            '随意用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231439V#1001F啊，那可是求之不得啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231440V嗯，有时间我们\n',
            '就去试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C20')

    def _loc_15DB(): pass

    label('loc_15DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1C20',
    )

    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0570231379V#680F哟，你们来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231411V#1006F你好，麻绪婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570231412V#680F艾丝蒂尔，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230859V与以前来的时候相比\n',
            '一下子变得更像大人了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231385V#1008F嘿嘿……是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040231386V#030F老板娘，上次麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0104, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231387V#683F哟，我还说怎么这么脸熟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231388V这不是奥利维尔先生吗？\n',
            '怎么连你也来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040231390V#035F呵呵，说来话长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231391V现在我作为协力人员\n',
            '和他们一起行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231392V#1004F你、你们认识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231393V#680F嗯，不久前他\n',
            '在这里住宿过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231394V#685F我还是第一次看到有客人\n',
            '在澡堂里弹琴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_18A9',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231395V#551F就是说他到哪儿\n',
            '都会做同样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E5')

    def _loc_18A9(): pass

    label('loc_18A9')

    ChrTalk(
        0x0103,
        (
            '#0030231396V#025F唉，就是说他到哪儿\n',
            '都会做同样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18E5(): pass

    label('loc_18E5')

    ChrTalk(
        0x0104,
        (
            '#0040231397V#031F哼哼，这是我们艺术家的宿命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231398V对为美的女神服务的人来说\n',
            '时间和空间根本就是无关紧要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231399V#1007F即便如此，在全裸的\n',
            '状态下弹琴也太那个什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231400V#1013F啊……不好……\n',
            '在脑中想象了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060231429V#540F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570231402V#680F算啦，无论如何，\n',
            '只要你们喜欢就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231403V这样的话，不如大家\n',
            '一起住下来怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1ADD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231432V#051F我们也很想啊，\n',
            '可惜现在正在调查的途中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231407V下次有机会再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B49')

    def _loc_1ADD(): pass

    label('loc_1ADD')

    ChrTalk(
        0x0103,
        (
            '#0030231434V#020F其实我们也很想那样，\n',
            '不巧的是我们还在调查的途中哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231409V下次有机会时再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B49(): pass

    label('loc_1B49')

    ChrTurnDirection(0x0008, 0x00F7, 400)

    ChrTalk(
        0x0008,
        (
            '#0570231436V#680F怎么？又有工作了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231437V那么至少\n',
            '去泡个澡吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570231438V我这里随时\n',
            '可以让你们使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231439V#1001F啊，那太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231440V嗯，有时间的话我们\n',
            '一定会去泡一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C20(): pass

    label('loc_1C20')

    OP_A2(0x1482)
    OP_A2(0x0000)
    def _loc_1C26(): pass

    label('loc_1C26')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1C2A
@scena.Code('func_04_1C2A')
def func_04_1C2A():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x1C2F
@scena.Code('func_05_1C2F')
def func_05_1C2F():
    TalkBegin(0x0009)
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
            TXT(0x01, '买东西\n'),
            TXT(0x02, '招牌菜『东方火锅·山』　1000米拉\n'),
            TXT(0x03, '退出\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CAE',
    )

    OP_0D()
    OP_A9(0xA2)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_1CAE(): pass

    label('loc_1CAE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DBC',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x3E8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1D87',
    )

    SubMira(1000)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x000B, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '东方火锅·山',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFD, 3000)
    SetChrStatus(ChrTable['约修亚'], 0xFD, 3000)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFD, 3000)
    SetChrStatus(ChrTable['奥利维尔'], 0xFD, 3000)
    SetChrStatus(ChrTable['科洛丝'], 0xFD, 3000)
    SetChrStatus(ChrTable['阿加特'], 0xFD, 3000)
    SetChrStatus(ChrTable['提妲'], 0xFD, 3000)
    SetChrStatus(ChrTable['金'], 0xFD, 3000)
    SetChrStatus(ChrTable['凯文神父'], 0xFD, 3000)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D79',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0004)"),
            Expr.Return,
        ),
        'loc_1D4D',
    )

    Jump('loc_1D79')

    def _loc_1D4D(): pass

    label('loc_1D4D')

    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '东方火锅·山',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D79(): pass

    label('loc_1D79')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_1DAD')

    def _loc_1D87(): pass

    label('loc_1D87')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_1DAD(): pass

    label('loc_1DAD')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0009)

    Return()

    def _loc_1DBC(): pass

    label('loc_1DBC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DCD',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_1DCD(): pass

    label('loc_1DCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1E77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E2E',
    )

    ChrTalk(
        0x0009,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '澡堂终于\n',
            '可以用了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请各位客人\n',
            '你们去泡一个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1E74')

    def _loc_1E2E(): pass

    label('loc_1E2E')

    ChrTalk(
        0x0009,
        (
            '澡堂终于\n',
            '可以用了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样一来我们的旅馆也\n',
            '也能照常营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E74(): pass

    label('loc_1E74')

    Jump('loc_223B')

    def _loc_1E77(): pass

    label('loc_1E77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1F4A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F05',
    )

    ChrTalk(
        0x0009,
        (
            '欢迎。\n',
            '欢迎来到『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是不好意思，\n',
            '现在澡堂不能用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '导力器竟然全都不行了，\n',
            '到底是什么原因呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1F47')

    def _loc_1F05(): pass

    label('loc_1F05')

    ChrTalk(
        0x0009,
        (
            '抱歉，\n',
            '澡堂不能用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真的很抱歉。\n',
            '虽然你们可能很期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F47(): pass

    label('loc_1F47')

    Jump('loc_223B')

    def _loc_1F4A(): pass

    label('loc_1F4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1FDB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1F8F',
    )

    ChrTalk(
        0x0009,
        (
            '吃饭前\n',
            '泡个澡怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '已经能照常\n',
            '使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FD8')

    def _loc_1F8F(): pass

    label('loc_1F8F')

    ChrTalk(
        0x0009,
        (
            '哎呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '吃饭前\n',
            '泡个澡怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '已经能照常\n',
            '使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1FD8(): pass

    label('loc_1FD8')

    Jump('loc_223B')

    def _loc_1FDB(): pass

    label('loc_1FDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2076',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_202F',
    )

    ChrTalk(
        0x0009,
        (
            '这样的事情至今为止\n',
            '一次也没有发生过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '到底发生了什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2073')

    def _loc_202F(): pass

    label('loc_202F')

    ChrTalk(
        0x0009,
        (
            '温泉竟然热到\n',
            '要沸腾的程度了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '地下到底在发生着什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_2073(): pass

    label('loc_2073')

    Jump('loc_223B')

    def _loc_2076(): pass

    label('loc_2076')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2197',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0070, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_20F6',
    )

    ChrTalk(
        0x0009,
        (
            '好像有魔兽\n',
            '闯进了露天澡堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '莫非偷窥色魔的传言\n',
            '就是说的那些魔兽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的，搞得这么沸沸扬扬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2194')

    def _loc_20F6(): pass

    label('loc_20F6')

    ChrTalk(
        0x0009,
        (
            '最近有传言说我们\n',
            '澡堂有人在偷窥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过又没人看清\n',
            '罪犯的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '又没有证据，\n',
            '光有传言传播出去真令人讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望你们游击士\n',
            '能赶紧想想办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2194(): pass

    label('loc_2194')

    Jump('loc_223B')

    def _loc_2197(): pass

    label('loc_2197')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_223B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_21E8',
    )

    ChrTalk(
        0x0009,
        (
            '我们的东方菜是很有名的哦。\n',
            '还有新菜单，\n',
            '请你们一定要试试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223B')

    def _loc_21E8(): pass

    label('loc_21E8')

    ChrTalk(
        0x0009,
        (
            '呀，欢迎。\n',
            '欢迎来到『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们的东方菜是很有名的哦。\n',
            '请随意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_223B(): pass

    label('loc_223B')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x223F
@scena.Code('func_06_223F')
def func_06_223F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2315',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_22B9',
    )

    ChrTalk(
        0x00FE,
        (
            '东方菜的优点在于\n',
            '灵活发挥材料特色的烹调法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是味觉敏锐的人\n',
            '是很难明白这其中的优点的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2312')

    def _loc_22B9(): pass

    label('loc_22B9')

    ChrTalk(
        0x00FE,
        (
            '这儿的东方菜\n',
            '可是丝毫不输原产地的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是安特洛丝的常客，\n',
            '听我的准没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2312(): pass

    label('loc_2312')

    Jump('loc_2424')

    def _loc_2315(): pass

    label('loc_2315')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_2371',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_233C',
    )

    ChrTalk(
        0x00FE,
        (
            '外面怎么这么吵？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_236E')

    def _loc_233C(): pass

    label('loc_233C')

    ChrTalk(
        0x00FE,
        (
            '外面怎么这么吵？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有魔兽\n',
            '闯进来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_236E(): pass

    label('loc_236E')

    Jump('loc_2424')

    def _loc_2371(): pass

    label('loc_2371')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_237B',
    )

    Jump('loc_2424')

    def _loc_237B(): pass

    label('loc_237B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2424',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_23CF',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵～好舒服的热水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '浴衣也很整洁。\n',
            '这儿的温泉质量真好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2424')

    def _loc_23CF(): pass

    label('loc_23CF')

    ChrTalk(
        0x00FE,
        (
            '我是千里迢迢从\n',
            '柏斯来这儿做温泉疗养的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这儿的温泉\n',
            '值得我这么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2424(): pass

    label('loc_2424')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x2428
@scena.Code('func_07_2428')
def func_07_2428():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_24F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_249C',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，你们几个，\n',
            '听说是你们修好了泵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，已经是第二次说这话了，\n',
            '今后也请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_24EE')

    def _loc_249C(): pass

    label('loc_249C')

    ChrTalk(
        0x00FE,
        (
            '今后也要指望你们\n',
            '这些游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为导力器不能用以后\n',
            '到处都很不容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24EE(): pass

    label('loc_24EE')

    Jump('loc_289E')

    def _loc_24F1(): pass

    label('loc_24F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_25D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_257F',
    )

    ChrTalk(
        0x00FE,
        (
            '我们这里的灶不是导力式的，\n',
            '所以不影响工作啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力虽然也很诱人，\n',
            '不过一发生这样的事，\n',
            '就能看到旧工具的好处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_25D1')

    def _loc_257F(): pass

    label('loc_257F')

    ChrTalk(
        0x00FE,
        (
            '我们这里的灶不是导力式的，\n',
            '所以不影响工作啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然工具还是\n',
            '越简单越好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25D1(): pass

    label('loc_25D1')

    Jump('loc_289E')

    def _loc_25D4(): pass

    label('loc_25D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2688',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_262B',
    )

    ChrTalk(
        0x000C,
        (
            '在你们的帮助下\n',
            '温泉也完全复原了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '下次你们趁休息\n',
            '过来玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2685')

    def _loc_262B(): pass

    label('loc_262B')

    ChrTalk(
        0x000C,
        (
            '哟，是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哎呀～在你们的帮助下\n',
            '温泉也完全复原了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '游击士果然可靠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2685(): pass

    label('loc_2685')

    Jump('loc_289E')

    def _loc_2688(): pass

    label('loc_2688')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_273C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_26F3',
    )

    ChrTalk(
        0x000C,
        (
            '不过还真没想到温泉\n',
            '会被煮得沸沸腾腾的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不管世间发生什么\n',
            '接下来会发生什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2739')

    def _loc_26F3(): pass

    label('loc_26F3')

    ChrTalk(
        0x000C,
        (
            '源泉的调查就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这样下去的话，\n',
            '我们没法营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2739(): pass

    label('loc_2739')

    Jump('loc_289E')

    def _loc_273C(): pass

    label('loc_273C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_280B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_27A3',
    )

    ChrTalk(
        0x000C,
        (
            '莉西亚不愧是我的女儿，\n',
            '味觉相当敏锐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过因为太像我，\n',
            '性格也大大咧咧的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2808')

    def _loc_27A3(): pass

    label('loc_27A3')

    ChrTalk(
        0x000C,
        (
            '最近我女儿莉西亚也\n',
            '来旅馆帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '虽然现在在打扫房间，\n',
            '不过也希望她将来能做我的帮手哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2808(): pass

    label('loc_2808')

    Jump('loc_289E')

    def _loc_280B(): pass

    label('loc_280B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_289E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2868',
    )

    ChrTalk(
        0x000C,
        (
            '都说东方菜的好处\n',
            '有三个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '第一是味道，接下来是外观，\n',
            '最后是健康。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_289E')

    def _loc_2868(): pass

    label('loc_2868')

    ChrTalk(
        0x000C,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '请一定尝尝我们\n',
            '拿手的东方菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_289E(): pass

    label('loc_289E')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x28A2
@scena.Code('func_08_28A2')
def func_08_28A2():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_299A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2939',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器都不能用了，\n',
            '大家怎么好像都不太着急呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反而是我这个旁观者\n',
            '都快要着急起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在蔡斯那边\n',
            '一定很混乱吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_2997')

    def _loc_2939(): pass

    label('loc_2939')

    ChrTalk(
        0x00FE,
        (
            '导力器都不能用了，\n',
            '大家怎么好像都不太着急呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反而是我这个旁观者\n',
            '都快要着急起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2997(): pass

    label('loc_2997')

    Jump('loc_2E0D')

    def _loc_299A(): pass

    label('loc_299A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 0, 0x1430)),
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2B51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B0E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2AC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2A25',
    )

    ChrTalk(
        0x000D,
        (
            '反正也是闲着，就开始\n',
            '打工了，打扫卫生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过都是一些上了年纪的客人，\n',
            '不太有干劲啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AC1')

    def _loc_2A25(): pass

    label('loc_2A25')

    ChrTalk(
        0x000D,
        (
            '反正也是闲着，就开始\n',
            '打工了，打扫卫生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过都是一些上了年纪的客人，\n',
            '不太有干劲啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '要是多一些像奥利维尔大人\n',
            '这样的有趣的客人该多好啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_2AC1(): pass

    label('loc_2AC1')

    Jump('loc_2B0B')

    def _loc_2AC4(): pass

    label('loc_2AC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_2B0B',
    )

    ChrTalk(
        0x000D,
        (
            '啊～还是\n',
            '奥利维尔大人优秀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '哎呀～请把我\n',
            '拐去帝都吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B0B(): pass

    label('loc_2B0B')

    Jump('loc_2B4E')

    def _loc_2B0E(): pass

    label('loc_2B0E')

    ChrTalk(
        0x000D,
        (
            '啊～还是\n',
            '奥利维尔大人优秀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '哎呀～请把我\n',
            '拐去帝都吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2B4E(): pass

    label('loc_2B4E')

    Jump('loc_2E0D')

    def _loc_2B51(): pass

    label('loc_2B51')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C86',
    )

    ChrTalk(
        0x000D,
        (
            '反正也是闲着，就开始\n',
            '打工了，打扫卫生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过都是一些上了年纪的客人，\n',
            '不太有干劲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '……咦？啊、啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '呀～！？　这不是奥利维尔大人么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我真高兴～！\n',
            '您又来啦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F（奥、奥利维尔大人～？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F呵呵，好久不见。\n',
            '还乖吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC1')

    def _loc_2C86(): pass

    label('loc_2C86')

    ChrTalk(
        0x000D,
        (
            '反正也是闲着，就开始\n',
            '打工了，打扫卫生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过都是一些上了年纪的客人，\n',
            '不太有干劲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0104, 500)

    ChrTalk(
        0x000D,
        (
            '……咦？啊、啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '那、那边是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F呵呵，好久不见。\n',
            '还乖吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '呀～！？\n',
            '果然是奥利维尔大人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我真高兴～！\n',
            '您又来啦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F（奥、奥利维尔大人～？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DC1(): pass

    label('loc_2DC1')

    ChrTalk(
        0x000D,
        (
            '奥利维尔先生～\n',
            '这次要再唱歌给我听哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '您弹琴的样子\n',
            '最帅了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1430)
    OP_A2(0x0005)
    def _loc_2E0D(): pass

    label('loc_2E0D')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x2E11
@scena.Code('func_09_2E11')
def func_09_2E11():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_2ED7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2E63',
    )

    ChrTalk(
        0x00FE,
        (
            '今天要采访\n',
            '东方菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～希望能找到\n',
            '好的表达方式……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ED7')

    def _loc_2E63(): pass

    label('loc_2E63')

    ChrTalk(
        0x00FE,
        (
            '要用文章来描写\n',
            '菜的可口是很难的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '越是真正的美味，\n',
            '越难写成文章。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为除了『好吃』以外\n',
            '无以形容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_2ED7(): pass

    label('loc_2ED7')

    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x2EDB
@scena.Code('func_0A_2EDB')
def func_0A_2EDB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_2F74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F3A',
    )

    ChrTalk(
        0x00FE,
        (
            '开水好像能出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，看来是阿尔宾的愿望\n',
            '传递到了女神那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_2F71')

    def _loc_2F3A(): pass

    label('loc_2F3A')

    ChrTalk(
        0x00FE,
        (
            '开水好像能出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再过一会儿\n',
            '去浴场看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F71(): pass

    label('loc_2F71')

    Jump('loc_30C4')

    def _loc_2F74(): pass

    label('loc_2F74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_30C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3064',
    )

    ChrTalk(
        0x00FE,
        (
            '为了治疗登山的疲劳，\n',
            '我和同伴温泉疗养来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过遗憾的是因为泵的问题，\n',
            '没法去洗温泉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我的同伴不死心，\n',
            '还是去了浴室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候就算勉强\n',
            '对自己也没好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是吃着美味的\n',
            '东方菜好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_30C4')

    def _loc_3064(): pass

    label('loc_3064')

    ChrTalk(
        0x00FE,
        (
            '明明知道不能洗，\n',
            '阿尔宾还是去了澡堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙是个一旦决定了什么就\n',
            '死也不会回头的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30C4(): pass

    label('loc_30C4')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x30C8
@scena.Code('func_0B_30C8')
def func_0B_30C8():
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
        'loc_30E8',
    )

    Call(0, 0x000D)
    Call(0, 0x000E)
    FadeIn(0, 0)

    def _loc_30E8(): pass

    label('loc_30E8')

    Fade(500)
    OP_6D(1600, 250, 5180, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    SetChrPos(0x0101, 3260, 250, 3540, 0)
    SetChrPos(0x0102, 2100, 250, 3530, 0)
    SetChrPos(0x00F8, 3700, 250, 2250, 0)
    SetChrPos(0x00F9, 2250, 250, 2250, 0)
    OP_8C(0x0008, 180, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_29(0x00C2, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_367F',
    )

    ChrTalk(
        0x0008,
        (
            '#0570370279V#680F#2P温泉的事\n',
            '你们不必在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370275V你们应该有你们\n',
            '应该做的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370276V要优先顾及那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【那我们就不客气了】\n'),
            TXT(0x01, '【硬着头皮帮忙】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3274',
    )

    OP_28(0x00C2, 0x01, 0x8000)
    EventEnd(0x00)

    Jump('loc_367C')

    def _loc_3274(): pass

    label('loc_3274')

    ChrTalk(
        0x0101,
        (
            '#0010370282V#1006F#6P不过，难得有机会，\n',
            '能不能交给我们试试？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370283V说不定会得到\n',
            '游击士才能给出的结果呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020370284V#1044F#5P艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370285V#683F#2P哦……？\n',
            '那是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370286V#1015F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370287V#1006F首先希望您能\n',
            '借给我们水泵小屋的钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370288V#680F#2P嗯，这倒没问题……',
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
            (TxtCtl.Item, ItemTable['水泵小屋的钥匙']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34D3',
    )

    ChrTurnDirection(0x0101, 0x0107, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010370289V#1006F#2P提妲，正好有机会，\n',
            '要不要去看看泵装置的状况？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370290V可能会发现\n',
            '一些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370291V#560F#6P啊，……嗯、是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3548')

    def _loc_34D3(): pass

    label('loc_34D3')

    OP_8C(0x0101, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010370292V#1006F#2P各位，正好有机会\n',
            '要不要去看看泵装置的状况？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370290V可能会发现\n',
            '一些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3548(): pass

    label('loc_3548')

    ChrTalk(
        0x0102,
        (
            '#0020370294V#1040F#5P原来是这样。',
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
        'loc_35AC',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050370295V#051F#6P真是没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35AC(): pass

    label('loc_35AC')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35E5',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030370296V#021F#6P我没意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35E5(): pass

    label('loc_35E5')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_362D',
    )

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080370297V#070F#6P总之先去\n',
            '确认一下情况吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_362D(): pass

    label('loc_362D')

    ChrTalk(
        0x0101,
        (
            '#0010370298V#1001F#2P那就决定了。\n',
            '去水泵小屋看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2007)
    OP_28(0x00C2, 0x04, 0x02)
    OP_28(0x00C2, 0x04, 0x08)
    OP_28(0x00C2, 0x01, 0x0001)
    EventEnd(0x00)

    def _loc_367C(): pass

    label('loc_367C')

    Jump('loc_3DC5')

    def _loc_367F(): pass

    label('loc_367F')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36E1',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370263V#063F#6P请问，麻绪婆婆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370264V我们有什么\n',
            '能帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_372B')

    def _loc_36E1(): pass

    label('loc_36E1')

    ChrTalk(
        0x0101,
        (
            '#0010370265V#1015F#6P麻绪婆婆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370266V我们有什么\n',
            '能帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_372B(): pass

    label('loc_372B')

    ChrTalk(
        0x0008,
        (
            '#0570370267V#680F#2P嗯，这个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370268V士兵已经开始\n',
            '定期巡逻了，\n',
            '所以安全方面没什么问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370269V硬要说的话，我希望可以\n',
            '想办法让温泉能恢复使用……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370270V#685F不过可能跟你们\n',
            '说了也没什么用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210313V#1015F#6P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        0,
        (
            TXT(0x00, '【到底还是太难了……】\n'),
            TXT(0x01, '【硬着头皮帮忙】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39BD',
    )

    ChrTalk(
        0x0101,
        (
            '#0010370272V#1007F#6P……抱歉，麻绪婆婆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370273V#1003F确实对我们来说\n',
            '太难了点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370274V#680F#2P嗯，没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370275V你们应该有你们\n',
            '应该做的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370276V要优先顾及那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370277V#1035F#6P……嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370278V#1025F#6P嗯……\n',
            '我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C2, 0x01, 0x8000)
    EventEnd(0x00)

    Jump('loc_3DC5')

    def _loc_39BD(): pass

    label('loc_39BD')

    ChrTalk(
        0x0101,
        (
            '#0010370282V#1006F#6P不过，难得有机会，\n',
            '能不能交给我们试试？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370283V说不定会得到\n',
            '游击士才能给出的结果呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020370284V#1044F#5P艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370285V#683F#2P哦……？\n',
            '那是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370286V#1015F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370287V#1006F首先希望你能\n',
            '借给我们水泵小屋的钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370288V#680F#2P嗯，这倒没问题……',
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
            (TxtCtl.Item, ItemTable['水泵小屋的钥匙']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['水泵小屋的钥匙'], 1)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C1C',
    )

    ChrTurnDirection(0x0101, 0x0107, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010370289V#1006F#2P提妲，正好有机会，\n',
            '要不要去看看泵装置的状况？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370290V可能会发现\n',
            '一些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370291V#560F#6P啊，……嗯、是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C91')

    def _loc_3C1C(): pass

    label('loc_3C1C')

    OP_8C(0x0101, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010370292V#1006F#2P各位，正好有机会\n',
            '要不要去看看泵装置的状况？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370290V可能会发现\n',
            '一些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C91(): pass

    label('loc_3C91')

    ChrTalk(
        0x0102,
        (
            '#0020370294V#1040F#5P原来是这样。',
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
        'loc_3CF5',
    )

    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050370295V#051F#6P真是没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CF5(): pass

    label('loc_3CF5')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D2E',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030370296V#021F#6P我没意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D2E(): pass

    label('loc_3D2E')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D76',
    )

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080370297V#070F#6P总之先去\n',
            '确认一下情况吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D76(): pass

    label('loc_3D76')

    ChrTalk(
        0x0101,
        (
            '#0010370298V#1001F#2P那就决定了。\n',
            '去水泵小屋看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2007)
    OP_28(0x00C2, 0x04, 0x02)
    OP_28(0x00C2, 0x04, 0x08)
    OP_28(0x00C2, 0x01, 0x0001)
    EventEnd(0x00)

    def _loc_3DC5(): pass

    label('loc_3DC5')

    CreateThread(0x0008, 0x00, 0x06, 0x0002)

    Return()

# id: 0x000C offset: 0x3DCD
@scena.Code('func_0C_3DCD')
def func_0C_3DCD():
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
        'loc_3DED',
    )

    Call(0, 0x000D)
    Call(0, 0x000E)
    FadeIn(0, 0)

    def _loc_3DED(): pass

    label('loc_3DED')

    OP_4A(0x0008, 255)
    OP_6D(1600, 250, 5180, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    SetChrPos(0x0101, 3260, 250, 3540, 0)
    SetChrPos(0x0102, 2100, 250, 3530, 0)
    SetChrPos(0x00F8, 3700, 250, 2250, 0)
    SetChrPos(0x00F9, 2250, 250, 2250, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0570370671V#680F#2P──没想到你们真能\n',
            '让泵动起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370672V#681F谢谢啊。\n',
            '这样一来就能让\n',
            '大家尽情地泡澡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370673V#1008F#6P嘿嘿……\n',
            '能帮上你们真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010370674V#1006F#2P不过９成是\n',
            '提妲的功劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370675V#067F#6P没、没有～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370676V#560F因为姐姐你们找来了\n',
            '必要的东西，\n',
            '我才能改造的。',
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
        'loc_40A1',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4000',
    )

    ChrTurnDirection(0x00F9, 0x0101, 400)

    Jump('loc_4007')

    def _loc_4000(): pass

    label('loc_4000')

    ChrTurnDirection(0x00F8, 0x0102, 400)

    def _loc_4007(): pass

    label('loc_4007')

    ChrTalk(
        0x0106,
        (
            '#0050370677V#551F#6P不过这次还真是\n',
            '让我们东奔西跑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370678V#555F这也是导力停止现象的危害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4077')
    def lambda_4077():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4077)

    Sleep(50)

    @scena.Lambda('lambda_408A')
    def lambda_408A():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_408A)

    Sleep(50)

    ChrTurnDirection(0x0107, 0x0106, 400)

    Jump('loc_422A')

    def _loc_40A1(): pass

    label('loc_40A1')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4167',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40C6',
    )

    ChrTurnDirection(0x00F9, 0x0101, 400)

    Jump('loc_40CD')

    def _loc_40C6(): pass

    label('loc_40C6')

    ChrTurnDirection(0x00F8, 0x0102, 400)

    def _loc_40CD(): pass

    label('loc_40CD')

    ChrTalk(
        0x0103,
        (
            '#0030370679V#025F#6P不过这次还真是\n',
            '让我们东奔西跑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370680V#022F这也是导力停止现象的危害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_413D')
    def lambda_413D():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_413D)

    Sleep(50)

    @scena.Lambda('lambda_4150')
    def lambda_4150():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4150)

    Sleep(50)

    ChrTurnDirection(0x0107, 0x0103, 400)

    Jump('loc_422A')

    def _loc_4167(): pass

    label('loc_4167')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_422A',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_418C',
    )

    ChrTurnDirection(0x00F9, 0x0101, 400)

    Jump('loc_4193')

    def _loc_418C(): pass

    label('loc_418C')

    ChrTurnDirection(0x00F8, 0x0102, 400)

    def _loc_4193(): pass

    label('loc_4193')

    ChrTalk(
        0x0108,
        (
            '#0080370681V#075F#6P不过这次还真是\n',
            '让我们东奔西跑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370682V#072F这也是导力停止现象的危害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4203')
    def lambda_4203():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4203)

    Sleep(50)

    @scena.Lambda('lambda_4216')
    def lambda_4216():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4216)

    Sleep(50)

    ChrTurnDirection(0x0107, 0x0108, 400)

    def _loc_422A(): pass

    label('loc_422A')

    WaitForThreadExit(0x0102, 0x0001)
    Sleep(200)

    ChrTalk(
        0x0102,
        (
            '#0020370683V#1043F#5P……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370684V#1035F技术方面的功能丧失，\n',
            '对以此为基础的社会\n',
            '有着严重的影响……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370685V#1042F这样下去的话\n',
            '事态只会不断恶化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370686V#063F#6P约修亚哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010370687V#1006F#4P好了，也没\n',
            '那么悲观了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370688V导力虽然停了，\n',
            '不过泵不也能用了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370689V#1001F人只要有决心\n',
            '什么都能做到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020370690V#1044F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570370691V#681F#2P哈哈，说得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370692V#680F总之这次\n',
            '真的是累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4430')
    def lambda_4430():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4430)

    Sleep(100)

    @scena.Lambda('lambda_4443')
    def lambda_4443():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4443)

    Sleep(100)

    @scena.Lambda('lambda_4456')
    def lambda_4456():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_4456)

    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_447A',
    )

    OP_8C(0x00F9, 0, 400)

    Jump('loc_4481')

    def _loc_447A(): pass

    label('loc_447A')

    OP_8C(0x00F8, 0, 400)

    def _loc_4481(): pass

    label('loc_4481')

    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0570370693V#680F#2P赶快先去泡个澡，\n',
            '消解旅行的疲劳吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370694V#681F对了，我家有祖传的\n',
            '有效的药草茶哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570370695V你们可以在洗完澡时喝。',
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
            '得到了４个',
            (TxtCtl.Item, ItemTable['最终浓缩药草茶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['最终浓缩药草茶'], 4)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '此后，泡了温泉的艾丝蒂尔一行\n',
            '在品尝了麻绪赖以自豪的东方菜后\n',
            '离开了『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.Eval, "OP_42(0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45E6',
    )

    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFB, 0)

    def _loc_45E6(): pass

    label('loc_45E6')

    If(
        (
            (Expr.Eval, "OP_42(0x01)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45F9',
    )

    SetChrStatus(ChrTable['约修亚'], 0xFB, 0)

    def _loc_45F9(): pass

    label('loc_45F9')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_460C',
    )

    SetChrStatus(ChrTable['雪拉扎德'], 0xFB, 0)

    def _loc_460C(): pass

    label('loc_460C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_461F',
    )

    SetChrStatus(ChrTable['阿加特'], 0xFB, 0)

    def _loc_461F(): pass

    label('loc_461F')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4632',
    )

    SetChrStatus(ChrTable['提妲'], 0xFB, 0)

    def _loc_4632(): pass

    label('loc_4632')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4645',
    )

    SetChrStatus(ChrTable['金'], 0xFB, 0)

    def _loc_4645(): pass

    label('loc_4645')

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【亚尔摩温泉的修复】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['水泵小屋的钥匙'], 1)
    RemoveItem(ItemTable['工房长的介绍信'], 1)
    OP_28(0x00C2, 0x04, 0x10)
    OP_28(0x00C2, 0x01, 0x2000)
    OP_28(0x00C2, 0x01, 0x4000)
    OP_A2(0x2012)
    ClearMapFlags(0x10000000)
    NewScene('ED6_DT21/T3200._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x46B5
@scena.Code('func_0D_46B5')
def func_0D_46B5():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_4732'),
        (0x00000001, 'loc_4738'),
        (-1, 'loc_473E'),
    )

    def _loc_4732(): pass

    label('loc_4732')

    OP_A2(0x1200)

    Jump('loc_473E')

    def _loc_4738(): pass

    label('loc_4738')

    OP_A2(0x1201)

    Jump('loc_473E')

    def _loc_473E(): pass

    label('loc_473E')

    Return()

# id: 0x000E offset: 0x473F
@scena.Code('func_0E_473F')
def func_0E_473F():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
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
            0x0007,
            0xFFFF,
        ),
    )

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

# id: 0x000F offset: 0x4798
@scena.Code('func_0F_4798')
def func_0F_4798():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '露天澡堂在这边 ≡',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
