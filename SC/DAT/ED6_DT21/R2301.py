import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡露娜'),
    TXT(0x02, '库拉茨'),
    TXT(0x03, '亡命守护者'),
    TXT(0x04, '亡命守护者'),
    TXT(0x05, '亡命守护者'),
    TXT(0x06, '亡命守护者'),
    TXT(0x07, '梅威海道方向'),
    TXT(0x08, '杰尼丝王立学院方向'),
    TXT(0x09, '水银蝰蛇'),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
    TXT(0x0E, ''),
    TXT(0x0F, ''),
    TXT(0x10, ''),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2301.x'
    header.mapIndex       = 102
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x41B8
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
        ('ED6_DT09/CH10520._CH', 'ED6_DT09/CH10520P._CP'),
        ('ED6_DT09/CH10521._CH', 'ED6_DT09/CH10521P._CP'),
        ('ED6_DT29/CH12040._CH', 'ED6_DT29/CH12040P._CP'),
        ('ED6_DT29/CH12041._CH', 'ED6_DT29/CH12041P._CP'),
        ('ED6_DT09/CH10340._CH', 'ED6_DT09/CH10340P._CP'),
        ('ED6_DT09/CH10341._CH', 'ED6_DT09/CH10341P._CP'),
        ('ED6_DT09/CH11040._CH', 'ED6_DT09/CH11040P._CP'),
        ('ED6_DT09/CH11041._CH', 'ED6_DT09/CH11041P._CP'),
        ('ED6_DT09/CH11070._CH', 'ED6_DT09/CH11070P._CP'),
        ('ED6_DT09/CH11071._CH', 'ED6_DT09/CH11071P._CP'),
        ('ED6_DT09/CH11080._CH', 'ED6_DT09/CH11080P._CP'),
        ('ED6_DT09/CH11081._CH', 'ED6_DT09/CH11081P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT09/CH11250._CH', 'ED6_DT09/CH11250P._CP'),
        ('ED6_DT09/CH11251._CH', 'ED6_DT09/CH11251P._CP'),
    ]

# id: 0x10002 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 128320,
            z                   = 20,
            y                   = -8070,
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
            x                   = 288640,
            z                   = 10,
            y                   = -9980,
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
            x                   = 219810,
            z                   = 770,
            y                   = -59460,
            direction           = 332,
            word_0E             = 15,
            dword_10            = 983040,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x252
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 164610,
            z           = 540,
            y           = -8970,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0196,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 161500,
            z           = -30,
            y           = -7250,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0196,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 193850,
            z           = 320,
            y           = -43450,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0191,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 218740,
            z           = 0,
            y           = -37100,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0195,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 235120,
            z           = -10,
            y           = -3610,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0193,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 230490,
            z           = 130,
            y           = -5740,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0194,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 210450,
            z           = 10,
            y           = -27270,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0195,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x316
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 219810,
            y           = -1000,
            z           = -59460,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x336
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x336
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_352',
    )

    OP_A3(0x10F0)
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0004)

    Jump('loc_387')

    def _loc_352(): pass

    label('loc_352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_36E',
    )

    OP_A3(0x10F1)
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0007)

    Jump('loc_387')

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_387',
    )

    OP_A3(0x10F2)
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x000E)

    def _loc_387(): pass

    label('loc_387')

    Return()

