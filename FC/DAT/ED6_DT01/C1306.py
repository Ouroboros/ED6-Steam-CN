import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1306_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1306   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '空贼阿伦'),
    TXT(0x02, '空贼洛西'),
    TXT(0x03, '空贼蒂诺'),
    TXT(0x04, '空贼雷古'),
    TXT(0x05, '空贼'),
    TXT(0x06, '空贼'),
    TXT(0x07, '空贼'),
    TXT(0x08, '空贼'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1306.x'
    header.mapIndex       = 52
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1977
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
            word_3A         = 52,
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
        ('ED6_DT07/CH00360._CH', 'ED6_DT07/CH00360P._CP'),
        ('ED6_DT07/CH00364._CH', 'ED6_DT07/CH00364P._CP'),
        ('ED6_DT07/CH00361._CH', 'ED6_DT07/CH00361P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT09/CH10380._CH', 'ED6_DT09/CH10380P._CP'),
        ('ED6_DT09/CH10381._CH', 'ED6_DT09/CH10381P._CP'),
        ('ED6_DT09/CH10390._CH', 'ED6_DT09/CH10390P._CP'),
        ('ED6_DT09/CH10391._CH', 'ED6_DT09/CH10391P._CP'),
        ('ED6_DT09/CH10250._CH', 'ED6_DT09/CH10250P._CP'),
        ('ED6_DT09/CH10251._CH', 'ED6_DT09/CH10251P._CP'),
        ('ED6_DT06/CH20074._CH', 'ED6_DT06/CH20074P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 800,
            z                   = 500,
            y                   = 500,
            direction           = 180,
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
            x                   = -1000,
            z                   = 500,
            y                   = -2800,
            direction           = 180,
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
            x                   = -3200,
            z                   = 500,
            y                   = -700,
            direction           = 180,
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
            x                   = -500,
            z                   = 500,
            y                   = 900,
            direction           = 180,
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
            x                   = -500,
            z                   = 500,
            y                   = 900,
            direction           = 180,
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
            x                   = -3200,
            z                   = 500,
            y                   = -700,
            direction           = 180,
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
            x                   = -2300,
            z                   = 500,
            y                   = -2700,
            direction           = 180,
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
            x                   = 1000,
            z                   = 500,
            y                   = -1900,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x21A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -57220,
            z           = 0,
            y           = -50730,
            word_0C     = 0x00B3,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00A6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -7780,
            z           = 0,
            y           = 56000,
            word_0C     = 0x0105,
            word_0E     = 0x000B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00AA,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 53910,
            z           = 0,
            y           = 56840,
            word_0C     = 0x007B,
            word_0E     = 0x000B,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00AB,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 104400,
            z           = 0,
            y           = 10510,
            word_0C     = 0x014B,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00AB,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
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
        ScenaActorData(
            triggerX            = -1020,
            triggerZ            = 0,
            triggerY            = -145940,
            triggerRange        = 800,
            actorX              = -1020,
            actorZ              = 1000,
            actorY              = -145940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -57350,
            triggerZ            = 0,
            triggerY            = 108350,
            triggerRange        = 800,
            actorX              = -57350,
            actorZ              = 1000,
            actorY              = 108350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -142790,
            triggerZ            = 0,
            triggerY            = 58560,
            triggerRange        = 1000,
            actorX              = -142760,
            actorZ              = 1500,
            actorY              = 59200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -55470,
            triggerZ            = 0,
            triggerY            = -105270,
            triggerRange        = 1000,
            actorX              = -54920,
            actorZ              = 1500,
            actorY              = -105280,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x31A
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_32E'),
        (0x00000083, 'loc_340'),
        (0x00000065, 'loc_353'),
        (-1, 'loc_366'),
    )

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 4, 0x354)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33D',
    )

    SetScenaFlags(ScenaFlag(0x006A, 4, 0x354))
    Event(0, 0x0003)

    def _loc_33D(): pass

    label('loc_33D')

    Jump('loc_366')

    def _loc_340(): pass

    label('loc_340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 1, 0x359)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_350',
    )

    Event(0, 0x000A)

    def _loc_350(): pass

    label('loc_350')

    Jump('loc_366')

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 0, 0x358)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 2, 0x35A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_363',
    )

    Event(0, 0x000B)

    def _loc_363(): pass

    label('loc_363')

    Jump('loc_366')

    def _loc_366(): pass

    label('loc_366')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 1, 0x359)),
            Expr.Return,
        ),
        'loc_429',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000D, 0x0800)
    SetChrFlags(0x000E, 0x0800)
    SetChrPos(0x000A, 56490, 0, -52990, 350)
    SetChrPos(0x000B, 56660, 0, -56070, 0)
    SetChrPos(0x000D, 55510, 0, -54710, 45)
    SetChrPos(0x000E, 55110, 0, -52150, 90)
    SetChrChipByIndex(0x000B, 13)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 13)
    SetChrChipByIndex(0x000A, 13)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000A, 0xFF)

    def _loc_429(): pass

    label('loc_429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 2, 0x35A)),
            Expr.Return,
        ),
        'loc_4EC',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    SetChrFlags(0x000F, 0x0800)
    SetChrPos(0x0008, 940, 0, -770, 0)
    SetChrPos(0x0009, 930, 0, -3680, 90)
    SetChrPos(0x000C, 510, 0, -2250, 300)
    SetChrPos(0x000F, 500, 0, 580, 45)
    SetChrChipByIndex(0x000C, 13)
    SetChrChipByIndex(0x000F, 13)
    SetChrChipByIndex(0x0008, 13)
    SetChrChipByIndex(0x0009, 13)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)

    def _loc_4EC(): pass

    label('loc_4EC')

    Return()

