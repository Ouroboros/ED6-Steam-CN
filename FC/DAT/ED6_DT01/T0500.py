import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵斯科特'),
    TXT(0x02, '士兵哈罗德'),
    TXT(0x03, '阿斯顿队长'),
    TXT(0x04, '士兵安托斯'),
    TXT(0x05, '士兵拉科斯'),
    TXT(0x06, '斯丁克'),
    TXT(0x07, '亚妮拉丝'),
    TXT(0x08, '士兵斯科特'),
    TXT(0x09, '士兵哈罗德'),
    TXT(0x0A, '艾丝蒂尔'),
    TXT(0x0B, '约修亚'),
    TXT(0x0C, '士兵斯科特'),
    TXT(0x0D, '士兵哈罗德'),
    TXT(0x0E, '艾丝蒂尔'),
    TXT(0x0F, '米尔西街道方向'),
    TXT(0x10, '东柏斯街道方向'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0500.x'
    header.mapIndex       = 18
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T0500._SN', 'ED6_DT01/T0500_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x292B
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
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 90,
            word_38         = 0,
            word_3A         = 18,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 135,
            word_32         = 0,
            word_34         = 360,
            word_36         = 90,
            word_38         = 0,
            word_3A         = 18,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00324._CH', 'ED6_DT07/CH00324P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00104P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
    ]

# id: 0x10002 offset: 0x136
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 2420,
            z                   = 0,
            y                   = -19010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 16920,
            z                   = 120,
            y                   = -7750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1400,
            z                   = 0,
            y                   = 21400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -3300,
            z                   = 0,
            y                   = 21400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 12900,
            z                   = 0,
            y                   = 4400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 5400,
            z                   = 0,
            y                   = 26700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -43000,
            z                   = 0,
            y                   = 42000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C9,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -1980,
            z                   = -410,
            y                   = -40440,
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
            x                   = 440,
            z                   = -510,
            y                   = 41850,
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

# id: 0x10003 offset: 0x336
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x336
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x336
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 5680,
            triggerZ            = -260,
            triggerY            = -27360,
            triggerRange        = 1500,
            actorX              = 5680,
            actorZ              = 1700,
            actorY              = -27360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9630,
            triggerZ            = -150,
            triggerY            = 27430,
            triggerRange        = 1500,
            actorX              = -9630,
            actorZ              = 1700,
            actorY              = 27430,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x37E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            Expr.Return,
        ),
        'loc_388',
    )

    Jump('loc_3AD')

    def _loc_388(): pass

    label('loc_388')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_397',
    )

    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_3AD')

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_3A1',
    )

    Jump('loc_3AD')

    def _loc_3A1(): pass

    label('loc_3A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_3AD',
    )

    ClearChrFlags(0x000E, 0x0080)

    def _loc_3AD(): pass

    label('loc_3AD')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_3B9'),
        (-1, 'loc_3C0'),
    )

    def _loc_3B9(): pass

    label('loc_3B9')

    Event(1, 0x0000)

    Jump('loc_3C0')

    def _loc_3C0(): pass

    label('loc_3C0')

    Return()

# id: 0x0001 offset: 0x3C1
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -129000, -127000, 196613)
    OP_72(0x0002, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 4, 0x36C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E7',
    )

    OP_6F(0x0002, 420)

    def _loc_3E7(): pass

    label('loc_3E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 4, 0x304)),
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 4, 0x36C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FF',
    )

    OP_6F(0x0001, 420)
    OP_72(0x0001, 0x0010)

    def _loc_3FF(): pass

    label('loc_3FF')

    Return()

# id: 0x0002 offset: 0x400
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_415',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_415(): pass

    label('loc_415')

    Return()

# id: 0x0003 offset: 0x416
@scena.Code('func_03_416')
def func_03_416():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_439',
    )

    OP_8D(0x00FE, 2000, 24900, 7200, 30100, 2000)

    Jump('func_03_416')

    def _loc_439(): pass

    label('loc_439')

    Return()