# id: 0x0001 offset: 0x388
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0x00014C08, 0xFFFDA670, 0x0023002A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3B8',
    )

    SetChrFlags(0x0010, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_3CA')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 2, 0x12FA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CA',
    )

    ClearChrFlags(0x0010, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_3CA(): pass

    label('loc_3CA')

    Return()

# id: 0x0002 offset: 0x3CB
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E0',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_3E0(): pass

    label('loc_3E0')

    Return()

# id: 0x0003 offset: 0x3E1
@scena.Code('func_03_3E1')
def func_03_3E1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 2, 0x12FA)),
            Expr.Return,
        ),
        'loc_3E9',
    )

    Return()

    def _loc_3E9(): pass

    label('loc_3E9')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
            TxtCtl.Enter,
        ),
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
        32,
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_4CE'),
        (-1, 'loc_4F1'),
    )

    def _loc_4CE(): pass

    label('loc_4CE')

    Fade(500)
    OP_89(0x0000, 217320, -20, -51680, 180)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_4F1(): pass

    label('loc_4F1')

    Battle(0x00000EDD, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 217320, -20, -51680, 180)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_52A'),
        (0x00000001, 'loc_52D'),
        (-1, 'loc_530'),
    )

    def _loc_52A(): pass

    label('loc_52A')

    EventEnd(0x00)

    Return()

    def _loc_52D(): pass

    label('loc_52D')

    OP_B4(0x00)

    Return()

    def _loc_530(): pass

    label('loc_530')

    EventBegin(0x01)
    SetChrFlags(0x0010, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x12FA)
    OP_28(0x00A1, 0x04, 0x10)
    OP_28(0x00A1, 0x04, 0x02)
    OP_28(0x00A1, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x59C
@scena.Code('func_04_59C')
def func_04_59C():
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
        'loc_5B3',
    )

    Call(0, 0x0015)
    Call(0, 0x0016)

    def _loc_5B3(): pass

    label('loc_5B3')

    Call(0, 0x0005)
    OP_6D(271510, 20, -9370, 0)
    OP_67(0, 10150, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    SetChrPos(0x000A, 269300, 750, -11440, 270)
    SetChrPos(0x000B, 269300, 750, -9000, 270)
    SetChrPos(0x000C, 272070, 750, -12200, 270)
    SetChrPos(0x000D, 272290, 750, -7890, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0101, 237740, 100, -15610, 90)
    SetChrPos(0x0102, 237590, 200, -16730, 90)
    SetChrPos(0x0103, 236640, -30, -15660, 90)
    SetChrPos(0x0108, 235150, -120, -16610, 90)
    SetChrPos(0x0107, 236340, 10, -17100, 90)
    SetChrPos(0x0106, 236570, 310, -18350, 90)
    OP_D2(0x002600FC, 0x00260101, 0x13)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_06ED')
    def lambda_06ED():
        OP_6D(237450, 80, -15960, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06ED)

    @scena.Lambda('lambda_0705')
    def lambda_0705():
        OP_67(0, 6890, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0705)

    @scena.Lambda('lambda_071D')
    def lambda_071D():
        OP_6B(2450, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_071D)

    @scena.Lambda('lambda_072D')
    def lambda_072D():
        OP_6E(332, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_072D)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_7AB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050360531V#053F#6P听说了情况\n',
            '就火速赶来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360532V#057F看来状况相当不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_884')

    def _loc_7AB(): pass

    label('loc_7AB')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_819',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360533V#026F#6P还好听说了情况\n',
            '就火速赶来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360534V#022F看来状况相当危险啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_884')

    def _loc_819(): pass

    label('loc_819')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_884',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360535V#074F#6P还好听说了情况\n',
            '就火速赶来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080360536V#072F看来状况相当严峻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_884(): pass

    label('loc_884')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_906',
    )

    ChrTalk(
        0x0107,
        (
            '#0070360537V#065F#6P虽、虽然让嘉恩先生\n',
            '联络了王国军……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070360538V但是他说援军前来\n',
            '可能要花费一点时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E7')

    def _loc_906(): pass

    label('loc_906')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_979',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360539V#072F#6P接待处的小哥\n',
            '已经联络了王国军……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080360540V但援军似乎不可能马上就到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E7')

    def _loc_979(): pass

    label('loc_979')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_9E7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360541V#022F#6P虽然让嘉恩先生\n',
            '联络了王国军……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360542V但援军似乎不可能马上就到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E7(): pass

    label('loc_9E7')

    OP_8C(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360543V#1003F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080360544V#074F#6P无论如何，既然导力兵器也不能用，\n',
            '军方的部队来了也帮不上什么忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080360545V#072F看来只能靠习惯白刃战的我们\n',
            '来解决这一次的事件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1B')

    def _loc_AC1(): pass

    label('loc_AC1')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B74',
    )

    OP_8C(0x0106, 0, 400)

    ChrTalk(
        0x0106,
        (
            '#0050360546V#053F#6P无论如何，既然导力兵器也不能用，\n',
            '军方的部队来了也帮不上什么忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360547V#050F只能靠习惯白刃战的我们\n',
            '来解决这一次的事件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C1B')

    def _loc_B74(): pass

    label('loc_B74')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C1B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360548V#026F#6P无论如何，既然导力兵器也不能用，\n',
            '军方的部队来了也帮不上什么忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360549V#022F只能靠习惯白刃战的我们\n',
            '来解决这一次的事件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C1B(): pass

    label('loc_C1B')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C89',
    )

    ChrTalk(
        0x0107,
        (
            '#0070360550V#065F#6P但、但是，学院的人们\n',
            '好像被抓起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070360551V怎么办才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D79')

    def _loc_C89(): pass

    label('loc_C89')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CFD',
    )

    ChrTalk(
        0x0103,
        (
            '#0030360552V#522F#6P只是，学院的相关人员\n',
            '肯定是被抓起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360553V轻举妄动就很危险吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D79')

    def _loc_CFD(): pass

    label('loc_CFD')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D79',
    )

    OP_8C(0x0106, 0, 400)

    ChrTalk(
        0x0106,
        (
            '#0050360554V#552F#4P只是，学院的相关人员\n',
            '被抓起来的可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360555V轻举妄动也很不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D79(): pass

    label('loc_D79')

    ChrTalk(
        0x0101,
        (
            '#0010360556V#1007F#5P确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360557V#1003F要是能想办法\n',
            '搞清楚内部的状况了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360558V#1042F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360559V#1035F……稍等一下。\n',
            '我去调查学院内的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0ED1')
    def lambda_0ED1():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0ED1)

    @scena.Lambda('lambda_0EDF')
    def lambda_0EDF():
        OP_8C(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0EDF)

    Sleep(100)

    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360560V#1004F约、约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030360561V#022F#6P……什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360562V#1040F#2P侦察之类的隐密活动\n',
            '是我最为擅长的领域。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360563V我想应该可以将敌方战力\n',
            '和人质的状况都调查出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360564V#555F#4P原来如此啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080360565V#074F#6P唔，能办到的话\n',
            '那就务必麻烦你跑一趟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070360566V#065F#6P但、但是！\n',
            '这不是很危险吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360567V#1040F#2P没问题，我过去曾经在\n',
            '更严苛的状况下进行过潜入活动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360568V不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070360569V#063F#6P但、但是但是～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010360570V#1002F#5P……约修亚。\n',
            '你真的坚持一个人去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020360571V#1043F#4P单独行动\n',
            '反而成功率比较高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360572V#1042F还是让我一个人去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360573V#1010F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360574V#1002F……那我就确认一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360575V那时候的约定……\n',
            '你还记得吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360576V#1053F#4P一起走到最后，对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360577V#1054F没问题──我绝对不会忘记的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360578V#1006F#5P嗯，那就行了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360579V#1025F约修亚……\n',
            '你要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360580V#1053F#4P嗯，我明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360581V#1040F#2P那么我去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0102, 90, 400)

    @scena.Lambda('lambda_1352')
    def lambda_1352():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1352')

    DispatchAsync2(0x0101, 0x0002, lambda_1352)

    @scena.Lambda('lambda_1363')
    def lambda_1363():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1363')

    DispatchAsync2(0x0103, 0x0002, lambda_1363)

    @scena.Lambda('lambda_1374')
    def lambda_1374():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1374')

    DispatchAsync2(0x0107, 0x0002, lambda_1374)

    @scena.Lambda('lambda_1385')
    def lambda_1385():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1385')

    DispatchAsync2(0x0106, 0x0002, lambda_1385)

    @scena.Lambda('lambda_1396')
    def lambda_1396():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_1396')

    DispatchAsync2(0x0108, 0x0002, lambda_1396)

    @scena.Lambda('lambda_13A7')
    def lambda_13A7():
        OP_6D(244310, 100, -18660, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13A7)

    @scena.Lambda('lambda_13BF')
    def lambda_13BF():
        OP_67(0, 4870, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13BF)

    @scena.Lambda('lambda_13D7')
    def lambda_13D7():
        OP_6B(2770, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_13D7)

    @scena.Lambda('lambda_13E7')
    def lambda_13E7():
        OP_6C(105000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13E7)

    @scena.Lambda('lambda_13F7')
    def lambda_13F7():
        OP_6E(371, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_13F7)

    OP_D2(0x002600FC, 0x00260101, 0x13)
    SetChrFlags(0x0102, 0x0004)
    OP_8E(0x0102, 239020, 1000, -17200, 5000, 0x00)
    OP_8E(0x0102, 245770, 1000, -20790, 5000, 0x00)
    SetChrChipByIndex(0x0102, 19)
    SetChrSubChip(0x0102, 1)
    Sleep(500)

    SetChrSubChip(0x0102, 0)
    OP_7D(0x00, 0x0102, 0x0014, 0x01F4)
    SetChrFlags(0x0102, 0x0020)
    SetChrFlags(0x0102, 0x1000)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_1469')
    def lambda_1469():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1469)

    OP_8F(0x0102, 245770, 5000, -20790, 10000, 0x00)
    OP_7D(0x01, 0x0102, 0x0000, 0x0000)
    SetChrFlags(0x0102, 0x0080)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0103, 0x02)
    TerminateThread(0x0107, 0x02)
    TerminateThread(0x0106, 0x02)
    TerminateThread(0x0108, 0x02)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    OP_6D(237450, 80, -15960, 0)
    OP_67(0, 6890, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    OP_0D()
    OP_8C(0x0106, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050360582V#552F喂……没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010360583V#1025F……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360584V这种情况下跟去\n',
            '反而会变成累赘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360585V#1012F而且……\n',
            '我相信约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15B4')
    def lambda_15B4():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_15B4)

    Sleep(100)

    @scena.Lambda('lambda_15C7')
    def lambda_15C7():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_15C7)

    Sleep(100)

    OP_8C(0x0103, 90, 400)

    ChrTalk(
        0x0107,
        (
            '#0070341446V#560F#6P姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030360587V#027F#6P呵呵……\n',
            '真是变成了一个越来越有魅力的女性了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0006)
    FormationReset()
    FormationAddMember(ChrTable['约修亚'], 0xF6, 0xFF)
    OP_A2(0x2013)
    OP_28(0x00C0, 0x04, 0x02)
    OP_28(0x00C0, 0x04, 0x08)
    OP_28(0x00C0, 0x01, 0x0001)
    SetMapFlags(0x02000000)
    OP_A2(0x10FE)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T2500._SN', 124, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x1682
@scena.Code('func_05_1682')
def func_05_1682():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_16BB',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_16BB(): pass

    label('loc_16BB')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_16F4',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16DC',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFA, 0xFF)

    Jump('loc_16E0')

    def _loc_16DC(): pass

    label('loc_16DC')

    FormationAddMember(ChrTable['阿加特'], 0xFB, 0xFF)

    def _loc_16E0(): pass

    label('loc_16E0')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_16F4(): pass

    label('loc_16F4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_172D',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1715',
    )

    FormationAddMember(ChrTable['提妲'], 0xFA, 0xFF)

    Jump('loc_1719')

    def _loc_1715(): pass

    label('loc_1715')

    FormationAddMember(ChrTable['提妲'], 0xFB, 0xFF)

    def _loc_1719(): pass

    label('loc_1719')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_172D(): pass

    label('loc_172D')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1748',
    )

    FormationAddMember(ChrTable['金'], 0xFB, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1748(): pass

    label('loc_1748')

    Return()

# id: 0x0006 offset: 0x1749
@scena.Code('func_06_1749')
def func_06_1749():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_1759',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_1759(): pass

    label('loc_1759')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1769',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_1769(): pass

    label('loc_1769')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_1779',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_1779(): pass

    label('loc_1779')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_1789',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_1789(): pass

    label('loc_1789')

    Return()

# id: 0x0007 offset: 0x178A
@scena.Code('func_07_178A')
def func_07_178A():
    EventBegin(0x00)
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xFF, 0xFF)
    SetChrFlags(0x010E, 0x0080)
    SetChrFlags(0x010A, 0x0080)
    OP_6D(235560, 50, -19240, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(45000, 0)
    OP_6E(427, 0)
    SetChrPos(0x0102, 235850, 100, -20090, 270)
    SetChrPos(0x0101, 233750, 10, -20340, 90)
    SetChrPos(0x0107, 234430, -10, -21490, 45)
    SetChrPos(0x0103, 234550, -10, -19020, 135)
    SetChrPos(0x0106, 233180, 10, -21580, 90)
    SetChrPos(0x0108, 233000, 30, -19660, 90)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020360696V#1040F#2P……以上就是在侦察中\n',
            '所得知的学院内大致的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080360697V#070F#6P是吗……\n',
            '调查得很清楚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360698V#051F啊啊，这下\n',
            '总算能制定详细的作战计划了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360699V#1007F#6P不过，想不到那个基尔巴特\n',
            '居然是袭击学院的罪魁祸首……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360700V#1019F而且似乎\n',
            '还想抓走科洛丝～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360701V#1022F在『方舟』见到时，\n',
            '就该把他揍个\n',
            '满地找牙才对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030360702V#026F#5P过去是才华横溢的市长秘书，\n',
            '现在变成了『结社』的走狗吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360703V#524F感觉这是一个曾经的精英人物\n',
            '在遭受挫折后人格扭曲的典型例子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360704V#1007F#6P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360705V#1015F……不过，怎么办呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360706V士兵的数量也相当多，\n',
            '还有人偶兵器和装甲兽吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070360707V#065F而且，既然有人偶兵器\n',
            '在活动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070360708V这就是说『结社』的人，在这种状况下\n',
            '还有可能使用导力器吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360709V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360710V#1035F#2P看来好像使用了\n',
            '和博士发明的『零力场发生器』\n',
            '相同的技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360711V#1042F而且似乎还没有数量限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360712V#052F#6P这么说来，他们可以\n',
            '随心所欲地使用枪或魔法了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360713V#057F还真是有点棘手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0103, 180, 400)

    ChrTalk(
        0x0103,
        (
            '#0030360714V#026F#5P嗯，虽然很麻烦，\n',
            '但还是兵分两路吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360715V#020F从正面诱出敌方战力，\n',
            '再由别动队从后方突袭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080360716V#074F#6P不过，要这么做\n',
            '战斗力有点不足啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080360717V#072F正面攻击的人\n',
            '至少要６个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360718V#1043F#2P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360719V#1035F这样的人数应该就可以把\n',
            '待命中的士兵吸引到这边来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360720V#1007F#6P不过６个人……\n',
            '不是这里全部人数吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360721V#1015F还是只能像这样子\n',
            '等待王国军部队抵达呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x010E, 221680, -40, -19680, 90)
    SetChrPos(0x010A, 221970, -50, -21480, 45)
    SetChrPos(0x0008, 220360, -20, -21540, 45)
    SetChrPos(0x0009, 220510, 30, -20230, 45)

    NpcTalk(
        0x010E,
        '男性的声音',
        (
            '#0330360722V#2P……这方面就\n',
            '让我们来补足吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1F82')
    def lambda_1F82():
        ChrTurnDirection(0x00FE, 0x010A, 400)
        Yield()

        Jump('lambda_1F82')

    DispatchAsync2(0x0101, 0x0001, lambda_1F82)

    Sleep(50)

    @scena.Lambda('lambda_1F98')
    def lambda_1F98():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1F98)

    Sleep(50)

    @scena.Lambda('lambda_1FAB')
    def lambda_1FAB():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1FAB)

    Sleep(50)

    @scena.Lambda('lambda_1FBE')
    def lambda_1FBE():
        ChrTurnDirection(0x00FE, 0x010A, 400)
        Yield()

        Jump('lambda_1FBE')

    DispatchAsync2(0x0107, 0x0001, lambda_1FBE)

    Sleep(50)

    @scena.Lambda('lambda_1FD4')
    def lambda_1FD4():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_1FD4')

    DispatchAsync2(0x0102, 0x0001, lambda_1FD4)

    Sleep(50)

    @scena.Lambda('lambda_1FEA')
    def lambda_1FEA():
        ChrTurnDirection(0x00FE, 0x010E, 400)
        Yield()

        Jump('lambda_1FEA')

    DispatchAsync2(0x0103, 0x0001, lambda_1FEA)

    Sleep(50)

    Fade(1000)
    OP_6D(231990, 10, -19220, 0)
    OP_67(0, 6070, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(314000, 0)
    OP_6E(330, 0)
    SetChrPos(0x0102, 235850, 100, -20090, 270)
    SetChrPos(0x0101, 234240, 0, -20170, 90)
    SetChrPos(0x0107, 234310, 0, -21170, 45)
    SetChrPos(0x0103, 234590, -10, -18900, 135)
    SetChrPos(0x0106, 233140, 20, -20930, 90)
    SetChrPos(0x0108, 233260, 50, -19170, 90)
    CreateThread(0x010E, 0x01, 0x00, 0x000A)
    CreateThread(0x010A, 0x01, 0x00, 0x000B)
    CreateThread(0x0008, 0x01, 0x00, 0x000C)
    CreateThread(0x0009, 0x01, 0x00, 0x000D)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0108, 0)
    SetChrSubChip(0x0106, 0)
    SetChrSubChip(0x0107, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0102, 0)
    Sleep(2000)

    CreateThread(0x0106, 0x01, 0x00, 0x0008)
    CreateThread(0x0108, 0x01, 0x00, 0x0009)
    WaitForThreadExit(0x0009, 0x0001)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0103, 0x01)
    WaitForThreadExit(0x0106, 0x0001)
    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0107,
        (
            '#0070360723V#064F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360724V#1004F啊啊～！\n',
            '亚妮拉丝你们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080360725V#071F#2P哈哈，你们来的\n',
            '真是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0310360726V#825F#5P嘿嘿，我们\n',
            '刚刚到达卢安支部的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320360727V#835F#5P听嘉恩一说\n',
            '就急急忙忙赶来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030360728V#021F真是的……\n',
            '实在是求之不得的援军啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2241')
    def lambda_2241():
        OP_6D(233430, 30, -19680, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2241)

    @scena.Lambda('lambda_2259')
    def lambda_2259():
        OP_67(0, 6760, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2259)

    @scena.Lambda('lambda_2271')
    def lambda_2271():
        OP_6B(2400, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2271)

    OP_8F(0x010A, 232640, 20, -19990, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x010A,
        (
            '#0120360729V#1314F#5P……艾丝蒂尔。\n',
            '在湖畔承蒙你解救后就没再见面了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360730V那个时候真是多谢了。\n',
            '在危机时刻救了我一命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360731V#1316F那之后，听说艾丝蒂尔\n',
            '被抓走了，\n',
            '我真是十分抱歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360732V#1016F#4P啊哈哈，没关系，\n',
            '反正我也平安无事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360733V#1006F而且……\n',
            '约修亚也回来了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190990V#1314F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360735V#819F嘿嘿……\n',
            '好久不见呢，约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360736V还记得姐姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360737V#1053F是……当然了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360738V#1054F我不在的时候，\n',
            '听说你们一直很照顾艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360739V请务必让我表示感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360740V#816F#5P呵呵，添麻烦的\n',
            '应该是我才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360741V#1311F话说回来我还想告诉你，\n',
            '你不在的时候\n',
            '艾丝蒂尔有多么寂寞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360742V#1013F#4P慢、慢着～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360743V#1315F#5P嘿嘿，开玩笑啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360744V#816F……现在的状况\n',
            '可容不得这么悠闲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360745V#1007F#4P嗯……其实正是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360746V#1015F#5P约修亚，再把学院内的情况\n',
            '说一遍好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360747V#1040F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_D2(0x002601B2, 0x002601B7, 0x11)
    Sleep(2000)

    SetChrPos(0x0101, 233370, 10, -20870, 270)
    SetChrPos(0x0102, 233420, 30, -19530, 270)
    SetChrPos(0x0107, 234280, 0, -20840, 270)
    SetChrPos(0x0103, 234500, 10, -19470, 270)
    SetChrPos(0x0106, 234780, 20, -22300, 270)
    SetChrPos(0x0108, 235690, 50, -21240, 270)
    SetChrPos(0x010A, 231370, 20, -20800, 90)
    OP_8C(0x0102, 270, 0)
    OP_8C(0x0101, 270, 0)
    OP_6D(231700, 0, -19410, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(314000, 0)
    OP_6E(334, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x010E,
        (
            '#0330360748V#843F#5P原来如此……这样的情况啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330360749V#842F的确需要兵分两路\n',
            '来迅速解决目前的事态才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0310360750V#824F#5P这么一来就有１０个人了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310360751V#820F分成正面６人、\n',
            '后方４人应该可以吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360752V#053F嗯，比较妥当。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360753V#051F问题在于\n',
            '要如何分组……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360754V#1004F啊，既然这样，\n',
            '我就从后方突袭吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360755V#1016F因为这个学院\n',
            '我比其它人要都熟悉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360756V#1035F我也一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360757V#1040F毕竟刚刚才\n',
            '潜入侦查过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360758V#1310F#5P那么我也加入\n',
            '后方的突袭组吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360759V#811F之前和艾丝蒂尔\n',
            '约定要一起作战的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360760V#1025F亚妮拉丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030360761V#020F从隐蔽性方面考虑\n',
            '确实是十分合适。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840026V#026F不过，你们３个\n',
            '都是近身作战的类型……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030360762V#027F要有个能做后援\n',
            '的人同行就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360763V#843F#5P那就让我来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330360764V#841F我应该可以用方术\n',
            '支持艾丝蒂尔他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360765V#1011F克鲁茨前辈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340430V#1040F拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360767V#051F哦，看来决定了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050360768V#052F说到这个，卡露娜……\n',
            '你的武器没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320360769V#833F#5P啊啊，导力枪是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320360770V#835F确实是伤脑筋，\n',
            '所以我准备了这个东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 17)
    SetChrSubChip(0x0008, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360771V#1004F那、那么大一把枪是！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070360772V#064F啊，那个难不成是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320360773V#831F#5P呵呵，是莱恩福尔特社\n',
            '制造的火药式突击步枪哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320360774V原本是武器店的爱珐小姐\n',
            '所收藏的古董。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320360775V被我强行借来使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050360776V#051F这实在是难得一见的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030360777V#027F没记错的话，火药式的枪\n',
            '现在根本见不到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0107, 400)
    Sleep(300)

    ChrTalk(
        0x0103,
        (
            '#0030360778V#023F#2P对了，提妲用的也是\n',
            '火药式的机关炮吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0103, 400)
    Sleep(300)

    ChrTalk(
        0x0107,
        (
            '#0070360779V#061F#6P嘿嘿，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070360780V#560F爷爷借给我的\n',
            '珍贵收藏品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E19')
    def lambda_2E19():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2E19)

    Sleep(100)

    OP_8C(0x0107, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#0320360781V#833F#5P老实说，和导力枪相比…\n',
            '不但很重，子弹也耗尽得很快，\n',
            '使用起来十分不方便呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320360782V#830F不过威力不容小觑，\n',
            '应该足够用于实战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080360783V#074F#4P唔，那么正面的\n',
            '佯攻组看来也没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080360784V#070F立刻开始作战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360785V#1018FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360786V#816F#5P加油！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(ChrTable['克鲁茨'], 0x00, 79)
    SetChrStatus(ChrTable['克鲁茨'], 0xFE, 0)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['风神雷神'], 0xFF)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['树脂装甲'], 0xFF)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['斯托雷加Ｇ'], 0xFF)
    OP_37(0x0D, 0x7F, 0x02)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['ＥＰ３'], 0x00)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['ＨＰ３'], 0x02)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['省ＥＰ３'], 0x03)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['攻击３'], 0x04)
    EquipCmd(ChrTable['克鲁茨'], ItemTable['防御３'], 0x05)
    AddCraft(ChrTable['克鲁茨'], 0x0000)
    OP_BB(0x0D, 0x06, 0x00000118)
    EquipCmd(ChrTable['亚妮拉丝'], 0x0000, 0xFF)
    SetChrStatus(ChrTable['亚妮拉丝'], 0x00, 77)
    SetChrStatus(ChrTable['亚妮拉丝'], 0xFE, 0)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['青龙剑'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['树脂装甲'], 0xFF)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['斯托雷加Ｇ'], 0xFF)
    OP_37(0x09, 0x7F, 0x02)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['妨害３'], 0x00)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['省ＥＰ３'], 0x01)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['防御３'], 0x02)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['回避２'], 0x04)
    EquipCmd(ChrTable['亚妮拉丝'], ItemTable['ＨＰ３'], 0x05)
    AddCraft(ChrTable['亚妮拉丝'], 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A3(0x0000)
    def _loc_3002(): pass

    label('loc_3002')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3235',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　更换队员，进行必要的装备变更，\n',
            '　确定后，请选择【继续】。\n',
            '　艾丝蒂尔，约修亚，亚妮拉丝，克鲁茨组队前进。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
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
            TXT(0x00, '【编成队伍】\n'),
            TXT(0x01, '【变更装备】\n'),
            TXT(0x02, '【继续】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_316B',
    )

    OP_A2(0x0000)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行暂时的队伍编组。\n',
            '　可以卸下其它同伴的装备给\n',
            '　亚妮拉丝等人装配。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

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
            0x0009,
            0x000D,
            0xFFFF,
        ),
    )

    Jump('loc_3232')

    def _loc_316B(): pass

    label('loc_316B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_31A4',
    )

    OP_C0(0x13, 0x00000078, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)

    Jump('loc_31CF')

    def _loc_31A4(): pass

    label('loc_31A4')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的编组之后再选择。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(100)

    def _loc_31CF(): pass

    label('loc_31CF')

    Jump('loc_3232')

    def _loc_31D2(): pass

    label('loc_31D2')

    SetChrName('')

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '※可以继续剧情了吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3232',
    )

    Jump('loc_3235')

    def _loc_3232(): pass

    label('loc_3232')

    Jump('loc_3002')

    def _loc_3235(): pass

    label('loc_3235')

    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，协会的学院解放作战开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特，雪拉扎德，金，\n',
            '卡露娜，库拉茨，提妲６人\n',
            '从正面将强化猎兵引诱出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔，约修亚，亚妮拉丝，克鲁茨\n',
            '则是负责从背后突袭并解放人质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)

    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    FormationAddMember(ChrTable['约修亚'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['亚妮拉丝'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['克鲁茨'], 0xF9, 0xFF)

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3342',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_3342(): pass

    label('loc_3342')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_335D',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_335D(): pass

    label('loc_335D')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3378',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_3378(): pass

    label('loc_3378')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3393',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_3393(): pass

    label('loc_3393')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33AE',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_33AE(): pass

    label('loc_33AE')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33C9',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_33C9(): pass

    label('loc_33C9')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33E4',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_33E4(): pass

    label('loc_33E4')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33FF',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0001)

    def _loc_33FF(): pass

    label('loc_33FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_346B',
    )

    Sleep(300)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※待命的成员\n',
            '　装备着『零力场发生器』。\n',
            '　将其回收加入队伍的携带品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_346B(): pass

    label('loc_346B')

    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x3478
@scena.Code('func_08_3478')
def func_08_3478():
    OP_8F(0x00FE, 233700, 0, -21900, 2000, 0x00)
    OP_8C(0x00FE, 315, 400)

    Return()

# id: 0x0009 offset: 0x3494
@scena.Code('func_09_3494')
def func_09_3494():
    OP_8F(0x00FE, 233290, 20, -18440, 2000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x000A offset: 0x34B0
@scena.Code('func_0A_34B0')
def func_0A_34B0():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 231280, -10, -19280, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000B offset: 0x34D1
@scena.Code('func_0B_34D1')
def func_0B_34D1():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 231370, 20, -20800, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000C offset: 0x34F2
@scena.Code('func_0C_34F2')
def func_0C_34F2():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 229880, 10, -20490, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000D offset: 0x3513
@scena.Code('func_0D_3513')
def func_0D_3513():
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 229790, 10, -18850, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x000E offset: 0x3534
@scena.Code('func_0E_3534')
def func_0E_3534():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_D2(0x00070239, 0x00070245, 0x11)
    OP_D2(0x002601B3, 0x002601B8, 0x12)
    OP_D2(0x00290143, 0x00290147, 0x14)
    OP_D2(0x00290145, 0x00290149, 0x15)
    OP_D2(0x00070218, 0x00070224, 0x16)
    OP_D2(0x000701D0, 0x000701DC, 0x17)
    OP_D2(0x00070248, 0x00070254, 0x18)
    OP_D2(0x0007026E, 0x00070275, 0x19)
    FormationAddMember(ChrTable['提妲'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['阿加特'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['雪拉扎德'], 0xFF, 0xFF)
    FormationAddMember(ChrTable['金'], 0xFF, 0xFF)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    OP_6D(256990, 0, -10720, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(2230, 0)
    OP_6C(45000, 0)
    OP_6E(317, 0)
    SetChrPos(0x000A, 269300, 700, -11440, 270)
    SetChrPos(0x000B, 269300, 700, -9000, 270)
    SetChrPos(0x000C, 272070, 700, -12200, 270)
    SetChrPos(0x000D, 272290, 700, -7890, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x0107, 256170, 0, -10610, 90)
    SetChrPos(0x0008, 256370, -10, -11780, 90)
    SetChrPos(0x0009, 254450, 10, -8039, 90)
    SetChrPos(0x0106, 255080, 10, -9150, 90)
    SetChrPos(0x0103, 254000, -30, -12610, 90)
    SetChrPos(0x0108, 254810, 0, -13860, 90)
    SetChrChipByIndex(0x0107, 17)
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 18)
    SetChrSubChip(0x0008, 4)
    SetChrChipByIndex(0x0106, 22)
    SetChrChipByIndex(0x0103, 23)
    SetChrChipByIndex(0x0108, 24)
    SetChrChipByIndex(0x0009, 25)
    SetChrSubChip(0x0106, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x0108, 0)
    SetChrSubChip(0x0009, 0)
    LoadEffect(0x00, 'scraft\\\\sc006_01.eff')
    LoadEffect(0x01, 'scraft\\\\sc006_02.eff')
    LoadEffect(0x02, 'scraft\\\\sc006_03.eff')
    LoadEffect(0x03, 'monster\\\\msc0310.eff')
    LoadEffect(0x04, 'battle\\\\btbomb00.eff')
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x0000, 246450, -10, -8780, 0)

    @scena.Lambda('lambda_3780')
    def lambda_3780():
        OP_99(0x0107, 0x00, 0x07, 0x00000FA0)
        Yield()

        Jump('lambda_3780')

    DispatchAsync2(0x0107, 0x0000, lambda_3780)

    PlayEffect(0x00, 0x00, 0x0107, 0, -300, 300, 90, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x01, 0x0107, 0, 500, 300, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0008, 0x01, 0x00, 0x000F)
    CreateThread(0x0008, 0x02, 0x00, 0x0014)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    @scena.Lambda('lambda_381A')
    def lambda_381A():
        OP_6D(269830, 60, -9380, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_381A)

    @scena.Lambda('lambda_3832')
    def lambda_3832():
        OP_67(0, 10620, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3832)

    @scena.Lambda('lambda_384A')
    def lambda_384A():
        OP_6B(2480, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_384A)

    Sleep(1000)

    CreateThread(0x000A, 0x02, 0x00, 0x0010)
    CreateThread(0x000B, 0x02, 0x00, 0x0011)
    CreateThread(0x000C, 0x02, 0x00, 0x0012)
    CreateThread(0x000D, 0x02, 0x00, 0x0013)
    Sleep(1500)

    Sleep(500)

    Sleep(1000)

    Sleep(500)

    Sleep(1000)

    SetMapFlags(0x02000000)
    OP_A2(0x201F)
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x07, 0xFF)
    OP_DC()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T2500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x38BB
@scena.Code('func_0F_38BB')
def func_0F_38BB():
    @scena.Lambda('lambda_38C1')
    def lambda_38C1():
        OP_99(0x0008, 0x04, 0x05, 0x000009C4)
        Yield()

        Jump('lambda_38C1')

    DispatchAsync2(0x0107, 0x0001, lambda_38C1)

    PlayEffect(0x03, 0x02, 0x0008, -100, 650, 1300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0x03, 0x0008, 0, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0010 offset: 0x3939
@scena.Code('func_10_3939')
def func_10_3939():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_39A1',
    )

    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 21)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    OP_8C(0x00FE, 270, 0)

    @scena.Lambda('lambda_396A')
    def lambda_396A():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_396A')

    DispatchAsync2(0x00FE, 0x0003, lambda_396A)

    OP_91(0x00FE, 60, 0, -10, 10000, 0x00)
    TerminateThread(0x00FE, 0x03)
    Sleep(300)

    Jump('func_10_3939')

    def _loc_39A1(): pass

    label('loc_39A1')

    Return()

# id: 0x0011 offset: 0x39A2
@scena.Code('func_11_39A2')
def func_11_39A2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A0A',
    )

    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 21)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    OP_8C(0x00FE, 270, 0)

    @scena.Lambda('lambda_39D3')
    def lambda_39D3():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_39D3')

    DispatchAsync2(0x00FE, 0x0003, lambda_39D3)

    OP_91(0x00FE, 50, 0, 10, 10000, 0x00)
    TerminateThread(0x00FE, 0x03)
    Sleep(100)

    Jump('func_11_39A2')

    def _loc_3A0A(): pass

    label('loc_3A0A')

    Return()

