import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0110   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '鲁克'),
    TXT(0x02, '鲁克'),
    TXT(0x03, '玛茜婆婆'),
    TXT(0x04, '帕特'),
    TXT(0x05, '雷特拉'),
    TXT(0x06, '赛拉'),
    TXT(0x07, '阿斯顿队长'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0110.x'
    header.mapIndex       = 11
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0110_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1EDA
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
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01110._CH', 'ED6_DT07/CH01110P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT26/CH20330._CH', 'ED6_DT26/CH20330P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 54480,
            z                   = 0,
            y                   = 163580,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 55200,
            z                   = 100,
            y                   = 159950,
            direction           = 180,
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
            x                   = 51750,
            z                   = 0,
            y                   = 163200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 56170,
            z                   = 0,
            y                   = 161420,
            direction           = 180,
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
            x                   = 93320,
            z                   = 0,
            y                   = 162900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 58080,
            z                   = 0,
            y                   = 198250,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 49300,
            z                   = 0,
            y                   = 161100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 94990,
            triggerZ            = 0,
            triggerY            = 166570,
            triggerRange        = 800,
            actorX              = 95120,
            actorZ              = 1400,
            actorY              = 165990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_22D',
    )

    SetChrFlags(0x000D, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20E',
    )

    SetChrPos(0x000B, 55510, 0, 163460, 270)

    Jump('loc_22A')

    def _loc_20E(): pass

    label('loc_20E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_219',
    )

    Jump('loc_22A')

    def _loc_219(): pass

    label('loc_219')

    SetChrPos(0x000B, 55510, 0, 163460, 270)

    def _loc_22A(): pass

    label('loc_22A')

    Jump('loc_2D2')

    def _loc_22D(): pass

    label('loc_22D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_237',
    )

    Jump('loc_2D2')

    def _loc_237(): pass

    label('loc_237')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_272',
    )

    SetChrPos(0x000A, 55120, 0, 161430, 180)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 92380, 0, 161500, 180)
    ClearChrFlags(0x0009, 0x0080)
    SetChrSubChip(0x0009, 4)

    Jump('loc_2D2')

    def _loc_272(): pass

    label('loc_272')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2A1',
    )

    SetChrFlags(0x000A, 0x0010)
    SetChrPos(0x000A, 55120, 0, 161430, 180)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrSubChip(0x0009, 4)

    Jump('loc_2D2')

    def _loc_2A1(): pass

    label('loc_2A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2BC',
    )

    SetChrPos(0x000D, 88100, 0, 162410, 270)

    Jump('loc_2D2')

    def _loc_2BC(): pass

    label('loc_2BC')

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000A, 49230, 0, 165600, 0)

    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_2E0',
    )

    OP_A3(0x10F0)
    Event(0, 0x0009)

    def _loc_2E0(): pass

    label('loc_2E0')

    Return()

# id: 0x0001 offset: 0x2E1
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2EB',
    )

    Jump('loc_317')

    def _loc_2EB(): pass

    label('loc_2EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2FC',
    )

    OP_6F(0x0002, 15)

    Jump('loc_317')

    def _loc_2FC(): pass

    label('loc_2FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_30D',
    )

    OP_6F(0x0002, 15)

    Jump('loc_317')

    def _loc_30D(): pass

    label('loc_30D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_317',
    )

    Jump('loc_317')

    def _loc_317(): pass

    label('loc_317')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_32A',
    )

    OP_65(0x00, 0x0001)

    def _loc_32A(): pass

    label('loc_32A')

    Return()