# id: 0x0001 offset: 0x4ED
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 6, 0x356)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_509',
    )

    OP_1B(0x26, 0x00, 0x0008)
    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)

    Jump('loc_50D')

    def _loc_509(): pass

    label('loc_509')

    OP_64(0x00, 0x0001)

    def _loc_50D(): pass

    label('loc_50D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 0, 0x370)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_526')

    def _loc_51F(): pass

    label('loc_51F')

    OP_6F(0x0002, 60)

    def _loc_526(): pass

    label('loc_526')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 1, 0x371)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_538',
    )

    OP_6F(0x0003, 0)

    Jump('loc_53F')

    def _loc_538(): pass

    label('loc_538')

    OP_6F(0x0003, 60)

    def _loc_53F(): pass

    label('loc_53F')

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_54E',
    )

    OP_64(0x01, 0x0001)

    def _loc_54E(): pass

    label('loc_54E')

    Return()

# id: 0x0002 offset: 0x54F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_564',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_564(): pass

    label('loc_564')

    Return()

# id: 0x0003 offset: 0x565
@scena.Code('func_03_565')
def func_03_565():
    EventBegin(0x00)
    CameraMove(3220, 1250, 4120, 0)
    SetChrPos(0x0101, 5490, 3500, 5190, 270)
    SetChrPos(0x0102, 5490, 3500, 5190, 270)
    SetChrPos(0x0103, 5490, 3500, 5190, 270)
    SetChrPos(0x0104, 5490, 3500, 5190, 270)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x0104, 0x0080)

    @scena.Lambda('lambda_05D6')
    def lambda_05D6():
        CameraMove(3150, 0, 510, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05D6)

    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    CreateThread(0x0102, 0x01, 0x00, 0x0005)
    CreateThread(0x0103, 0x01, 0x00, 0x0006)
    CreateThread(0x0104, 0x01, 0x00, 0x0007)
    WaitForThreadExit(0x0104, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010031450V#002F说起来……\n',
            '这里到底是个什么地方啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031451V就算是他们建的基地，\n',
            '也未免太大、太古老了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    ChrTalk(
        0x0103,
        (
            '#0030031452V#020F应该是古时候残存下来的堡垒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031453V空贼团发现这里之后，\n',
            '当作是自己的基地来用了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031454V#030F『大崩坏』之后，\n',
            '整个世界可是持续了数百年的战乱啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031455V有这样大规模的堡垒残留下来，\n',
            '也没什么不可思议的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031456V#004F『大崩坏』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031457V#012F就是距今１２００年前\n',
            '所发生的古代塞姆里亚文明崩溃。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031458V传说是因为天地异变造成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031459V#501F啊，之前亚鲁瓦教授也说过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031460V#027F把这种地方用作自己的基地，\n',
            '空贼还真是完全没品位可言呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031461V#027F不仅四周有魔兽游荡……\n',
            '而且充满男人的臭汗味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031462V#018F我说雪拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031463V#034F这还真是激烈又极端的看法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x930
@scena.Code('func_04_930')
def func_04_930():
    ClearChrFlags(0x0101, 0x0080)
    ChrWalkTo(0x00FE, 3027, 2000, 4693, 5000, 0x00)
    ChrWalkTo(0x00FE, 2740, 0, -1190, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0102, 400)

    Return()

# id: 0x0005 offset: 0x965
@scena.Code('func_05_965')
def func_05_965():
    Sleep(800)

    ClearChrFlags(0x0102, 0x0080)
    ChrWalkTo(0x00FE, 3027, 2000, 4693, 3000, 0x00)
    ChrWalkTo(0x00FE, 2690, 0, 880, 3000, 0x00)
    ChrWalkTo(0x00FE, 1830, 0, 110, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0006 offset: 0x9B3
@scena.Code('func_06_9B3')
def func_06_9B3():
    Sleep(1600)

    ClearChrFlags(0x0103, 0x0080)
    ChrWalkTo(0x00FE, 3027, 2000, 4693, 3000, 0x00)
    ChrWalkTo(0x00FE, 3355, 0, 200, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0007 offset: 0x9ED
@scena.Code('func_07_9ED')
def func_07_9ED():
    Sleep(2400)

    ClearChrFlags(0x0104, 0x0080)
    ChrWalkTo(0x00FE, 3027, 2000, 4693, 3000, 0x00)
    ChrWalkTo(0x00FE, 2690, 0, 880, 3000, 0x00)

    Return()

# id: 0x0008 offset: 0xA20
@scena.Code('func_08_A20')
def func_08_A20():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 6, 0x356)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BE6',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_B0D',
    )

    @scena.Lambda('lambda_0A4A')
    def lambda_0A4A():
        CameraMove(-4700, 0, -147260, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0A4A)

    Sleep(600)

    SetChrDirection(0x0102, 90, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031465V#012F等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031466V从那道门可以听到说话的声音。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AB2')
    def lambda_0AB2():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0AB2)

    @scena.Lambda('lambda_0AC0')
    def lambda_0AC0():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AC0)

    SetChrDirection(0x0103, 90, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031467V#022F看起来空贼就在这里呢。\n',
            '先把他们解决掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BCB')

    def _loc_B0D(): pass

    label('loc_B0D')

    @scena.Lambda('lambda_0B13')
    def lambda_0B13():
        CameraMove(-4700, 0, -147260, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0B13)

    Sleep(600)

    SetChrDirection(0x0104, 90, 400)

    ChrTalk(
        0x0104,
        (
            '#0040031468V#033F哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031469V从那道门可以听到说话的声音呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B7B')
    def lambda_0B7B():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0B7B)

    @scena.Lambda('lambda_0B89')
    def lambda_0B89():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B89)

    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031470V#002F难道是空贼？\n',
            '那先把这里解决掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCB(): pass

    label('loc_BCB')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_BE6(): pass

    label('loc_BE6')

    Return()

