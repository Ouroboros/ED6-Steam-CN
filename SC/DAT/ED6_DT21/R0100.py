import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '利吉'),
    TXT(0x02, '旅行者'),
    TXT(0x03, '旅行者'),
    TXT(0x04, '旅行者'),
    TXT(0x05, '旅行者'),
    TXT(0x06, '洛连特方向'),
    TXT(0x07, '布莱特家方向'),
    TXT(0x08, '格鲁纳门方向'),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0100.x'
    header.mapIndex       = 23
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1132
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
        ('ED6_DT09/CH10240._CH', 'ED6_DT09/CH10240P._CP'),
        ('ED6_DT09/CH10241._CH', 'ED6_DT09/CH10241P._CP'),
        ('ED6_DT09/CH10230._CH', 'ED6_DT09/CH10230P._CP'),
        ('ED6_DT09/CH10231._CH', 'ED6_DT09/CH10231P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
    ]

# id: 0x10002 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -14030,
            z                   = 1000,
            y                   = 217340,
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
            x                   = -60890,
            z                   = 1030,
            y                   = 216800,
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
            x                   = -39320,
            z                   = 1000,
            y                   = 90280,
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

# id: 0x10003 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -47710,
            z           = 1070,
            y           = 180970,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0015,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -13870,
            z           = 990,
            y           = 154000,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0016,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -46050,
            z           = 970,
            y           = 122240,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0017,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28090,
            z           = 2080,
            y           = 121460,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0014,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x2A2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -22940,
            y           = 0,
            z           = 197540,
            range       = -5430,
            dword_10    = 0x000007D0,
            dword_14    = 0x00030AC0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = -44530,
            y           = 500,
            z           = 103860,
            range       = -33910,
            dword_10    = 0x000007D0,
            dword_14    = 0x0001A054,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10005 offset: 0x2E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -36800,
            triggerZ            = 1000,
            triggerY            = 152300,
            triggerRange        = 1500,
            actorX              = -36800,
            actorZ              = 2500,
            actorY              = 152800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -39100,
            triggerZ            = 1000,
            triggerY            = 153300,
            triggerRange        = 1500,
            actorX              = -39100,
            actorZ              = 2200,
            actorY              = 153300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x32B
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFD7F60, 0x00006D60, 0x00230008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_354',
    )

    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x14),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_354(): pass

    label('loc_354')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_396',
    )

    OP_B5(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_381',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)

    Jump('loc_396')

    def _loc_381(): pass

    label('loc_381')

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x00013880, 0x00000000)

    def _loc_396(): pass

    label('loc_396')

    Return()