# id: 0x0004 offset: 0x43A
@scena.Code('func_04_43A')
def func_04_43A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_593',
    )

    Sleep(3000)

    SetChrDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 17290, -60, -24940, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, -21570, -120, -25580, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, -21690, -260, -29240, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 4090, -270, -28620, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 180, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 4180, -240, -30280, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 11280, -470, -30200, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 11290, 80, -10340, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 16950, 10, -10520, 2500, 0x00)
    Sleep(500)

    SetChrDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrWalkTo(0x00FE, 16920, 120, -7750, 2500, 0x00)

    Jump('func_04_43A')

    def _loc_593(): pass

    label('loc_593')

    Return()

# id: 0x0005 offset: 0x594
@scena.Code('func_05_594')
def func_05_594():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　洛连特市　１７２塞尔矩\n',
            '西　柏斯市　　４２０塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x5FC
@scena.Code('func_06_5FC')
def func_06_5FC():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　柏斯市　　４２０塞尔矩\n',
            '东　洛连特市　１７２塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x664
@scena.Code('func_07_664')
def func_07_664():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_F1C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 3, 0x303)),
            Expr.Return,
        ),
        'loc_C88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 4, 0x304)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C15',
    )

    EventBegin(0x00)
    OP_4A(0x0008, 0)
    Fade(1000)
    SetChrPos(0x0101, 2370, 0, -20490, 0)
    SetChrPos(0x0102, 3130, 0, -21420, 0)
    SetChrPos(0x0103, 1570, 0, -21630, 0)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_6C(45000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 2, 0x302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_972',
    )

    ChrTalk(
        0x00FE,
        (
            '#1120020299V哟，各位辛苦了。\n',
            '你们打算去柏斯吗？ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020300V#000F是的……\n',
            '你是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020301V像你们这样的旅行者，\n',
            '今天有很多从这里通过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020302V而且是平常通行量的好几倍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020303V#012F是因为柏斯上空\n',
            '实行了飞行管制的缘故吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020304V正是如此。\n',
            '搞得我现在忙死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020305V#027F要知道，\n',
            '实施飞行管制的是你们王国军队哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020306V难道你还有抱怨的立场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020307V唔，话虽如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020308V对了，\n',
            '这个关所也实行了通行管制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020309V想要通过的话，\n',
            '就到旁边的柜台向队长拿通行证吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020310V#000F啊，我们已经拿到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x032F, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '通行许可证',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x00FE,
        (
            '#1120020311V哦，还真是准备充分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A06')

    def _loc_972(): pass

    label('loc_972')

    ChrTalk(
        0x0101,
        (
            '#0010020312V#000F给，我们已经拿到通行证了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x032F, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '通行许可证',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x00FE,
        (
            '#1120020313V哦，真快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A06(): pass

    label('loc_A06')

    ChrTalk(
        0x00FE,
        (
            '#1120020314V那么就让你们通行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 270, 400)
    Sleep(500)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '士兵操作遥控装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    SetChrDirection(0x0101, 315, 400)
    SetChrDirection(0x0102, 315, 400)
    SetChrDirection(0x0103, 315, 400)
    Sleep(1000)

    @scena.Lambda('lambda_0A85')
    def lambda_0A85():
        CameraMove(-900, 0, -9960, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0A85)

    @scena.Lambda('lambda_0A9D')
    def lambda_0A9D():
        OP_6C(0, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0A9D)

    @scena.Lambda('lambda_0AAD')
    def lambda_0AAD():
        OP_67(0, 4000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0AAD)

    @scena.Lambda('lambda_0AC5')
    def lambda_0AC5():
        CameraSetDistance(5500, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_0AC5)

    Sleep(4000)

    PlaySE(208, 0x00, 0x64)
    OP_72(0x0001, 0x0800)
    OP_70(0x0001, 420)
    OP_73(0x0001)
    Sleep(1000)

    Fade(1000)
    CameraMove(2200, 0, -20370, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1120020315V好了，可以通过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)
    SetChrDirection(0x0102, 0, 400)
    SetChrDirection(0x0103, 0, 400)

    ChrTalk(
        0x00FE,
        (
            '#1120020316V顺便提一下，一旦过了这个关所，\n',
            '不拿到那一边的通行许可证\n',
            '是不能再回到这边来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020317V这件事请一定要注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020318V#000F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 0)
    EventEnd(0x00)
    OP_28(0x0052, 0x01, 0x0002)
    SetScenaFlags(ScenaFlag(0x0060, 4, 0x304))

    Jump('loc_C85')

    def _loc_C15(): pass

    label('loc_C15')

    ChrTalk(
        0x00FE,
        (
            '顺便提一下，一旦过了这个关所，\n',
            '不拿到那一边的通行许可证\n',
            '是不能再回到这边来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这件事请一定要注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_C85(): pass

    label('loc_C85')

    Jump('loc_F19')

    def _loc_C88(): pass

    label('loc_C88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 2, 0x302)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EB7',
    )

    EventBegin(0x00)

    ChrTalk(
        0x00FE,
        (
            '#1120020287V哟，各位辛苦了。\n',
            '你们打算去柏斯吗？ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020288V#000F是的……\n',
            '你是怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020289V像你们这样的旅行者，\n',
            '今天有很多从这里通过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020290V而且是平常通行量的好几倍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020291V#012F是因为柏斯上空\n',
            '实行了飞行管制的缘故吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020292V正是如此。\n',
            '搞得我现在忙死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020293V#027F要知道，\n',
            '实施飞行管制的是你们王国军队哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020294V难道你还有抱怨的立场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020295V唔，话虽如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020296V对了，\n',
            '这个关所也实行了通行管制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1120020297V想要通过的话，\n',
            '就到旁边的柜台向队长拿通行证吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020298V#000F知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0060, 2, 0x302))
    EventEnd(0x01)

    Jump('loc_F19')

    def _loc_EB7(): pass

    label('loc_EB7')

    ChrTalk(
        0x00FE,
        (
            '目前这个关所\n',
            '这个关所也实行了通行管制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要通过的话，\n',
            '就到旁边的柜台向队长拿通行证吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F19(): pass

    label('loc_F19')

    Jump('loc_13AA')

    def _loc_F1C(): pass

    label('loc_F1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_FEA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F78',
    )

    ChrTalk(
        0x00FE,
        (
            '旁边的柏斯地区\n',
            '最近连续发生了强盗案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是空贼干的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE7')

    def _loc_F78(): pass

    label('loc_F78')

    ChrTalk(
        0x00FE,
        (
            '旁边的柏斯地区\n',
            '最近连续发生了强盗案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是空贼干的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样，事先训练说不定能得到回报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FE7(): pass

    label('loc_FE7')

    Jump('loc_13AA')

    def _loc_FEA(): pass

    label('loc_FEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1173',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1079',
    )

    ChrTalk(
        0x00FE,
        (
            '不过也只能在这里说说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长在王都的总队中\n',
            '好像非常有威望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然被编配到这种地方来，\n',
            '是不是出什么事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1170')

    def _loc_1079(): pass

    label('loc_1079')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1130',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '队长在王都的总队中\n',
            '好像非常有威望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟然被编配到这种地方来，\n',
            '是不是出什么事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……说起来，\n',
            '一来就进行战斗训练也太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好痛，身子还是很痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1170')

    def _loc_1130(): pass

    label('loc_1130')

    ChrTalk(
        0x00FE,
        (
            '一来就进行战斗训练也太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好痛，身子还是很痛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1170(): pass

    label('loc_1170')

    Jump('loc_13AA')

    def _loc_1173(): pass

    label('loc_1173')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_12C6',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1265',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1213',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '今天也这样站了一天，\n',
            '通行的人还真的很少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，真无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无聊的时候就看看云的形状，\n',
            '然后就开始玩起联想游戏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1262')

    def _loc_1213(): pass

    label('loc_1213')

    ChrTalk(
        0x00FE,
        (
            '啊啊，真无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无聊的时候就看看云的形状，\n',
            '然后就开始玩起联想游戏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1262(): pass

    label('loc_1262')

    Jump('loc_12C3')

    def _loc_1265(): pass

    label('loc_1265')

    ChrTalk(
        0x00FE,
        (
            '虽然我很讨厌无聊，\n',
            '但是我更讨厌训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '训练完了之后\n',
            '浑身上下都痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好痛…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_12C3(): pass

    label('loc_12C3')

    Jump('loc_13AA')

    def _loc_12C6(): pass

    label('loc_12C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_13AA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1359',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '定期船开始运航之后，\n',
            '就基本没有人在街道上旅行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '就这样守卫关所也挺无聊的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有队长一个人干劲十足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AA')

    def _loc_1359(): pass

    label('loc_1359')

    ChrTalk(
        0x00FE,
        (
            '因为通行的人减少了，\n',
            '守卫关所也变得无聊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有队长一个人干劲十足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13AA(): pass

    label('loc_13AA')

    TalkEnd(0x0008)

    Return()

# id: 0x0008 offset: 0x13AE
@scena.Code('func_08_13AE')
def func_08_13AE():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1540',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 4, 0x29C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14B6',
    )

    SetScenaFlags(ScenaFlag(0x0053, 4, 0x29C))

    ChrTalk(
        0x00FE,
        (
            '自从我参军之后，\n',
            '还是第一次这么忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在可不是一边钓鱼，\n',
            '一边看书的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这本书刚买不久……\n',
            '就送给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是被队长发现了，\n',
            '又要挨骂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0213, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第２卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_153D')

    def _loc_14B6(): pass

    label('loc_14B6')

    ChrTalk(
        0x00FE,
        (
            '自从我参军之后，\n',
            '还是第一次这么忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就这样一直看守着\n',
            '没什么人经过的关所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我第一次真实地感受到\n',
            '自己是一名王国军军人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_153D(): pass

    label('loc_153D')

    Jump('loc_195A')

    def _loc_1540(): pass

    label('loc_1540')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_161C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15B3',
    )

    ChrTalk(
        0x00FE,
        (
            '现在也算是处于警戒状态中。\n',
            '柏斯地区有一些坏人为非作歹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼……\n',
            '不要来这里就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1619')

    def _loc_15B3(): pass

    label('loc_15B3')

    ChrTalk(
        0x00FE,
        (
            '现在也算是处于警戒状态中。\n',
            '柏斯地区有一些坏人为非作歹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼……\n',
            '我只希望在训练中进行战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1619(): pass

    label('loc_1619')

    Jump('loc_195A')

    def _loc_161C(): pass

    label('loc_161C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_176E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1703',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16B0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我在那条河里钓鱼，\n',
            '结果被队长怒斥了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得河里有那么多鱼，\n',
            '河水也很清凉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易有点心情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1700')

    def _loc_16B0(): pass

    label('loc_16B0')

    ChrTalk(
        0x00FE,
        (
            '我在那条河里钓鱼，\n',
            '结果被队长怒斥了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '难得这里有这么多鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1700(): pass

    label('loc_1700')

    Jump('loc_176B')

    def _loc_1703(): pass

    label('loc_1703')

    ChrTalk(
        0x00FE,
        (
            '之前我在那条河里钓鱼，\n',
            '结果被队长怒斥了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，是不是因为这个\n',
            '队长才那么严厉地训练我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_176B(): pass

    label('loc_176B')

    Jump('loc_195A')

    def _loc_176E(): pass

    label('loc_176E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1906',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0008, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1871',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1814',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '这个关所平时很少有人通过，\n',
            '所以非常安静。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来这里一听，\n',
            '只有河水的流淌声和鸟鸣声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起我以前工作的农场\n',
            '还要悠闲自得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_186E')

    def _loc_1814(): pass

    label('loc_1814')

    ChrTalk(
        0x00FE,
        (
            '站在这里仔细听，\n',
            '只有河水的流淌声和鸟鸣声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起我以前工作的农场\n',
            '还要悠闲自得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_186E(): pass

    label('loc_186E')

    Jump('loc_1903')

    def _loc_1871(): pass

    label('loc_1871')

    ChrTalk(
        0x00FE,
        (
            '这个关所平时很少有人通过，\n',
            '所以非常安静。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '来这里一听，\n',
            '只有河水的流淌声和鸟鸣声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，如果没有那样的训练，\n',
            '真的比农场还要悠闲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1903(): pass

    label('loc_1903')

    Jump('loc_195A')

    def _loc_1906(): pass

    label('loc_1906')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_195A',
    )

    ChrTalk(
        0x00FE,
        (
            '我才刚被编配到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来是在农场工作，\n',
            '但是还是想来参加王国军。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_195A(): pass

    label('loc_195A')

    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x195E
@scena.Code('func_09_195E')
def func_09_195E():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_19BD',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯的盗窃案件\n',
            '原来是空贼干的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于能够重归平静，\n',
            '过回安稳生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E38')

    def _loc_19BD(): pass

    label('loc_19BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1ABA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A59',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '听说柏斯被强盗袭击了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事情了……\n',
            '我好想现在就赶过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我刚才看到\n',
            '国境守备队的飞艇飞过来了，\n',
            '应该是去调查了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB7')

    def _loc_1A59(): pass

    label('loc_1A59')

    ChrTalk(
        0x00FE,
        (
            '空贼也好，强盗也好，\n',
            '真是有点为所欲为了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也不想呆在关所的守备队，\n',
            '我想去前线啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AB7(): pass

    label('loc_1AB7')

    Jump('loc_1E38')

    def _loc_1ABA(): pass

    label('loc_1ABA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1B3F',
    )

    ChrTalk(
        0x00FE,
        (
            '国境守备队好像\n',
            '逮捕了不少嫌疑犯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一个由凶暴的女孩子领导的团体\n',
            '和一个性格古怪的骗子，\n',
            '但是这两者似乎都不是犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E38')

    def _loc_1B3F(): pass

    label('loc_1B3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1C24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BCD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '现在，\n',
            '关所那边也没有什么新的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军该如何行动，\n',
            '现在一点也不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是急人啊……\n',
            '我们也想出动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C21')

    def _loc_1BCD(): pass

    label('loc_1BCD')

    ChrTalk(
        0x00FE,
        (
            '现在，\n',
            '关所那边也没有什么新的消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军该如何行动，\n',
            '现在一点也不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C21(): pass

    label('loc_1C21')

    Jump('loc_1E38')

    def _loc_1C24(): pass

    label('loc_1C24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1C90',
    )

    ChrTalk(
        0x00FE,
        (
            '和东侧比起来，\n',
            '这个关所西侧聚集了更多经验丰富的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '戴恩副长\n',
            '是个对工作一丝不苟的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E38')

    def _loc_1C90(): pass

    label('loc_1C90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1DC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D51',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '对面的阿斯顿队长还真是厉害呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了重新锻炼新兵，\n',
            '将他们全部都配置到自己的队里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是个非常厉害而且正直的人，\n',
            '但是这样要\n',
            '付出常人两倍的辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DC4')

    def _loc_1D51(): pass

    label('loc_1D51')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '对面的阿斯顿队长还真是厉害呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是个非常厉害而且正直的人，\n',
            '但是这样要\n',
            '付出常人两倍的辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DC4(): pass

    label('loc_1DC4')

    Jump('loc_1E38')

    def _loc_1DC7(): pass

    label('loc_1DC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1E38',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，你们要去柏斯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在可是非常时期呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在检查\n',
            '从柏斯到洛连特的人群中\n',
            '有没有可疑的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E38(): pass

    label('loc_1E38')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x1E3C
@scena.Code('func_0A_1E3C')
def func_0A_1E3C():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1E91',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船的运营\n',
            '好像已经恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能将犯人们逮捕归案\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2242')

    def _loc_1E91(): pass

    label('loc_1E91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1EEF',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然定期船恢复运航，\n',
            '但是关所的盘查仍在进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能够\n',
            '早些恢复原状啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2242')

    def _loc_1EEF(): pass

    label('loc_1EEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1FE2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F89',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '西向航线的『赛希莉亚号』\n',
            '好像再次开航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因如此，\n',
            '经过这里的人又变少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '东向航线的『林德号』\n',
            '什么时候再次开航呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FDF')

    def _loc_1F89(): pass

    label('loc_1F89')

    ChrTalk(
        0x00FE,
        (
            '西向航线的『赛希莉亚号』\n',
            '好像再次开航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因如此，\n',
            '经过这里的人又变少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FDF(): pass

    label('loc_1FDF')

    Jump('loc_2242')

    def _loc_1FE2(): pass

    label('loc_1FE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2116',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20AF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我们的队长和副长\n',
            '都是参加过百日战役的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然两个人的性格不同，\n',
            '但是都非常沉着冷静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是副长，\n',
            '该说他是我行我素的人吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '见到什么都一副\n',
            '非常感兴趣的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2113')

    def _loc_20AF(): pass

    label('loc_20AF')

    ChrTalk(
        0x00FE,
        (
            '我们的队长和副长\n',
            '都是参加过百日战役的士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然两个人的性格不同，\n',
            '但是都非常沉着冷静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2113(): pass

    label('loc_2113')

    Jump('loc_2242')

    def _loc_2116(): pass

    label('loc_2116')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2165',
    )

    ChrTalk(
        0x00FE,
        (
            '如果飞艇失踪是帝国干的好事，\n',
            '可能又要挑起战争了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2242')

    def _loc_2165(): pass

    label('loc_2165')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_21C7',
    )

    ChrTalk(
        0x00FE,
        (
            '采取这样的戒严状态，\n',
            '还是百日战役以来的首次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一说，\n',
            '我就会觉得非常紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2242')

    def _loc_21C7(): pass

    label('loc_21C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2242',
    )

    ChrTalk(
        0x00FE,
        (
            '从东柏斯街道\n',
            '向北方延伸的钢壁之路\n',
            '现在正处在封锁中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要去北部国境的话，\n',
            '只能先去柏斯，\n',
            '然后等待封锁解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2242(): pass

    label('loc_2242')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x2246
@scena.Code('func_0B_2246')
def func_0B_2246():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24BC',
    )

    SetScenaFlags(ScenaFlag(0x006B, 7, 0x35F))
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0101,
        (
            '#000F（约修亚，\n',
            '　这个人难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，好像和我们一样\n',
            '　都是游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F你好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F你还是那样讨人厌呢，\n',
            '斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '你……\n',
            '上次的实习游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F很漂亮的回答。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '托您的福，现在\n',
            '我已经取得正游击士称号了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……看起来的确成熟了不少。\n',
            '在柏斯支部有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，现在就在工作中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近发生了很多事情，\n',
            '柏斯的游击士都出动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那就靠你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 180, 0)

    ChrTalk(
        0x0101,
        (
            '#000F（是雪拉姐的朋友。\n',
            '　总觉得他有点可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（但是那走路的动作……\n',
            '　看来是个非常厉害的人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2567')

    def _loc_24BC(): pass

    label('loc_24BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2531',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样仅今天\n',
            '就打败了四头魔兽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果库拉茨\n',
            '从王都回来的话，\n',
            '我们还能开心一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2567')

    def _loc_2531(): pass

    label('loc_2531')

    ChrTalk(
        0x00FE,
        (
            '如果库拉茨\n',
            '从王都回来的话，\n',
            '我们还能开心一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2567(): pass

    label('loc_2567')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x256B
@scena.Code('func_0C_256B')
def func_0C_256B():
    TalkBegin(0x000E)
    ChrTurnDirection(0x00FE, 0x0103, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27C7',
    )

    SetScenaFlags(ScenaFlag(0x006C, 0, 0x360))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120020665V#814F啊，难不成……\n',
            '这不是雪拉扎德前辈吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020666V#850F很久不见了啊。\n',
            '自从您去修行之后就再没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020667V#020F这不是亚妮拉丝吗。\n',
            '你在这里做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120020668V#810F呵呵，协会委派我来这里\n',
            '执行击退魔兽的任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020669V#020F是这样啊……辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020670V对了，你已经找到\n',
            '所谓的剑之道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120020671V#819F呵呵，前辈您就别问了。\n',
            '我还是处在修行阶段呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020672V#810F说起来，前辈您也是在\n',
            '执行协会的任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020673V#020F是啊，不过我和你的任务性质不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120020674V#810F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020675V这个地方\n',
            '最近发生很多事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020676V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2908')

    def _loc_27C7(): pass

    label('loc_27C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_289C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120020677V#850F啊，雪拉扎德前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020678V#020F亚妮拉丝，来这里工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120020679V#810F是啊，虽然都不是大事，\n',
            '但是最近这里\n',
            '发生了不少各式各样的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020680V#856F连休息的时间都没有～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2908')

    def _loc_289C(): pass

    label('loc_289C')

    ChrTalk(
        0x00FE,
        (
            '#0120020681V#810F虽然都不是大事，\n',
            '但是最近这里\n',
            '发生了不少各式各样的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120020682V#856F连休息的时间都没有～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2908(): pass

    label('loc_2908')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x290C
@scena.Code('func_0D_290C')
def func_0D_290C():
    EventBegin(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