# id: 0x0009 offset: 0xBE7
@scena.Code('func_09_BE7')
def func_09_BE7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 6, 0x356)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CE0',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有男人说话的声音传出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020031464V#012F又有说话声。\n',
            '……要闯进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【闯进去】\n'),
            TXT(0x01, '【还是算了】\n'),
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
        (0x00000001, 'loc_CCC'),
        (0x00000000, 'loc_CD1'),
        (-1, 'loc_CE0'),
    )

    def _loc_CCC(): pass

    label('loc_CCC')

    EventEnd(0x01)

    Jump('loc_CE0')

    def _loc_CD1(): pass

    label('loc_CD1')

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C1304._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_CE0')

    def _loc_CE0(): pass

    label('loc_CE0')

    Return()

# id: 0x000A offset: 0xCE1
@scena.Code('func_0A_CE1')
def func_0A_CE1():
    EventBegin(0x00)
    CameraMove(59090, 0, -54570, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000A, 57770, 0, -52340, 180)
    SetChrPos(0x000B, 59050, 0, -52450, 180)
    SetChrPos(0x000D, 60650, 0, -51550, 180)
    SetChrPos(0x000E, 56680, 0, -51410, 180)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0101, 58000, 0, -56220, 0)
    SetChrPos(0x0102, 57090, 0, -57040, 0)
    SetChrPos(0x0103, 59130, 0, -56480, 0)
    SetChrPos(0x0104, 59940, 0, -57280, 0)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 4)
    SetChrChipByIndex(0x0103, 5)
    SetChrChipByIndex(0x0104, 6)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#1040031687V给我站住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1050031688V有我们在，你们休想通过这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031689V#004F已、已经醒过来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031690V#012F很顽强的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031691V#024F呼，既然不听劝，\n',
            '就别怪我们动用武力了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    SetChrChipByIndex(0x000B, 2)
    SetChrChipByIndex(0x000A, 2)
    SetChrChipByIndex(0x000D, 2)
    SetChrChipByIndex(0x000E, 2)

    @scena.Lambda('lambda_0EBA')
    def lambda_0EBA():
        ChrWalkTo(0x00FE, 58020, 0, -78470, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0EBA)

    @scena.Lambda('lambda_0ED5')
    def lambda_0ED5():
        ChrWalkTo(0x00FE, 58020, 0, -78470, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0ED5)

    @scena.Lambda('lambda_0EF0')
    def lambda_0EF0():
        ChrWalkTo(0x00FE, 58020, 0, -78470, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0EF0)

    @scena.Lambda('lambda_0F0B')
    def lambda_0F0B():
        ChrWalkTo(0x00FE, 58020, 0, -78470, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0F0B)

    Sleep(400)

    Battle(0x0000038D, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_F3E'),
        (-1, 'loc_F41'),
    )

    def _loc_F3E(): pass

    label('loc_F3E')

    OP_B4(0x00)

    Return()

    def _loc_F41(): pass

    label('loc_F41')

    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000D, 0x0800)
    SetChrFlags(0x000E, 0x0800)
    SetChrPos(0x000A, 56490, 0, -52990, 350)
    SetChrPos(0x000B, 56660, 0, -56070, 0)
    SetChrPos(0x000D, 55510, 0, -54710, 45)
    SetChrPos(0x000E, 55110, 0, -52150, 90)
    SetChrChipByIndex(0x000B, 13)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 13)
    SetChrChipByIndex(0x000A, 13)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x0104, 65535)
    SetChrPos(0x0101, 58700, 0, -53950, 270)
    SetChrPos(0x0102, 58700, 0, -53950, 270)
    SetChrPos(0x0103, 58700, 0, -53950, 270)
    SetChrPos(0x0104, 58700, 0, -53950, 270)
    CameraMove(58700, 0, -53950, 0)
    CameraSetDistance(2600, 0)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x006B, 1, 0x359))
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x107A
@scena.Code('func_0B_107A')
def func_0B_107A():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(2880, 0, -3610, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 2970, 0, -700, 180)
    SetChrPos(0x0009, 1580, 0, -1100, 180)
    SetChrPos(0x000C, 3050, 0, 910, 180)
    SetChrPos(0x000F, 1640, 0, 500, 180)
    SetChrPos(0x0101, 1560, 0, -5690, 0)
    SetChrPos(0x0102, 510, 0, -6570, 0)
    SetChrPos(0x0103, 2530, 0, -5860, 0)
    SetChrPos(0x0104, 3240, 0, -6510, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrChipByIndex(0x0101, 3)
    SetChrChipByIndex(0x0102, 4)
    SetChrChipByIndex(0x0103, 5)
    SetChrChipByIndex(0x0104, 6)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1250031692V哼！\n',
            '别想再上去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1260031693V快点带着人质滚吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031694V#007F又来了……\n',
            '真是不知悔改的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031695V#012F为了让首领逃跑，\n',
            '打算这样拖延时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1260031696V哈，我们平时受到\n',
            '大哥他们很多的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1250031697V这回是报恩的时候了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetChrChipByIndex(0x000C, 2)
    SetChrChipByIndex(0x000F, 2)
    SetChrChipByIndex(0x0008, 2)
    SetChrChipByIndex(0x0009, 2)

    @scena.Lambda('lambda_1293')
    def lambda_1293():
        ChrWalkTo(0x00FE, 1840, 0, -15030, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1293)

    @scena.Lambda('lambda_12AE')
    def lambda_12AE():
        ChrWalkTo(0x00FE, 1840, 0, -15030, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_12AE)

    @scena.Lambda('lambda_12C9')
    def lambda_12C9():
        ChrWalkTo(0x00FE, 1840, 0, -15030, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_12C9)

    @scena.Lambda('lambda_12E4')
    def lambda_12E4():
        ChrWalkTo(0x00FE, 1840, 0, -15030, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_12E4)

    Sleep(500)

    Battle(0x0000038E, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1317'),
        (-1, 'loc_131A'),
    )

    def _loc_1317(): pass

    label('loc_1317')

    OP_B4(0x00)

    Return()

    def _loc_131A(): pass

    label('loc_131A')

    SetChrPos(0x0008, 940, 0, -770, 0)
    SetChrPos(0x0009, 930, 0, -3680, 90)
    SetChrPos(0x000C, 510, 0, -2250, 300)
    SetChrPos(0x000F, 500, 0, 580, 45)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    SetChrFlags(0x000F, 0x0800)
    SetChrChipByIndex(0x000C, 13)
    SetChrChipByIndex(0x000F, 13)
    SetChrChipByIndex(0x0008, 13)
    SetChrChipByIndex(0x0009, 13)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    SetChrPos(0x0101, 3010, 0, -1740, 270)
    SetChrPos(0x0102, 3010, 0, -1740, 270)
    SetChrPos(0x0103, 3010, 0, -1740, 270)
    SetChrPos(0x0104, 3010, 0, -1740, 270)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x0104, 65535)
    CameraMove(3010, 0, -1740, 0)
    CameraSetDistance(2600, 0)
    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x006B, 2, 0x35A))
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x1453
@scena.Code('func_0C_1453')
def func_0C_1453():
    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16F0',
    )

    SetMapFlags(0x08000000)
    EventBegin(0x01)
    Fade(1000)
    SetChrPos(0x0101, -56980, 0, 107430, 0)
    SetChrPos(0x0102, -57900, 0, 106910, 0)
    SetChrPos(0x0103, -57000, 0, 105940, 0)
    SetChrPos(0x0104, -57970, 0, 105640, 0)
    OP_0D()
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010151345V#501F这是什么…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151346V#010F是导力吸尘器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151347V而且好像还是最新型号的，\n',
            '也许是被偷来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151348V#501F呼～原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151349V#004F……咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151350V那是什么啊？\n',
            '吸尘器盖子上夹着什么东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '黑色笔记本',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x0014, 0x01, 0x8000)
    AddItem(0x0338, 1)
    OP_64(0x01, 0x0001)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020151351V#014F这是……笔记本？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151352V#505F嗯，好像是呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151353V不过为什么吸尘器里面\n',
            '会有这种东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151354V#020F这东西的来头可能不简单。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151355V为了慎重起见，还是把它保管起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151356V#006F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(50)

    EventEnd(0x04)
    ClearMapFlags(0x08000000)

    def _loc_16F0(): pass

    label('loc_16F0')

    Return()

# id: 0x000D offset: 0x16F1
@scena.Code('func_0D_16F1')
def func_0D_16F1():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 0, 0x370)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17DB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x0060, 1)"),
            Expr.Return,
        ),
        'loc_1765',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '狩猎枪',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006E, 0, 0x370))

    Jump('loc_17D8')

    def _loc_1765(): pass

    label('loc_1765')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '狩猎枪',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '狩猎枪',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_17D8(): pass

    label('loc_17D8')

    Jump('loc_1811')

    def _loc_17DB(): pass

    label('loc_17DB')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x13)
    def _loc_1811(): pass

    label('loc_1811')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x181F
@scena.Code('func_0E_181F')
def func_0E_181F():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006E, 1, 0x371)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1915',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x0116, 1)"),
            Expr.Return,
        ),
        'loc_1897',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加Ｒ',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x006E, 1, 0x371))

    Jump('loc_1912')

    def _loc_1897(): pass

    label('loc_1897')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加Ｒ',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '斯托雷加Ｒ',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_1912(): pass

    label('loc_1912')

    Jump('loc_194B')

    def _loc_1915(): pass

    label('loc_1915')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x14)
    def _loc_194B(): pass

    label('loc_194B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