# id: 0x0002 offset: 0x397
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 1, 0x1811)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3A4',
    )

    Return()

    def _loc_3A4(): pass

    label('loc_3A4')

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
        'loc_3C4',
    )

    Call(0, 0x0007)
    FadeIn(0, 0)
    Call(0, 0x0008)

    def _loc_3C4(): pass

    label('loc_3C4')

    Fade(1000)
    OP_6D(-14210, 1000, 198480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -14640, 1000, 198480, 0)
    SetChrPos(0x0103, -13640, 1000, 198480, 0)
    SetChrPos(0x00F8, -14890, 1000, 197480, 0)
    SetChrPos(0x00F9, -13390, 1000, 197480, 0)
    OP_0D()
    SetChrPos(0x0008, -14040, 1000, 212170, 180)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#3350281135V#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#3350281136V#4P那不是\n',
            '前辈吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50B',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_549')

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_532',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_549')

    def _loc_532(): pass

    label('loc_532')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_549(): pass

    label('loc_549')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_570',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_5AE')

    def _loc_570(): pass

    label('loc_570')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_597',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_5AE')

    def _loc_597(): pass

    label('loc_597')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_5AE(): pass

    label('loc_5AE')

    Sleep(1000)

    @scena.Lambda('lambda_05B9')
    def lambda_05B9():
        OP_6D(-13440, 1000, 202010, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05B9)

    @scena.Lambda('lambda_05D1')
    def lambda_05D1():
        OP_67(0, 8050, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05D1)

    @scena.Lambda('lambda_05E9')
    def lambda_05E9():
        OP_6C(49000, 2500)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_05E9)

    @scena.Lambda('lambda_05F9')
    def lambda_05F9():
        OP_6E(293, 2500)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_05F9)

    SetChrPos(0x0008, -13760, 1000, 215490, 180)
    SetChrPos(0x0009, -13260, 1000, 215490, 180)
    SetChrPos(0x000A, -14260, 1000, 215490, 180)
    SetChrPos(0x000B, -13260, 1000, 215490, 180)
    SetChrPos(0x000C, -14260, 1000, 215490, 180)
    ClearChrFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_0663')
    def lambda_0663():
        OP_90(0x00FE, 0, 0, -13500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0663)

    Sleep(500)

    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_0688')
    def lambda_0688():
        OP_90(0x00FE, 0, 0, -12500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0688)

    Sleep(100)

    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_06AD')
    def lambda_06AD():
        OP_90(0x00FE, 0, 0, -12500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_06AD)

    Sleep(500)

    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_06D2')
    def lambda_06D2():
        OP_90(0x00FE, 0, 0, -11500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_06D2)

    Sleep(100)

    ClearChrFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_06F7')
    def lambda_06F7():
        OP_90(0x00FE, 0, 0, -11500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_06F7)

    WaitForThreadExit(0x0008, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B3',
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
        0,
        (
            TXT(0x00, '【◇在第４章和利吉再会过】\n'),
            TXT(0x01, '【◇在第４章没有和利吉再会过】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_7A7'),
        (0x00000001, 'loc_7AD'),
        (-1, 'loc_7B3'),
    )

    def _loc_7A7(): pass

    label('loc_7A7')

    OP_A3(0x1880)

    Jump('loc_7B3')

    def _loc_7AD(): pass

    label('loc_7AD')

    OP_A2(0x1880)

    Jump('loc_7B3')

    def _loc_7B3(): pass

    label('loc_7B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 0, 0x1880)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9B5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030281137V#023F#2P哎呀，这不是利吉吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281138V#1011F#6P利吉先生，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281139V#5P啊，艾丝蒂尔。\n',
            '自从你到训练场后就没再见面了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281140V#5P我听爱娜说过了。\n',
            '说你在做很重要的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281141V#1016F#6P嗯，是呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281142V#1015F利吉先生是在\n',
            '进行护卫的工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281143V#5P嗯，这些客人\n',
            '好像有急事要去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281144V#5P按现在这种情形，\n',
            '今天的定期船恐怕也没法航行了，\n',
            '所以就由我送他们过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281145V#1006F#6P原来如此，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A7A')

    def _loc_9B5(): pass

    label('loc_9B5')

    ChrTalk(
        0x0103,
        (
            '#0030281146V#020F#2P哎呀，这不是利吉吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281147V#1011F#6P要出发去王都了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281148V#5P嗯，客人已经\n',
            '全部到齐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281149V#5P到那边之后，我也要\n',
            '顺便去一趟王都支部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A7A(): pass

    label('loc_A7A')

    ChrTalk(
        0x0103,
        (
            '#0030281150V#021F#2P呵呵，辛苦了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281151V#5P前辈你们才是。\n',
            '雾的调查工作辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281152V#5P街道的状況怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281153V#020F#2P艾利兹街道的雾\n',
            '并没有扩散得很远。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281154V稍走一走\n',
            '立刻视野就开阔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281155V#5P呼，那太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281156V#5P那么\n',
            '我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#3350281157V#4P各位，\n',
            '我们出发前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3350281158V#4P请不要离我太远啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '商人',
        (
            '#3360281159V#2P噢！拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000A,
        '旅行者',
        (
            '#3370281160V#1P全靠你了啊，游击士先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1811)
    OP_8C(0x0008, 180, 400)

    @scena.Lambda('lambda_0C81')
    def lambda_0C81():
        OP_90(0x00FE, 0, 0, -15000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C81)

    Sleep(50)

    @scena.Lambda('lambda_0CA1')
    def lambda_0CA1():
        OP_90(0x00FE, 0, 0, -15000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0CA1)

    Sleep(30)

    @scena.Lambda('lambda_0CC1')
    def lambda_0CC1():
        OP_90(0x00FE, 0, 0, -15000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CC1)

    Sleep(50)

    @scena.Lambda('lambda_0CE1')
    def lambda_0CE1():
        OP_90(0x00FE, 0, 0, -15000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CE1)

    Sleep(30)

    @scena.Lambda('lambda_0D01')
    def lambda_0D01():
        OP_90(0x00FE, 0, 0, -15000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0D01)

    Sleep(300)

    CreateThread(0x0101, 0x01, 0x00, 0x0003)
    Sleep(50)

    CreateThread(0x0103, 0x01, 0x00, 0x0004)
    Sleep(200)

    CreateThread(0x00F8, 0x01, 0x00, 0x0005)
    Sleep(50)

    CreateThread(0x00F9, 0x01, 0x00, 0x0006)

    @scena.Lambda('lambda_0D4C')
    def lambda_0D4C():
        OP_6D(-15630, 1000, 200190, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D4C)

    @scena.Lambda('lambda_0D64')
    def lambda_0D64():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_0D64)

    @scena.Lambda('lambda_0D7C')
    def lambda_0D7C():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_0D7C)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0000, 0x03)
    TerminateThread(0x0001, 0x03)
    TerminateThread(0x0002, 0x03)
    TerminateThread(0x0003, 0x03)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0xDB7
@scena.Code('func_03_DB7')
def func_03_DB7():
    OP_8F(0x00FE, -15630, 1000, 200190, 2000, 0x00)

    @scena.Lambda('lambda_0DD1')
    def lambda_0DD1():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0DD1')

    DispatchAsync2(0x00FE, 0x0003, lambda_0DD1)

    Return()

# id: 0x0004 offset: 0xDDD
@scena.Code('func_04_DDD')
def func_04_DDD():
    OP_8F(0x00FE, -15630, 1000, 199190, 2000, 0x00)

    @scena.Lambda('lambda_0DF7')
    def lambda_0DF7():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0DF7')

    DispatchAsync2(0x00FE, 0x0003, lambda_0DF7)

    Return()

# id: 0x0005 offset: 0xE03
@scena.Code('func_05_E03')
def func_05_E03():
    OP_8F(0x00FE, -15630, 1000, 198190, 2000, 0x00)

    @scena.Lambda('lambda_0E1D')
    def lambda_0E1D():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0E1D')

    DispatchAsync2(0x00FE, 0x0003, lambda_0E1D)

    Return()

# id: 0x0006 offset: 0xE29
@scena.Code('func_06_E29')
def func_06_E29():
    OP_8F(0x00FE, -15630, 1000, 197190, 2000, 0x00)

    @scena.Lambda('lambda_0E43')
    def lambda_0E43():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0E43')

    DispatchAsync2(0x00FE, 0x0003, lambda_0E43)

    Return()

# id: 0x0007 offset: 0xE4F
@scena.Code('func_07_E4F')
def func_07_E4F():
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
        (0x00000000, 'loc_ECC'),
        (0x00000001, 'loc_ED2'),
        (-1, 'loc_ED8'),
    )

    def _loc_ECC(): pass

    label('loc_ECC')

    OP_A2(0x1200)

    Jump('loc_ED8')

    def _loc_ED2(): pass

    label('loc_ED2')

    OP_A2(0x1201)

    Jump('loc_ED8')

    def _loc_ED8(): pass

    label('loc_ED8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_EE6',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_EEA')

    def _loc_EE6(): pass

    label('loc_EE6')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_EEA(): pass

    label('loc_EEA')

    Return()

# id: 0x0008 offset: 0xEEB
@scena.Code('func_08_EEB')
def func_08_EEB():
    ClearMapFlags(0x00000001)
    OP_6D(20400, 1640, 198520, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
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

# id: 0x0009 offset: 0xF3D
@scena.Code('func_09_F3D')
def func_09_F3D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FCE',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010190296V#505F啊，走过头了。\n',
            '必须快点回家才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0142, 0x0000, 400)

    ChrTalk(
        0x0142,
        (
            '#0180190297V#1060F呵呵，早点回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_106E')

    def _loc_FCE(): pass

    label('loc_FCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_106E',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FF2',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_FF9')

    def _loc_FF2(): pass

    label('loc_FF2')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_FF9(): pass

    label('loc_FF9')

    ChrTalk(
        0x0103,
        (
            '#0030290314V#020F这边和城里是反方向啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290315V不要耽误时间了，\n',
            '快点去协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_106E(): pass

    label('loc_106E')

    Return()

# id: 0x000A offset: 0x106F
@scena.Code('func_0A_106F')
def func_0A_106F():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　洛连特市　　　４９塞尔矩\n',
            '南　格鲁纳门　　２５９塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x10DB
@scena.Code('func_0B_10DB')
def func_0B_10DB():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　布莱特家',
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