# id: 0x0012 offset: 0x3A0B
@scena.Code('func_12_3A0B')
def func_12_3A0B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A73',
    )

    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 21)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    OP_8C(0x00FE, 270, 0)

    @scena.Lambda('lambda_3A3C')
    def lambda_3A3C():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_3A3C')

    DispatchAsync2(0x00FE, 0x0003, lambda_3A3C)

    OP_91(0x00FE, 50, 0, -10, 10000, 0x00)
    TerminateThread(0x00FE, 0x03)
    Sleep(200)

    Jump('func_12_3A0B')

    def _loc_3A73(): pass

    label('loc_3A73')

    Return()

# id: 0x0013 offset: 0x3A74
@scena.Code('func_13_3A74')
def func_13_3A74():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3ADC',
    )

    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 21)
    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    OP_8C(0x00FE, 270, 0)

    @scena.Lambda('lambda_3AA5')
    def lambda_3AA5():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00001388, 0x000007D0)
        Yield()

        Jump('lambda_3AA5')

    DispatchAsync2(0x00FE, 0x0003, lambda_3AA5)

    OP_91(0x00FE, 110, 0, 10, 10000, 0x00)
    TerminateThread(0x00FE, 0x03)
    Sleep(250)

    Jump('func_13_3A74')

    def _loc_3ADC(): pass

    label('loc_3ADC')

    Return()

