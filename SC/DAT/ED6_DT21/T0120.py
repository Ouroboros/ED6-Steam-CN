import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0120   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '佛莱迪'),
    TXT(0x02, '梅尔达斯'),
    TXT(0x03, '埃尔格'),
    TXT(0x04, '斯蒂娜'),
    TXT(0x05, '提克'),
    TXT(0x06, '莫莉'),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0120.x'
    header.mapIndex       = 4
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T0120._SN', 'ED6_DT21/T0120_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6313
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
    ]

# id: 0x10002 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -38180,
            z                   = 0,
            y                   = -497,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -39499,
            z                   = 0,
            y                   = 678,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -36678,
            z                   = 0,
            y                   = 73751,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -86132,
            z                   = 0,
            y                   = 71210,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -45100,
            z                   = 0,
            y                   = 1430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -44360,
            z                   = 0,
            y                   = -390,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10003 offset: 0x192
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x192
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x192
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -38537,
            triggerZ            = 0,
            triggerY            = -1845,
            triggerRange        = 400,
            actorX              = -38180,
            actorZ              = 1500,
            actorY              = -497,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -41599,
            triggerZ            = 0,
            triggerY            = 299,
            triggerRange        = 1000,
            actorX              = -39499,
            actorZ              = 1500,
            actorY              = 678,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -36170,
            triggerZ            = 0,
            triggerY            = 71651,
            triggerRange        = 1000,
            actorX              = -36678,
            actorZ              = 1500,
            actorY              = 73751,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1FE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_20D',
    )

    SetChrFlags(0x0009, 0x0080)

    Jump('loc_241')

    def _loc_20D(): pass

    label('loc_20D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_217',
    )

    Jump('loc_241')

    def _loc_217(): pass

    label('loc_217')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_22B',
    )

    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_241')

    def _loc_22B(): pass

    label('loc_22B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_23A',
    )

    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_241')

    def _loc_23A(): pass

    label('loc_23A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_241',
    )

    def _loc_241(): pass

    label('loc_241')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_267',
    )

    SetChrFlags(0x0008, 0x0080)
    OP_64(0x01, 0x0001)
    SetChrPos(0x0009, -38180, 0, -497, 180)

    def _loc_267(): pass

    label('loc_267')

    Return()

# id: 0x0001 offset: 0x268
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_279',
    )

    OP_71(0x0001, 0x0004)

    def _loc_279(): pass

    label('loc_279')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_289',
    )

    OP_64(0x01, 0x0001)

    def _loc_289(): pass

    label('loc_289')

    Return()

# id: 0x0002 offset: 0x28A
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29D',
    )

    Call(0, 0x0006)

    Jump('loc_2A1')

    def _loc_29D(): pass

    label('loc_29D')

    Call(0, 0x0005)

    def _loc_2A1(): pass

    label('loc_2A1')

    Return()

# id: 0x0003 offset: 0x2A2
@scena.Code('func_03_2A2')
def func_03_2A2():
    Call(0, 0x0006)

    Return()

# id: 0x0004 offset: 0x2A7
@scena.Code('func_04_2A7')
def func_04_2A7():
    Call(0, 0x0007)

    Return()