# id: 0x0002 offset: 0x32B
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
        'loc_350',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_492')

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_369',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_492')

    def _loc_369(): pass

    label('loc_369')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_382',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_492')

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39B',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_492')

    def _loc_39B(): pass

    label('loc_39B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B4',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_492')

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CD',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_492')

    def _loc_3CD(): pass

    label('loc_3CD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E6',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_492')

    def _loc_3E6(): pass

    label('loc_3E6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FF',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_492')

    def _loc_3FF(): pass

    label('loc_3FF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_418',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_492')

    def _loc_418(): pass

    label('loc_418')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_431',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_492')

    def _loc_431(): pass

    label('loc_431')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44A',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_492')

    def _loc_44A(): pass

    label('loc_44A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_463',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_492')

    def _loc_463(): pass

    label('loc_463')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47C',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_492')

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_492',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_492(): pass

    label('loc_492')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_492')

    def _loc_4A7(): pass

    label('loc_4A7')

    Return()

# id: 0x0003 offset: 0x4A8
@scena.Code('func_03_4A8')
def func_03_4A8():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_4FA',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，鲁克回来得真晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候还这样，\n',
            '小孩子真是不懂事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B9C')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_616',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5BD',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上，火炉点不着了，\n',
            '不过以为只是故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去了梅尔达斯工房后，\n',
            '发现现在到处都是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这大概是\n',
            '遭到女神的报应了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是在斥责我们\n',
            '不应该太过于享乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_613')

    def _loc_5BD(): pass

    label('loc_5BD')

    ChrTalk(
        0x00FE,
        (
            '导力器的事，\n',
            '大概是遭到女神的报应了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是在斥责我们\n',
            '不应该太过于享乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_613(): pass

    label('loc_613')

    Jump('loc_B9C')

    def _loc_616(): pass

    label('loc_616')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_81C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_662',
    )

    ChrTalk(
        0x00FE,
        (
            '那料理的事\n',
            '不太清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，请去问别人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_819')

    def _loc_662(): pass

    label('loc_662')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_68D',
    )

    Call(1, 0x0000)

    Jump('loc_819')

    def _loc_68D(): pass

    label('loc_68D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_73B',
    )

    ChrTalk(
        0x00FE,
        (
            '我家的鲁克啊，\n',
            '终于醒来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下又能看着他\n',
            '和阿斯顿一起练剑了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样看来\n',
            '小孩的教育怎么样还真是次要的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之只要那孩子健康\n',
            '就是我的幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_819')

    def _loc_73B(): pass

    label('loc_73B')

    ChrTalk(
        0x00FE,
        (
            '哎呀，是游击士们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的鲁克\n',
            '终于醒来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经完全恢复了呢。\n',
            '现在已经出去玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，也不想想\n',
            '自己多让人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过也算了……\n',
            '今天就不唠叨他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那孩子醒来了。\n',
            '现在这样就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_819(): pass

    label('loc_819')

    Jump('loc_B9C')

    def _loc_81C(): pass

    label('loc_81C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_946',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_89E',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，他爸爸阿斯顿\n',
            '也回了一趟家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看了看鲁克的情况\n',
            '又回去警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就不能找别人\n',
            '暂代一下任务吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_943')

    def _loc_89E(): pass

    label('loc_89E')

    ChrTalk(
        0x00FE,
        (
            '刚才，他爸爸阿斯顿\n',
            '也回了一趟家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看了看鲁克的情况\n',
            '又回去警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我知道公事很重要，\n',
            '但他还是有点逞强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿斯顿他呀……\n',
            '其实应该非常担心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_943(): pass

    label('loc_943')

    Jump('loc_B9C')

    def _loc_946(): pass

    label('loc_946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_A43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_9A5',
    )

    ChrTalk(
        0x00FE,
        (
            '帕特也来了。\n',
            '已经可以出去玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是平时的你，\n',
            '应该早就跳起来了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A40')

    def _loc_9A5(): pass

    label('loc_9A5')

    SetChrName('玛茜婆婆')

    ChrTalk(
        0x00FE,
        (
            '鲁克啊……\n',
            '已经到早上了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，起来啦。\n',
            '今天雾也很大哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帕特也来了……\n',
            '随时都可以出去玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂，鲁克……\n',
            '早点起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_A40(): pass

    label('loc_A40')

    Jump('loc_B9C')

    def _loc_A43(): pass

    label('loc_A43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_B53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AB9',
    )

    ChrTalk(
        0x00FE,
        (
            '鲁克那淘气的样子\n',
            '到底像谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个样子，教他剑的\n',
            '阿斯顿也够辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定相当\n',
            '棘手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B50')

    def _loc_AB9(): pass

    label('loc_AB9')

    ChrTalk(
        0x00FE,
        (
            '鲁克那淘气的样子\n',
            '到底像谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早饭也不吃\n',
            '就飞奔出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易开始学剑，\n',
            '却一点都没长进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他爸爸阿斯顿以前\n',
            '可是很安分的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_B50(): pass

    label('loc_B50')

    Jump('loc_B9C')

    def _loc_B53(): pass

    label('loc_B53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_B9C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，鲁克\n',
            '去哪里了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '马上就要吃午饭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B9C(): pass

    label('loc_B9C')

    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0xBA0
@scena.Code('func_04_BA0')
def func_04_BA0():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_D33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 3, 0x1033)),
            Expr.Return,
        ),
        'loc_C05',
    )

    ChrTalk(
        0x00FE,
        (
            '据说，从现在起王国军\n',
            '就要进行大规模的组织改革了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也快要忙起来喽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D33')

    def _loc_C05(): pass

    label('loc_C05')

    ChrTalk(
        0x00FE,
        (
            '啊，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '何时回到洛连特的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F刚刚才到的，阿斯顿先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，你回来了\n',
            '我家鲁克一定会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鲁克最近，总是\n',
            '缠着我要学剑术呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还以为突然怎么了呢，\n',
            '问他理由也不说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能因为我常常不在家，\n',
            '怎么和儿子交流还真是伤脑筋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，真难为情了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1033)

    def _loc_D33(): pass

    label('loc_D33')

    TalkEnd(0x000E)

    Return()

# id: 0x0005 offset: 0xD37
@scena.Code('func_05_D37')
def func_05_D37():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_E36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_D8F',
    )

    ChrTalk(
        0x000B,
        (
            '吃完晚饭\n',
            '我再去找鲁克。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果我去了，鲁克一定\n',
            '也会想出去玩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E33')

    def _loc_D8F(): pass

    label('loc_D8F')

    ChrTalk(
        0x000B,
        (
            '我本来是\n',
            '和鲁克在一起的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是被妈妈\n',
            '硬拖回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，吃完晚饭\n',
            '我会再去看他的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果我在，鲁克一定\n',
            '也会想出去玩的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '顺利的话，\n',
            '说不定会醒过来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_E33(): pass

    label('loc_E33')

    Jump('loc_F35')

    def _loc_E36(): pass

    label('loc_E36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_F35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_E84',
    )

    ChrTalk(
        0x000B,
        (
            '鲁克虽然没醒来，\n',
            '但表情好像挺开心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一定在做美梦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F35')

    def _loc_E84(): pass

    label('loc_E84')

    ChrTalk(
        0x000B,
        (
            '啊，艾丝蒂尔姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '到了早上\n',
            '鲁克还没起来啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '玛茜婆婆的声音\n',
            '好象也听不到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……不过啊，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '鲁克的睡脸……\n',
            '看起来好像很开心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为鲁克他，\n',
            '一定在做美梦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_F35(): pass

    label('loc_F35')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0xF39
@scena.Code('func_06_F39')
def func_06_F39():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_FD2',
    )

    ChrTalk(
        0x00FE,
        (
            '我妻子赛拉和儿子帕特\n',
            '现在正打算去参加婚礼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这时候举行婚礼\n',
            '真是不合时宜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，正因为这样\n',
            '更要祝福他们\n',
            '新婚生活幸福呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17DD')

    def _loc_FD2(): pass

    label('loc_FD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_10E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_109F',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，导力器居然停了，\n',
            '真令人吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正读着喜欢的书，\n',
            '突然就变得漆黑一片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以为是故障去了工房，\n',
            '结果说原因不明……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再加上那个出现在空中的岛，\n',
            '总有点不吉利的预感啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_10E4')

    def _loc_109F(): pass

    label('loc_109F')

    ChrTalk(
        0x00FE,
        (
            '导力器不能用的原因\n',
            '好像还不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总有点不吉利的预感啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10E4(): pass

    label('loc_10E4')

    Jump('loc_17DD')

    def _loc_10E7(): pass

    label('loc_10E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1304',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0800)"),
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1187',
    )

    ChrTalk(
        0x00FE,
        (
            '看来食谱\n',
            '已经找到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '传统料理能够复活，\n',
            '我个人也是非常期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以的话真想加进\n',
            '亚班特酒馆的例牌菜单啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1301')

    def _loc_1187(): pass

    label('loc_1187')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0400)"),
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11E7',
    )

    ChrTalk(
        0x00FE,
        (
            '食谱册应该\n',
            '放在哪个书架上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思\n',
            '你们自己找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1301')

    def _loc_11E7(): pass

    label('loc_11E7')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1212',
    )

    Call(1, 0x0001)

    Jump('loc_1301')

    def _loc_1212(): pass

    label('loc_1212')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1262',
    )

    ChrTalk(
        0x00FE,
        (
            '帕特和鲁克一起\n',
            '飞奔出去了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，鲁克\n',
            '醒来了就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1301')

    def _loc_1262(): pass

    label('loc_1262')

    ChrTalk(
        0x00FE,
        (
            '帕特和鲁克一起\n',
            '飞奔出去了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，鲁克\n',
            '醒来了就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，雾散天晴的同时\n',
            '那孩子就醒了过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这几天的事情\n',
            '真是难以理解啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1301(): pass

    label('loc_1301')

    Jump('loc_17DD')

    def _loc_1304(): pass

    label('loc_1304')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1449',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_136B',
    )

    ChrTalk(
        0x00FE,
        (
            '在雾中行走之时，\n',
            '骑士也忘记了使命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看到现在的洛连特，\n',
            '真让人想起这传说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1446')

    def _loc_136B(): pass

    label('loc_136B')

    ChrTalk(
        0x00FE,
        (
            '前来警备的士兵们，\n',
            '对这雾也很困惑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如此浓雾……\n',
            '简直像是中世纪文学中\n',
            '所描绘的神秘森林一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在雾中前进之时，\n',
            '勇敢的骑士们也迷失了方向，\n',
            '最后连使命也忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看到现在的洛连特，\n',
            '真让人想起这传说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1446(): pass

    label('loc_1446')

    Jump('loc_17DD')

    def _loc_1449(): pass

    label('loc_1449')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_154F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_14B7',
    )

    ChrTalk(
        0x00FE,
        (
            '今天是互不侵犯条约的签字议式吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该是值得纪念的一天，\n',
            '但却总是没有祝贺的心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154C')

    def _loc_14B7(): pass

    label('loc_14B7')

    ChrTalk(
        0x00FE,
        (
            '今天是互不侵犯条约的签字议式吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明是值得纪念的一天，\n',
            '城市被不吉利的雾所覆盖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再加上鲁克他们的事，\n',
            '怎么也没有了祝贺的心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_154C(): pass

    label('loc_154C')

    Jump('loc_17DD')

    def _loc_154F(): pass

    label('loc_154F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_16D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_15B0',
    )

    ChrTalk(
        0x00FE,
        (
            '以前这一带\n',
            '也常有旅行艺人来表演。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近是没见过了，\n',
            '还真想再去看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16D5')

    def _loc_15B0(): pass

    label('loc_15B0')

    ChrTalk(
        0x00FE,
        (
            '哎呀～今天的雾可真厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '湿气会伤书本，\n',
            '因此急急忙忙开始整理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果偶然发现了\n',
            '令人怀念的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……居然是１０年以前看\n',
            '旅行艺人表演的票呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为跟妻子的首次约会纪念\n',
            '被夹在书里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，回想起来。\n',
            '那时候的赛拉可真漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，不过……\n',
            '当然现在也很漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_16D5(): pass

    label('loc_16D5')

    Jump('loc_17DD')

    def _loc_16D8(): pass

    label('loc_16D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_17DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_174C',
    )

    ChrTalk(
        0x00FE,
        (
            '政变的时候\n',
            '遭到他国侵略，\n',
            '这在历史上也经常发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '担心帝国会不会攻过来，\n',
            '总是心惊胆战的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17DD')

    def _loc_174C(): pass

    label('loc_174C')

    ChrTalk(
        0x00FE,
        (
            '理查德上校的政变\n',
            '是相当严重的事件吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政变的时候\n',
            '遭到他国侵略，\n',
            '这在历史上也经常发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是担心帝国会不会攻过\n',
            '来，心惊胆战的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_17DD(): pass

    label('loc_17DD')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x17E1
@scena.Code('func_07_17E1')
def func_07_17E1():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_18E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_185B',
    )

    ChrTalk(
        0x00FE,
        (
            '看到帕特他们就在想，\n',
            '是不是我也该和老公一起出去转转呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，像以前那样\n',
            '约会一下也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18DF')

    def _loc_185B(): pass

    label('loc_185B')

    ChrTalk(
        0x00FE,
        (
            '鲁克也醒了过来，\n',
            '总算能放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得雾散了天也晴了，\n',
            '是不是去约约老公看看呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，像以前那样\n',
            '约会一下也不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_18DF(): pass

    label('loc_18DF')

    Jump('loc_1CEC')

    def _loc_18E2(): pass

    label('loc_18E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1996',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然不大好……\n',
            '还是把帕特带回家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这个事件的原因\n',
            '还不清楚吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是什么病\n',
            '连这孩子都会遭到牵连。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然对不住玛茜婆婆，\n',
            '但保护孩子是父母的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CEC')

    def _loc_1996(): pass

    label('loc_1996')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1A7F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_19ED',
    )

    ChrTalk(
        0x00FE,
        (
            '帕特一起床\n',
            '就去看鲁克了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不希望这孩子\n',
            '再遭遇到那种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A7C')

    def _loc_19ED(): pass

    label('loc_19ED')

    ChrTalk(
        0x00FE,
        (
            '帕特一起床\n',
            '就去看鲁克了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然明白他的担心，\n',
            '但也不能连早饭也不吃啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真怕连那孩子\n',
            '也会倒下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望别变成\n',
            '鲁克那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1A7C(): pass

    label('loc_1A7C')

    Jump('loc_1CEC')

    def _loc_1A7F(): pass

    label('loc_1A7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1BEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0217, 2, 0x10BA)),
            Expr.Return,
        ),
        'loc_1B11',
    )

    ChrTalk(
        0x00FE,
        (
            '我老公真是的，\n',
            '又在翻看旧书了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且从刚才开始\n',
            '就一直看着那些旧纸片傻笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……是不是湿气太重\n',
            '连脑袋里都发霉了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BE9')

    def _loc_1B11(): pass

    label('loc_1B11')

    ChrTalk(
        0x00FE,
        (
            '我老公真是的，\n',
            '又在翻看旧书了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一时冲动买下的书\n',
            '还真是存了不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正要扔掉，\n',
            '送人还不至于浪费。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，给。\n',
            '这个给你。',
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
            (TxtCtl.Item, ItemTable['牌技师杰克 ６卷']),
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
    AddItem(ItemTable['牌技师杰克 ６卷'], 1)
    OP_A2(0x10BA)

    def _loc_1BE9(): pass

    label('loc_1BE9')

    Jump('loc_1CEC')

    def _loc_1BEC(): pass

    label('loc_1BEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_1CEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C6E',
    )

    ChrTalk(
        0x00FE,
        (
            '那孩子和鲁克\n',
            '一起玩挺让人担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但和我老公在一起\n',
            '也不大放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要能再找个\n',
            '出色点的人看着就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CEC')

    def _loc_1C6E(): pass

    label('loc_1C6E')

    ChrTalk(
        0x00FE,
        (
            '最近，帕特经常和老公\n',
            '一起看书呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '书是精神食粮，\n',
            '对那孩子也是好事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是担心会不会\n',
            '受些什么奇怪的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1CEC(): pass

    label('loc_1CEC')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0x1CF0
@scena.Code('func_08_1CF0')
def func_08_1CF0():
    TalkBegin(0x0008)
    TalkEnd(0x0008)

    Return()

# id: 0x0009 offset: 0x1CF7
@scena.Code('func_09_1CF7')
def func_09_1CF7():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_4A(0x0009, 255)
    OP_6F(0x0002, 15)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0002)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0009, 55200, 100, 159950, 180)
    SetChrPos(0x000A, 55120, 0, 161430, 180)
    SetChrPos(0x000B, 56170, 0, 161420, 180)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrChipByIndex(0x0009, 6)
    SetChrSubChip(0x0009, 4)
    OP_6D(51920, 350, 164390, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_1DBC')
    def lambda_1DBC():
        OP_6D(54630, 350, 161690, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1DBC)

    FadeIn(1000, 0)
    Sleep(2500)

    SetChrSubChip(0x0009, 5)
    Sleep(200)

    OP_4A(0x000B, 255)
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_8C(0x000E, 90, 400)
    CreateThread(0x000B, 0x01, 0x00, 0x000A)
    Sleep(300)

    @scena.Lambda('lambda_1E36')
    def lambda_1E36():
        OP_8E(0x00FE, 50680, 0, 159610, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_1E36)

    WaitForThreadExit(0x000E, 0x0000)

    @scena.Lambda('lambda_1E56')
    def lambda_1E56():
        OP_8E(0x00FE, 53410, 0, 159810, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_1E56)

    WaitForThreadExit(0x000E, 0x0000)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0131._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x1E9B
@scena.Code('func_0A_1E9B')
def func_0A_1E9B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1EC3',
    )

    OP_95(0x000B, 0x00000000, 0x00000000, 0x00000000, 0x00000320, 0x00002EE0)
    Sleep(400)

    Jump('func_0A_1E9B')

    def _loc_1EC3(): pass

    label('loc_1EC3')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