# id: 0x0014 offset: 0x3ADD
@scena.Code('func_14_3ADD')
def func_14_3ADD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_40A9',
    )

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
        'loc_3BE5',
    )

    PlayEffect(0x01, 0x04, 0x000A, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x05, 0x000C, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x06, 0x00FF, 265880, 0, -10420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x07, 0x000B, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_40A1')

    def _loc_3BE5(): pass

    label('loc_3BE5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CD8',
    )

    PlayEffect(0x01, 0x04, 0x000B, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x05, 0x00FF, 266880, 0, -8420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x06, 0x000D, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x07, 0x000A, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_40A1')

    def _loc_3CD8(): pass

    label('loc_3CD8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DCB',
    )

    PlayEffect(0x01, 0x04, 0x000C, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x05, 0x00FF, 273220, 0, -9550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x06, 0x00FF, 273220, 0, -6550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x07, 0x00FF, 274220, 0, -8550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_40A1')

    def _loc_3DCB(): pass

    label('loc_3DCB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EBE',
    )

    PlayEffect(0x01, 0x04, 0x000D, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x05, 0x000A, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x06, 0x00FF, 268880, 0, -9420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x07, 0x000B, 0, 300, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_40A1')

    def _loc_3EBE(): pass

    label('loc_3EBE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FB1',
    )

    PlayEffect(0x01, 0x04, 0x00FF, 268880, 100, -9420, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x05, 0x000B, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x04, 0x000A, 0, 400, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x05, 0x000C, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Jump('loc_40A1')

    def _loc_3FB1(): pass

    label('loc_3FB1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40A1',
    )

    PlayEffect(0x01, 0x04, 0x00FF, 275220, 0, -8550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x04, 0x000D, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x04, 0x000A, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    PlayEffect(0x01, 0x06, 0x00FF, 274220, 0, -5550, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_40A1(): pass

    label('loc_40A1')

    Sleep(100)

    Jump('func_14_3ADD')

    def _loc_40A9(): pass

    label('loc_40A9')

    Return()

# id: 0x0015 offset: 0x40AA
@scena.Code('func_15_40AA')
def func_15_40AA():
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
        (0x00000000, 'loc_4124'),
        (0x00000001, 'loc_412A'),
        (-1, 'loc_4130'),
    )

    def _loc_4124(): pass

    label('loc_4124')

    OP_A2(0x1200)

    Jump('loc_4130')

    def _loc_412A(): pass

    label('loc_412A')

    OP_A2(0x1201)

    Jump('loc_4130')

    def _loc_4130(): pass

    label('loc_4130')

    Return()

# id: 0x0016 offset: 0x4131
@scena.Code('func_16_4131')
def func_16_4131():
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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