# id: 0x0005 offset: 0x2AC
@scena.Code('func_05_2AC')
def func_05_2AC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 2, 0x188A)),
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 2, 0x209A)),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_305',
    )

    Call(6, 0x0003)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F4',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_2EE',
    )

    OP_A9(0x07)

    Jump('loc_2F0')

    def _loc_2EE(): pass

    label('loc_2EE')

    OP_A9(0x00)

    def _loc_2F0(): pass

    label('loc_2F0')

    TalkEnd(0x0008)

    Return()

    def _loc_2F4(): pass

    label('loc_2F4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_305',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_305(): pass

    label('loc_305')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_10FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 2, 0x209A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F03',
    )

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -38800, 0, -2650, 0)
    SetChrPos(0x0102, -38000, 0, -2850, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36F',
    )

    SetChrPos(0x00F9, -38400, 0, -3850, 0)
    SetChrPos(0x00F8, -37500, 0, -4050, 0)

    Jump('loc_391')

    def _loc_36F(): pass

    label('loc_36F')

    SetChrPos(0x00F8, -38400, 0, -3850, 0)
    SetChrPos(0x00F9, -37500, 0, -4050, 0)

    def _loc_391(): pass

    label('loc_391')

    OP_8C(0x0008, 180, 0)
    OP_6D(-37570, 0, -1360, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀，艾丝蒂尔和约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '……咦，这不是约修亚吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F#2P您好，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F#3P我把他带来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哎呀～好久不见呢。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们两人在一起，\n',
            '感觉好久没见过了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F#3P啊哈哈，确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F#2P佛莱迪先生\n',
            '一点都没变呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，我倒没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不巧店里\n',
            '有点困难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔你们也很辛苦，\n',
            '可惜帮不上什么忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_59F',
    )

    ChrTalk(
        0x0101,
        (
            '#1018F#3P啊，这个请放心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们带了好东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咦？怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A12')

    def _loc_59F(): pass

    label('loc_59F')

    ChrTalk(
        0x0101,
        (
            '#1007F#3P是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '维修导力器的\n',
            '工具也不能动啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯……不过真伤脑筋啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结晶回路的合成和结晶孔的强化\n',
            '都完全不能进行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_66D',
    )

    ChrTalk(
        0x0103,
        (
            '#025F嗯嗯，难得有了这的发生器，\n',
            '真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_708')

    def _loc_66D(): pass

    label('loc_66D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6B0',
    )

    ChrTalk(
        0x0108,
        (
            '#072F唔，难得有了这的发生器，\n',
            '真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_708')

    def _loc_6B0(): pass

    label('loc_6B0')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_708',
    )

    ChrTalk(
        0x0106,
        (
            '#552F啊啊，难得有了这的发生器，\n',
            '恢复导力魔法了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这真是太可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_708(): pass

    label('loc_708')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_75D',
    )

    ChrTalk(
        0x0107,
        (
            '#064F啊，不过姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果只是一小会儿，\n',
            '那我或许有点办法喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7AB')

    def _loc_75D(): pass

    label('loc_75D')

    ChrTalk(
        0x0102,
        (
            '#1043F#2P话是没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1040F不过，如果只是一小会儿\n',
            '那我或许有点办法喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7AB(): pass

    label('loc_7AB')

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_828',
    )

    @scena.Lambda('lambda_07DB')
    def lambda_07DB():
        ChrTurnDirection(0x0000, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_07DB)

    Sleep(120)

    @scena.Lambda('lambda_07EE')
    def lambda_07EE():
        ChrTurnDirection(0x0001, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_07EE)

    @scena.Lambda('lambda_07FC')
    def lambda_07FC():
        ChrTurnDirection(0x0002, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_07FC)

    Sleep(120)

    @scena.Lambda('lambda_080F')
    def lambda_080F():
        ChrTurnDirection(0x0003, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_080F)

    @scena.Lambda('lambda_081D')
    def lambda_081D():
        ChrTurnDirection(0x0008, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_081D)

    Jump('loc_82F')

    def _loc_828(): pass

    label('loc_828')

    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_82F(): pass

    label('loc_82F')

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#1004F#3P咦……！？',
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
        'loc_88C',
    )

    ChrTalk(
        0x0106,
        (
            '#052F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E7')

    def _loc_88C(): pass

    label('loc_88C')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BA',
    )

    ChrTalk(
        0x0103,
        (
            '#023F能让工房运作起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E7')

    def _loc_8BA(): pass

    label('loc_8BA')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8E7',
    )

    ChrTalk(
        0x0108,
        (
            '#073F能让工房运作起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E7(): pass

    label('loc_8E7')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_92B',
    )

    ChrTalk(
        0x0107,
        (
            '#062F是、是啊，大概……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '用那个发生器的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_973')

    def _loc_92B(): pass

    label('loc_92B')

    ChrTalk(
        0x0102,
        (
            '#1040F#2P是，可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果使用那个发生器，\n',
            '应该能在短时间内复原。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_973(): pass

    label('loc_973')

    ChrTalk(
        0x0101,
        (
            '#1018F#3P啊，原来如此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那～约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就是说，什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09C2')
    def lambda_09C2():
        ChrTurnDirection(0x0000, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_09C2)

    Sleep(120)

    @scena.Lambda('lambda_09D5')
    def lambda_09D5():
        ChrTurnDirection(0x0001, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_09D5)

    @scena.Lambda('lambda_09E3')
    def lambda_09E3():
        ChrTurnDirection(0x0002, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_09E3)

    Sleep(120)

    @scena.Lambda('lambda_09F6')
    def lambda_09F6():
        ChrTurnDirection(0x0003, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_09F6)

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    def _loc_A12(): pass

    label('loc_A12')

    ChrTalk(
        0x0102,
        (
            '#1040F#2P嗯、其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了使用『零力场发生器』\n',
            '可暂时恢复工房机能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '啊～～～很厉害的装置啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，我没有异议。\n',
            '马上试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#3P谢谢，佛莱迪先生。',
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
        'loc_B13',
    )

    ChrTalk(
        0x0107,
        (
            '#560F那么～\n',
            '请稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3F')

    def _loc_B13(): pass

    label('loc_B13')

    ChrTalk(
        0x0102,
        (
            '#1040F#2P那么，就稍微\n',
            '借用一下机械了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B3F(): pass

    label('loc_B3F')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_22(0x009D, 0x00, 0x64)
    OP_8C(0x0008, 90, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用『零力场发生器』将工房机能恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '真的啊……\n',
            '机械真的开动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C06',
    )

    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '好，趁着机械开动时\n',
            '赶快办事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    Jump('loc_D23')

    def _loc_C06(): pass

    label('loc_C06')

    ChrTalk(
        0x0101,
        (
            '#1000F#3P太好了……看来成功了呢。',
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
        'loc_C7F',
    )

    ChrTalk(
        0x0107,
        (
            '#063F嗯，不过这\n',
            '只是暂时能动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#561F马上又会恢复原状的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD1')

    def _loc_C7F(): pass

    label('loc_C7F')

    ChrTalk(
        0x0102,
        (
            '#1040F#2P嗯，虽然运作得很好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但并不是真的修好了。\n',
            '过一段时间又会停止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD1(): pass

    label('loc_CD1')

    ChrTurnDirection(0x0008, 0x0000, 400)

    ChrTalk(
        0x0008,
        (
            '原来如此，从原理看来\n',
            '确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好，趁机械开动时\n',
            '赶快办事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    def _loc_D23(): pass

    label('loc_D23')

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x07)
    OP_56(0x00)
    OP_0D()
    Sleep(30)

    ChrTalk(
        0x0008,
        (
            '想使用工房的时候，\n',
            '就拿那个装置来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '随时乐意\n',
            '帮你们调整。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DE5',
    )

    ChrTalk(
        0x0103,
        (
            '#020F协会也正为查明原因\n',
            '竭尽全力哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说可能会花一些时间，\n',
            '但请努力坚持一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3E')

    def _loc_DE5(): pass

    label('loc_DE5')

    ChrTalk(
        0x0102,
        (
            '#1040F#2P协会也正为查明原因\n',
            '竭尽全力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说可能会花一些时间，\n',
            '但请努力坚持一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E3E(): pass

    label('loc_E3E')

    ChrTalk(
        0x0008,
        (
            '啊啊，能做的事\n',
            '我会尽量做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那，艾丝蒂尔你们\n',
            '工作也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这种时候能依靠的\n',
            '还是只有游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#3P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F#2P我们会不负众望，\n',
            '尽一切努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)
    OP_A2(0x188A)
    OP_A2(0x209A)
    OP_A2(0x20E6)
    EventEnd(0x00)

    Jump('loc_10F9')

    def _loc_F03(): pass

    label('loc_F03')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1082',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_F5D',
    )

    ChrTalk(
        0x0008,
        (
            '想使用工房的时候，\n',
            '就拿那个装置来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '随时乐意\n',
            '帮你们调整。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0006)

    Jump('loc_107F')

    def _loc_F5D(): pass

    label('loc_F5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1021',
    )

    ChrTalk(
        0x0008,
        (
            '老爸应潘杜爷爷的请求\n',
            '去观察钟楼的情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看他还没回来，\n',
            '应该还在眺望浮游岛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好像相当在意那个东西，\n',
            '还画了草图呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是的，多大年纪了，\n',
            '好奇心还跟孩子一样强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_107F')

    def _loc_1021(): pass

    label('loc_1021')

    ChrTalk(
        0x0008,
        (
            '老爸应潘杜爷爷的请求\n',
            '去观察钟楼的情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看他还没回来，\n',
            '应该还在眺望那个浮游岛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_107F(): pass

    label('loc_107F')

    Jump('loc_10F9')

    def _loc_1082(): pass

    label('loc_1082')

    ChrTalk(
        0x0008,
        (
            '想使用工房的时候\n',
            '就拿那个装置来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '随时乐意\n',
            '帮你们调整。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，真希望中央工房\n',
            '赶快将那个发生器量产化啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_10F9(): pass

    label('loc_10F9')

    Jump('loc_1B1A')

    def _loc_10FC(): pass

    label('loc_10FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_135F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 1, 0x1A59)),
            Expr.Return,
        ),
        'loc_1173',
    )

    ChrTalk(
        0x0008,
        (
            '虽说好像发生了不少事件，\n',
            '但不管怎样雾散天晴就好多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '洛连特也好久没来了，\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_135C')

    def _loc_1173(): pass

    label('loc_1173')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀，艾丝蒂尔和雪拉扎德。\n',
            '这次真是辛苦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽说好像发生了不少事件，\n',
            '但不管怎样雾散天晴就好多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '去做下一件工作之前\n',
            '好好休息一下如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F啊，嗯！\n',
            '我们也正是这个打算。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F那么，这就\n',
            '陪我喝一杯如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咳、咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '这、这个任务就交给\n',
            '亚班特的福克纳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '遗，遗憾的是我\n',
            '还有工作要做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '总、总而言之，暂时\n',
            '放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好久没回\n',
            '洛连特了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    OP_A2(0x1A59)

    def _loc_135C(): pass

    label('loc_135C')

    Jump('loc_1B1A')

    def _loc_135F(): pass

    label('loc_135F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_15A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_13F1',
    )

    ChrTalk(
        0x0008,
        (
            '王国军刚刚才到达。\n',
            '已经开始警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '没想到为了这样的雾\n',
            '连王国军都出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是不是出了什么事，\n',
            '刚才还和老爸说起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_159F')

    def _loc_13F1(): pass

    label('loc_13F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 2, 0x188A)),
            Expr.Return,
        ),
        'loc_1426',
    )

    ChrTalk(
        0x0008,
        (
            '王国军刚刚才到达。\n',
            '就已经开始警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_150F')

    def _loc_1426(): pass

    label('loc_1426')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀，艾丝蒂尔和雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好久不见呢。\n',
            '完成一项工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F啊……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F有点急事呢。\n',
            '刚刚才回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……对了，王国军\n',
            '好象已经开始城里的警备了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊啊，刚刚才到达的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188A)

    def _loc_150F(): pass

    label('loc_150F')

    ChrTalk(
        0x0008,
        (
            '队长是阿斯顿先生，\n',
            '倒是令人比较安心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过严重到要出动军队，\n',
            '反而就觉得有些不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是不是出了什么事，\n',
            '刚才还和老爸说起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_159F(): pass

    label('loc_159F')

    Jump('loc_1B1A')

    def _loc_15A2(): pass

    label('loc_15A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1786',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_15FE',
    )

    ChrTalk(
        0x0008,
        (
            '今天早上也起了好大的雾哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哎呀哎呀，什么时候\n',
            '才能重现蓝天呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1783')

    def _loc_15FE(): pass

    label('loc_15FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 2, 0x188A)),
            Expr.Return,
        ),
        'loc_1631',
    )

    ChrTalk(
        0x0008,
        (
            '呀，早上好。\n',
            '今天的雾还是那么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1732')

    def _loc_1631(): pass

    label('loc_1631')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀，艾丝蒂尔和雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好久不见呢。\n',
            '你们看起来很精神，这就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，佛莱迪先生也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，看起来很精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊啊，托你们的福\n',
            '工作也很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '话虽如此……\n',
            '今天早上也起了好大的雾哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188A)

    def _loc_1732(): pass

    label('loc_1732')

    ChrTalk(
        0x0008,
        (
            '搞不好这雾\n',
            '比昨天更浓了不是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哎呀哎呀，什么时候\n',
            '才能重现蓝天呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_1783(): pass

    label('loc_1783')

    Jump('loc_1B1A')

    def _loc_1786(): pass

    label('loc_1786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1B1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 2, 0x188A)),
            Expr.Return,
        ),
        'loc_186F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1814',
    )

    ChrTalk(
        0x0008,
        (
            '呀，欢迎。\n',
            '外边的雾还是那么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这么浓的雾，老爸\n',
            '好像也是头一次见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '工作时在外走动\n',
            '要特别注意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_186C')

    def _loc_1814(): pass

    label('loc_1814')

    ChrTalk(
        0x0008,
        (
            '需要调整导力器的时候\n',
            '随时来找我就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会用中央工房学来的技术\n',
            '完美调整好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_186C(): pass

    label('loc_186C')

    Jump('loc_1B1A')

    def _loc_186F(): pass

    label('loc_186F')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀，艾丝蒂尔和雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好久不见呢。\n',
            '你们看起来很精神，这就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0285, 2, 0x142A)),
            Expr.Return,
        ),
        'loc_194F',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，佛莱迪先生也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '蔡斯的研修，\n',
            '看来圆满结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F呵呵，很想赶快\n',
            '展示一下成果吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AC2')

    def _loc_194F(): pass

    label('loc_194F')

    ChrTalk(
        0x0101,
        (
            '#1000F你好，佛莱迪先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F你看来也\n',
            '很精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '啊啊，去了趟蔡斯，\n',
            '仔细学习了新型导力器的构造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以现在可以好好的\n',
            '回来努力工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F咦，佛莱迪先生\n',
            '也去了蔡斯！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F哎呀……刚好错过\n',
            '没能遇见真是遗憾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '应该去了不少次\n',
            '中央工房的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F不过，对于使用战术导力器\n',
            '的人来说可帮了大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '马上把研修成果\n',
            '向我们展示一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AC2(): pass

    label('loc_1AC2')

    ChrTalk(
        0x0008,
        (
            '啊啊，当然。\n',
            '随时来找我就是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会用中央工房学来的技术\n',
            '完美的调整好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188A)
    OP_A2(0x0005)

    def _loc_1B1A(): pass

    label('loc_1B1A')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x1B1E
@scena.Code('func_06_1B1E')
def func_06_1B1E():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1D35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 0, 0x1A58)),
            Expr.Return,
        ),
        'loc_1BA7',
    )

    ChrTalk(
        0x0009,
        (
            '游击士真是忙得\n',
            '不可开交啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，工作告一段落的时候\n',
            '再来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '到那时，\n',
            '可要把约修亚那小子也带来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D32')

    def _loc_1BA7(): pass

    label('loc_1BA7')

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '哟，是你们。\n',
            '这次也真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '莫非已经有了别的地区工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，有是有啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F不过在此之前打算\n',
            '先做做这边的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不帮一下支部的忙的话，\n',
            '恐怕爱娜要恨死我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '工作接连不断，也真是够忙的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，事情告一段落了\n',
            '再来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '对了对了，到那时\n',
            '可要把约修亚那小子也带来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F啊……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A58)

    def _loc_1D32(): pass

    label('loc_1D32')

    Jump('loc_25DE')

    def _loc_1D35(): pass

    label('loc_1D35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1EF7',
    )

    If(
        (
            (Expr.PushLong, 0x4),
            Expr.Return,
        ),
        'loc_1D98',
    )

    ChrTalk(
        0x0009,
        (
            '不过，没想到\n',
            '连王国军都出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过是点雾而已，\n',
            '为什么闹得这么大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EF4')

    def _loc_1D98(): pass

    label('loc_1D98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 1, 0x1889)),
            Expr.Return,
        ),
        'loc_1DCF',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔你们啊。\n',
            '看起来好像很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E9A')

    def _loc_1DCF(): pass

    label('loc_1DCF')

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '哦，艾丝蒂尔……\n',
            '还有雪拉扎德也一起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '为了这次的雾\n',
            '你们好像很忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1003F嗯……事情是不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 400)

    ChrTalk(
        0x0103,
        (
            '#020F您这儿没什么问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哦，完全没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1889)

    def _loc_1E9A(): pass

    label('loc_1E9A')

    ChrTalk(
        0x0009,
        (
            '不过，没想到\n',
            '连王国军都出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '再怎么说\n',
            '也不过是场雾嘛。\n',
            '是不是紧张过头了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1EF4(): pass

    label('loc_1EF4')

    Jump('loc_25DE')

    def _loc_1EF7(): pass

    label('loc_1EF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_213D',
    )

    If(
        (
            (Expr.PushLong, 0x4),
            Expr.Return,
        ),
        'loc_1F53',
    )

    ChrTalk(
        0x0009,
        (
            '外边的雾仍旧很大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我在这里住了这么久，\n',
            '这种事还是头一回呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213A')

    def _loc_1F53(): pass

    label('loc_1F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 1, 0x1889)),
            Expr.Return,
        ),
        'loc_1FB5',
    )

    ChrTalk(
        0x0009,
        (
            '哦，是你们啊。\n',
            '外边的雾仍旧很大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我在这里住了这么久，\n',
            '这种事还是头一回呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20ED')

    def _loc_1FB5(): pass

    label('loc_1FB5')

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '哦，艾丝蒂尔……\n',
            '还有雪拉扎德也在一起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们终于来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……\n',
            '抱歉哦，这么晚才来打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F您看来一点也没变呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 400)

    ChrTalk(
        0x0009,
        (
            '哦，当然啦。\n',
            '可不会输给年轻人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '话说回来，今早也仍旧\n',
            '是浓雾弥漫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我在这儿住了这么久\n',
            '这种事还是头一回呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1889)

    def _loc_20ED(): pass

    label('loc_20ED')

    ChrTalk(
        0x0009,
        (
            '你们在外走动\n',
            '也要注意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这么大的雾，走在街道上\n',
            '视野也很差吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_213A(): pass

    label('loc_213A')

    Jump('loc_25DE')

    def _loc_213D(): pass

    label('loc_213D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_23DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 1, 0x1889)),
            Expr.Return,
        ),
        'loc_2235',
    )

    If(
        (
            (Expr.PushLong, 0x4),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21E4',
    )

    ChrTalk(
        0x0009,
        (
            '哦，辛苦了。\n',
            '在这大雾下工作也很辛苦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '新型导力器的事\n',
            '就交给佛莱迪那家伙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '他可是特地跑去\n',
            '蔡斯研修过的嘛。\n',
            '尽量使唤他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2232')

    def _loc_21E4(): pass

    label('loc_21E4')

    ChrTalk(
        0x0009,
        (
            '去蔡斯研修的\n',
            '佛莱迪也回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '新型导力器的调整\n',
            '就尽管交给那家伙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2232(): pass

    label('loc_2232')

    Jump('loc_23D7')

    def _loc_2235(): pass

    label('loc_2235')

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '哦，艾丝蒂尔……\n',
            '还有雪拉扎德也在一起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好久不见了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿……\n',
            '梅尔达斯先生，看起来不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，一点也没变嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 400)

    ChrTalk(
        0x0009,
        (
            '哦，当然啦。\n',
            '可不会输给年轻人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 6, 0x102E)),
            Expr.Return,
        ),
        'loc_236A',
    )

    ChrTalk(
        0x0009,
        (
            '佛莱迪那家伙\n',
            '也从蔡斯回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '新型导力器的调整\n',
            '就通通都交给他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D1')

    def _loc_236A(): pass

    label('loc_236A')

    ChrTalk(
        0x0009,
        (
            '为了新型导力器的研修\n',
            '去了蔡斯的佛莱迪\n',
            '也终于回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果要调整或者开封\n',
            '就尽管交给那家伙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23D1(): pass

    label('loc_23D1')

    OP_A2(0x1889)
    OP_A2(0x0004)
    def _loc_23D7(): pass

    label('loc_23D7')

    Jump('loc_25DE')

    def _loc_23DA(): pass

    label('loc_23DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_25DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 6, 0x102E)),
            Expr.Return,
        ),
        'loc_2448',
    )

    ChrTalk(
        0x0009,
        (
            '佛莱迪那家伙\n',
            '去蔡斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '具体的不太清楚，\n',
            '不过他说要去中央工房\n',
            '研修战术导力器来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25DE')

    def _loc_2448(): pass

    label('loc_2448')

    ChrTalk(
        0x0009,
        (
            '哟，欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x0101, 400)
    Sleep(600)

    OP_63(0x0009)

    ChrTalk(
        0x0009,
        (
            '艾丝蒂尔……\n',
            '好久不见了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿……\n',
            '梅尔达斯先生，看起来不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '当然了。\n',
            '可不会输给年轻人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '对了，佛莱迪那家伙\n',
            '去蔡斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F蔡斯？为什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '其实我也不太清楚，\n',
            '不过他说要去中央工房\n',
            '研修战术导力器来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的，因此\n',
            '害我忙得快昏头了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '研修什么的管它那么多，\n',
            '赶快回来才是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x102E)

    def _loc_25DE(): pass

    label('loc_25DE')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x25E2
@scena.Code('func_07_25E2')
def func_07_25E2():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2870',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 7, 0x102F)),
            Expr.Return,
        ),
        'loc_2671',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2626',
    )

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔，代我向约修亚问好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_266E')

    def _loc_2626(): pass

    label('loc_2626')

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '…………不，没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_266E(): pass

    label('loc_266E')

    Jump('loc_286C')

    def _loc_2671(): pass

    label('loc_2671')

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '回来了吗！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F叔叔，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我听说你们的活跃表现了哦。\n',
            '当上正游击士了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的，你们可是\n',
            '一次又一次的让人吃惊呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '卡西乌斯似乎也平安无事，\n',
            '真是个命大的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……哎呀，说起来，\n',
            '约修亚怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F应该先回家了。\n',
            '我也打算这就回去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是……那样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '回来也不打个招呼，\n',
            '那个家伙还真是薄情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F约修亚没来过\n',
            '这里吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F那好，回家后\n',
            '我会让他来露个脸的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊，啊啊……拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1067F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x102F)
    def _loc_286C(): pass

    label('loc_286C')

    TalkEnd(0x000A)

    Return()

    def _loc_2870(): pass

    label('loc_2870')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 4, 0x188C)),
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 4, 0x209C)),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_28C6',
    )

    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28B5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_28AF',
    )

    OP_A9(0x08)

    Jump('loc_28B1')

    def _loc_28AF(): pass

    label('loc_28AF')

    OP_A9(0x01)

    def _loc_28B1(): pass

    label('loc_28B1')

    TalkEnd(0x000A)

    Return()

    def _loc_28B5(): pass

    label('loc_28B5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28C6',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_28C6(): pass

    label('loc_28C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2D20',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 4, 0x209C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A73',
    )

    ChrTurnDirection(0x000A, 0x0102, 400)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦，约修亚。\n',
            '总算回来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F埃尔格先生。\n',
            '我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯……\n',
            '现在壮多了喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看来好像积累了\n',
            '不少经验嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是，是成熟些了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1043F不过，同时也\n',
            '让大家担了不少心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，男人嘛，\n',
            '这点事没关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '约修亚，你可是\n',
            '这个城市引以为傲的人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '终于回来了………\n',
            '暂时休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '工作做完了之后，\n',
            '一定会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)
    OP_A2(0x209C)

    Jump('loc_2D1D')

    def _loc_2A73(): pass

    label('loc_2A73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2ACD',
    )

    ChrTalk(
        0x000A,
        (
            '碰到斯蒂娜了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还没有的话，\n',
            '去见见她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '她可比我\n',
            '还担心你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D1D')

    def _loc_2ACD(): pass

    label('loc_2ACD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_2C2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BA6',
    )

    ChrTalk(
        0x000A,
        (
            '哦，艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '定期船的停运倒是知道，\n',
            '但竟然连搬运车也不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '也就是说，流通路径\n',
            '完全停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽说洛连特附近有田地\n',
            '稍微还好一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那柏斯和王都\n',
            '今后会怎样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_2C27')

    def _loc_2BA6(): pass

    label('loc_2BA6')

    ChrTalk(
        0x000A,
        (
            '由于这次的事，流通路径\n',
            '好像都完全停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽说洛连特附近有田地\n',
            '稍微还好一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但柏斯和王都\n',
            '形势不知道有多严重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C27(): pass

    label('loc_2C27')

    Jump('loc_2D1D')

    def _loc_2C2A(): pass

    label('loc_2C2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CCD',
    )

    ChrTalk(
        0x000A,
        (
            '哦，是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，难得返乡…\n',
            '时机可不太好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在市内的导力器\n',
            '全都不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽说没有太大的混乱，\n',
            '但还是有点麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_2D1D')

    def _loc_2CCD(): pass

    label('loc_2CCD')

    ChrTalk(
        0x000A,
        (
            '现在市内的导力器\n',
            '全都不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '到底是什么原因，\n',
            '问了工房也不清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D1D(): pass

    label('loc_2D1D')

    Jump('loc_43DD')

    def _loc_2D20(): pass

    label('loc_2D20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_3168',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 2, 0x1A5A)),
            Expr.Return,
        ),
        'loc_2EEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E69',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2D96',
    )

    ChrTalk(
        0x000A,
        (
            '这次事件的事\n',
            '以后有机会再问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '到那时还有约修亚的事\n',
            '可都要老实交代清楚哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E66')

    def _loc_2D96(): pass

    label('loc_2D96')

    ChrTalk(
        0x000A,
        (
            '这次事件中你看来\n',
            '也是相当活跃嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '到底怎么解决的，\n',
            '真是令人感兴趣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '具体的以后有机会\n',
            '再说来听听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，到那时候可得\n',
            '把约修亚那小子也带来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我有些男人之间的话\n',
            '想和那家伙谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_2E66(): pass

    label('loc_2E66')

    Jump('loc_2EEC')

    def _loc_2E69(): pass

    label('loc_2E69')

    ChrTalk(
        0x000A,
        (
            '这次事件的冒险故事\n',
            '以后有机会再问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '下次来的时候，可一定\n',
            '要把约修亚也带来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我有些男人之间的话\n',
            '想和那家伙谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2EEC(): pass

    label('loc_2EEC')

    Jump('loc_3165')

    def _loc_2EEF(): pass

    label('loc_2EEF')

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '哟，艾丝蒂尔和雪拉扎德。\n',
            '今天天气真好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '睡着的人们\n',
            '似乎也都醒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……话说，这还是\n',
            '你们的功劳吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯、嗯……\n',
            '有点微妙啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F嗯，\n',
            '就算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我就知道\n',
            '你们一定能做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽说想好好问问\n',
            '到底是怎么解决的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过，你们现在这么忙。\n',
            '下面还有工作等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然可惜，冒险故事的发表\n',
            '还是等下次机会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F啊，啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F（不，不愧是埃尔格先生。\n',
            '  完全把我看穿了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，说实话真是帮了大忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，日后有机会再叙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊啊，到那时\n',
            '无论如何也要和约修亚一起来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我也会向女神祈祷的，\n',
            '希望早日收到那家伙的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x1A5A)
    OP_A2(0x0001)
    def _loc_3165(): pass

    label('loc_3165')

    Jump('loc_43DD')

    def _loc_3168(): pass

    label('loc_3168')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_36E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 5, 0x188D)),
            Expr.Return,
        ),
        'loc_3384',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3312',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3228',
    )

    ChrTalk(
        0x000A,
        (
            '王国军的部队好像\n',
            '已经加入城市警备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样的话你们游击士\n',
            '也能专心地好好调查了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '事情虽然很严重，\n',
            '不过我还是期待你们的表现。\n',
            '等你们的好消息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_330F')

    def _loc_3228(): pass

    label('loc_3228')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '哟，艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '刚才王国军的士兵\n',
            '过来打过招呼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '说是今天开始\n',
            '加入城中警备来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽说平时那么严肃、\n',
            '感觉很难以接近似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但这种时候有士兵在\n',
            '还是能够壮胆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哎呀，人真是\n',
            '势利的生物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_330F(): pass

    label('loc_330F')

    Jump('loc_3381')

    def _loc_3312(): pass

    label('loc_3312')

    ChrTalk(
        0x000A,
        (
            '事件的调查……\n',
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是，你们\n',
            '也不能鲁莽行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果游击士都倒下了，\n',
            '就什么希望也没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3381(): pass

    label('loc_3381')

    Jump('loc_36E6')

    def _loc_3384(): pass

    label('loc_3384')

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 4, 0x188C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3467',
    )

    ChrTalk(
        0x000A,
        (
            '哎呀，是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，还在想你们什么时候会来，\n',
            '昨天就开始做准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F哎呀呀……\n',
            '看来让您久等了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还是那么忙的样子嘛。\n',
            '真是的，一大早就那么辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188C)

    Jump('loc_3498')

    def _loc_3467(): pass

    label('loc_3467')

    ChrTalk(
        0x000A,
        (
            '哟，是艾丝蒂尔你们啊。\n',
            '早上开始就这么忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3498(): pass

    label('loc_3498')

    ChrTalk(
        0x000A,
        (
            '鲁克他们的情况似乎\n',
            '暂且也稳定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然希望他们早点醒来，\n',
            '但为这个干着急也无济于事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔你们\n',
            '也不能鲁莽行事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果你们都倒下了，\n',
            '那才是彻底没希望了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F没关系的，别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这孩子也是经验丰富、\n',
            '独当一面的游击士了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿，就算是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F不过，和雪拉姐\n',
            '还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，还有心给师姐面子，\n',
            '看来是不要紧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那么，调查要努力哦。\n',
            '期待你们的好消息。',
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
        'loc_3663',
    )

    ChrTalk(
        0x0106,
        (
            '#050F啊啊，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36E0')

    def _loc_3663(): pass

    label('loc_3663')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3691',
    )

    ChrTalk(
        0x0108,
        (
            '#070F啊啊，尽力而为了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36E0')

    def _loc_3691(): pass

    label('loc_3691')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36C3',
    )

    ChrTalk(
        0x0104,
        (
            '#030F呵，尽情期待我的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36E0')

    def _loc_36C3(): pass

    label('loc_36C3')

    ChrTalk(
        0x0103,
        (
            '#525F嗯嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36E0(): pass

    label('loc_36E0')

    OP_A2(0x188D)
    OP_A2(0x0001)
    def _loc_36E6(): pass

    label('loc_36E6')

    Jump('loc_43DD')

    def _loc_36E9(): pass

    label('loc_36E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_3CFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 5, 0x188D)),
            Expr.Return,
        ),
        'loc_3883',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3811',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3759',
    )

    ChrTalk(
        0x000A,
        (
            '虽然我也觉得那雾不寻常，\n',
            '但竟然发生这种事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们也要\n',
            '十分小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_380E')

    def _loc_3759(): pass

    label('loc_3759')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '哟，艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然我就觉得这雾不寻常，\n',
            '但竟然还发生了昏睡事件什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唉，到底是事件还是意外\n',
            '都不知道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的……\n',
            '真相真的全在雾中某处吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_380E(): pass

    label('loc_380E')

    Jump('loc_3880')

    def _loc_3811(): pass

    label('loc_3811')

    ChrTalk(
        0x000A,
        (
            '事件的调查……\n',
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是，你们\n',
            '也不能鲁莽行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果游击士都倒下了，\n',
            '就什么希望也没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3880(): pass

    label('loc_3880')

    Jump('loc_3CF7')

    def _loc_3883(): pass

    label('loc_3883')

    ChrTalk(
        0x0101,
        (
            '#1011F早上好，埃尔格先生。',
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
        'loc_38C4',
    )

    ChrTalk(
        0x0105,
        (
            '#040F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38C4(): pass

    label('loc_38C4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38E9',
    )

    ChrTalk(
        0x0107,
        (
            '#060F嗯，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38E9(): pass

    label('loc_38E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 4, 0x188C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39C8',
    )

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '哟，是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，还在想你们什么时候会来，\n',
            '昨天就开始做准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F啊哈哈……\n',
            '看来让您久等了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还是那么忙的样子嘛。\n',
            '今天也是一早就这么辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188C)

    Jump('loc_3A0B')

    def _loc_39C8(): pass

    label('loc_39C8')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '哟，是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天也是一早就这么辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A0B(): pass

    label('loc_3A0B')

    ChrTalk(
        0x0103,
        (
            '#025F嗯嗯，真的是……\n',
            '还想多睡会儿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F（不，不过，熬夜\n',
            '  会这样也是当然的啦……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0103, 400)

    ChrTalk(
        0x000A,
        (
            '这时候，身为游击士前辈\n',
            '一定要好好撑下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '鲁克他们的情况似乎\n',
            '暂且也稳定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然希望他们早点醒来，\n',
            '但为这个干着急也无济于事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔你们\n',
            '也不能鲁莽行事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果你们都倒下了\n',
            '那才是彻底没希望了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F没关系的，别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这孩子也是经验丰富、\n',
            '独当一面的游击士了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿，就算是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F不过，和雪拉姐\n',
            '还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哈哈，还有心给师姐面子，\n',
            '看来是不要紧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那么，调查要努力哦。\n',
            '期待你们的好消息。',
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
        'loc_3C74',
    )

    ChrTalk(
        0x0106,
        (
            '#050F啊啊，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF1')

    def _loc_3C74(): pass

    label('loc_3C74')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CA2',
    )

    ChrTalk(
        0x0108,
        (
            '#070F啊啊，尽力而为了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF1')

    def _loc_3CA2(): pass

    label('loc_3CA2')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3CD4',
    )

    ChrTalk(
        0x0104,
        (
            '#030F呵，尽情期待我的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CF1')

    def _loc_3CD4(): pass

    label('loc_3CD4')

    ChrTalk(
        0x0103,
        (
            '#525F嗯嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CF1(): pass

    label('loc_3CF1')

    OP_A2(0x188D)
    OP_A2(0x0001)
    def _loc_3CF7(): pass

    label('loc_3CF7')

    Jump('loc_43DD')

    def _loc_3CFA(): pass

    label('loc_3CFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_43D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 4, 0x188C)),
            Expr.Return,
        ),
        'loc_3E06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D98',
    )

    ChrTalk(
        0x000A,
        (
            '话说回来这么大的雾，\n',
            '可真是前所未见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '定期船都停航了，\n',
            '真是麻烦的天气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哎呀，很快就会天晴的吧。\n',
            '不用那么担心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E03')

    def _loc_3D98(): pass

    label('loc_3D98')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '别一个人背负一切\n',
            '有话想说随时都可以来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们这边也准备了各种各样\n',
            '高质量的装备等着你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E03(): pass

    label('loc_3E03')

    Jump('loc_43D3')

    def _loc_3E06(): pass

    label('loc_3E06')

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '哦，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好久不见啦。\n',
            '从你去了训练场以后头一次见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F埃尔格先生，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊啊，终于回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '雪拉扎德也在一起，\n',
            '是不是又在执行协会的什么任务啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听爱娜说了，\n',
            '你们俩都很努力嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '特别是艾丝蒂尔成为正游击士后\n',
            '表现更加活跃了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是的，才这么一会儿不见，\n',
            '就变得这么出色了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '当年你那么讨厌考试，\n',
            '在研修中发牢骚，真令人怀念啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1008F我、我说埃尔格先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4004')
    def lambda_4004():
        ChrTurnDirection(0x0000, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4004)

    @scena.Lambda('lambda_4012')
    def lambda_4012():
        ChrTurnDirection(0x0001, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4012)

    @scena.Lambda('lambda_4020')
    def lambda_4020():
        ChrTurnDirection(0x0002, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4020)

    ChrTurnDirection(0x0003, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#021F哎呀，有什么好隐瞒的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '考试确实是很惨，\n',
            '但实技方面可是出类拔萃。',
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
        'loc_40C2',
    )

    ChrTalk(
        0x0106,
        (
            '#051F哈哈，果然是这样吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真像你的风格啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4176')

    def _loc_40C2(): pass

    label('loc_40C2')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40F8',
    )

    ChrTalk(
        0x0107,
        (
            '#560F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哎～姐姐真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4176')

    def _loc_40F8(): pass

    label('loc_40F8')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4135',
    )

    ChrTalk(
        0x0104,
        (
            '#031F呵，感觉\n',
            '真像是艾丝蒂尔的过去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4176')

    def _loc_4135(): pass

    label('loc_4135')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4176',
    )

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，别害羞嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '人有缺点才显得可爱嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4176(): pass

    label('loc_4176')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4197',
    )

    ChrTalk(
        0x0105,
        (
            '#041F嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4197(): pass

    label('loc_4197')

    ChrTalk(
        0x000A,
        (
            '呀，抱歉抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '老说过去的事，\n',
            '大概是因为上了年纪啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '话说回来，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '关于约修亚\n',
            '有什么消息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4217')
    def lambda_4217():
        ChrTurnDirection(0x0000, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4217)

    @scena.Lambda('lambda_4225')
    def lambda_4225():
        ChrTurnDirection(0x0001, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4225)

    @scena.Lambda('lambda_4233')
    def lambda_4233():
        ChrTurnDirection(0x0002, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4233)

    ChrTurnDirection(0x0003, 0x000A, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1003F嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F调查了不少，\n',
            '但没发现什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是吗……\n',
            '果然没那么简单吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听卡西乌斯说起的时候，\n',
            '担心的不得了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但现在看来…艾丝蒂尔。\n',
            '你是没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是，觉得难过的时候\n',
            '随时都可以来这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不介意的话我和斯蒂娜\n',
            '都可以听你倾诉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F埃尔格先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F……嗯，谢谢。\n',
            '我一定会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊啊，常来逛逛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '各种高品质的装备\n',
            '都等着你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188C)
    OP_A2(0x0000)
    def _loc_43D3(): pass

    label('loc_43D3')

    Jump('loc_43DD')

    def _loc_43D6(): pass

    label('loc_43D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_43DD',
    )

    def _loc_43DD(): pass

    label('loc_43DD')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x43E1
@scena.Code('func_08_43E1')
def func_08_43E1():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4946',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 5, 0x209D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4680',
    )

    ChrTurnDirection(0x000B, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '呀，艾丝蒂尔。\n',
            '欢迎，终于来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '……哎呀？哎呀呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莫非是……\n',
            '……约修亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了。\n',
            '斯蒂娜阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，不是做梦……\n',
            '真的是约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，你之前到底\n',
            '跑到哪里去了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1043F抱歉……\n',
            '让您担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '对，对不起哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不应该责备\n',
            '约修亚的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最难过的\n',
            '应该你自己呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F阿姨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '约修亚……\n',
            '抬起头来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你现在能回到洛连特，\n',
            '这就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，别那样\n',
            '一脸阴沉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易才见面，\n',
            '不高兴点多难受啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F哈哈……\n',
            '确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，果然\n',
            '年轻人的笑容就是无敌呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后都要用这个笑容\n',
            '突破工作中的难关哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    OP_A2(0x209D)

    Jump('loc_4943')

    def _loc_4680(): pass

    label('loc_4680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_4821',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4720',
    )

    ChrTalk(
        0x00FE,
        (
            '阿姨也要努力做家务，\n',
            '不能输给艾丝蒂尔你们才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么说扫除和洗衣\n',
            '全部都得靠手来做呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照平时那样子，\n',
            '不一会儿太阳都要下山了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_481E')

    def _loc_4720(): pass

    label('loc_4720')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47D2',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，是艾丝蒂尔啊。\n',
            '工作的情形怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿姨也在努力\n',
            '做家务哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么说扫除和洗衣\n',
            '全部都得靠手来做呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然辛苦，\n',
            '但这可是显示主妇毅力的地方呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_481E')

    def _loc_47D2(): pass

    label('loc_47D2')

    ChrTalk(
        0x00FE,
        (
            '阿姨也在努力\n',
            '做家务哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然辛苦，\n',
            '但这可是显示主妇毅力的地方呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_481E(): pass

    label('loc_481E')

    Jump('loc_4943')

    def _loc_4821(): pass

    label('loc_4821')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_48BC',
    )

    ChrTurnDirection(0x000B, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '阿姨也不会\n',
            '再提过去的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最难过的\n',
            '毕竟是约修亚你自己嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，抬起头\n',
            '开朗一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '年轻人还是\n',
            '最适合明朗的笑容了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4943')

    def _loc_48BC(): pass

    label('loc_48BC')

    ChrTalk(
        0x00FE,
        (
            '导力器不能动了，\n',
            '真是奇怪的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家的工作也增加了，\n',
            '不过可千万别勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '累了就该好好休息……\n',
            '这个可绝对不能忘哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4943(): pass

    label('loc_4943')

    Jump('loc_60DB')

    def _loc_4946(): pass

    label('loc_4946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_50F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 3, 0x1A5B)),
            Expr.Return,
        ),
        'loc_4B9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_49AE',
    )

    ChrTalk(
        0x00FE,
        (
            '很可惜，详细的做法\n',
            '我也没有听过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定是只在\n',
            '洛连特流传的乡土料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B99')

    def _loc_49AE(): pass

    label('loc_49AE')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0020)"),
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
        'loc_49D9',
    )

    Call(1, 0x0000)

    Jump('loc_4B99')

    def _loc_49D9(): pass

    label('loc_49D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B2F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4A52',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '那么，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要多注意身体，\n',
            '打起精神来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待着你和\n',
            '约修亚一起回来的日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B2C')

    def _loc_4A52(): pass

    label('loc_4A52')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔你们似乎\n',
            '这次也是十分活跃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于雾散天晴了，\n',
            '恢复到原来明亮的城市了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔\n',
            '好像又要去别处了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要多注意身体，\n',
            '打起精神来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待着你和约修亚\n',
            '一起回来的那一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_A2(0x0002)

    def _loc_4B2C(): pass

    label('loc_4B2C')

    Jump('loc_4B99')

    def _loc_4B2F(): pass

    label('loc_4B2F')

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '……雪拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿姨相信你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F没、没问题的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#525F你们可以尽管放心，\n',
            '只管等吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B99(): pass

    label('loc_4B99')

    Jump('loc_50F2')

    def _loc_4B9C(): pass

    label('loc_4B9C')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '哎呀，欢迎。\n',
            '艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼嘿嘿……\n',
            '看来非常活跃呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F哪里……\n',
            '没做什么的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，怎么说艾丝蒂尔\n',
            '现在都是游击士了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得，好像不是\n',
            '阿姨认识的艾丝蒂尔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜……\n',
            '阿姨感到有点寂寞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F我、我说阿姨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嘿嘿，开玩笑啦～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，艾丝蒂尔\n',
            '的修行还远远不够呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F呜、呜……别这么说嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（阿、阿姨装哭的功力\n',
            '  可不是盖的啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔你们\n',
            '好像又要去别处了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要多加注意身体，\n',
            '打起精神来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待着你和约修亚\n',
            '一起回来的那一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '所以啦，雪拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔的事，\n',
            '就交给你照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对不能\n',
            '让她喝酒哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，这没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#525F不强人所难\n',
            '是我的原则嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(15)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4E7E',
    )

    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    def _loc_4E7E(): pass

    label('loc_4E7E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EA8',
    )

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    def _loc_4EA8(): pass

    label('loc_4EA8')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4ED2',
    )

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    def _loc_4ED2(): pass

    label('loc_4ED2')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EFC',
    )

    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    def _loc_4EFC(): pass

    label('loc_4EFC')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F26',
    )

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    def _loc_4F26(): pass

    label('loc_4F26')

    Sleep(1000)

    @scena.Lambda('lambda_4F31')
    def lambda_4F31():
        ChrTurnDirection(0x0000, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4F31)

    @scena.Lambda('lambda_4F3F')
    def lambda_4F3F():
        ChrTurnDirection(0x0001, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4F3F)

    @scena.Lambda('lambda_4F4D')
    def lambda_4F4D():
        ChrTurnDirection(0x0002, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4F4D)

    ChrTurnDirection(0x0003, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#1020F咦咦……！？',
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
        'loc_4FA5',
    )

    ChrTalk(
        0x0107,
        (
            '#065F你、你刚才说什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FA5(): pass

    label('loc_4FA5')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FD6',
    )

    ChrTalk(
        0x0105,
        (
            '#542F（是、是不是听错了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FD6(): pass

    label('loc_4FD6')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FF9',
    )

    ChrTalk(
        0x0104,
        (
            '#036F呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FF9(): pass

    label('loc_4FF9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5026',
    )

    ChrTalk(
        0x0108,
        (
            '#073F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5026(): pass

    label('loc_5026')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5053',
    )

    ChrTalk(
        0x0106,
        (
            '#055F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5053(): pass

    label('loc_5053')

    OP_62(0x0103, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0103, 0x0003, 400)
    Sleep(400)

    ChrTurnDirection(0x0103, 0x0000, 400)

    ChrTalk(
        0x0103,
        (
            '#023F哎呀，大家怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿、阿姨也\n',
            '开始觉得有点不安了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……雪拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的交给你了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A5B)
    OP_A2(0x0003)
    def _loc_50F2(): pass

    label('loc_50F2')

    Jump('loc_60DB')

    def _loc_50F5(): pass

    label('loc_50F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_579B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 6, 0x188E)),
            Expr.Return,
        ),
        'loc_53DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5364',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_51D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_5170',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军都出动，\n',
            '让人有点吃惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，有士兵在\n',
            '总算比较放心倒是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51D4')

    def _loc_5170(): pass

    label('loc_5170')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_51D4',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '事件的调查很辛苦，\n',
            '不过可千万别勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔要是倒下了…\n',
            '阿姨会哭的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51D4(): pass

    label('loc_51D4')

    Jump('loc_5361')

    def _loc_51D7(): pass

    label('loc_51D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_52A9',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎。\n',
            '艾丝蒂尔你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，看来今天也\n',
            '一早就在努力工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军都出动，\n',
            '虽然吓了一跳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，有士兵在\n',
            '总算比较放心倒是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，艾丝蒂尔\n',
            '工作中也要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_535E')

    def _loc_52A9(): pass

    label('loc_52A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_535E',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '哎呀，是艾丝蒂尔啊。\n',
            '早上好，今天也这么早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事件的调查很辛苦，\n',
            '不过可千万别勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔要是倒下了…\n',
            '阿姨会哭的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F我、我会小心的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_535E(): pass

    label('loc_535E')

    OP_A2(0x0002)
    def _loc_5361(): pass

    label('loc_5361')

    Jump('loc_53DA')

    def _loc_5364(): pass

    label('loc_5364')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔看来\n',
            '也在努力工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也像个女孩子似的爱干净\n',
            '穿得整整洁洁的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，阿姨\n',
            '也感到安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_53DA(): pass

    label('loc_53DA')

    Jump('loc_5798')

    def _loc_53DD(): pass

    label('loc_53DD')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哎呀…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呀～怎么办呀。\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天就听到传闻\n',
            '我正等着你来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……\n',
            '斯蒂娜阿姨，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F抱歉这么晚才来打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里，别介意。\n',
            '工作很忙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说约修亚的事时\n',
            '还有点担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，艾丝蒂尔看来\n',
            '也在努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯、嗯……算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，这事就不提了，\n',
            '艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（盯……………………\n',
            '　……………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F什、什么？\n',
            '突然盯着我看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我、我刷了牙，\n',
            '脸也洗了才来的呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3S真是的，好漂亮呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事，穿这裙子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有种活跃女孩子的感觉哦～～\n',
            '很适合你哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……是、是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这个，是雪拉姐\n',
            '在王都给我买的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '作为当上正游击士的祝贺哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦～到底是雪拉。\n',
            '很有品味嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，阿姨\n',
            '喜欢就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '注意仪容\n',
            '可是有心思的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为这次的事件\n',
            '好像也很努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，即使成为正游击士\n',
            '看来也能做得很出色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188E)
    OP_A2(0x0003)
    def _loc_5798(): pass

    label('loc_5798')

    Jump('loc_60DB')

    def _loc_579B(): pass

    label('loc_579B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_5D4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 6, 0x188E)),
            Expr.Return,
        ),
        'loc_5822',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔看来\n',
            '也在努力工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也像个女孩子似的爱干净\n',
            '穿得整整洁洁的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，阿姨\n',
            '也感到安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D49')

    def _loc_5822(): pass

    label('loc_5822')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '哎呀…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呀～怎么办呀。\n',
            '这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀，仔细一看\n',
            '连雪拉也在一起呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的～真是好久不见哦！\n',
            '阿姨都急死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '昨天就听到传闻，\n',
            '但去碰你却一直没碰上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈，对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F不过，艾丝蒂尔\n',
            '也有很多事情啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就原谅她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没问题，这点事\n',
            '阿姨还是明白的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说约修亚的事时，\n',
            '还有点担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，看来艾丝蒂尔\n',
            '也很努力的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯、嗯……算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，别提了，\n',
            '艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（盯……………………\n',
            '　……………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F什、什么？\n',
            '突然盯着我看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我、我刷了牙，\n',
            '脸也洗了才来的呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3S真是的，多漂亮呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#1004F哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事，穿这裙子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有种活跃女孩子的感觉哦～～\n',
            '很适合你哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……是、是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这个，是雪拉姐\n',
            '在王都给我买的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '作为当上正游击士的祝贺哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦～到底是雪拉。\n',
            '很有品味嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，阿姨\n',
            '喜欢就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '注意仪容\n',
            '可是有心思的表现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，即使成为正游击士\n',
            '看来也能做得很出色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前那么邋遢的艾丝蒂尔\n',
            '打扮得这么有模有样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜……\n',
            '阿、阿姨都快流眼泪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F哈，哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1013F（没，没想到\n',
            '  穿条裙子她都会哭啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F（要是看到艾丝蒂尔穿婚纱\n',
            '那还不得昏倒了啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x188E)

    def _loc_5D49(): pass

    label('loc_5D49')

    Jump('loc_60DB')

    def _loc_5D4C(): pass

    label('loc_5D4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_60DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 0, 0x1030)),
            Expr.Return,
        ),
        'loc_5DA6',
    )

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，下次\n',
            '要和约修亚一起来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会做好吃的等着你们来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60DB')

    def _loc_5DA6(): pass

    label('loc_5DA6')

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(600)

    OP_63(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '……艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F Hi～斯蒂娜阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是真正的艾丝蒂尔！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，感觉已经\n',
            '１０年没见了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F哪、哪有那么夸张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我每天都和家里人\n',
            '说起你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么都不告诉阿姨，\n',
            '就突然去旅行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F嗯……对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没关系啦，发生那么多\n',
            '事情，也没办法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，赶快\n',
            '说说旅行的故事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也好想见见约修亚呢。\n',
            '他在洛连特吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F唔，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F……稍微打扰一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0142, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，你是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F初次见面，我是巡回神父\n',
            '凯文·格拉汉姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '打扰你们久别重逢很抱歉，\n',
            '但现在艾丝蒂尔有急事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哎，哎呀……是这样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '阿姨真是的，\n',
            '不知不觉就啰嗦起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哪里，别在意。\n',
            '我会再来看您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，我会做艾丝蒂尔\n',
            '喜欢吃的等着你来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次要和约修亚\n',
            '一起来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1030)

    def _loc_60DB(): pass

    label('loc_60DB')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x60DF
@scena.Code('func_09_60DF')
def func_09_60DF():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_6168',
    )

    ChrTalk(
        0x00FE,
        (
            '在雾散之前，\n',
            '好像定期船都不能飞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说，暂时\n',
            '都会待在这里了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～至少去看看\n',
            '附近的名胜就不会觉得无聊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6168(): pass

    label('loc_6168')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x616C
@scena.Code('func_0A_616C')
def func_0A_616C():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_61D3',
    )

    ChrTalk(
        0x00FE,
        (
            '格鲁纳门啦、威尔特桥什么的，\n',
            '想拍的地方还不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得来到洛连特\n',
            '感觉真可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62F9')

    def _loc_61D3(): pass

    label('loc_61D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_62F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_6242',
    )

    ChrTalk(
        0x00FE,
        (
            '本来是来冲洗之前\n',
            '旅行拍摄的照片的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于雾太大哪里也不能去，\n',
            '想着就看看照片也好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62F9')

    def _loc_6242(): pass

    label('loc_6242')

    ChrTalk(
        0x00FE,
        (
            '本来是来冲洗之前\n',
            '旅行拍摄的照片的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于雾太大哪里也不能去，\n',
            '想着就看看照片也好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也有兴趣去拍摄\n',
            '洛连特的钟楼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是这种天气……\n',
            '也只是浪费感光结晶回路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_62F9(): pass

    label('loc_62F9')

    TalkEnd(0x000D)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
